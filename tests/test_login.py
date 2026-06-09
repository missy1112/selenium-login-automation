from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test_valid_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get("https://the-internet.herokuapp.com/login")

        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        success_message = driver.find_element(By.ID, "flash").text

        assert "You logged into a secure area!" in success_message

    finally:
        driver.quit()


def test_invalid_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        driver.get("https://the-internet.herokuapp.com/login")

        driver.find_element(By.ID, "username").send_keys("wronguser")
        driver.find_element(By.ID, "password").send_keys("wrongpassword")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        error_message = driver.find_element(By.ID, "flash").text

        assert "Your username is invalid!" in error_message

    finally:
        driver.quit()