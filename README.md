# LinkedIn Company Scraper

This repository contains a script to extract company names and logos from LinkedIn's search results. 

## Data Source

Data is pulled via "View Source" on LinkedIn. To replicate the process:

1. Visit: [LinkedIn Company Search Results](https://www.linkedin.com/search/results/companies/)
2. Look for the tag:
    ```html
    <main class="scaffold-layout__main">
    ```
3. Copy the outer HTML into a file. In this case, I pulled a few results and saved them into a single file.

## Requirements

This script uses BeautifulSoup to parse the company names and logos from the HTML tags.

### Installation

To set up the project, follow these steps:

```bash
git clone git@github.com:svsaraf/licompanyscraper.git
cd licompanyscraper
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```