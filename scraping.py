import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from bs4 import BeautifulSoup

chromedriver_autoinstaller.install()

def scraping(website):
    print('Launching chrome driver...')
    
    #chrome_path = './chromedriver.exe'
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    

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
