Data pulled via "View Source" on LI. To replicate, view source on:

https://www.linkedin.com/search/results/companies/

Look for the tag "<main class="scaffold-layout__main">" and copy the outer HTML into a file. In this case I pulled a few and dropped it into the file. 

This script uses beautifulsoup to parse the names and company logos from the tags.

Usage:
    git clone git@github.com:svsaraf/licompanyscraper.git
    cd licompanyscraper
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python parse.py
