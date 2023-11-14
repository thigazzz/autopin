from dataclasses import dataclass
from typing import List
from itertools import count
from unittest.mock import patch, Mock
import requests
from bs4 import BeautifulSoup
from .fakes.html import html_w_1_e, html_w_3_e, html_w_m11_e
from pytest import mark


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

    def get_images_from_topic(self, topic: str, ammount=5) -> List[Image]:
        """
        Raspa dados de imagens de um respectivo tópico e estrutura em
        uma lista de Imagens (Images)

        Param:
            Topic: Um tópico
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


@patch("requests.get")
@mark.parametrize(
    "html,expected",
    [
        (html_w_1_e, [Image(id=1, topic="any", src="any", name="any")]),
        (
            html_w_3_e,
            [
                Image(id=1, topic="any", src="any", name="any"),
                Image(id=2, topic="any", src="any", name="any"),
                Image(id=3, topic="any", src="any", name="any"),
            ],
        ),
        (
            html_w_m11_e,
            [
                Image(id=1, topic="any", src="any", name="any"),
                Image(id=2, topic="any", src="any", name="any"),
                Image(id=3, topic="any", src="any", name="any"),
                Image(id=4, topic="any", src="any", name="any"),
                Image(id=5, topic="any", src="any", name="any"),
            ],
        ),
    ],
)
def test_get_and_stucture_an_image(mock_request, html, expected):
    mock_request.return_value = Mock(text=html, status_code=200)
    scrapper = Scrapper()
    topic = Topic(name="any", url="any")
    sut = Images(scrapper)

    result = sut.get_images_from_topic(topic)

    assert result == expected


@patch("requests.get")
def test_get_images_according_to__last_number(mock_request):
    mock_request.return_value = Mock(text=html_w_m11_e, status_code=200)
    scrapper = Scrapper()
    expected_10_images = 10
    topic = Topic(name="any", url="any")
    sut = Images(scrapper)

    result = sut.get_images_from_topic(topic, ammount=10)

    assert len(result) == expected_10_images
