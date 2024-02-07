"""
Module containing struct objects used throughout the application.
"""

from dataclasses import dataclass

@dataclass
class Image:
    """
    Data structure representing an image in the application.

    Attributes:
        - id (int): Unique identifier for identification.
        - topic (str): The topic from which the image originated.
        - src (str): Link to the image (web).
        - name (str): Title of the image (obtained from the site).
    """
    id: int
    topic: str
    src: str
    name: str


@dataclass
class Topic:
    """
    Data structure representing a topic in the application.

    Attributes:
        - name (str): Title of the topic (obtained from the site).
        - description (str): Description of the topic (obtained from the site).
        - url (str): Link to the topic page on Pinterest.
    """
    name: str
    description: str
    url: str

