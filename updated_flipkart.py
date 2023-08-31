import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# This code is to scrape the mobile phone data from Flipkart.

# Create a Chrome options object and set the "detach" flag to True.
# This will allow the browser window to be closed automatically after the script finishes running.
opt = Options()
opt.add_experimental_option("detach", True)

# Create a Chrome driver object and set the implicit wait time to 5 seconds.
driver = webdriver.Chrome(options=opt)
driver.implicitly_wait(5)
driver.maximize_window()

# Navigate to the Flipkart website.
driver.get("https://www.flipkart.com/")

# Try to click the OTP overlay. If it is not present, then skip.
try:
    otpEscape = WebDriverWait(driver, 5, ignored_exceptions= [Exception, TimeoutError ])
    otpEscape.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/button'))).click()
except:
    pass

# Find the search input field and enter the keyword "mobiles".
search = driver.find_element(By.XPATH, "//input[@name='q']")
search.send_keys("mobiles")

# Submit the search form.
search.submit()

# Initialize the variables to store the mobile name, price, features, and rating.
name = []
price = []
features = []
rating = []
count = 0

# The loop will run 42 times, which is the maximum number of pages of results that Flipkart shows.
while True:
    count += 1

    # Get the current page number.
    page_number = count

    # Navigate to the specified page.
    driver.get(f"https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as-off&page={page_number}")

    # Get the page source.
    page_source = driver.page_source

    # Parse the page source using BeautifulSoup.
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find all the mobile names, prices, features, and ratings on the page.
    name_ = soup.find_all("div", class_ ="_4rR01T")
    price_ = soup.find_all("div", class_ ="_30jeq3 _1_WHN1")
    features_ = soup.find_all("div", class_="fMghEO")
    rating_ = soup.find_all("div", class_="_3LWZlK")

    # Append the mobile name, price, features, and rating to the corresponding lists.
    for i, j, k, l in zip(name_, price_, features_, rating_):
        name.append(i.text)
        price.append(j.text)
        features.append(k.text)
        rating.append(l.text)

    # Check if the current page is the last page.
    if count == 42:
        break

# Create a Pandas DataFrame and store the mobile name, price, features, and rating.
df = pd.DataFrame({"moble": name, "price": price, "features": features, "rating": rating})

# Save the DataFrame to a CSV file.
df.to_csv("mobiles_data.csv")
