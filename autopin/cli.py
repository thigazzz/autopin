"""
Module defining and organizing the CLI functionality.
"""

import sys
from typing import List
from .entites import Topic, Image
from .topics import Topics
from .scrapper import Scrapper
from .images import Images

def in_list(key, item):
    return "- {}: {}\n".format(key, item)

def show_topics(topics: List[Topic]) -> str:
    text = ""
    for topic in topics:
        text += in_list(topic.name, topic.description)

    return text


def show_images(images: List[Image]) -> str:
    text = ""
    for image in images:
        text += in_list(image.name, image.src)

    return text

def get_topics_command() -> None:
    today_topics = topics_obj.get_today_topics()
    print("\n Esses são os tópicos de hoje: \n\n" + show_topics(today_topics))

def get_images_command(topic_from_gui: str) -> None:
    today_topics = topics_obj.get_today_topics()
    for today_topic in today_topics:
        if today_topic.name in topic_from_gui.replace("-", " ").strip():
            _topic = today_topic
            images = images_obj.get_images_from_topic(_topic)
            print(
                "\n Esses são as imagens e seus links do tópico {}: \n\n {}".format(
                    topic_from_gui, show_images(images)
                )
            )
            return


scrapper_obj = Scrapper()
topics_obj = Topics(scrapper_obj)
images_obj = Images(scrapper_obj)


def run():
    """
    Main function to run the CLI. Get the commands and direct to the right place.

    Structure of command:
        python3 [section] [args]

        - section: can be 'topics' or 'images'

    Section 'Topics':
        
        Return all topics from Pinterest Explorer in a list.

        >>> python3 topics
        >>> - topic1: description1
        >>> - topic2: description2
        >>> - topic3: description3
    
    Section 'Images':
        
        Return all images from a topic.

        >>> python3 images [topic] 
        tip: the topic must be separate by '-' not spaces.
        Example: is 'any-topic-1', not 'any topic 1'
        >>> - image1: src1 
        >>> - image2: src2 
        >>> - image3: src3 
    """
    command = sys.argv

    if command[1] == "topics":
        get_topics_command()

    if command[1] == "images":
        get_images_command(command[2])


if __name__ == "__main__":
    run()
