# web-scraping-of-mobile-phone-data-from-Flipkart-using-Selenium-and-BeautifulSoup
This code performs web scraping of mobile phone data from Flipkart using Selenium and BeautifulSoup.

1. Import necessary libraries: Import the required libraries, including pandas, BeautifulSoup, and Selenium.

2. Configure Chrome options: Create a Chrome options object, allowing the browser window to remain open after the script finishes.

3. Initialize the Selenium driver: Create a Chrome WebDriver object, set implicit wait time, and maximize the browser window.

4. Navigate to Flipkart: Open the Flipkart website.

5. Handle OTP overlay (if present): Attempt to click on the OTP overlay to close it. This is done using Selenium's WebDriverWait.

6. Enter the search query: Find the search input field, enter "mobiles," and submit the search form.

7. Initialize data storage: Create empty lists to store mobile names, prices, features, and ratings.

8. Scrape data from multiple pages: Use a while loop to iterate through 42 pages of mobile search results on Flipkart. The loop navigates to each page and extracts relevant data using BeautifulSoup.

9. Append data to lists: Extract mobile names, prices, features, and ratings from the page source and append them to their respective lists.

10. Check for the last page: Determine if the current page is the last page of results.

11. Create a DataFrame: Use pandas to create a DataFrame from the collected data.

12. Save data to CSV: Save the DataFrame to a CSV file named "mobiles_data.csv."

13. The code effectively scrapes mobile phone data from multiple pages on Flipkart and stores it in a CSV file for further analysis.




