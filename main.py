from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the URL
driver.get("https://github.com/raaasin")

# Refresh the page for 10000a loops
for i in range(10000):
    # Refresh the page
    driver.refresh()
    print(f"Refreshed {i+1} times.")
    time.sleep(0.2)  # Wait for 0.2 second before the next refresh

# Close the WebDriver
driver.quit()
