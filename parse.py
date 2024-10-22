from bs4 import BeautifulSoup
import csv

# Function to extract company information from HTML content
def extract_companies(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    companies = []

    # Find all the main tags
    main_tags = soup.find_all('main')

    for main in main_tags:
        # Find all the company result containers within each main tag
        results = main.select('.reusable-search__result-container')

        for result in results:
            # Find the image element and get the src attribute
            img_element = result.select_one('img')
            image_url = img_element['src'].replace('&amp;', '&') if img_element else None

            # Find the company name
            name_element = result.select_one('.entity-result__title-text a')
            company_name = name_element.text.strip() if name_element else None

            # Append the results to the list
            if image_url and company_name:
                companies.append({'name': company_name, 'logo': image_url})

    return companies

# Read the massive HTML file
with open('scraped_company_names.txt', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Extract companies
companies = extract_companies(html_content)

# Write results to a CSV file
with open('companies.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['name', 'logo']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()  # Write the header
    for company in companies:
        writer.writerow(company)  # Write each company data

print("Data has been written to companies.csv")