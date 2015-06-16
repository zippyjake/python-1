'''The asking question'''

import colors as c
import random

def ask(question,color=c.yellow):
    print(question)
    anwser = input('> ' + c.base3).lower().strip()
    print(c.reset)
    return anwser

if __name__ == '__main__':
    print(c.clear)
    name = ask('What is you name?')
    color = ask('What is your favorite color?',c.random_color())
