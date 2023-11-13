from unittest.mock import patch, Mock
from autopin.today import get_images_from_today_topic as sut
from .fake_html import fake_html_for_get_images_test


@patch("requests.get")
def test_get_images_from_today_topic(mocked_get):
    mocked_get.return_value = Mock(text=fake_html_for_get_images_test, status_code=200)
    images_from_today = sut(
        {
            "title": "any topic",
            "description": "...",
            "link": "today/best/unhas-amendoadas/115555/",
        }
    )

    assert images_from_today == {"topic": "any topic", "images": [{"link": "any link"}]}
