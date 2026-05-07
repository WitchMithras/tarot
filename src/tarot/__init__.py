"""tarot staging package shim.
"""

from .core import (
	get_decan_index,
	get_decan_card,
	check_element,
	shuffle_deck,
	next_card,
	pick_cards,
	draw_tarot_card,
	draw_tarot_read

)

__all__ = [
	"get_decan_index",
	"get_decan_card",
	"check_element",
	"shuffle_deck",
	"next_card",
	"pick_cards",
	"draw_tarot_card",
	"draw_tarot_read"
]
