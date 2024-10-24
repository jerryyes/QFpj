from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest
import threading
import time


# 定义测试函数
def test_google_search(driver_path):
    chrome_options = Options()
    # 如果Chrome安装在非默认位置，设置binary_location
    chrome_options.binary_location = driver_path

    # 如果不使用webdriver_manager，需要手动指定ChromeDriver路径
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://www.google.com")
        assert "Google" in driver.title
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("pytest selenium")
        search_box.submit()
        assert "pytest selenium" in driver.page_source
    finally:
        driver.quit()


# 定义线程类
class TestThread(threading.Thread):
    def __init__(self, driver_path):
        threading.Thread.__init__(self)
        self.driver_path = driver_path

    def run(self):
        test_google_search(self.driver_path)


# 主函数
def main():
    # ChromeDriver的路径
    driver_path = "E:\\Projects\\chrome-win64\\chrome-win64\\chrome.exe"  # 替换为实际的ChromeDriver路径

    # 创建线程列表
    threads = []

    # 创建并启动多个线程
    for i in range(3):  # 假设我们要运行5个并行测试
        thread = TestThread(driver_path)
        threads.append(thread)
        thread.start()

        # 等待所有线程完成
    for thread in threads:
        thread.join()

    # 如果这个脚本是作为主程序运行，则调用main函数


if __name__ == "__main__":
    main()
