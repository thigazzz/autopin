from typing import Any
import requests
from bs4 import BeautifulSoup


class Scrapper:
    def request_page(self, url: str) -> Any:
        """ "
        Faz uma requisição GET para alguma URL

        Param:
            url: URL da página

        Returns:
            Um objeto de algum Scrapper (Beatiful Soup, etc)
        """
        html = requests.get(url).text
        return BeautifulSoup(html, "html.parser")

    def find_all_by_attribute(self, obj: Any, attrs: dict[str, str]) -> Any:
        """
        Seleciona elementos a partir de seus atributos

        Param:
            obj: Instancia de algum Scrapper (Beatiful Soup, etc)
            attrs: Dicionario com chave e valor do atributo {atributo: valor}

        Returns:
            Lista de Elementos selecionados
        """
        return obj.find_all(attrs=attrs)

    def find_element(self, obj: Any, selector: str) -> Any:
        """ "
        Seleciona um elemento de acordo com seu seletor

        Param:
            obj: Instancia de algum Scrapper (Beatiful Soup, etc)
            selector: Seletor para selecionar elemento

        Returns:
            Um elemento
        """
        return obj.select_one(selector)

    def get_attribute(self, obj: Any, name: str) -> Any:
        """ "
        Seleciona atributo de um elemento

        Param:
            obj: Instancia de algum Scrapper (Beatiful Soup, etc)
            name: atributo a ser selecionado

        Returns:
            Um elemento
        """
        return obj[name]
