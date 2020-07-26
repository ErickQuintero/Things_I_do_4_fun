'''On TV, I watched an iterview with POTUS (Donald Trump) in which he was asked
about a recent cognitive test he took. In what is common fashion for POTUS, he
began to boast about the results and how hard the test was. Turns out one of the
questions was to count down from 100 by 7s. I decided to write a Python program
that will output the same results as that test question in just one line of code'''

print([i for i in sorted(range(1,101), reverse = True)[::7]])
