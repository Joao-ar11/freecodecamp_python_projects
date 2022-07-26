from random import choice
from copy import deepcopy
class Hat:
    contents = list()
    def __init__(self, **balls):
        self.contents = [color for color, number in balls.items() for _ in range(number)]
    
    
    def draw(self, draws):
        drawn = list()
        if draws > len(self.contents):
            draws = len(self.contents)
        for i in range(0, draws):
            draw = choice(self.contents)
            self.contents.remove(draw)
            drawn.append(draw)
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):   
    result = 0
    drawn = list()
    for _ in range(0, num_experiments):
        exp_hat = deepcopy(hat)
        drawn = exp_hat.draw(num_balls_drawn)
        balls_req = sum([1 for k, v in expected_balls.items() if drawn.count(k) >= v])
        result += 1 if balls_req == len(expected_balls) else 0
    return result / num_experiments

        