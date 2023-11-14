from typing import Any
import requests
from bs4 import BeautifulSoup


class Scrapper:
    def request_page(self, url) -> Any:
        """
        Requisita uma página

        Param:
            url: URL da página

        Returns:
            Uma instancia de algum scrapper (Beatiful Soup, etc)
        """
        html = requests.get(url).text
        return BeautifulSoup(html, "html.parser")

    def find_all_by_attributes(self, obj: Any, attrs: dict[str, str]) -> Any:
        """
        Seleciona todos os elementos pelo seu atributo

        Param:
            obj: Uma instancia de algum scrapper (Beatiful Soup, etc)
            attrs: Dicionario do Nome e Valor do Atributo {nome: valor}

        Returns:
            Um conjunto de Elementos
        """
        return obj.find_all(attrs=attrs)

    def find_one(self, obj: Any, selector: str) -> Any:
        """
        Seleciona um elementos por seletor

        Param:
            obj: Uma instancia de algum scrapper (Beatiful Soup, etc)
            seletor: Caminho para localizar elemento no HTML

        Returns:
            Um elemento
        """
        return obj.select_one(selector)

    def get_from_attribute(self, obj, name) -> str:
        """
        Pega o valor de um atributo de um elemento

        Param:
            obj: Uma instancia de algum scrapper (Beatiful Soup, etc)
            name: Nome do atributo

        Returns:
            Valor do atributo
        """
        return obj[name]
