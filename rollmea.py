"""
RollMeA: A D&D Dice Roll Simulator
By: Ethan Parizeau
Email: ethanparizeau@gmail.com
Github: github.com/ethanparizeau
"""
import sys
import random

# Class to manage dice
class dice:
    # Total after roll
    total = 0
    def __init__(self, num, sides):
        # Number of dice
        self.num = num
        # Number of sides 
        self.sides = sides
    
    def roll(self):
        """ Roll the dice """
        # Let user know what dice are rolling
        print("Rolling {0}d{1}".format(self.num, self.sides))
        # Roll each dice
        for i in range(1, self.num + 1):
            # Get roll result
            result = random.randrange(1, self.sides + 1)
            # Inform user of result
            print("#{0} - {1}".format(i, result))
            # Add result to total
            self.total += result
        # Inform user of total
        print("Total:", self.total)

def main():
    # Get index of d
    diff_index = sys.argv[1].find('d')
    # Get the number of dice then convert to int
    num = int(sys.argv[1][:diff_index])
    # Get the number of sides then convert to int
    sides = int(sys.argv[1][diff_index+1:])
    # Roll dice
    dice(num, sides).roll()


if __name__ == "__main__":
    main()