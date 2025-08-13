import streamlit as st


def format_url(url):
    if url.startswith('http://'):
        url = url[len('http://'):]
    elif url.startswith('https://'):
        url = url[len('https://'):]
        
    if url.startswith('www.'):
        url = url[len('www.'):]

    formatted_url = 'https://www.' + url
    return formatted_url

st.title('Website Connectivity Checker 🌐')
