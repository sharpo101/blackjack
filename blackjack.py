import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True
no_bust = True

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit        
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):        
        return self.rank + " of " + self.suit

class Deck:
    
    def __init__(self):        
        self.deck = []        
        for suit in suits:            
            for rank in ranks:
                created_card = Card(suit,rank)                
                self.deck.append(created_card)
                
    def __str__(self):
        for card in self.deck:
            return f'the cards in the deck are {card}'
                
    def shuffle(self):        
        random.shuffle(self.deck)
        
    def deal_one(self):        
        return self.deck.pop()

class Hand:
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True
no_bust = True

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit        
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):        
        return self.rank + " of " + self.suit

class Deck:
    
    def __init__(self):        
        self.deck = []        
        for suit in suits:            
            for rank in ranks:
                created_card = Card(suit,rank)                
                self.deck.append(created_card)
                
    def __str__(self):
        for card in self.deck:
            return f'the cards in the deck are {card}'
                
    def shuffle(self):        
        random.shuffle(self.deck)
        
    def deal_one(self):        
        return self.deck.pop()

class Hand:
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        
    def add_card(self,card):
        self.cards.append(card)
        self.value += card.value
        return self.value
        self.adjust_for_aces()
        
    def get_value(self,card):
        self.value += card.value
        return self.value
            
    def adjust_for_aces(self):
        if 'Ace' in [card.rank for card in self.cards]:
            self.aces += 1
            ace_value = int(input('Ace value 1 or 11?: '))
            self.value += ace_value

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet * 2

    def lose_bet(self):
        self.total -= self.bet

def take_bet():

    while True:    
        try:
            player_bet.bet = int(input('Place your bet: $'))
            return player_bet.bet
            while player_bet.bet > player_bet.total:
                print('Not enough chips')
                player_bet.bet = int(input('Place your bet: $'))
                return player_bet.bet

        except:
            print('Please place a valid bet')
            continue

        else:
            print(f'Your bet is ${player_bet.bet}')
            print(f'Your total is ${player_bet.total}')
            break
            

def hit(deck,hand):
    hand.add_card(deck.deal_one())

def hit_or_stand(deck,hand):
    global playing
    options = ['hit','stand']
    hitorstand = True
    
    while hitorstand:
        try:
            player_choice = input('Would you like to hit or stand? ')
            while player_choice not in options:
                print('Please choose hit or stand')
                player_choice = input('Would you like to hit or stand? ')

        except:
            print('Please choose hit or stand!')
            continue

        else:
            if player_choice == 'hit':
                hit(deck,hand)
                hitorstand = False
                break
                
            elif player_choice == 'stand':
                global playing
                playing = False
                hitorstand = False
                break
            

def show_some(player,dealer):
    print('\nyour cards:')
    for card in player:
        print(card)
    
    print(f"\nDealer's cards:")
    print(dealer.cards[1])
        
def show_all(player,dealer):
    print(f'\nyour cards are')
    for card in player:
        print(card)
 
    print("\nthe dealer's cards are")   
    for card in dealer:
        print(card)

def player_busts(player,chips):
    global playing
    global no_bust
    if player.value > 21:
        chips.lose_bet()
        print('\nYou Bust!')
        playing = False
        no_bust = False

def player_wins(player,dealer,chips):
    global no_bust
    if player.value > dealer.value and player.value <= 21:
        chips.win_bet()
        print('\nYou win!')
        no_bust = False

def dealer_busts(dealer,chips):
    global no_bust
    if dealer.value > 21:
        print('\nDealer busts!')
        chips.win_bet()
        no_bust = False
    
def dealer_wins(player,dealer,chips):
    global no_bust
    if dealer.value > player.value and dealer.value <= 21:
        print('\nDealer wins!')
        chips.lose_bet()
        no_bust = False
    
def push(player,dealer):
    global no_bust
    if player.value == dealer.value:
        print('\nPUSH')
        no_bust = False

def game_over():
    gameover = True
    while gameover:
        try:
            playagain = ['Y','N']
            play_again = input('Would you like to play again? Y or N: ')
            while play_again not in playagain:
                play_again = input('Please choose Y or N: ')
        except:
            print('Please choose Y or N')

        else:
            if play_again == 'Y':
                playing = True
                blackjack()
            elif play_again == 'N':
                playing = False
                game_on = False
                break

def new_hand():
    player_hand.cards = []
    dealer_hand.cards = []
    for i in range(2):
        player_hand.add_card(game_deck.deal_one())
    for i in range(2):
        dealer_hand.add_card(game_deck.deal_one())

player_hand = Hand()
dealer_hand = Hand()
player_bet = Chips()
game_deck = Deck()

def game_start():
    global playing
    playing = True
    print('Welcome to blackjack!')
    player_hand = Hand()
    dealer_hand = Hand()
    player_bet = Chips()

