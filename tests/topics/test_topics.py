from pytest import mark
from unittest.mock import patch, Mock
from autopin.entities import Topic
from autopin.scrapper import Scrapper
from autopin.topics import Topics
from .fake.html import html_w_1_e, html_w_2_e


@patch("requests.get")
@mark.parametrize(
    "fake_html,expected",
    [
        (html_w_1_e, [Topic(name="any", description="any", url="any")]),
        (
            html_w_2_e,
            [
                Topic(name="any", description="any", url="any"),
                Topic(name="any2", description="any2", url="any2"),
            ],
        ),
    ],
)
def test_get_today_recommended_topics(mock_requests, fake_html, expected):
    mock_requests.return_value = Mock(text=fake_html, status_code=200)
    scrapper = Scrapper()
    sut = Topics(scrapper)

    result = sut.get_today_topics()

    assert result == expected
