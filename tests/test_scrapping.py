from src.scrapping.scrap import get_title


def test_google_title():
    title = get_title("https://www.google.com")
    assert "Google" in title


