import pytest
from autopin.today import get_topics
from .fake_html import fake_html


def test_get_topics_from_today():
    html = fake_html

    topics = get_topics(html)

    assert topics == {
        "day": "8 de Novembro de 2023",
        "topics": [{"title": "Natureza", "description": "Ar livre"}],
    }


def test_show_message_says_there_were_problems_picking_topics():
    html = "broken html"

    with pytest.raises(Exception) as error:
        get_topics(html)

    assert str(error.value) == "Tivemos problemas ao coletar os tópicos de hoje"
