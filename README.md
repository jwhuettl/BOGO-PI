# BOGO PI - V2.0

**DISCLAIMER: THIS IS KINDA POINTLESS**

## Purpose

honestly, there really is no purpose to this, other than curiosity about the worse possible sorting algorithm. additionally, there is something both absurd and strangely interesting about testing possibly the worst performing sorting algorithm that will eventually (at some point) maybe finishing sorting the input. 

### How It Works

this is an implementation of randomized bogosort and works its way through input sizes from 1 item to 52 items (the size of a deck of cards). randomized bogosort works by shuffling all items and checking each item for sortedness, this process is repeated until the sort array is returned. 

> see the /docs directory for a more detailed and mathematical evaluation and description of bogosort.

### Why Python

python was chosen as it is pretty simple to code and the language has a builtin shuffle function, which makes much of the work much simpler. additionally, python is really human readable, and provides a lot of easy extension and freedom in both typing and without many of the seeming limitations of other languages. 

> honestly, its just what i though of at the time, between the builtin shuffle and it kind of seeming as if there is no integer limit.

### Dependencies

1. Python 3
2. Time (honestly probably too much)
3. Unused Hardware


### Logging

there will be both local and and external logging for the progress of the algorithm as it makes its way through the different length arrays. both logging forms will probably be quite sparse as the amount of permutations will be quite high and there will most likely be many attempts at each array length.

the most prudent methodology will be either daily or twice daily, as this provides a decent amount of data and require the least amount of storage. this should also provide 

### Hardware

for a multitude of reasons, this project will need some sort of hardware, and due to the eventuality of maxing out 32-bit architecture and its max integer limit, 64-bit will be necessary. 

however, for the time being i have some unsued raspberry pis yet they are earily generation, so they both have 32-bit architecture but for the interim, they should be functional.





