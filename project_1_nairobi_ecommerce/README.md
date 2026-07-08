# Nairobi E-Commerce Phone Price Monitor

## Project Overview
This project is an automated web scraper designed to monitor smartphone pricing across Nairobi-based retail brands. Specifically, it targets **Phoneplace Kenya**, extracting real-time data on smartphone models, their current prices in KSh, and direct product links. 

This tool is highly useful for:
- **Competitor Analysis:** Keeping track of how local retailers price their devices.
- **Price Tracking:** Monitoring market trends for specific phone models in Kenya.
- **Data Aggregation:** Building a centralized database of tech pricing for international clients looking to enter the East African market.

## Technologies Used
- **Python 3:** The core programming language.
- **Cloudscraper:** Used to bypass Cloudflare/bot-protection mechanisms (solving 403 Forbidden errors).
- **BeautifulSoup4:** For parsing HTML and navigating the DOM tree to extract specific data points.
- **CSV Module:** For structuring and exporting the scraped data into a clean, readable spreadsheet format.

## Project Structure
```text
project_1_nairobi_ecommerce/
│
├── data/
│   └── nairobi_phones_all_pages.csv  # The final extracted dataset (200+ items)
├── venv/                             # Python virtual environment
├── scrapper.py                       # The main scraping script
└── README.md                         # Project documentation.
```


## How to Run
    1. Clone or download this repository.
    2. Navigate to the project directory in your terminal.
    3. Activate the virtual environment:
        Linux/Mac: `source venv/bin/activate`
        Windows: `venv\Scripts\activate`
    4. Install dependencies: pip install cloudscraper beautifulsoup4
    5. Run the script: python scrapper.py

## Sample Output
The script automatically handles pagination, scraping all available pages and saving the data to data/nairobi_phones_all_pages.csv. 
Columns include:

    Name: The exact model of the smartphone.
    Price: The current retail price in Kenyan Shillings (KSh).
    Link: Direct URL to the product page.