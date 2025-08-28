from bs4 import BeautifulSoup
import requests

def get_title(url):

    response = requests.get(url)
    parser = BeautifulSoup(response.content, 'html.parser')
    return parser.title