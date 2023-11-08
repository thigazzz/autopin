"""

Coleta tópicos, imagens, etc, recomendada no site do Pinterest

"""
import requests
from bs4 import BeautifulSoup


def show_topics():
    """ "

    Faz a requição para o Pinterest e mostra os topics de hoje

    >>> show_topics()
    - Natureza
    - Carros

    """
    url = "https://br.pinterest.com/today/"
    request = requests.get(url)

    if request.status_code != 200:
        raise Exception("Erro ao se conectar ao site do Pinterest")

    topics = get_topics(request.text)
    print(topics["topics"])

    _topics = []

    for topic in topics["topics"]:
        print(topic["title"])
        _topics.append("{}: {}".format(topic["title"], topic["description"]))

    return _topics


def get_topics(content: str) -> dict[str, str | list]:
    """

    Coleta tópicos do dia do HTML

    >>> get_topics("<html>...</html>")
    {
        "day": "8 de Novembro de 2023"
        "topics": [
            {
                "title": "Natureza"
                "description"; "Ar livre"
            }
        ]
    }

    """
    soup = BeautifulSoup(content, "html.parser")

    try:
        today = soup.find(attrs={"data-test-id": "today-tab-header"}).text.strip()
        topics_cards = soup.find_all(attrs={"data-test-id": "today-tab-article"})

        topics = []
        for topic_card in topics_cards:
            topic_title = topic_card.select_one(
                "a > div > div > div > div > div > div > div > div > div"
            ).text
            topic_description = topic_card.select_one(
                "a > div > div > div > div > div > div > div h1"
            ).text
            topics.append({"title": topic_title, "description": topic_description})

        return {"day": today, "topics": topics}
    except:
        raise Exception("Tivemos problemas ao coletar os tópicos de hoje")
