"""

Coleta tópicos e faz donwload de imagens recomendadas no dia atual

"""
import requests
from bs4 import BeautifulSoup

URL = "https://br.pinterest.com/today/"
STATUS_CODE = {"success": "2", "failure": "4"}


def show_topics():
    """ "

    Faz a requição para o Pinterest e mostra os topics de hoje

    >>> show_topics()
    ["Natureza', "Carros"]

    """
    request = request_page(URL)

    if _is_request_failure(request.status_code):
        raise Exception("Erro ao se conectar ao site do Pinterest")

    topics = get_topics(request.text)

    return _format_topics(topics)


def request_page(url: str):
    return requests.get(URL)


def get_topics(content: str) -> dict[str, str | list]:
    """

    Coleta tópicos do dia do HTML

    >>> get_topics("<html>...</html>")
    {
        "day": "8 de Novembro de 2023"
        "topics": [
            {
                "title": "Natureza",
                "description"; "Ar livre",
                "link": "..."
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
            topic_link = topic_card.find("a")["href"]
            topics.append(
                {
                    "title": topic_title,
                    "description": topic_description,
                    "link": topic_link,
                }
            )

        return {"day": today, "topics": topics}
    except:
        raise Exception("Tivemos problemas ao coletar os tópicos de hoje")


def _is_request_failure(status_code: int) -> bool:
    status_code = list(str(status_code))

    if status_code[0] == STATUS_CODE["success"]:
        return False

    return True


def _format_topics(topics):
    return [
        _format_string_in_title_and_description(topic["title"], topic["description"])
        for topic in topics["topics"]
    ]


def _format_string_in_title_and_description(title, description):
    return "{}: {}".format(title, description)
