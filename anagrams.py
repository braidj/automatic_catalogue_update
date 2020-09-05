#!/usr/bin/env python3

from itertools import combinations, permutations
import enchant
import sys

def fibonacci(n):
    """ Returns Fibonacci Number at nth position using recursion"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def combos(word):
    for i in range(len(word)):
        yield(word[i])        
        for s in combos(word[:i] + word[i+1:]):
            yield(word[i] + s)

def rotate(word):

    perms = [''.join(p) for p in permutations(word)]
    unique_perms = set(perms)
    return unique_perms

if __name__ == "__main__":

    d = enchant.Dict("en_UK")

    word = "trumper"
    print(f"Getting all words from {word}")
    merged_list = []

    for l in combos(word):

        perms = [''.join(p) for p in permutations(l)]
        cleansed = [x for x in perms if len(x) > 1]
        merged_list.extend(cleansed)

    unique_list = set(merged_list)
    word_list = [x for x in unique_list if d.check(x)] # only genuine words
    threeplus = [x for x in word_list if len(x) >= 3]
    print(f"Results {len(threeplus)}")
    threeplus.sort(key=len,reverse=True)
    print("\n".join(threeplus))
