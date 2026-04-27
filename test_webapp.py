from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_webapp():
    # Set up Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Open the local web app
        driver.get("file:///C:/Users/sit.lab1/Desktop/devops/index.html")

        # Check page title
        assert "College Registration Form" in driver.title, f"Title mismatch: {driver.title}"

        # Check main heading
        h1 = driver.find_element("tag name", "h1")
        assert "College Registration Form" in h1.text, f"H1 text mismatch: {h1.text}"

        # Check name input
        name_input = driver.find_element("id", "name")
        assert name_input.get_attribute("type") == "text", "Name input not found"

        # Check radio buttons
        radios = driver.find_elements("name", "gender")
        assert len(radios) == 3, f"Expected 3 gender radios, found {len(radios)}"

        # Check checkboxes
        checkboxes = driver.find_elements("name", "subjects")
        assert len(checkboxes) == 4, f"Expected 4 subject checkboxes, found {len(checkboxes)}"

        # Check submit button
        submit_button = driver.find_element("tag name", "button")
        assert submit_button.get_attribute("type") == "submit", "Submit button not found"

        print("All tests passed! College registration form is working correctly.")

        # Keep the browser open for 10 seconds
        time.sleep(10)

    finally:
        driver.quit()

if __name__ == "__main__":
    test_webapp()