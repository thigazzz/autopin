from dataclasses import dataclass
from typing import List
from itertools import count
from unittest.mock import patch, Mock
import requests
from bs4 import BeautifulSoup
from .fakes.html import html_w_1_e, html_w_3_e


@dataclass
class Image:
    id: int
    topic: str
    src: str
    name: str


@dataclass
class Topic:
    name: str
    url: str


class Scrapper:
    ...


class Images:
    counter = count(1)

    def __init__(self, scrapper: Scrapper) -> None:
        self.scrapper = scrapper

    def get_images_from_topic(self, topic: str) -> List[Image]:
        """
        Raspa dados de imagens de um respectivo tópico e estrutura em
        uma lista de Imagens (Images)

        Param:
            Topic: Um tópico

        Result:
            Conjunto de Imagens
        """
        self.counter = count(1)
        html = requests.get(topic.url).text

        soup = BeautifulSoup(html, "html.parser")

        images = []
        image_cards = soup.find_all(attrs={"data-test-id": "pin-visual-wrapper"})
        for image_card in image_cards:
            image = image_card.select_one("div > div img")
            name = image["alt"]
            link = image["src"]
            images.append(
                Image(id=next(self.counter), topic=topic.name, src=link, name=name)
            )

        return images


@patch("requests.get")
def test_get_and_stucture_an_image(mock_request):
    mock_request.return_value = Mock(text=html_w_1_e, status_code=200)
    scrapper = Scrapper()
    expected = [Image(id=1, topic="any", src="any", name="any")]
    topic = Topic(name="any", url="any")
    sut = Images(scrapper)

    result = sut.get_images_from_topic(topic)

    assert result == expected


@patch("requests.get")
def test_get_and_stucture_an_ammount_of_images(mock_request):
    mock_request.return_value = Mock(text=html_w_3_e, status_code=200)
    scrapper = Scrapper()
    expected = [
        Image(id=1, topic="any", src="any", name="any"),
        Image(id=2, topic="any", src="any", name="any"),
        Image(id=3, topic="any", src="any", name="any"),
    ]
    topic = Topic(name="any", url="any")
    sut = Images(scrapper)

    result = sut.get_images_from_topic(topic)
    print(result)

    assert result == expected
