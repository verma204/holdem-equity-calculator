import treys


evaluator = treys.Evaluator()


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

def evaluateTurn(board, player1_range, player2_range):

    total_equity = 0.0
    count = 0

    ranks='23456789TJQKA'
    suits='chds' 
    for rank in ranks:
        for suit in suits:
            cardInt = treys.Card.new(rank + suit)
            if cardInt not in board:
                total_equity += rangeOnRange(board + [cardInt], player1_range, player2_range)
                count += 1

    return total_equity / count


def evaluateFlop(board, player1_range, player2_range):

    total_equity = 0.0
    count = 0

    ranks='23456789TJQKA'
    suits='chds' 
    for rank in ranks:
        for suit in suits:
            cardInt = treys.Card.new(rank + suit)
            if cardInt not in board:
                total_equity += evaluateTurn(board + [cardInt], player1_range, player2_range)
                count += 1

    return total_equity / count


    






    
