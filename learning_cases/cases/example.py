from selenium import webdriver
# 如果不需要自动管理ChromeDriver，可以删除以下导入
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def driver():
    try:
        chrome_options = Options()
        # 如果Chrome安装在非默认位置，设置binary_location
        chrome_options.binary_location = "E:\\Projects\\chrome-win64\\chrome-win64\\chrome.exe"
        # 如果需要无头模式或禁用GPU，取消注释以下行
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--disable-gpu")

        # 如果使用webdriver_manager，使用以下方式创建Service
        # service = Service(ChromeDriverManager().install())
        # driver = webdriver.Chrome(service=service, options=chrome_options)

        # 如果不使用webdriver_manager，需要手动指定ChromeDriver路径
        driver = webdriver.Chrome(options=chrome_options)

        print("Browser started successfully.")
        yield driver
        driver.quit()
    except Exception as e:
        print(f"Error starting browser: {e}")
        raise


def test_google_search(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("pytest selenium")
    search_box.submit()
    assert "pytest selenium" in driver.page_source


