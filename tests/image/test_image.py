from unittest.mock import patch, Mock
from .fakes.html import html_w_1_e, html_w_3_e, html_w_m11_e
from pytest import mark
from autopin.images import Images
from autopin.entities import Image, Topic
from autopin.scrapper import Scrapper


@patch("requests.get")
@mark.parametrize(
    "html,expected",
    [
        (html_w_1_e, [Image(id=1, topic="any", src="any", name="any")]),
        (
            html_w_3_e,
            [
                Image(id=1, topic="any", src="any", name="any"),
                Image(id=2, topic="any", src="any", name="any"),
                Image(id=3, topic="any", src="any", name="any"),
            ],
        ),
        (
            html_w_m11_e,
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
    topic = Topic(name="any", description="any")
    topic.url = "any"
    sut = Images(scrapper)

    result = sut.get_images_from_topic(topic)

    assert result == expected


@patch("requests.get")
def test_get_images_according_to__last_number(mock_request):
    mock_request.return_value = Mock(text=html_w_m11_e, status_code=200)
    scrapper = Scrapper()
    expected_10_images = 10
    topic = Topic(name="any", description="any")
    topic.url = "any"
    sut = Images(scrapper)

    result = sut.get_images_from_topic(topic, ammount=10)

    assert len(result) == expected_10_images
