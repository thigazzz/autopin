"""
Module defining and organizing the CLI functionality.
"""

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
