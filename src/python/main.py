
from bogo import randomized_bogosort

# creates a deck of size size

def build_deck(size):
    return list(range(0, size))

def main():
    limit = 10 # will change to input var

    for input in range(limit):
        deck = build_deck(input)
        sorted = False

        while not sorted:
            output = randomized_bogo(deck)

            if (output)
                sorted = True


if __name__ == '__main__':
    main()
