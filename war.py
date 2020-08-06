class Card:
    suits=["spades","hearts","diamonds","clubs"]
    values=[None,None,"2","3","4","5","6","7","8","9",\
    "10","Jack","Queen","King","Ace"]

    def __init__(self,value,suit):
        self.value=value
        self.suit=suit

    def __lt__(self,other):
        if self.value<other.value:
            return True
        if self.value==other.value:
            if self.suit<other.suit:
                return True
            else:
                return False
        return False

    def __gt__(self,other):
        if self.value>other.value:
            return True
        if self.value==other.value:
            if self.suit>other.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        return self.values[self.value]+" of "+self.suits[self.suit]

from random import shuffle
class Deck:
    def __init__(self):
        self.cards=[]
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards)==0:
            return
        else:
            return self.cards.pop()

class Player:
    def __init__(self,name):
        self.wins=int(0)
        self.card=None
        self.name=name

class Game:
    def __init__(self):
        self.p1=Player(input("Type player 1's name: "))
        self.p2=Player(input("Type player 2's name: "))
        self.deck=Deck()
    def wins(self,p):
        p.wins+=1
        print("{} wins this round.".format(p.name))
    def draw(self,p1n,p1c,p2n,p2c):
        print("{} draws {}. {} draws {}.".format(p1n,p1c,p2n,p2c))
    def play_game(self):
        cards=self.deck.cards
        print("War game is set.")
        while len(cards)>=2:
            if input("Type q to quit: ")=="q":
                break
            p1c=self.deck.rm_card()
            p2c=self.deck.rm_card()
            p1n=self.p1.name
            p2n=self.p2.name
            self.draw(p1n,p1c,p2n,p2c)
            if p1c>p2c:
                self.wins(self.p1)
            else:
                self.wins(self.p2)
        print("The game is finished. {}"\
        .format(self.winner(self.p1,self.p2)))
    def winner(self,p1,p2):
        if p1.wins>p2.wins:
            return "Winner is {}.".format(p1.name)
        if p2.wins>p1.wins:
            return "Winner is {}.".format(p2.name)
        else:
            return "A tied game."

game=Game()
game.play_game()
print("{} got {} wins.".format(game.p1.name,game.p1.wins))
print("{} got {} wins.".format(game.p2.name,game.p2.wins))
