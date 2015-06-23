'''PFUDOR quiz'''

import colors as c
from ask import ask

intro = c.magenta + "Welcome to the PFUDOR Quiz, you must anwser 3 question. Let's see what you know"

def q1():
    anwser = ask(c.magenta + 'What color are the unicorns?' + c.magenta)
    if anwser.startswith('pink'):
        return True
    return False

def q2():
    anwser = ask(c.magenta + 'Where are they danceing?')
    if anwser.startswith('rainbows'):
        return True
    return False

def q3():
    anwser = ask(c.magenta + 'Please use one word to describe the texture of their magical fur:')
    if anwser.startswith('smiles'):
        return True
    return False

questions = [q1,q2,q3]

