from typing import List
from .entites import Topic
from .scrapper import Scrapper


class Topics:
    def __init__(self, scrapper: Scrapper) -> None:
        self.scrapper = scrapper

    def get_today_topics(self) -> List[Topic]:
        """
        Extraí quais são os tópicos recomendados hoje
        """
        soup = self.scrapper.request_page("https://br.pinterest.com/today/")

        topics_cards = self.scrapper.find_all_by_attributes(
            soup, {"data-test-id": "today-tab-article"}
        )

        topics = []
        for topic_card in topics_cards:
            topic_title = self.scrapper.find_one(
                topic_card, "a > div > div > div > div > div > div > div > div > div"
            ).text
            topic_description = self.scrapper.find_one(
                topic_card, "a > div > div > div > div > div > div > div h1"
            ).text
            topic_link = topic_card.find("a")["href"]
            topics.append(
                Topic(name=topic_title, description=topic_description, url=topic_link)
            )

        return topics
