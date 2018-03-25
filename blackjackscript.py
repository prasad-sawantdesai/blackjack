from enum import Enum
import random

class Suit(Enum):
    spade = 1
    heart = 2
    club = 3
    diamond = 4

class card(object):
    def __init__(self, val, suit):
        self.__numeric_value = val
        self.__suit = suit

    @property
    def numeric_value(self):
        return self.__numeric_value
    
    @property
    def suit(self):
        return self.__suit

        
class BlackJackCard(card):
    def __init__(self, val, suit):
        super(BlackJackCard, self).__init__(val, suit)

    @property
    def numeric_value(self):
        original_value = super(BlackJackCard, self).numeric_value
        if self.is_ace(original_value):
            return 11
        if self.is_facecard(original_value):
            return 10       
        return original_value;        

    def get_facecard_value(self):
        return super(BlackJackCard, self).numeric_value
        
    def is_ace(self, face_value):
        if face_value == 1:
            return True;
        return False

    def is_facecard(self, face_value):
        if face_value >= 11 and face_value <= 13:
            return True;
        return False
    
class Player(object):
    def __init__(self, player_id, bet):
        self.player_id = player_id
        self.bet = bet
        self.points = []
        self.cards = []
        self.total_points = 0     
        self.player_status = "" 
        self.deal_first_card()
    
    def deal_first_card(self):
        self.cards.append(BlackJackCard(random.randint(1,13) ,Suit(random.randint(1,4))))
        self.cards.append(BlackJackCard(random.randint(1,13) ,Suit(random.randint(1,4))))
        self.add_points(self.cards[0]);
        self.add_points(self.cards[1]);  
        self.assess_score_status()

    def add_points(self, bjcard):
        self.points.append(bjcard.numeric_value)
        self.total_points += bjcard.numeric_value        

    def get_total_points(self):
        return self.total_points

    def print_points(self):
        print "\nPoints"
        print '  '.join([str(x) for x in self.points]) 

    def print_cards(self):
        print "\nCards :"

        for card in self.cards:
            print str(card.numeric_value) + " " +  str(card.suit)
        
    def get_another_card(self): 
        if self.player_status == "playing":
            self.cards.append(BlackJackCard(random.randint(1,13) ,Suit(random.randint(1,4))))
            self.add_points(self.cards[-1]); 
            self.assess_score_status()
              
    def assess_score_status(self): 
        self.player_status = "playing"
        
        if self.total_points == 21:
            self.player_status = "blackjack" 
        if self.total_points > 21:
            self.player_status = "bust" 
        
        self.print_cards()
        print "Status :" + self.player_status  
        print "Points :" + str(self.total_points )  
        
        return  self.player_status
    
    
class Dealer(Player):
    def __init__(self, player_id, bet):
        super(Dealer, self).__init__(player_id, bet)
        
    def deal_first_card(self):
        self.cards.append(BlackJackCard(random.randint(1,13) ,Suit(random.randint(1,4))))
        self.add_points(self.cards[0]);
        self.assess_score_status()        

#main program
print "PLAYER"
player = Player(1, 1000)
print "---------------------------------------------------------"
print "DEALER"
dealer = Dealer(0, 1000)
print "---------------------------------------------------------"
if player.player_status == "blackjack":
    print "Player won!!"
elif player.player_status == "bust":
    print "Player loose!!"
else:
    #Player deal
    while True:
        print "Press 0 for hit and 1 for stand"
        x = input()
        if x == 0:
            player.get_another_card()
            if player.player_status == "blackjack":
                print "Player won!!"
                break
            elif player.player_status == "bust":
                print "Player loose!!"
                break
        else:
            player.player_status = "stand"
            break
    
    #Dealer deal 
    if player.player_status == "stand":
        while dealer.total_points <= 16:
            dealer.get_another_card()
            if dealer.player_status == "blackjack":
                print "Dealer won!!"   
            elif dealer.player_status == "bust":
                print "Player won!!"        
    
    if player.player_status == "stand" and dealer.player_status == "playing":
        if player.total_points > dealer.total_points:
            print "Player won"
        elif  player.total_points < dealer.total_points:   
            print "Dealer won"
        else:
            print "Tie"
