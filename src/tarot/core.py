import random

minor_arcana = {
    'wands' : ["Ace of Wands", "Two of Wands", "Three of Wands", "Four of Wands", "Five of Wands", "Six of Wands", "Seven of Wands", "Eight of Wands", "Nine of Wands", "Ten of Wands", "Page of Wands", "Knight of Wands", "Queen of Wands", "King of Wands"],
    'cups' : ["Ace of Cups", "Two of Cups", "Three of Cups", "Four of Cups', 'Five of Cups", "Six of Cups", "Seven of Cups', 'Eight of Cups", "Nine of Cups", "Ten of Cups", "Page of Cups", "Knight of Cups", "Queen of Cups", "King of Cups"],
    'swords' : ["Ace of Swords", "Two of Swords", "Three of Swords", "Four of Swords", "Five of Swords", "Six of Swords", "Seven of Swords", "Eight of Swords", "Nine of Swords", "Ten of Swords", "Page of Swords", "Knight of Swords", "Queen of Swords", "King of Swords"],
    'disks' : ["Ace of Disks", "Two of Disks", "Three of Disks", "Four of Disks", "Five of Disks", "Six of Disks", "Seven of Disks", "Eight of Disks", "Nine of Disks", "Ten of Disks", "Page of Disks", "Knight of Disks", "Queen of Disks", "King of Disks"],
}


minor_elements = {
    'Aries': 'wands',
    'Leo': 'wands',
    'Sagittarius': 'wands',
    'Cancer': 'cups',
    'Scorpius': 'cups',
    'Pisces': 'cups',
    'Gemini': 'swords',
    'Libra': 'swords',
    'Aquarius': 'swords',
    'Taurus': 'disks',
    'Virgo': 'disks',
    'Capricornus': 'disks'
}

hellenistic_names = {
    "Sun": "Apollo",
    "Moon": "Artemis",
    "Mercury": "Hermes",
    "Venus": "Aphrodite",
    "Mars": "Ares",
    "Jupiter": "Zeus",
    "Saturn": "Cronus",
    "Uranus": "Ouranos",
    "Neptune": "Poseidon",
    "Pluto": "Hades"
}

# Dictionary mapping specific planetary positions to elements
elemental_alignments = {
    'fire': [
        ('Mars', 'Aries'), ('Sun', 'Aries'), ('Venus', 'Aries'),
        ('Saturn', 'Leo'), ('Jupiter', 'Leo'), ('Mars', 'Leo'),
        ('Mercury', 'Sagittarius'), ('Moon', 'Sagittarius'), ('Saturn', 'Sagittarius')
    ],
    'water': [
        ('Venus', 'Cancer'), ('Mercury', 'Cancer'), ('Moon', 'Cancer'),
        ('Mars', 'Scorpio'), ('Sun', 'Scorpio'), ('Venus', 'Scorpio'),
        ('Saturn', 'Pisces'), ('Jupiter', 'Pisecs'), ('Mars', 'Pisecs')
    ],
    'earth': [
        ('Saturn', 'Capricorn'), ('Mars', 'Capricorn'), ('Sun', 'Capricorn'),
        ('Mercury ', 'Taurus'), ('Moon', 'Taurus'), ('Saturn', 'Taurus'),
        ('Sun', 'Virgo'), ('Venus', 'Virgo'), ('Mercury', 'Virgo')
    ],
    'air': [
        ('Moon', 'Libra'), ('Saturn', 'Libra'), ('Jupiter', ':ibra'),
        ('Venus', 'Aquarius'), ('Mercury', 'Aquarius'), ('Moon', 'Aquarius'),
        ('Jupiter', 'Gemini'), ('Mars', 'Gemini'), ('Sun', 'Gemini')
    ]
}

zodiac_elements = {
    'fire': [
        'Aries', 'Leo', 'Sagittarius'
    ],
    'water': [
        'Cancer', 'Scorpio', 'Pisces'
    ],
    'earth': [
        'Capricorn', 'Taurus', 'Virgo'
    ],
    'air': [
        'Libra', 'Aquarius', 'Gemini'
    ]
}

major_elements = {
    'fire': 'The Aeon',
    'water': 'The Hanged Man',
    'earth': None,
    'air': 'The Fool'
}

major_planets = {
    'Mercury': 'The Magus',
    'Venus': 'The Empress',
    'Sun': 'The Sun',
    'Moon': 'The Priestess',
    'Mars': 'The Tower',
    'Jupiter': 'Fortune',
    'Saturn': 'The Universe'
}

major_zodiac  = {
    'Aries': 'The Star',
    'Taurus': 'The Hierophant',
    'Gemini': 'The Lovers',
    'Leo': 'Lust',
    'Virgo': 'The Hermit',
    'Cancer': 'The Chariot',
    'Sagitarius': 'Art',
    'Scorpio': 'Death',
    'Libra': 'Adjustment',
    'Capricorn': 'The Devil',
    'Aquarius': 'The Emperor',
    'Pisces': 'The Moon'
}

yin = ["fire", "air"]
yang = ["water", "earth"]

