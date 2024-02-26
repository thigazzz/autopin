"""
Module containing well-structured functions for web scraping Pinterest
"""
from typing import Any
import requests
from bs4 import BeautifulSoup


class Scrapper:
    def __init__(self):
        self.HTML = None
    def request_page(self, url) -> Any:
        """
        Requests a page

        Args:
            url: URL of the page

        Returns:
            An instance of a scraper (Beautiful Soup, etc)
        """
        html = requests.get(url).text
        self.HTML = BeautifulSoup(html, "html.parser")

    def find_children(self, parent, selector: str):
        return parent.select_one(selector)
        
    def find_all_by_attributes(self, obj: Any, attrs: dict[str, str]) -> Any:
        return self.HTML.find_all(attrs=attrs)


    def get_attribute(self, obj, name) -> str:
        return obj[name]
