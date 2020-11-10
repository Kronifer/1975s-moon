from adventurelib import *

intropod = Room ("""
You're in your space pod, on Mars. 

You've been dreaming about going to the moon, and now you might get the chance.
You see, you're a gamer, and play a game called "To the moon", a game about space exploraton. 
The devs have announced a contest called "Moonshot". 

The challenge is to develop your own space-based game, about going to the moon. You've
dabbled with coding, and think you've got a chance of winning. All you have to do is *wake up*.
""")



current_room = intropod

@when('wake up')
def wup():
     global current_room

start("""
a
""")