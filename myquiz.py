"""my quiz"""

import colors as c
import random
from ask import ask

intro = c.yellow + "Welcome to a quiz about Jake!!!!" 

def q1():
    anwser = ask(c.yellow + 'How old is Jake?' + c.yellow)
    if anwser.startswith('12.5'):
        return True
    return False

def q2():
     anwser = ask(c.yellow + "What is Jake's favorite video game franchise" + c.yellow)
     if anwser.startswith('pokemon' or 'mother' or 'zelda' or 'earthbound'):
         return True
     return False

def q3():
     anwser = ask(c.yellow + "Who is Jake's best friend" + c.yellow)
     if anwser.startswith('Rees' or 'Drake' or 'John' or 'Grayson' or 'Christon' or 'Lydia' or 'Connor' or 'Fisher'):
         return True
     return False


