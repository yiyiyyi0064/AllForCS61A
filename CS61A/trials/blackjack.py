#Blackjack

import random

points = {'J':10, 'Q':11, 'K':12, 'A':1}

def hand_score(hand):
    """Total score for a hand

    >>> hand_score(['A',3,6])
    20
    >>> hand_score(['A','J','A'])
    12
    """
    total=sum([points.get(card,card) for card in hand])
    if total <= 11 and 'A' in hand:
            return total+10
    return total

def shuffle_cards():
      deck = (['J','Q','K','A']+list(range(2,10)))
      random.shuffle(deck)
      return iter(deck)
        #It will not use the same cards again while using iter
def player_turn( up_card, cards,strategy, deck):
    while hand_score(cards)<=21 and strategy(up_card,cards):
          cards.append(next(deck))

def dealer_turn(cards, deck):
      while hand_score(cards)<17:
            cards.append(next(deck))

def blackjack(strategy, announce=print):
      """Play a hand of casino blackjack"""
      deck=shuffle_cards()

      player_cards=[next(deck)] #这里就是洗牌 然后发牌得到新的牌
      up_card=next(deck) #这个牌是没有翻过来的 这张牌是dealer的牌
      player_cards.append(next(deck))
      hole_card= next(deck)

      player_turn(up_card, player_cards, strategy,deck)
      if hand_score(player_cards)>21:
            announce('Player goes bust with', player_cards,'against a',up_card)
            return -1
      dealer_cards=[up_card,hole_card]
      dealer_turn(dealer_cards,deck)
      if hand_score(dealer_cards)>21:
            announce('Dealer busts with', dealer_cards)
            return 1
      else:
            announce('Player has', hand_score(player_cards),'and dealer has',hand_score(dealer_cards))
            diff=hand_score(player_cards)-hand_score(dealer_cards)
            return max(-1,min(1,diff))
      
def basic_strategy(up_card,cards):
      if hand_score(cards) <= 11:
            return True
      if up_card in [2,3,4,5,6]:
            return False
      return hand_score(cards)<17
def shhh(*args):
      "Dont print or do anything else."

def gamble(strategy, hands=1000):
      return sum([blackjack(strategy,shhh) for _ in range(hands)])
      