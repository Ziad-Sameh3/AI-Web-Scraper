import streamlit as st
from scraping import scraping, extract_body_content, clean_body_content, split_cleaned_content
from parsing import parse_content
url = st.text_input("Enter a Website URL")

if st.button("Scrape Site"):
    
    st.write("Scraped Content")
    result = scraping(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    
    st.session_state.content = cleaned_content
    with st.expander('View Content'):
        st.text_area("Content Extracted", cleaned_content, height=300)

if "content" in st.session_state:
    parse_description = st.text_area("Describe What You Want To Parse?")
    
    if st.button('Parse Content'):
        st.write("Parsed Conent")
        splited_content = split_cleaned_content(st.session_state.content)
        
        result = parse_content(splited_content, parse_description)
        st.write(result)