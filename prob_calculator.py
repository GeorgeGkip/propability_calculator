import copy
import random


class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        self.balls = kwargs
        for key, value in kwargs.items():
            for i in range(0, int(value)):
                self.contents.append(key)

    def draw(self, num_balls_drawn):
        drawn_balls = []
        hat_balls = copy.deepcopy(self.contents)
        if num_balls_drawn > len(hat_balls):
            drawn_balls = hat_balls
        else:
            for i in range(0, num_balls_drawn):
                random_ball = random.randrange(0, len(hat_balls))
                drawn_balls.append(hat_balls[random_ball])
                hat_balls.remove(hat_balls[random_ball])
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    N = num_experiments
    M = 0
    for i in range(0, N):
        drawn_balls_dic = {}
        drawn_balls_list = hat.draw(num_balls_drawn)

        for key in drawn_balls_list:
            drawn_balls_dic[key] = drawn_balls_dic.get(key, 0) + 1

        if expected_balls == drawn_balls_dic:
            M += 1

    return M/N


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                         expected_balls={"red": 2, "green": 1},
                         num_balls_drawn=3,
                         num_experiments=2000)


print(probability)
