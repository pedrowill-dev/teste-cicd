import requests
from bs4 import BeautifulSoup

def get_title(url: str) -> str:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.title.string if soup.title else "Sem título"


def test_google_title():
    title = get_title("https://www.google.com")
    assert "Google" in title


