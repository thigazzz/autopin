import sys
from typing import List
from .entites import Topic
from .topics import Topics
from .scrapper import Scrapper


def show_topics(topics: List[Topic]):
    text = ""
    for topic in topics:
        text += "- {}: {}\n".format(topic.name, topic.description)

    return text


def run():
    """

    command: autopin today topics

    result: Mostrar os tópicos de hoje em uma lista
    """
    command = sys.argv

    if command[1] == "today" and command[2] == "topics":
        topics = Topics(Scrapper())
        today_topics = topics.get_today_topics()
        print("\n Esses são os tópicos de hoje: \n\n" + show_topics(today_topics))
