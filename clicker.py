from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import service
from dotenv import load_dotenv
import time


def main():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--log-level=3")
    webdriver_service = service.Service("operadriver_win64\\operadriver.exe")
    webdriver_service.start()
    driver = webdriver.Remote(
        webdriver_service.service_url,
        webdriver.DesiredCapabilities.OPERA,
        options=chrome_options,
    )
    driver.get("https://freebitco.in")
    time.sleep(2)
    # yield
    driver.close()
    driver.quit()


if __name__ == "__main__":
    main()
