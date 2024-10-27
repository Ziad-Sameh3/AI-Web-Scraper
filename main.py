import streamlit as st
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pyppeteer

def scraping(website):
    st.write("Launching Chrome driver...")

    # Install Pyppeteer's Chrome
    pyppeteer.install()

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.binary_location = pyppeteer.launcher.DEFAULT_ARGS['binary_location']

    # Use WebDriver Manager to automatically handle the ChromeDriver setup
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Fetch the web page
    driver.get(website)
    html = driver.page_source
    driver.quit()  # Close the driver after fetching page source
    return html

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(['script', 'style']):
        script_or_style.extract()

    clean_content = soup.get_text(separator='\n')
    clean_content = "\n".join(
        line.strip() for line in clean_content.splitlines() if line.strip()
    )

    return clean_content

def split_cleaned_content(cleaned_content, max_length=6000):
    return [
        cleaned_content[i : i + max_length] for i in range(0, len(cleaned_content), max_length)
    ]
