import sys
from .today import show_topics


def _pretty_print(content):
    text = ""
    for item in content:
        text += "- " + item + "\n"

    return text


def run():
    """

    command: autopin today topics

    result: Mostrar os tópicos de hoje em uma lista
    """
    command = sys.argv

    if command[1] == "today" and command[2] == "topics":
        topics = show_topics()
        print("\n Esses são os tópicos de hoje: \n\n" + _pretty_print(topics))
