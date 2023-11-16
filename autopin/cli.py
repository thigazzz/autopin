import sys
from typing import List
from .entites import Topic, Image
from .topics import Topics
from .scrapper import Scrapper
from .images import Images


def show_topics(topics: List[Topic]) -> str:
    text = ""
    for topic in topics:
        text += "- {}: {}\n".format(topic.name, topic.description)

    return text


def show_images(images: List[Image]) -> str:
    text = ""
    for image in images:
        text += "- {}: {}\n".format(image.name, image.src)

    return text


def run():
    """

    command: autopin today topics

    result: Mostrar os tópicos de hoje em uma lista
    """
    command = sys.argv

    if command[1] == "topics":
        topics = Topics(Scrapper())
        today_topics = topics.get_today_topics()
        print("\n Esses são os tópicos de hoje: \n\n" + show_topics(today_topics))
    if command[1] == "images":
        _s = Scrapper()
        topics = Topics(_s)
        today_topics = topics.get_today_topics()
        _images_obj = Images(_s)

        for today_topic in today_topics:
            if today_topic.name in command[2].replace("-", " ").strip():
                _topic = today_topic
                images = _images_obj.get_images_from_topic(_topic)
                print(
                    "\n Esses são as imagens e seus links do tópico {}: \n\n {}".format(
                        command[2], show_images(images)
                    )
                )


if __name__ == "__main__":
    run()
