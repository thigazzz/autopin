from typing import List
from itertools import count
from .entites import Image, Topic
from .scrapper import Scrapper


class Images:
    counter = count(1)

    def __init__(self, scrapper: Scrapper) -> None:
        self.scrapper = scrapper

    def get_images_from_topic(self, topic: Topic, ammount=5) -> List[Image]:
        """
        Raspa dados de imagens de um respectivo tópico e estrutura em
        uma lista de Imagens (Images)

        Param:
            Topic: Um objeto de tópico
            Ammount: Quantidade de imagens a serem pegas

        Result:
            Conjunto de Imagens
        """
        self.counter = count(1)
        soup = self.scrapper.request_page("https://br.pinterest.com" + topic.url)

        images = []
        image_cards = self.scrapper.find_all_by_attributes(
            soup, {"data-test-id": "pin-visual-wrapper"}
        )

        for index in range(0, ammount):
            try:
                image = self.scrapper.find_one(image_cards[index], "div > div img")
            except IndexError:
                break
            name = self.scrapper.get_from_attribute(image, "alt")
            link = self.scrapper.get_from_attribute(image, "src")
            images.append(
                Image(id=next(self.counter), topic=topic.name, src=link, name=name)
            )

        return images
