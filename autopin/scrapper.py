"""
Module containing well-structured functions for web scraping Pinterest
"""
from typing import Any
import requests
from bs4 import BeautifulSoup


class Scrapper:
    def request_page(self, url) -> Any:
        """
        Requests a page

        Args:
            url: URL of the page

        Returns:
            An instance of a scraper (Beautiful Soup, etc)
        """
        html = requests.get(url).text
        return BeautifulSoup(html, "html.parser")

    def find_one(self, obj: Any, selector: str) -> Any:
        """
        Selects an element by selector

        Args:
            obj: An instance of a scraper (Beautiful Soup, etc)
            selector: Path to locate the element in the HTML

        Returns:
            An element
        """
        return obj.select_one(selector)
    def find_all_by_attributes(self, obj: Any, attrs: dict[str, str]) -> Any:
        return obj.find_all(attrs=attrs)


    def get_from_attribute(self, obj, name) -> str:
        return obj[name]
