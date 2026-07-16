import cloudscraper
from bs4 import BeautifulSoup

# The URL you provided
url = "https://www.myjobmag.co.ke/search/jobs?q=&location=Nairobi&location-sinput=Nairobi&field=Data%2C+Business+Analysis+and+AI&field-sinput=Data%2C+Business+Analysis+and+AI"

# Bypass bot protection
scraper = cloudscraper.create_scraper()
response = scraper.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find the very first job listing using the parent class you found
    first_job = soup.find("li", class_="job-list-li")
    
    if first_job:
        print("\n--- RAW HTML OF THE FIRST JOB LISTING ---\n")
        # prettify() formats the HTML with nice line breaks and indentation so it's easy to read
        print(first_job.prettify())
        print("\n-----------------------------------------\n")
    else:
        print("Could not find 'job-list-li'. The website might have changed or blocked us.")
        print("Here is the first 500 characters of the page text to check:")
        print(soup.get_text()[:500])
else:
    print(f"Failed to connect. Status code: {response.status_code}")