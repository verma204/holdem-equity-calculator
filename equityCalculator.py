import treys


evaluator = treys.Evaluator()

player1range = [
    [
        treys.Card.new("Kh"),
        treys.Card.new("Kd")
    ],
    [
        treys.Card.new("Ks"),
        treys.Card.new("Kd")
    ],
    [
        treys.Card.new("Kc"),
        treys.Card.new("Kd")
    ]
]


player2range = [
    [
        treys.Card.new("As"),
        treys.Card.new("Ac")
    ],
    [
        treys.Card.new("As"),
        treys.Card.new("Ah")
    ],
    [
        treys.Card.new("As"),
        treys.Card.new("Ad")
    ],
    [
        treys.Card.new("Ac"),
        treys.Card.new("Ah")
    ],
    [
        treys.Card.new("Ac"),
        treys.Card.new("Ad")
    ],
    [
        treys.Card.new("Ah"),
        treys.Card.new("Ad")
    ],
    [
        treys.Card.new("Qs"),
        treys.Card.new("Qc")
    ],
    [
        treys.Card.new("Qd"),
        treys.Card.new("Qh")
    ]
]



board = [
    treys.Card.new("7s"),
    treys.Card.new("7d"),
    treys.Card.new("2s"),
    treys.Card.new("2d"),
    treys.Card.new("5h"),
]



def handOnHand(board, player1, player2):
    rank1 = evaluator.evaluate(board, player1)
    rank2 = evaluator.evaluate(board, player2)
    if rank1 < rank2:
        return 1.0
    elif rank1 > rank2:
        return 0.0
    else:
        return 0.5

def handOnRange(board, player1, player2_range):
    total_equity = 0.0
    count = 0

    known_cards = set(board + player1)

    for player2 in player2_range:
        if set(player2) & known_cards:
            continue
        total_equity += handOnHand(board, player1, player2)
        count += 1

        if count == 0:
            raise ValueError("No legal hands in range")

    return total_equity / count

def rangeOnRange(board, player1_range, player2_range):

    total_equity = 0.0
    count = 0

    for player1 in player1_range:
        total_equity += handOnRange(board, player1, player2_range)
        count += 1
    return total_equity / count



def userInput():
    board = input("Board: ")
    player1 = input("Range of player 1: ")
    player2 = input("Range of player 2: ")



print(rangeOnRange(board, player1range, player2range))
    
