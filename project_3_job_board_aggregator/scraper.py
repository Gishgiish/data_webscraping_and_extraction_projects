import cloudscraper
from bs4 import BeautifulSoup
import csv
import os
import time

# Base URL for Data, Business Analysis and AI jobs in Nairobi
base_url = "https://www.myjobmag.co.ke/search/jobs?q=&location=Nairobi&location-sinput=Nairobi&field=Data%2C+Business+Analysis+and+AI&field-sinput=Data%2C+Business+Analysis+and+AI"
base_domain = "https://www.myjobmag.co.ke"

all_jobs = []

seen_links = set() # A set to keep track of URLs we've already scraped

# Master Loop for 3 pages
for page_num in range(1, 4):
    print(f"--- Scraping Page {page_num} ---")
    
    # Build URL (MyJobMag uses &page=X for pagination)
    if page_num == 1:
        url = base_url
    else:
        url = f"{base_url}&page={page_num}"
        
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        jobs = soup.find_all("li", class_="job-list-li")
        print(f"Found {len(jobs)} job listings on Page {page_num}.")
        
        for job in jobs:
            # 1. Find the main link and raw title text
            mag_b_tag = job.find("li", class_="mag-b")
            if not mag_b_tag:
                continue # Skip if the structure is broken
                
            link_tag = mag_b_tag.find("a")
            if not link_tag:
                continue
                
            raw_title_text = link_tag.get_text(strip=True)
            
            # 2. THE SURGEON: Split Title and Company
            if " at " in raw_title_text:
                # split(" at ", 1) ensures we only split on the FIRST " at "
                parts = raw_title_text.split(" at ", 1) 
                job_title = parts[0].strip()
                company_name = parts[1].strip()
            else:
                job_title = raw_title_text
                company_name = "Unknown Company"
                
            # 3. Fix Relative URL
            raw_link = link_tag.get("href")
            if raw_link.startswith("/"):
                full_link = base_domain + raw_link
            else:
                full_link = raw_link

            # 4. Check for duplicates
            if full_link in seen_links:
                continue
            seen_links.add(full_link)

            
            # 5. Extract Date Posted (Replacing Location)
            date_tag = job.find("li", id="job-date")
            job_date = date_tag.get_text(strip=True) if date_tag else "No Date"
            
            # Add to master list
            all_jobs.append({
                "Title": job_title,
                "Company": company_name,
                "Date Posted": job_date,
                "Link": full_link
            })
            
        # Polite delay
        time.sleep(2)
        
    else:
        print(f"Failed to connect to Page {page_num}. Status: {response.status_code}")

# Save to CSV
print("\n--- All pages scraped! Saving to file... ---")
os.makedirs("data", exist_ok=True)
csv_filename = "data/nairobi_data_jobs.csv"

with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    headers = ["Title", "Company", "Date Posted", "Link"]
    writer = csv.DictWriter(file, fieldnames=headers)
    
    writer.writeheader()
    writer.writerows(all_jobs)
    
print(f"Success! Scraped a total of {len(all_jobs)} jobs, after duplicates and saved to '{csv_filename}'.")