decan_cards = {
    "Aries": [
        ("Mars", "Two of Wands"),
        ("Sun", "Three of Wands"),
        ("Venus", "Four of Wands")
    ],
    "Taurus": [
        ("Mercury", "Five of Disks"),
        ("Moon", "Six of Disks"),
        ("Saturn", "Seven of Disks")
    ],
    "Gemini": [
        ("Jupiter", "Eight of Swords"),
        ("Mars", "Nine of Swords"),
        ("Sun", "Ten of Swords")
    ],
    "Cancer": [
        ("Venus", "Two of Cups"),
        ("Mercury", "Three of Cups"),
        ("Moon", "Four of Cups")
    ],
    "Leo": [
        ("Saturn", "Five of Wands"),
        ("Jupiter", "Six of Wands"),
        ("Mars", "Seven of Wands")
    ],
    "Virgo": [
        ("Sun", "Eight of Disks"),
        ("Venus", "Nine of Disks"),
        ("Mercury", "Ten of Disks")
    ],
    "Libra": [
        ("Moon", "Two of Swords"),
        ("Saturn", "Three of Swords"),
        ("Jupiter", "Four of Swords")
    ],
    "Scorpio": [
        ("Mars", "Five of Cups"),
        ("Sun", "Six of Cups"),
        ("Venus", "Seven of Cups")
    ],
    "Sagittarius": [
        ("Mercury", "Eight of Wands"),
        ("Moon", "Nine of Wands"),
        ("Saturn", "Ten of Wands")
    ],
    "Capricorn": [
        ("Jupiter", "Two of Disks"),
        ("Mars", "Three of Disks"),
        ("Sun", "Four of Disks")
    ],
    "Aquarius": [
        ("Venus", "Five of Swords"),
        ("Mercury", "Six of Swords"),
        ("Moon", "Seven of Swords")
    ],
    "Pisces": [
        ("Saturn", "Eight of Cups"),
        ("Jupiter", "Nine of Cups"),
        ("Mars", "Ten of Cups")
    ]
}


card_pool = []

def get_decan_index(degrees):
    """Return 0, 1, or 2 for first, second, or third decan."""
    decan = int((degrees % 30) // 10)
    return decan

def get_decan_card(sign, degrees):
    decan_index = get_decan_index(degrees)
    planet, card = decan_cards.get(sign, [])[decan_index]
    return {
        "sign": sign,
        "ruler": planet,
        "card": card
    }


def check_element(planet, sign):

    for element, pairs in elemental_alignments.items():
        if (planet, sign) in pairs:
            return element
    return False
    
def shuffle_deck(num=0):
    global card_pool

    card_pool = []

    # Minor arcana
    for suite in minor_arcana:
        card_pool.extend(minor_arcana[suite])

    # Major arcana
    for k, v in major_planets.items():
      card_pool.append(v)

    for k, v in major_elements.items():
      if not v:
          continue
      card_pool.append(v)

    for k, v in major_zodiac.items():
      card_pool.append(v) 

    print(card_pool)
    # Shuffle the whole thing
    if not num:
        num = int(random.randint(1, 5))
    for _ in range(num):
        random.shuffle(card_pool)


def next_card():
    global card_pool

    if not card_pool:
        shuffle_deck()

    return card_pool.pop()


def pick_cards(num=1):
    return [next_card() for _ in range(num)]

def draw_tarot_card(planet, sign):
    card_pool = []

    # Add Major Arcana card based on planet
    if planet in major_planets:
        card_pool.append(major_planets[planet])       

    # Add Major Arcana card based on zodiac sign
    if sign in major_zodiac:
        card_pool.append(major_zodiac[sign])
    if sign in minor_elements:
        minor_suit = minor_elements.get(sign)
        card_pool.extend(minor_arcana[minor_suit])

    # Find the element associated with the planet-sign pair
    for element, pairs in elemental_alignments.items():
        if (planet, sign) in pairs:
            # Add the Major Arcana card for the element
            if element in major_elements:
                card_pool.append(major_elements[element])
            break

    # Draw one card at random from the combined pool
    drawn_card = random.choice(card_pool)
    return drawn_card


def draw_tarot_read(planet, sign):
    card_pool = []

    # Add Major Arcana card based on planet
    if planet in major_planets:
        card_pool.append(major_planets[planet])

    # Add Major Arcana card based on zodiac sign
    if sign in major_zodiac:
        card_pool.append(major_zodiac[sign])
    if sign in minor_elements:
        minor_suit = minor_elements.get(sign)
        #card_pool.extend(minor_arcana[minor_suit])
        card_pool.append(random.choice(minor_arcana[minor_suit]))

    # Find the element associated with the planet-sign pair
    for element, pairs in elemental_alignments.items():
        if (planet, sign) in pairs:
            # Add the Major Arcana card for the element
            if element in major_elements:
                card_pool.append(major_elements[element])
            break

    # Draw one card at random from the combined pool
    drawn_card = random.choice(card_pool)
    return drawn_card


if __name__ == "__main__":
    print(pick_cards(3))
