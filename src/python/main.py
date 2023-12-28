from randomized_bogo import randomized_bogosort, recursive_randomized_bogosort
from helper import deck_builder

def main():
  results = []

  for input in range(10):
    deck = deck_builder(input)
    sorted = False
    iteration = 0

    while not sorted:
      output = randomized_bogosort(deck)
      iteration += 1
      

      if (output[0]):
        sorted = True
        dict = {
          'length': input,
          'iterations': iteration
        }

        results.append(dict)

    print(output)


def recursive_main():

  results = []

  for input in range(10):
    deck = deck_builder(input)
    
    result = recursive_randomized_bogosort(deck, 0)

    print(result)
  
  
    




if __name__ == '__main__':
  recursive_main()



