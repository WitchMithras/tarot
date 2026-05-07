"""Tarot and astrological correspondence utilities."""

__version__ = "0.1.0"

from .core import (
	check_element,
	draw_tarot_card,
	draw_tarot_read,
	get_decan_card,
	get_decan_index,
	next_card,
	pick_cards,
	shuffle_deck,
)

__all__ = [
	"__version__",
	"get_decan_index",
	"get_decan_card",
	"check_element",
	"shuffle_deck",
	"next_card",
	"pick_cards",
	"draw_tarot_card",
	"draw_tarot_read"
]
