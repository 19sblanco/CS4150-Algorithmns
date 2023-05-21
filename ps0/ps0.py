import sys
"""
Author: Steven Blanco Aug 30 2022
===
Input: n, k and a list of words from stdin in the following form,
where n is the number of words and k is the number of letters in each word

n k
word_0
word_1
...
word_n

Output: the number of words that are not anagrams of eachother, this means
the number of words that have a unique set of letters
"""

def main():
    number_of_words = int(input().split()[0])

    # get the words, alphabetize them and add them to a list named words
    words = ["".join(sorted(sys.stdin.readline())) for i in range(number_of_words)]

    # collect the words as keys in the dictionary, the value is the number of occurances in the dictionary
    dictionary = {}
    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    # add 1 to unique_words for every word with a count of 1
    unique_words = 0
    for key in dictionary:
        if dictionary[key] == 1:
            unique_words += 1


    print(unique_words)

if __name__ == "__main__":
    main()

