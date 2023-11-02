import random

# class Card:
def _init_(self, suit, rank):
    self.suit = suit
    self.rank = rank

def _str_(self):
        return self.suit + self.rank

# class Deck:
def _init_(self):
    self.cards = []
    for suit in ['S', 'H', 'D', 'C']:
        for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            self.cards.append(Card(suit, rank))

def shuffle(self):
    random.shuffle(self.cards)

def draw(self):
    return self.cards.pop()

# class Player:
def _init_(self, name):
    self.name = name
    self.hand = []

def draw_card(self, deck):
    self.hand.append(deck.draw())

def play_card(self):
    card = self.hand.pop()
    return card

# class Game:
def _init_(self, players):
    self.deck = Deck()
    self.deck.shuffle()
    self.players = players
    self.current_player = self.players[0]
    self.discard_pile = []
    self.played_cards = []

def play_round(self):
        # Draw a card for each player
    for player in self.players:
        player.draw_card(self.deck)

        # Play the first card
    card = self.current_player.play_card()
    self.discard_pile.append(card)
    self.played_cards.append(card)

        # Play the remaining cards
    for player in self.players[1:]:
        card = player.play_card()
        self.discard_pile.append(card)
        self.played_cards.append(card)

        # Determine the winner of the round
    winner = self.get_winner_of_round(self.played_cards)

        # Draw a card for the winner
    winner.draw_card(self.deck)

def get_winner_of_round(self, played_cards):
        # TODO: Implement this method to determine the winner of the round based on the played cards

    def play_game(self):
        # Play rounds until one player has no cards left in their hand
        while len(self.players[0].hand) > 0 and len(self.players[1].hand) > 0:
            self.play_round()

        # Determine the winner of the game
        winner = self.get_winner_of_game()

        return winner

def get_winner_of_game(self):
        # TODO: Implement this method to determine the winner of the game based on the players' hands

# Create a new game
game = Game(['Alice', 'Bob'])

# Play the game
winner = game.play_game()

# Print the winner
print(winner + ' wins!')