import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
import csv

if __name__ == "__main__":
    # Set up undetected Chrome
    options = uc.ChromeOptions()
    options.headless = False  # Set to True to run in the background

    driver = uc.Chrome(options=options, use_subprocess=False)

    # Go to Yellow Pages search results
    url = "https://www.yellowpages.com.au/search/listings?clue=strata+management&locationClue=New+South+Wales&lat=&lon="
    driver.get(url)
    time.sleep(5)  # Wait for page to load

    companies = []

    # Find all listing elements on the page
    listings = driver.find_elements(By.CSS_SELECTOR, "div.cell.in-area-cell")  # Selector for each listing

    for listing in listings:
        try:
            name = listing.find_element(By.CSS_SELECTOR, "a.listing-name").text
        except:
            name = ""
        try:
            phone = listing.find_element(By.CSS_SELECTOR, "a.contact-phone").text
        except:
            phone = ""
        companies.append([name, phone])

    # Save to CSV
    with open("strata_companies_yellowpages.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Company Name", "Phone"])
        writer.writerows(companies)

    driver.quit()
    print("Done! Data saved to strata_companies_yellowpages.csv")
