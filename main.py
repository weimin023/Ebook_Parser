import argparse
import time, os, subprocess
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from js_script import*

# Set the download preferences to automatically download files without prompting
DOWNLOAD_PATH = os.path.join(os.getcwd(), "save")


def main():
    parser = argparse.ArgumentParser(description="Ebook downloader v1_2023.08.14")
    parser.add_argument("-link", type=str, help="Link to the book (doc88.com)")
    parser.add_argument("-begin", type=int, help="Starting page number")
    parser.add_argument("-end", type=int, help="Ending page number")    
    
    args = parser.parse_args()

    if not args.link or not args.begin or not args.end:
        print ("ERROR: Check Options.")
        return
    
    if not os.path.exists(DOWNLOAD_PATH):
        os.mkdir(DOWNLOAD_PATH)

    options = webdriver.EdgeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    driver = webdriver.Edge(options=options)

    download_preferences = {
        "profile.default_content_settings.popups": 0,
        "download.prompt_for_download": "false",
        "download.default_directory": DOWNLOAD_PATH,
        "profile.default_content_setting_values.automatic_downloads": 1
    }
    options.add_experimental_option("prefs", download_preferences)

    try:
        driver.get(args.link)
        js_utils.run_javascript(driver, args.begin, args.end)

    finally:
        print("All operations completed.")


if __name__ == "__main__":
    main()

