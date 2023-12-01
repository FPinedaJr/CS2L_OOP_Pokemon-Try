from ...models import PokemonCard

# Create a new PokemonCard instance
card = PokemonCard(name="Pikachu", rarity="Rare",hp=60, card_type="Electric", attack="Thunder Shock",
                            description="A mouse-like pokemon that can generate electricity.",
                            weakness="Ground", card_number=25, release_date="1996-02-27", evolution_stage="Basic",
                            abilities="Static")

# Check if the card has an id (if it's been saved to the database)
if card.id is not None:
    # The card has an id, so it's saved to the database, and you can delete it
    card.delete()
else:
    # The card hasn't been saved to the database, so discard it
    card._state.adding = False  # Set the adding attribute to False
    card._state.db = None  # Set the db attribute to None
    card._state._committed = False  # Set the committed attribute to False
    card.discard()
