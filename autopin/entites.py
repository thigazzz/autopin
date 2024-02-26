"""
Module containing struct objects used throughout the application.
"""

from collections import namedtuple

"""
Data structure representing an image in the application.
Attributes:
    - id (int): Unique identifier for identification.
    - topic (str): The topic from which the image originated.
    - src (str): Link to the image (web).
    - name (str): Title of the image (obtained from the site).
"""
Image = namedtuple("Image", 'id, topic, src, name')


"""
Data structure representing a topic in the application.
Attributes:
    - name (str): Title of the topic (obtained from the site).
    - description (str): Description of the topic (obtained from the site).
    - url (str): Link to the topic page on Pinterest.
"""
Topic = namedtuple("Topic", "name, description, url")
