tarot_cards = {
    "The Fool": "Symbolizes new beginnings, freedom, and adventure.",
    "The Magician": "Represents creativity, intelligence, and control.",
    "The High Priestess": "Symbolizes intuition, subconscious, and wisdom.",
    "The Empress": "Symbolizes nurturing, love, and creativity.",
    "The Emperor": "Symbolizes power, stability, and responsibility.",
    "The Lovers": "Represents love, relationships, and choices.",
    "The Chariot": "Represents willpower, victory, and progress.",
    "The Hermit": "Symbolizes introspection, wisdom, and solitude.",
    "Wheel of Fortune": "Represents destiny, cycles, and changes."
}

def analyze_tarot(card_name):
    return tarot_cards.get(card_name, "Unknown Tarot card.")
