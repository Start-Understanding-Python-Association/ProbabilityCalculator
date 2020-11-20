# This entrypoint file to be used in development. Start by reading README.md
import prob_calculator
from unittest import main

# hat = prob_calculator.Hat(blue=3, red=2, green=6)
#
#
# x = prob_calculator.copy.copy(hat)
# # print(x.draw(3))
# # print(x.contents)
# probability = prob_calculator.experiment(hat=hat,
#                                          expected_balls={"blue": 2,
#                                                          "green": 1},
#                                          num_balls_drawn=20,
#                                          num_experiments=100)
# print("Probability:", probability)

# Run unit tests automatically
main(module='test_module', exit=False)