def blackjack():
    game_on = True
    game_start()
    
    game_deck.shuffle()
    print(f'Starting chips: ${player_bet.total}')
    
    while game_on:
        global playing
        global no_bust
        playing = True
        no_bust = True

        new_hand()

        take_bet()

        show_some(player_hand.cards,dealer_hand)

        while playing:

            hit_or_stand(game_deck,player_hand)

            player_hand.adjust_for_aces()

            show_some(player_hand.cards,dealer_hand)

            player_busts(player_hand,player_bet)
            
            break

        show_all(player_hand.cards,dealer_hand.cards)
        
        while no_bust:
        
            if dealer_hand.value >= 17:

                hit(game_deck,dealer_hand)

            show_all(player_hand.cards,dealer_hand.cards)

            player_wins(player_hand,dealer_hand,player_bet)

            dealer_busts(dealer_hand,player_bet)

            dealer_wins(player_hand,dealer_hand,player_bet)
            
            push(player_hand,dealer_hand)
            
            break

        print(f'\nYour chip total is: ${player_bet.total}')

        if player_bet.total == 0:
            game_over()
        break

        
            

blackjack()

    def add_card(self,card):
        self.cards.append(card)
        self.value += card.value
        return self.value
        self.adjust_for_aces()
        
    def get_value(self,card):
        self.value += card.value
        return self.value
            
    def adjust_for_aces(self):
        if self.cards == ['Ace']:
            self.aces += 1
            ace_value = int(input('Ace value 1 or 11?: '))
            self.value += ace_value

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet * 2
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet():

    while True:    
        try:
            player_bet.bet = int(input('Place your bet: $'))
            return player_bet.bet
            while player_bet.bet > player_bet.total:
                print('Not enough chips')
                player_bet.bet = int(input('Place your bet: $'))
                return player_bet.bet

        except:
            print('Please place a valid bet')
            continue

        else:
            print(f'Your bet is ${player_bet.bet}')
            print(f'Your total is ${player_bet.total}')
            break
            

def hit(deck,hand):
    hand.add_card(deck.deal_one())

def hit_or_stand(deck,hand):
    global playing
    options = ['hit','stand']
    hitorstand = True
    
    while hitorstand:
        try:
            player_choice = input('Would you like to hit or stand? ')
            while player_choice not in options:
                print('Please choose hit or stand')
                player_choice = input('Would you like to hit or stand? ')

        except:
            print('Please choose hit or stand!')
            continue

        else:
            if player_choice == 'hit':
                hit(deck,hand)
                hitorstand = False
                break
                
            elif player_choice == 'stand':
                global playing
                playing = False
                hitorstand = False
                break
            

def show_some(player,dealer):
    print('\nyour cards:')
    for card in player:
        print(card)
    
    print(f"\nDealer's cards:")
    print(dealer.cards[1])
        
def show_all(player,dealer):
    print(f'\nyour cards are')
    for card in player:
        print(card)
 
    print("\nthe dealer's cards are")   
    for card in dealer:
        print(card)

def player_busts(player,chips):
    global playing
    global no_bust
    if player.value > 21:
        chips.lose_bet()
        print('You Bust!')
        playing = False
        no_bust = False

def player_wins(player,dealer,chips):
    global no_bust
    if player.value > dealer.value and player.value <= 21:
        player.win_bet()
        print('You win!')
        no_bust = False

def dealer_busts(dealer,chips):
    global no_bust
    if dealer.value > 21:
        print('Dealer busts!')
        chips.win_bet()
        no_bust = False
    
def dealer_wins(player,dealer,chips):
    global no_bust
    if dealer.value > player.value and dealer.value <= 21:
        print('Dealer wins!')
        chips.lose_bet()
        no_bust = False
    
def push(player,dealer):
    global no_bust
    if player.value == dealer.value:
        print('PUSH')
        no_bust = False

def game_over():
    gameover = True
    while gameover:
        try:
            playagain = ['Y','N']
            play_again = input('Would you like to play again? Y or N: ')
            while play_again not in playagain:
                play_again = input('Please choose Y or N: ')
        except:
            print('Please choose Y or N')

        else:
            if play_again == 'Y':
                playing = True
                blackjack()
            elif play_again == 'N':
                playing = False
                game_on = False
                break

def new_hand():
    player_hand.cards = []
    dealer_hand.cards = []
    for i in range(2):
        player_hand.add_card(game_deck.deal_one())
    for i in range(2):
        dealer_hand.add_card(game_deck.deal_one())

player_hand = Hand()
dealer_hand = Hand()
player_bet = Chips()
game_deck = Deck()

def game_start():
    global playing
    playing = True
    print('Welcome to blackjack!')
    player_hand = Hand()
    dealer_hand = Hand()
    player_bet = Chips()

def blackjack():
    game_on = True
    game_start()
    
    game_deck = Deck()
    game_deck.shuffle()
    print(f'Starting chips: ${player_bet.total}')
    
    while game_on:
        global playing
        global no_bust
        playing = True
        no_bust = True

        new_hand()

        take_bet()

        show_some(player_hand.cards,dealer_hand)

        while playing:

            hit_or_stand(game_deck,player_hand)

            player_hand.adjust_for_aces()

            show_some(player_hand.cards,dealer_hand)

            player_busts(player_hand,player_bet)
            
            break

        show_all(player_hand.cards,dealer_hand.cards)
        
        while no_bust:
        
            if dealer_hand.value >= 17:

                hit(game_deck,dealer_hand)

            show_all(player_hand.cards,dealer_hand.cards)

            player_wins(player_hand,dealer_hand,player_bet)

            dealer_busts(dealer_hand,player_bet)

            dealer_wins(player_hand,dealer_hand,player_bet)
            
            push(player_hand,dealer_hand)
            
            break

        print(f'\nYour chip total is: ${player_bet.total}')

        if player_bet.total == 0:
            game_over()
        break

        
            

blackjack()
