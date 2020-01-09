# BOGO PI

**DISCLAIMER: THIS IS HORRIBLE and PROBABLY THE WORST THING EVER**

#### Purpose
To create something so utterly stupid and without purpose, that it will actually never finish. Also, I thought it might be a bit funny, and when, the robots take over, I will probably be executed for forcing a machine to do this.

#### What it is
A python script that implements an algorithm called RANDOMIZED BOGO sort, which basically shuffles the unordered array and then checks to see if the new array has been sorted. This process is repeated until the sorted array is found.

In BOGO PI, the script will be running at all times, and working its way up from a 1 integer array, all the way to a 52 integer array (basically a full deck of cards). In theory, it should probably never finish the 52 integer array as the amount of permutations is about 52!, which is a very large number.

> NOTE:  <br />
> 52! is equal to this:
>
> 80,658,175,170,943,878,571,660,636,856,403,766,975,289,505,440,883,277,824,000,000,000,000

#### Why
Why not?

Because I can.

Also, because I think that this is hilarious

#### RANDOMIZED BOGO
This is a special version of BOGO sort in which the algorithm does not store the work it has done, it simply shuffles the entire array again a checks to see if the list is sorted. Basically, the algorithm (if it can really be called that) tries every possible permutation of the array, which will eventually find the sorted permutation. This gives it a complexity of O(n*n!), n! for the number of permutations and n for the checking of said permutations.

However, it gets worse, this implementation of the algorithm does not hold on to any of the work it has already done, as it reshuffles the array each time. The complexity then is basically infinite, but there is an element of chance, which can means that it can take less then n! to find the sorted array.

To keep the algorithm in its intended shittiness, it does check through every single element of each permutation, which is to say it keeps the complexity of O(n*n!).

> NOTE: In this case, *n* is equal to the size of the array in question.  


#### How it works
For each integer *n*, a 'deck' (implemented as an array) is built containing [0, *n*-1] integers, this is then shuffled to create an unsorted deck. The RANDOMIZED BOGO 'algorithm' is then run on the deck until a fully sorted deck has been found. Each time the algorithm is run, the deck is copied to the corresponding log folder (located in logs/*n*.log), show the multitude of decks created by the 'algorithm'. A timer is started after the creation of the original deck but before the first RANDOMIZED BOGO run, the timer is then stopped once the sorted deck has been found. Both the time elapsed and the number of permutations are then appended to the corresponding log file.

#### Uses
There are none.

Pointless attempt at humor?

A *possibly* never ending and horribly written CPU benchmark?

#### What is next?
1. Make a twitter bot
2. Put it on a RaspberryPI
3. Let it goooooooooooooo (for a long-ass time)
4. ????????
5. Profit?!

#### TO DO
1. Restart function (in the event of power loss or moving the machine)
2. BOGO-PI paper
3. ~Twitter Bot~
