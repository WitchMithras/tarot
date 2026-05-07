from tarot import __version__, get_decan_card, pick_cards


def test_package_exposes_version():
    assert __version__ == "0.1.0"


def test_get_decan_card_returns_expected_correspondence():
    assert get_decan_card("Aries", 0) == {
        "sign": "Aries",
        "ruler": "Mars",
        "card": "Two of Wands",
    }


def test_pick_cards_returns_requested_count():
    assert len(pick_cards(3)) == 3
