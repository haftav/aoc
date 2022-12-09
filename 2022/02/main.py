results_1 = {
    'X': {
        'A': 3,
        'B': 0,
        'C': 6
    },
    'Y': {
        'A': 6,
        'B': 3,
        'C': 0
    },
    'Z': {
        'A': 0,
        'B': 6,
        'C': 3
    }
}

results_2 = {
    'A': {
        'X': 'C',
        'Y': 'A',
        'Z': 'B' 
    },
    'B': {
        'X': 'A',
        'Y': 'B',
        'Z': 'C' 
    },
    'C': {
        'X': 'B',
        'Y': 'C',
        'Z': 'A' 
    }
}


score_table = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

move_scores = {
    'A': 1,
    'B': 2,
    'C': 3
}

result_scores = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

def calculate_score_q1(opponent, player):
    score = results_1.get(player).get(opponent) + score_table.get(player)
    return score

def calculate_score_q2(opponent, result):
    player_move =  results_2.get(opponent).get(result)
    return move_scores.get(player_move) + result_scores.get(result)
    
def q1():
    with open('input.txt', encoding='utf-8') as f:
        score = 0
        for line in f.read().split("\n"):
            if not line:
                break
            split = line.split(' ')
            opponent, player = split[0], split[1]
            score += calculate_score_q1(opponent, player)
    print(score)


def q2():
    with open('input.txt', encoding='utf-8') as f:
        score = 0
        for line in f.read().split("\n"):
            if not line:
                break
            split = line.split(' ')
            opponent, result = split[0], split[1]
            score += calculate_score_q2(opponent, result)
    print(score)

q2()
