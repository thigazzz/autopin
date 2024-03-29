from unittest.mock import patch, Mock
from autopin import cli as sut
from autopin.entites import Image, Topic
from .factory.make_fake_html import make_fake_html

@patch("requests.get")
def test_show_all_today_topics(mocked_get, monkeypatch, capsys):
    """
    >> autopin topics

    >>> - Topic1: Description1
    >>> - Topic2: Description2
    >>> - Topic3: Description3
    """
    mocked_get.return_value = Mock(text=make_fake_html('topic', 1), status_code=200)
    monkeypatch.setattr("sys.argv", ["dir", "topics"])
    sut.run()

    out, _ = capsys.readouterr()

    assert "any1: any1" in out


@patch("autopin.images.Images.get_images_from_topic")
@patch("autopin.topics.Topics.get_today_topics")
def test_show_images_from_topic(Topics_mocked, Images_mocked, monkeypatch, capsys):
    """
    >> autopin images [topic] 

    >>> - Image1: Description1
    >>> - Image2: Description2
    >>> - Image3: Description3
    """
    Topics_mocked.return_value = [
        Topic(name="any", description="any", url="any"),
        Topic(name="any2", description="any2", url="any2"),
    ]

    Images_mocked.return_value = [
        Image(name="any title 1", src="any link 1", topic="any", id=1),
        Image(name="any title 2", src="any link 2", topic="any", id=2),
        Image(name="any title 3", src="any link 3", topic="any", id=3),
    ]
    monkeypatch.setattr("sys.argv", ["dir", "images", "any"])
    sut.run()

    out, _ = capsys.readouterr()

    assert "any title 1: any link 1" in out
    assert "any title 2: any link 2" in out
    assert "any title 3: any link 3" in out
