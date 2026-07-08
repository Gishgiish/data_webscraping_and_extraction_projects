import cloudscraper
from bs4 import BeautifulSoup
import csv
import os
import time

base_url = "https://www.property24.co.ke/property-for-sale-in-nairobi-c1890"
base_domain = "https://www.property24.co.ke"

all_properties = []

for page_num in range(1, 4):
    print(f"--- Scraping Page {page_num} ---")
    
    if page_num == 1:
        url = base_url
    else:
        url = f"{base_url}?Page={page_num}"
        
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        properties = soup.find_all("div", class_="p24_regularTile")
        print(f"Found {len(properties)} total tiles on Page {page_num}.")
        
        for prop in properties:
            # Extract Title
            title_tag = prop.find("span", class_="p24_propertyTitle")
            title = title_tag.get_text(strip=True) if title_tag else "No Title"
            
            # Extract Price
            price_tag = prop.find("span", class_="p24_price")
            price = price_tag.get_text(strip=True) if price_tag else "No Price"
            
            # --- THE NOISE FILTER ---
            # If it's a Development or an Ad, it won't have a standard title/price.
            # 'continue' tells Python to skip this tile and move to the next one!
            if title == "No Title" or price == "No Price":
                continue 
            # --------------------------
            
            # Extract Location
            loc_tag = prop.find("span", class_="p24_location")
            location = loc_tag.get_text(strip=True) if loc_tag else "No Location"
            
            # Extract Link
            link_tag = prop.find("a")
            if link_tag and link_tag.get("href"):
                raw_link = link_tag.get("href")
                if raw_link.startswith("/"):
                    link = base_domain + raw_link
                else:
                    link = raw_link
            else:
                link = "No Link"
                
            # Add to master list (This only happens if it passed the filter!)
            all_properties.append({
                "Title": title,
                "Price": price,
                "Location": location,
                "Link": link
            })
            
        print(f"Finished processing Page {page_num}. Pausing...")
        time.sleep(2)
        
    else:
        print(f"Failed to connect to Page {page_num}. Status: {response.status_code}")

print("\n--- All pages scraped! Saving to file... ---")
os.makedirs("data", exist_ok=True)
csv_filename = "data/nairobi_properties_clean.csv"

with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    headers = ["Title", "Price", "Location", "Link"]
    writer = csv.DictWriter(file, fieldnames=headers)
    
    writer.writeheader()
    writer.writerows(all_properties)
    
print(f"Success! After filtering out the noise, we have {len(all_properties)} clean properties.")
print(f"Data saved to '{csv_filename}'.")