import requests
from bs4 import BeautifulSoup
import csv

# URL of the directory listing
url = 'https://directory.strata.community/listing/strata-management-company'

# Send HTTP request
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Open CSV file for writing
with open('strata_companies.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Company Name', 'Phone', 'Email'])

    # Adjust the selector based on actual HTML structure
    for listing in soup.select('.listing-class'):  # Replace with actual class
        name = listing.select_one('.company-name-class').get_text(strip=True) if listing.select_one('.company-name-class') else ''
        phone = listing.select_one('.phone-class').get_text(strip=True) if listing.select_one('.phone-class') else ''
        email = listing.select_one('.email-class').get_text(strip=True) if listing.select_one('.email-class') else ''
        writer.writerow([name, phone, email])
