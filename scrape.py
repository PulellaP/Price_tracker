# Import Statements
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Web Scraping
# - Use a Python library like BeautifulSoup or Scrapy to scrape product prices from eBay, Amazon, Alibaba, etc.
# - Be mindful of the terms of service for each platform to ensure compliance.

# create webdriver object
driver = webdriver.Firefox()
# get google.co.in
driver.get("https://www.amazon.com")
# get element of search box
searchbox_element = driver.find_element(By.ID, "twotabsearchtextbox")
# send keys
searchbox_element.send_keys("Phone")
searchbox_element.send_keys(Keys.ENTER)

# Use WebDriverWait to wait for the presence of search results
# Adjust the timeout based on your network speed and website responsiveness
wait = WebDriverWait(driver, 10)  # Set a timeout of 10 seconds

# Wait for the search results to load
wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@data-component-type='s-search-result']")))


# Find all product div elements
product_divs = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")

# create a list to add dictionary items containing the products
productsList = []

# Iterate through each product div and extract the item name
for product_div in product_divs:
    try:
        # Find the h2 tag within the product div and store it
        h2_tag = product_div.find_element(By.TAG_NAME, "h2")

        # Find the price whole within the product div
        price_whole = product_div.find_element(By.CLASS_NAME, "a-price-whole")
        
        #Find the price decimal within the product div
        price_decimal = product_div.find_element(By.CLASS_NAME, "a-price-decimal")

        # Put price into text
        price = int(price_whole.text)

        # Item in productsList list as a dict
        p = {"title" : h2_tag.text, "Price" : price}
        productsList.append(p)

    except Exception as e:
        # Handle exceptions (e.g., if the h2 tag is not found within the div)
        print(f"Error: {e}")

# Close the browser window
driver.quit()

for product in productsList:
    print(product["title"] + " Price: $" + str(product["Price"]))

# Data Entry
# - Organize the scraped data into a structured format, such as a pandas DataFrame.
# - Include relevant information like product name, price, timestamp, and platform.

# Data Storage
# - Choose a storage solution for your data, such as SQLite, MySQL, or MongoDB.
# - Write Python code to store the structured data in the chosen database.

# Data Analysis
# - Utilize pandas and numpy for basic data analysis.
# - Calculate statistical measures like mean, median, and standard deviation of prices.

# Excel Integration
# - Use the openpyxl or xlrd libraries to read and write Excel files in Python.
# - Create Excel sheets to display the scraped data and the results of data analysis.
# - Include graphs and charts using Microsoft Excel formulas and features.
