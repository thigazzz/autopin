from typing import List
from itertools import count
import requests
from bs4 import BeautifulSoup
from autopin.entities import Image, Topic


class Scrapper:
    ...


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
        html = requests.get(topic.url).text

        soup = BeautifulSoup(html, "html.parser")

        images = []
        image_cards = soup.find_all(attrs={"data-test-id": "pin-visual-wrapper"})

        for index in range(0, ammount):
            try:
                image = image_cards[index].select_one("div > div img")
            except IndexError:
                break
            name = image["alt"]
            link = image["src"]
            images.append(
                Image(id=next(self.counter), topic=topic.name, src=link, name=name)
            )

        return images
