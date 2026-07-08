import cloudscraper
from bs4 import BeautifulSoup
import csv
import os

# 1. Define the base URL (Page 1)
base_url = "https://www.phoneplacekenya.com/product-category/smartphones/"

# Create an empty list to hold ALL phones from ALL pages
all_phones = []

# 2. The Master Loop: Count from 1 to 4
for page_num in range(1, 5):
    print(f"--- Starting to scrape Page {page_num} ---")
    
    # Build the correct URL for the current page
    if page_num == 1:
        url = base_url
    else:
        url = f"{base_url}page/{page_num}/"
        
    # Bypass bot protection for this specific page
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Find all products on THIS specific page
        products = soup.find_all("div", class_="product-wrapper")
        print(f"Found {len(products)} products on Page {page_num}.")
        
        # Loop through the products on this page
        for product in products:
            name_tag = product.find("h3", class_="heading-title product-name")
            product_name = name_tag.get_text(strip=True) if name_tag else "No Name"
            
            link_tag = name_tag.find("a") if name_tag else None
            product_link = link_tag.get("href") if link_tag else "No Link"
            
            price_tag = product.find("span", class_="price")
            product_price = price_tag.get_text(strip=True) if price_tag else "No Price"
            
            phone_data = {
                "Name": product_name,
                "Price": product_price,
                "Link": product_link
            }
            
            # Add this phone to our master list
            all_phones.append(phone_data)
            
        print(f"Finished Page {page_num}!\n")
        
    else:
        print(f"Failed to connect to Page {page_num}. Status code: {response.status_code}")

# 3. Save the data to a CSV file (This happens AFTER the loop finishes all pages)
print("--- All pages scraped! Saving to file... ---")

# 1. Create the 'data' folder if it doesn't already exist
os.makedirs('data', exist_ok=True)

# 2. Define the file path to go INSIDE the data folder
csv_filename = "data/nairobi_phones_all_pages.csv"

# 3. Open and write the file (this part is the same)
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    headers = ["Name", "Price", "Link"]
    writer = csv.DictWriter(file, fieldnames=headers)
    
    writer.writeheader()
    writer.writerows(all_phones)
    
print(f"Success! Scraped a total of {len(all_phones)} phones across all pages.")
print(f"Data saved to '{csv_filename}'.")