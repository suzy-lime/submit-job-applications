from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
import os

chrome_path = "C:/Users/ccesports2/Development/chromedriver"
my_email = os.environ.get("MY_EMAIL")
my_password = os.environ.get("MY_PASSWORD")
my_phone = os.environ.get("MY_PHONE")

driver = webdriver.Chrome(chrome_path)

driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=92000001&keywords=python%20developer&location=Remote")
driver.maximize_window()

sign_in = driver.find_element_by_css_selector(".nav__button-secondary")
sign_in.click()

email = driver.find_element_by_id("username")
email.send_keys(my_email)

password = driver.find_element_by_id("password")
password.send_keys(my_password)

sign_in_again = driver.find_element_by_css_selector(".btn__primary--large")
sign_in_again.click()

time.sleep(5)

job_cards_elements = driver.find_elements_by_class_name("job-card-container")

for job_card in job_cards_elements:

    job_card.click()

    time.sleep(3)

    try:
        apply_now = driver.find_element_by_css_selector("div .jobs-apply-button--top-card")
        apply_now.click()

        time.sleep(3)
    except NoSuchElementException:
        continue

    try:
        phone = driver.find_element_by_css_selector("div .display-flex input")
        phone.send_keys(my_phone)
    except NoSuchElementException:
        close_button = driver.find_element_by_css_selector("svg .mercado-match")
        close_button.click()
        continue

    try:
        next_button = driver.find_element_by_css_selector("div .justify-flex-end button")
        next_button.click()

        time.sleep(3)
    except ElementClickInterceptedException:
        close_button = driver.find_element_by_css_selector("svg .mercado-match")
        close_button.click()

    try:
        review_button = driver.find_element_by_class_name("artdeco-button--primary")
        review_button.click()
    except ElementClickInterceptedException:
        close_button = driver.find_element_by_css_selector("svg .mercado-match")
        close_button.click()

    try:
        submit_button = driver.find_element_by_class_name("artdeco-button--primary")
        submit_button.click()
    except ElementClickInterceptedException:
        close_button = driver.find_element_by_css_selector("svg .mercado-match")
        close_button.click()
