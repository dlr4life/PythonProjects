from selenium import webdriver

# Set up the Selenium WebDriver (this example uses Firefox)
driver = webdriver.Firefox()

# Navigate to the webpage
driver.get("https://index.medium.com/")

# Extract the page source
html = driver.page_source

# Close the browser
driver.quit()

# Print the HTML
print(html)
