# Data Web Scraping & Extraction Projects

A collection of lightweight, robust Python-based data extraction pipelines designed to transform unstructured web data into clean, structured formats (CSV, JSON, Excel) for business intelligence and lead generation.

## Projects

### 1. Nairobi E-commerce Price Tracker
- **Goal**: Extract product names, prices, and availability from local Kenyan e-commerce sites for market analysis.
- **Tech Stack**: Python, Requests, BeautifulSoup, Pandas.
- **Key Features**: Handles pagination, cleans currency strings, and exports to structured CSV. Implements random delays to respect `robots.txt` and avoid IP bans.

### 2. B2B Lead Generation Engine
- **Goal**: Automate the collection of company names, industries, and contact details from online business directories.
- **Tech Stack**: Python, Selenium (Headless), Pandas.
- **Key Features**: Navigates dynamic JavaScript-rendered pages, deduplicates records, and validates email formats before export.

### 3. Job Board Aggregator Pipeline
- **Goal**: Consolidate job postings from multiple niche job boards into a single, normalized dataset.
- **Tech Stack**: Python, BeautifulSoup, SQLite.
- **Key Features**: Standardizes job titles, locations, and salary ranges; stores data in a lightweight SQLite database for easy querying.

## Technical Approach
- **Efficiency**: Designed to run efficiently on low-resource environments (e.g., 2GB RAM), utilizing lightweight libraries (`requests` > `selenium` where possible).
- **Reliability**: Includes error handling, retry logic, and comprehensive logging.
- **Data Quality**: Uses `pandas` for post-scraping data cleaning (removing duplicates, handling null values, standardizing formats).

