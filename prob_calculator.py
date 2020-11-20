import copy
import random
# Consider using the modules imported above.


class Hat:
    """Math hat with various colored balls."""

    def __init__(self, **kwargs):
        self.contents = []
        for keys in kwargs.keys():
            count = 0
            while count < kwargs[keys]:
                self.contents.append(keys)
                count = count + 1

    def draw(self, number):
        if number > len(self.contents):
            drawn = self.contents
            self.contents.clear()
            return drawn
        else:
            drawn = random.sample(self.contents, number)
            for i in drawn:
                self.contents.remove(i)
            return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    count1 = 0
    expected_balls_contents = []
    for keys in expected_balls.keys():
        count2 = 0
        while count2 < expected_balls[keys]:
            expected_balls_contents.append(keys)
            count2 = count2 + 1
    while count1 < num_experiments:
        x = copy.deepcopy(hat)
        drawn_balls = x.draw(num_balls_drawn)
        for i in expected_balls_contents:
            if i in drawn_balls:
                drawn_balls.remove(i)
        count1 = count1 + 1
        if len(drawn_balls) <= num_balls_drawn - len(expected_balls_contents):
            m = m + 1
    return m / num_experiments
