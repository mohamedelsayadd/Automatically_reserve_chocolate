# Importing necessary modules from selenium for web automation
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Installing ChromeDriver and initializing the browser
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

# Navigating to the chocolate shop website
browser.get("https://fixchocolates.shop/")
time.sleep(2)  # Waiting for 2 seconds to let the page load

# XPaths of the chocolate items
first_chocolate = "//*[@id='content']/div[6]/div[1]/div/div[2]/div[2]/div[1]/p[2]/a"
second_chocolate = "//*[@id='content']/div[6]/div[2]/div/div[2]/div[2]/div[1]/p[2]/a"
third_chocolate = "//*[@id='content']/div[6]/div[3]/div/div[2]/div[2]/div[1]/p[2]/a"
fourth_chocolate = "//*[@id='content']/div[6]/div[4]/div/div[2]/div[2]/div[1]/p[2]/a"
fifth_chocolate = "//*[@id='content']/div[6]/div[5]/div/div[2]/div[2]/div[1]/p[2]/a"
sixth_chocolate = "//*[@id='content']/div[6]/div[6]/div/div[2]/div[2]/div[1]/p[2]/a"

# XPaths of the "Add to Cart" buttons for each chocolate
first_add_to_cart = "//*[@id='product-14417']/div/div[1]/div/div[2]/form/div/div/button"
second_add_to_cart = "//*[@id='product-15073']/div/div[1]/div/div[2]/form/div/div/button"
third_add_to_cart = "//*[@id='product-15074']/div/div[1]/div/div[2]/form/div/div/button"
fourth_add_to_cart = "//*[@id='product-15075']/div/div[1]/div/div[2]/form/div/div/button"
fifth_add_to_cart = "//*[@id='product-15077']/div/div[1]/div/div[2]/form/div/div/button"
sixth_add_to_cart = "//*[@id='product-15076']/div/div[1]/div/div[2]/form/div/div/button"

# XPath for the checkout button
checkout = "//*[@id='cart-popup']/div/div[2]/p[2]/a[2]"

# Selecting the fourth chocolate item and adding it to the cart
choose_chocolate_button = browser.find_element(By.XPATH, fourth_chocolate)
choose_chocolate_button.click()

# Clicking the "Add to Cart" button for the selected chocolate
add_to_cart_button = browser.find_element(By.XPATH, fourth_add_to_cart)
add_to_cart_button.click()

# Clicking the checkout button to proceed to the checkout page
checkout_button = browser.find_element(By.XPATH, checkout)
checkout_button.click()

# Defining the number of bars to purchase
number = 10
num = number - 1  # Subtracting 1 to match the iteration count

# Adjusting the number of chocolate bars in the cart by clicking the plus button
for i in range(num):
    number_of_bars = browser.find_element(By.XPATH, "//*[@id='main']/div[2]/div/div[2]/div[1]/form/div/table/tbody/tr[1]/td[5]/div/input[3]")
    number_of_bars.click()

# If the number of bars is 10 or more, proceed with the checkout process
if number >= 10:
    time.sleep(5)  # Waiting for 5 seconds before proceeding
    proceed_button = browser.find_element(By.XPATH, "//*[@id='main']/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div/a")
    proceed_button.click()

# Filling out the checkout form
email = "mohamedelsayad866@gmail.com"
email_text_box = browser.find_element(By.XPATH, "//*[@id='billing_email']")
email_text_box.send_keys(email)

first_name = "Mohamed"
first_name_button = browser.find_element(By.XPATH, "//*[@id='billing_first_name']")
first_name_button.send_keys(first_name)

last_name = "Elsayad"
last_name_button = browser.find_element(By.XPATH, "//*[@id='billing_last_name']")
last_name_button.send_keys(last_name)

# Selecting the country from the dropdown menu
country = "Cuba"
dropdown = browser.find_elements(By.XPATH, "//*[@id='billing_country']/option")
i = 0  # Index variable for the loop
while i < len(dropdown):
    if dropdown[i].text == country:
        dropdown[i].click()  # Select the desired country
        break
    i += 1

# Entering the billing address details
address = "anything"
address_button = browser.find_element(By.XPATH, "//*[@id='billing_address_1']")
address_button.send_keys(address)

state = "balabala"
state_button = browser.find_element(By.XPATH, "//*[@id='billing_state']")
state_button.send_keys(state)

ZIP = "35644"
ZIP_button = browser.find_element(By.XPATH, "//*[@id='billing_postcode']")
ZIP_button.send_keys(ZIP)

city = "Cairo"
city_button = browser.find_element(By.XPATH, "//*[@id='billing_city']")
city_button.send_keys(city)

# Entering the phone number
phone = "+201063827738"
phone_button = browser.find_element(By.XPATH, "//*[@id='billing_phone']")
phone_button.send_keys(phone)

# Agreeing to the terms and conditions by clicking the checkbox
time.sleep(3)  # Waiting for 3 seconds
agree_checkbox = browser.find_element(By.ID, "terms")
agree_checkbox.click()

# Submitting the order
submit_button = browser.find_element(By.XPATH, "//*[@id='place_order']")
submit_button.click()

# Saving a screenshot after the reservation
time.sleep(4)
screenshot = browser.save_screenshot('screenshot_after_reservation.png')

# Keeping the browser open indefinitely for debugging purposes
while True:
    
    time.sleep(1)  # Pausing for 1 second repeatedly
    if screenshot : 
        break
# Quitting the browser (this code is unreachable due to the infinite loop)
browser.quit()
