"""
Module to get images from a topic
"""
from typing import List
from itertools import count
from .entites import Image, Topic
from .scrapper import Scrapper
from .selectors import CSS


class Images:
    counter = count(1)

    def __init__(self, scrapper: Scrapper) -> None:
        self.scrapper = scrapper

    def get_images_from_topic(self, topic: Topic, ammount=5) -> List[Image]:
        """
        Get main informations of a image from a topic

        Param:
            Topic: An instance of Topic
            Ammount: Amount of images to get, default 5

        Result:
            A list of images
        """
        self.counter = count(1)
        soup = self.scrapper.request_page("https://br.pinterest.com" + topic.url)

        image_cards = self.scrapper.find_all_by_attributes(
            soup, {"data-test-id": "pin-visual-wrapper"}
        )

        images = []
        for index in range(0, ammount):
            try:
                image, name, link = self._get_image_element(image_cards[index])
                images.append(
                    Image(id=next(self.counter), topic=topic.name, src=link, name=name)
                )
            except IndexError:
                break

        return images

    def _get_image_element(self, parent_element):
            image = self.scrapper.find_children(parent_element, CSS["image"])
            name = self.scrapper.get_attribute(image, "alt")
            link = self.scrapper.get_attribute(image, "src")
            return  [image, name, link]
