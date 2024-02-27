from unittest.mock import patch, Mock
from pytest import mark
from autopin.images import Images
from autopin.entites import Image
from autopin.scrapper import Scrapper
from autopin.topics import Topic
from .factory.make_fake_html import make_fake_html


@patch("requests.get")
@mark.parametrize(
    "html,expected",
    [
        (make_fake_html('image', 1), [Image(id=1, topic="any", src="any", name="any")]),
        (
            make_fake_html('image', 3),
            [
                Image(id=1, topic="any", src="any", name="any"),
                Image(id=2, topic="any", src="any", name="any"),
                Image(id=3, topic="any", src="any", name="any"),
            ],
        ),
        (
            make_fake_html('image', 11),
            [
                Image(id=1, topic="any", src="any", name="any"),
                Image(id=2, topic="any", src="any", name="any"),
                Image(id=3, topic="any", src="any", name="any"),
                Image(id=4, topic="any", src="any", name="any"),
                Image(id=5, topic="any", src="any", name="any"),
            ],
        ),
    ],
)
def test_get_and_stucture_an_image(mock_request, html, expected):
    mock_request.return_value = Mock(text=html, status_code=200)
    scrapper = Scrapper()
    topic = Topic(name="any", description="any", url="any")
    sut = Images(scrapper)

    result = sut.get_images_from_topic(topic)

    assert result == expected


@patch("requests.get")
def test_get_images_according_to__last_number(mock_request):
    """
    Test the feature of get a defined number of images
        
    Input:
    >>> get_images_from_topic(any_topic, 5)

    Expect:
       result (list(Topic)[5]: A list of five images

    Input:
    >>> get_images_from_topic(any_topic, 20)

    Expect:
       result (list(Topic)[20]: A list of twenty images
    """
    mock_request.return_value = Mock(text=make_fake_html('image', 11), status_code=200)
    scrapper = Scrapper()
    expected_10_images = 10
    topic = Topic(name="any", description="any", url="any")
    sut = Images(scrapper)

    result = sut.get_images_from_topic(topic, ammount=10)

    assert len(result) == expected_10_images
