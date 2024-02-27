from pytest import mark
from unittest.mock import patch, Mock
from autopin.entites import Topic
from autopin.scrapper import Scrapper
from autopin.topics import Topics
from .factory.make_fake_html import make_fake_html


@patch("requests.get")
@mark.parametrize(
    "fake_html,expected",
    [
        (make_fake_html("topic", 1), [Topic(name="any1", description="any1", url="any1")]),
        (
            make_fake_html("topic", 2),
            [
                Topic(name="any1", description="any1", url="any1"),
                Topic(name="any2", description="any2", url="any2"),
            ],
        ),
    ],
)
def test_get_today_recommended_topics(mock_requests, fake_html, expected):
    """
    Expected:
        result (list(Topic)]: List of topics

    Mock:
        requests.get: Mock request
        fake_html: HTML with the scruture of topic in Pinterest site
    """
    mock_requests.return_value = Mock(text=fake_html, status_code=200)
    scrapper = Scrapper()
    sut = Topics(scrapper)

    result = sut.get_today_topics()

    assert result == expected
