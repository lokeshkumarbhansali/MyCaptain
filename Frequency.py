from collections import Counter

def my_frequency(input_word):
    freq = Counter(input_word)
    for key , value in sorted(freq.items() , key = lambda x:x[1] , reverse = True):
        print(key , '=' , value)

input_word = input(' Enter the input :')

my_frequency(input_word)
