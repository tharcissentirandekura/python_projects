import random

def blackjack(deck,player_card_value,dealer_card_value):

    standard_card = 2 # card to have at the initial game

    for _ in range(standard_card):
        random.shuffle(deck)
        player = random.choice(deck)
        print("The player has the cards:",player)
        deck.remove(player)

        if player in ['Q','K','J']:
            player = 10
        elif player == 'A':
            player = 1 or 11

        player_card_value.append(player)

        dealer = random.choice(deck)

        print("dealer:",dealer)
        deck.remove(dealer)
        if dealer in ['Q','K','J']:
            dealer = 10
        elif dealer == 'A':
            dealer = 1 or 11

        dealer_card_value.append(dealer)

    print(len(deck))

global full_deck
global card_face_value
global dealer_face

full_deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,'Q',8,'Q',8,9,9,9,9,10,10,10,10,'Q','Q','K','K','K','K','J','J','J','J','A','A','A','A']

card_face_value = []
dealer_face = []

player_turn = blackjack(full_deck,card_face_value,dealer_face)
if player_turn:
    print(player_turn)


def hit(card,player_card):

    random.shuffle(card)
    choice = random.choice(card)

    card.remove(choice)
    if choice in ['Q','K','J']:
            choice = 10
    elif choice == 'A':
        choice = 1 or 11
    player_card.append(choice)

    return player_card


def total_score(face_value,count = 0):
     for i in face_value:
          count += i
     return count

def first_win(player_choice):
    total_score_dealer = total_score(player_choice,count = 0)
    total_score_player = dealer_face
    print("The dealer has the card of value of:",total_score_player[0])
    return total_score_dealer

print(".....welcome to the Blackjack game casino developed by Tharcisse.....\n\n")

first_player_score = first_win(card_face_value)
print("You have the cards with the value of:",first_player_score)

print("1.hit \t\t2.pick card/ stand")

flag = True

while flag == True:
    player_score = 0
    ask = int(input("Choose:"))
    if ask == 1:
        player_hit = hit(full_deck,card_face_value)
        score_player = total_score(player_hit,count = 0)

        print("you have score of:",score_player)
        if score_player > 21:
            print("Bust\n")
            print("Player score:",score_player)
            print("The dealer won")
            flag = False

    elif ask == 2:
        first_dealer_score = first_win(dealer_face)
        print("The dealer,you have the cars with values of:",first_dealer_score)
        print("dealer value:",dealer_face)
        play = hit(full_deck,card_face_value)

        dealer_hit = hit(full_deck,dealer_face)
        dealer_score = total_score(dealer_hit,count = 0)
        print("The Dealer score is:",dealer_hit)
        print("The dealer's chosen card value is:",dealer_face[-1])


        score_player_card = total_score(play,count = 0)
        if dealer_score > 21:
             print("Oops, Bust")
             print("Player won")
             flag = False

        elif dealer_score == 21 and score_player_card > dealer_score:
            print("Dealer won")
            flag = False

        elif score_player_card < dealer_score:
             print("Dealer won")
             flag = False

        elif dealer_score < 21:
            if dealer_score > score_player_card:
                print("Dealer won")
                flag = False

