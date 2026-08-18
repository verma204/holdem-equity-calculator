from treys import Card





def normalize_cards(text):
    """
    Input text, returns removed spaces and commas
    """
    return text.replace(" ", "").replace(",", "")

def createBoard(flop="", turn="", river=""):
    board = []

    if flop:
        for i in range(0, len(flop), 2):
            board.append(Card.new(flop[i:i+2]))

    if turn:
        board.append(Card.new(turn))

    if river:
        board.append(Card.new(river))

    return board

def createRange(hands):
    hands = normalize_cards(hands)

    if len(hands) % 4 != 0:
        raise ValueError("Range must contain complete two-card hands")

    player = []

    for i in range(0, len(hands), 4):
        hand = [
                Card.new(hands[i:i+2]),
                Card.new(hands[i+2:i+4])
            ]

        player.append(hand)

    return player


