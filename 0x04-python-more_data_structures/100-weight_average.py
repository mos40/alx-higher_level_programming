#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    final_score = sum(score * weight for score, weight in my_list)
    final_weight = sum(weight for _, weight in my_list)

    return final_score / final_weight if final_weight != 0 else 0
