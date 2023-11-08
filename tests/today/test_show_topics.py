import pytest
from unittest.mock import Mock, patch
from autopin.today import show_topics
from .fake_html import fake_html_with_two_topics


@patch("requests.get")
def test_get_today_topics_from_pinterest(mocked_get):
    mocked_get.return_value = Mock(text=fake_html_with_two_topics, status_code=200)
    sut = show_topics

    topics = sut()

    assert topics == ["Natureza: Ar livre", "Carros: Os melhores"]


@patch("requests.get")
def test_show_site_server_error_when_request_fails(mocked_get):
    mocked_get.return_value = Mock(status_code=400)
    sut = show_topics

    with pytest.raises(Exception) as error:
        topics = sut()
        assert topics == None

    assert str(error.value) == "Erro ao se conectar ao site do Pinterest"
