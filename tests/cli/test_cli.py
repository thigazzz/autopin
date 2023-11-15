import sys
from unittest.mock import patch, Mock
from autopin import cli as sut
from .fake.html import html_w_1_e


@patch("requests.get")
def test_show_all_today_topics(mocked_get, monkeypatch, capsys):
    """
    command: autopin today topics

    result:
    - Natureza: Respectiva Descrição
    - Carros
    - Etc
    """
    mocked_get.return_value = Mock(text=html_w_1_e, status_code=200)
    monkeypatch.setattr("sys.argv", ["dir", "today", "topics"])
    sut.run()

    out, _ = capsys.readouterr()

    assert "any topic: any description" in out
