"""
Module to get topics from the Explore page of Pinterest
"""
from typing import List
from .entites import Topic
from .scrapper import Scrapper
from .selectors import CSS


class Topics:
    def __init__(self, scrapper: Scrapper) -> None:
        self.scrapper = scrapper

    def get_today_topics(self) -> List[Topic]:
        """
        Get topics from the Explore page of Pinterest

        Params:
            scrapper: instance of a Scrapper
        
        Results:
            A list of all topics
        """

        html = self.scrapper.request_page("https://br.pinterest.com/today/")

        topics_cards = self.scrapper.find_all_by_attributes(
            html, {"data-test-id": "today-tab-article"}
        )

        topics = []
        for topic_card in topics_cards:
            topic_title, topic_description, topic_link = self._get_topic_card_element(topic_card)
            topics.append(
                Topic(name=topic_title, description=topic_description, url=topic_link)
            )

        return topics

    def _get_topic_card_element(self, parent_element):
        topic_title = self.scrapper.find_one(
            parent_element, CSS["topic_title"]
        ).text
        topic_description = self.scrapper.find_one(
            parent_element, CSS["topic_description"]
        ).text.strip()
        topic_link = self.scrapper.find_one(parent_element, CSS["anchor"])
        topic_link = self.scrapper.get_from_attribute(topic_link, "href")
        return [topic_title, topic_description, topic_link]
