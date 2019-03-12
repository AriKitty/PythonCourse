import random

try:
    import tkinter
except ImportError:  # pythin 2
    import Tkinter as tkinter


# Load the card images
def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']

    # Check for Tkinter version. >= 8.6 can use png images
    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'

    # for each suit, retrieve the image for the cards
    for suit in suits:

        # number cards
        for card in range(1, 11):
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image,))

        # face cards
        for card in face_cards:  # face cards
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image,))


def _shuffle():
    random.shuffle(deck)


def _new_game():
    global dealer_card_frame
    global player_card_frame

    # clears card from the screen
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

    # resets hands and text
    result_text.set("")
    player_hand.clear()
    dealer_hand.clear()

    # deals new cards from new deck
    _shuffle()
    _deal_player()
    dealer_hand.append(_deal_card(dealer_card_frame))
    dealer_score_label.set(_score_hand(dealer_hand))
    _deal_player()


def _deal_card(frame):
    # pop the next card off of the top of the deck
    next_card = deck.pop(0)

    # add it to the back of the pack
    deck.append(next_card)

    # add the image to a Label and display the label
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')

    # return the card's face value
    return next_card


def _deal_dealer():
    dealer_score = _score_hand(dealer_hand)

    while 0 < dealer_score < 17:
        dealer_hand.append(_deal_card(dealer_card_frame))
        dealer_score = _score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = _score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer wins!")

    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player wins!")

    elif dealer_score > player_score:
        result_text.set("Dealer wins!")

    else:
        result_text.set("Draw!")


def _deal_player():
    player_hand.append(_deal_card(player_card_frame))
    player_score = _score_hand(player_hand)
    player_score_label.set(player_score)

    if player_score > 21:
        result_text.set("Dealer Wins!")


def _score_hand(hand):
    # calculate the total score of all cards in the list.
    # only 1 ace can have the value of 11 and it will reduce to 1 if bust
    score = 0
    ace = False

    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value

        # if we would bust, check if there is an ace and subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False

    return score


def play():
    _new_game()
    main_window.mainloop()


main_window = tkinter.Tk()

# Set up the screen and frames for the dealer and player
main_window.title("Black Jack")
main_window.geometry("640x480")
main_window.config(background="green")

result_text = tkinter.StringVar()
result = tkinter.Label(main_window, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(main_window, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

# embedded frame to hold the card images
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

# embedded frame to hold the card images
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tkinter.Frame(main_window)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(button_frame, text="Stay", command=_deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Hit", command=_deal_player)
player_button.grid(row=0, column=1)

new_game_button = tkinter.Button(button_frame, text="New Game", command=_new_game)
new_game_button.grid(row=0, column=2)

shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=_shuffle)
shuffle_button.grid(row=0, column=3)

# load cards
cards = []
load_images(cards)

# create a new deck of cards and shuffle them
deck = list(cards) + list(cards) + list(cards)
_shuffle()

# create the list to store the dealer's and player's hands
dealer_hand = []
player_hand = []

if __name__ == "__main__":
    play()
