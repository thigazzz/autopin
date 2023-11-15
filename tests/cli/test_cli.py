import sys
from unittest.mock import patch, Mock
from autopin import cli as sut
from ..today.fake_html import fake_html_with_two_topics


@patch("requests.get")
def test_show_all_today_topics(mocked_get, monkeypatch, capsys):
    """
    command: autopin today topics

    result:
    - Natureza: Respectiva Descrição
    - Carros
    - Etc
    """
    mocked_get.return_value = Mock(text=fake_html_with_two_topics, status_code=200)
    monkeypatch.setattr("sys.argv", ["dir", "today", "topics"])
    sut.run()

    out, _ = capsys.readouterr()

    assert "Natureza: Ar livre" in out
