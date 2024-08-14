import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)


def test_login():
    # Initialize the WebDriver (Chrome)
    driver = webdriver.Chrome()
    # Navigate to eBay
    driver.get("https://www.ebay.com")
    driver.maximize_window()
    # Search for "16GB laptop"
    search_box = driver.find_element(By.CSS_SELECTOR, value="input[id='gh-ac']")
    search_box.send_keys("16gb laptop")

    submit_btn = driver.find_element(By.CSS_SELECTOR, value="input[type='submit']")
    submit_btn.click()
    # Wait for the search results to load and select the first laptop
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".s-item"))
    )
    list_results = driver.find_elements(By.CSS_SELECTOR, value="span[role='heading']")
    # List all the elements with heading 16gb laptop
    for i in list_results:
        print(i.text)
    print("-----------------------------------------------------")

    screen_16 = driver.find_element(By.XPATH, value="//input[@aria-label='16-16.9 in'][1]")
    screen_16.click()

    WebDriverWait(driver, 10)
    list_results = driver.find_elements(By.CSS_SELECTOR, value="span[role='heading']")
    price = driver.find_elements(By.CSS_SELECTOR, value="span[class='s-item__price']")

    for i, j in zip(list_results, price):
        print(i.text, "--->", j.text)

    WebDriverWait(driver, 5)
    first_laptop = driver.find_element(By.XPATH, "(//a[@class='s-item__link'])[3]")
    first_laptop.click()
    driver.switch_to.window(driver.window_handles[-1])

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Add to cart')]")))

    add_to_cart_button = driver.find_element(By.XPATH, "//span[contains(text(),'Add to cart')]")
    add_to_cart_button.click()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://cart.payments.ebay.com/"))

    check_out_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Go to checkout']")
    check_out_btn.click()
    WebDriverWait(driver, 10).until(EC.url_contains("https://signin.ebay.com/"))
    username = driver.find_element(By.ID, "userid")
    username.send_keys("chinu.pande@gmail.com")
    continue_btn = driver.find_element(By.ID, "signin-continue-btn")
    continue_btn.click()
    time.sleep(5)
    password = driver.find_element(By.ID, "pass")
    password.send_keys("chinu@123")
    signin = driver.find_element(By.ID, "sgnBt")
    signin.click()

    time.sleep(20)
    driver.quit()
