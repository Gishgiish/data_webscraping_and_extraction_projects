# Nairobi Tech Job Board Aggregator

## Project Overview
This project is an advanced, automated web scraper designed for recruitment market research and job aggregation in Nairobi, Kenya. It targets **MyJobMag Kenya**, extracting high-value job listings in the Data, Business Analysis, and AI sectors, including job titles, company names, posting dates, and direct application links.

Unlike basic scrapers, this script is engineered to handle real-world data anomalies, including "Frankenstein" text structures (where titles and companies are merged), missing location data, and pagination-induced duplicate listings.

## Technologies Used
- **Python 3:** Core programming language.
- **Cloudscraper:** Bypasses Cloudflare/bot-protection mechanisms.
- **BeautifulSoup4:** Parses HTML and navigates the DOM tree.
- **CSV & OS Modules:** Handles data structuring, file exporting, and dynamic directory creation.
- **Time Module:** Implements polite scraping delays (`time.sleep`) to prevent IP bans.

## Key Technical Challenges Solved
1. **"Frankenstein" Text Splitting:** The website merged the Job Title and Company Name into a single string (e.g., "Data Analyst at TechCorp"). The script uses Python's `.split(" at ", 1)` method to surgically separate these into two clean, distinct CSV columns.
2. **Deduplication Logic:** Due to website pagination quirks, search results sometimes repeat across pages. The script utilizes a Python `set()` to track scraped URLs, automatically discarding duplicate entries to ensure a 100% unique, high-quality dataset.
3. **Relative URL Fixing:** Automatically detects and fixes partial links (e.g., `/job/data-analyst`) by prepending the base domain.
4. **Adaptive Data Extraction:** Recognized that location data was omitted from the search results page and adaptively extracted the "Date Posted" instead, maintaining high dataset value for market trend analysis.

## Project Structure
```text
project_3_job_board_aggregator/
│
├── data/
│   └── nairobi_data_jobs_clean.csv  # The final extracted dataset (18 unique, high-value listings)
├── venv/                            # Python virtual environment
├── scraper.py                       # The main scraping script
└── README.md                        # Project documentation 
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
The script scrapes multiple pages, applies strict data validation and deduplication, and saves the clean data to data/nairobi_data_jobs_clean.csv. 
Columns include:

    Title: The specific role (e.g., "M&E Data Coordinator").
    Company: The hiring organization (e.g., "GrowthAfrica").
    Date Posted: The date the listing went live (e.g., "14 July").
    Link: Direct, fully-qualified URL to the job posting.

Built as a portfolio project demonstrating advanced DOM traversal, string manipulation, data deduplication, and robust automated web scraping.