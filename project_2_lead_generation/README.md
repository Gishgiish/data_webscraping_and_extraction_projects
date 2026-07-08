#  Nairobi Real Estate Lead Generator

## Project Overview
This project is an advanced, automated web scraper designed for real estate market research and lead generation in Nairobi, Kenya. It targets **Property24 Kenya**, extracting high-value property listings, including titles, prices, locations, and direct links.

Unlike basic scrapers, this script is engineered to handle real-world web complexities, including dynamic class names, relative URLs, and mixed-content "noise" (filtering out property developments and ads to isolate individual listings).

## Technologies Used
- **Python 3:** Core programming language.
- **Cloudscraper:** Bypasses Cloudflare/bot-protection mechanisms.
- **BeautifulSoup4:** Parses HTML and navigates the DOM tree.
- **CSV & OS Modules:** Handles data structuring, file exporting, and dynamic directory creation.
- **Time Module:** Implements polite scraping delays (`time.sleep`) to prevent IP bans.

## Key Technical Challenges Solved
1. **Dynamic CSS Classes:** Property24 uses randomized class names (e.g., `DittiesPillion`) that change on every reload. The script uses Tree Traversal to find the stable underlying class (`js_listingTile` / `p24_regularTile`).
2. **Relative URLs:** Automatically detects and fixes partial links (e.g., `/for-sale/...`) by prepending the base domain.
3. **Mixed Content Filtration:** Uses conditional logic (`continue`) to automatically discard "Development" projects and "Featured Ads" that lack standard data structures, ensuring a 100% clean dataset.

##  Project Structure
```text
project_2_lead_generation/
│
├── data/
│   └── nairobi_properties_clean.csv  # The final extracted dataset (42 premium listings)
├── venv/                             # Python virtual environment
├── scraper.py                        # The main scraping script
└── README.md                         # Project documentation
```

## How to Run

    Clone or download this repository.
    Navigate to the project directory in your terminal.
    Activate the virtual environment:
        Linux/Mac: source venv/bin/activate
        Windows: venv\Scripts\activate
    Install dependencies: pip install cloudscraper beautifulsoup4
    Run the script: python scraper.py

## Dataset Details
The script scrapes multiple pages, applies strict data validation, and saves the clean data to data/nairobi_properties_clean.csv. 
Columns include:

    Title: Property type and bedroom count (e.g., "3 Bedroom Apartment / Flat").
    Price: The listing price in Kenyan Shillings (KSh).
    Location: The specific neighborhood (e.g., "Kilimani", "Westlands").
    Link: Direct, fully-qualified URL to the property listing.

Built as a portfolio project demonstrating advanced DOM traversal, data filtration, and robust automated web scraping.