from adventurelib import *

intropod = Room ("See intro")

say("""
You're in your space pod, on Mars. 

You've been dreaming about going to the moon, and now you might get the chance.
You see, you're a gamer, and play a game called "To the moon", a game about space exploraton. 
The devs have announced a contest called "Moonshot". 

The challenge is to develop your own space-based game, about going to the moon. You've
dabbled with coding, and think you've got a chance of winning. All you have to do is *wake up*.
""")

current_room = intropod

set_context('asleep')

@when('wake up', context='asleep')
def wup():
     global current_room
     say("""
     You wake up, ready to start the day off. But, you decide it's a good idea to *have breakfast*."""
     )
     set_context('intropod')

@when('have breakfast', context='intropod')
def breakfasttime():
     say("""
     You head into the kitchen, and start cooking up some eggs and toast.

     As you cook, you think about the contest, and about the moon. The moons always been a dream of yours.

     As your breakfast finishes, you decide you could either *eat it*, or go *find a style of game to make*.
     """)
start()

