from typing import List, Any
from itertools import count
from autopin.entities import Image, Topic
from autopin.scrapper import Scrapper


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

        soup = self.scrapper.request_page(topic.url)

        images = []
        image_cards = self.scrapper.find_all_by_attribute(
            soup, {"data-test-id": "pin-visual-wrapper"}
        )

        for index in range(0, ammount):
            try:
                images.append(self.__get_image(image_cards[index], topic))
            except IndexError:
                break

        return images

    def __get_image(self, image_element, topic):
        """
        Extrai informações de uma imagem

        Param:
            image_element: Elemento de imagem
            Topic: Topic da Imagem (vai mudar)

        Returns:
            Uma instancia de Imagem
        """
        image = self.scrapper.find_element(image_element, "div > div img")
        name, link = self.__get_informations_from_image(image)
        return Image(id=next(self.counter), topic=topic.name, src=link, name=name)

    def __get_informations_from_image(self, image_element: Any) -> List[str]:
        """
        Extrai os atributos 'alt' e 'src' de uma elemento de imagem

        Param:
            image_element: Elemento de imagem

        Returns:
            Os valore de 'alt' e 'src' em lista

        """
        name = self.scrapper.get_attribute(image_element, "alt")
        link = self.scrapper.get_attribute(image_element, "src")
        return name, link
