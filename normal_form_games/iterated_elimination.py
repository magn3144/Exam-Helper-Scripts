import numpy as np
import copy

from normal_form_games.classify_strategies import classify_dominant_strategies


def iterated_elimination(game_arr):
    _game_arr = copy.deepcopy(game_arr)
    strictly_dominated_exists = True
    while strictly_dominated_exists:
        strategies_classification = classify_dominant_strategies(_game_arr)
        strictly_dominated_exists = False
        for i in range(1, -1, -1):
            for j in range(len(strategies_classification[i]) - 1, -1, -1):
                if strategies_classification[i][j] == 0:
                    strictly_dominated_exists = True
                    _game_arr = np.delete(_game_arr, j, i)
    return _game_arr