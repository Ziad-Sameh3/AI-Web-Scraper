'''import streamlit as st
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def scraping(website):
    st.write("Launching Chrome driver...")
    

def scraping(website):
    print('Launching chrome driver...')
   
    chrome_path = './chromedriver.exe'
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_path), options=options)

    driver.get(website)
    html = driver.page_source
    return html

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content,'html.parser')
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for scriptOrStyle in soup(['script', 'style']):
        scriptOrStyle.extract()

    clean_content = soup.get_text(separator='\n')
    clean_content = "\n".join(
        line.strip() for line in clean_content.splitlines() if line.split()
    )

    return clean_content

def split_cleaned_content(cleaned_content, max_length=6000):

    return [
        cleaned_content[i : i + max_length] for i in range(0, len(cleaned_content), max_length)
        ]
'''
import streamlit as st
from bs4 import BeautifulSoup
import asyncio
from pyppeteer import launch

async def fetch_html(website):
    # Launching a headless browser instance with Pyppeteer
    browser = await launch(headless=True, args=['--no-sandbox', '--disable-dev-shm-usage'])
    page = await browser.newPage()
    await page.goto(website)
    html = await page.content()
    await browser.close()
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

# Streamlit app interface
website = st.text_input("Enter website URL")
if st.button("Fetch Content"):
    if website:
        st.write("Fetching content, please wait...")
        # Run the fetch_html coroutine
        html_content = asyncio.run(fetch_html(website))
        body_content = extract_body_content(html_content)
        cleaned_content = clean_body_content(body_content)
        split_content = split_cleaned_content(cleaned_content)
        
        for part in split_content:
            st.write(part)
