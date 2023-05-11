import numpy as np


def classify_dominant_strategies(game_arr):
    game_arr = np.array(game_arr)

    strategies_dominance_p0 = np.zeros(game_arr.shape[0], dtype=np.int32)
    for i in range(game_arr.shape[0]):
        dominance_score = 3
        strongly_dominated = True
        for j in range(game_arr.shape[0]):
            for k in range(game_arr.shape[1]):
                if i == j:
                    break
                a = game_arr[i,k,0]
                b = game_arr[j,k,0]
                if a == b:
                    if dominance_score == 3:
                        dominance_score = 2
                if a < b:
                    if dominance_score in [2,3]:
                        dominance_score = 1
                if a >= b:
                    strongly_dominated = False
        if strongly_dominated and len(strategies_dominance_p0) > 1:
            dominance_score = 0
        strategies_dominance_p0[i] = dominance_score
    
    strategies_dominance_p1 = np.zeros(game_arr.shape[1], dtype=np.int32)
    for i in range(game_arr.shape[1]):
        dominance_score = 3
        strongly_dominated = True
        for j in range(game_arr.shape[1]):
            for k in range(game_arr.shape[0]):
                if i == j:
                    break
                a = game_arr[k,i,1]
                b = game_arr[k,j,1]
                if a == b:
                    if dominance_score == 3:
                        dominance_score = 2
                if a < b:
                    if dominance_score in [2,3]:
                        dominance_score = 1
                if a >= b:
                    strongly_dominated = False
        if strongly_dominated and len(strategies_dominance_p1) > 1:
            dominance_score = 0
        strategies_dominance_p1[i] = dominance_score
    
    return [strategies_dominance_p0, strategies_dominance_p1]

