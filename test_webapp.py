from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_webapp():
    # Set up Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        # Open the local web app
        driver.get("file:///C:/Users/sit.lab1/Desktop/devops/index.html")

        # Check page title
        assert "Simple Web App" in driver.title, f"Title mismatch: {driver.title}"

        # Check main heading
        h1 = driver.find_element("tag name", "h1")
        assert "Welcome to My Simple Web App" in h1.text, f"H1 text mismatch: {h1.text}"

        # Check for features list
        ul = driver.find_element("tag name", "ul")
        lis = ul.find_elements("tag name", "li")
        assert len(lis) == 3, f"Expected 3 features, found {len(lis)}"

        # Check button presence
        button = driver.find_element("tag name", "a")
        assert button.text == "Learn More", f"Button text mismatch: {button.text}"

        print("All tests passed! Web app is working correctly.")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_webapp()