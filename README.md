# BOGO PI - V2.0

**DISCLAIMER: THIS IS HORRIBLE and PROBABLY THE WORST THING EVER**

## Purpose

honestly, there really is no purpose to this, other than curiosity about the worse possible sorting algorithm. additionally, there is something both absurd and hilarious about testing possibly the worst performing sorting algorithm that will eventually (at some point) maybe finishing sorting the input. 

### How It Works

this is an implementation of randomized bogosort and works its way through input sizes from 1 item to 52 items (the size of a deck of cards). randomized bogosort works by shuffling all items and checking each item for sortedness, this process is repeated until the sort array is returned. 

> see the /docs directory for a more detailed and mathematical evaluation and description of bogosort.

### Why Python

python was chosen as it is pretty simple to code and the language has a builtin shuffle function, which makes much of the work much simpler. additionally, python is really human readable, and provides a lot of easy extension and freedom in both typing and without many of the seeming limitations of other languages. 

> honestly, its just what i though of at the time, between the builtin shuffle and it being the first language i ever learned.

### Dependencies

1. Python 3
2. time (honestly probably too much)

### Hardware

for a multitude of reasons, this project will need some sort of hardware, and due to the eventuality of maxing out 32-bit architecture and its max integer limit, 64-bit will be necessary. 





