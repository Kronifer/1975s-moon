from adventurelib import *

say("""
Welcome to the Moon of 1975! This is a game about making a game.

The goal of the game is to win a game dev contest about the moon.

To start the game, use the wake up command.
""")

set_context("start")

@when('wake up', context="start")
def wup():
     say("""
     You wake up, ready to start the new day. You 
     went to bed last night thinking about this
     game jam you heard of, called Moonshot.

     The prize for winning is an all-expenses paid
     trip to the Moon, a place you've always dreamed
     of going. But, before you do any work, you might 
     want to make some breakfast. To do that, just head into the kitchen.
     """)
     set_context('kitchentime')

@when('head into the kitchen', context='kitchentime')
@when('go into the kitchen', context='kitchentime')
def gointokitchen():
     say("""
     You head into the kitchen, thinking about what to make.

     You decide it's a good time to start cooking breakfast.
     """)

     set_context('cookbreakfast')

@when('start cooking breakfast', context='cookbreakfast')
@when('cook breakfast', context='cookbreakfast')
def breakcook():
     say("""
     You throw some bacon and eggs on the frying pan,
     and put bread in the toaster. Your breakfast is ready soon enough.

     Soon, you're done eating, and you decide to either scour the internet,
     or go outside for inspiration for your game.
     """)
     set_context('breakchoice')
@when('go outside', context='breakchoice')
@when('head outside', context='breakchoice')
@when('go outside for inspiration', context='breakchoice')
@when('go outside for inspiration for your game', context='breakchoice')
def outsidesearch():
     say("""
     You head outside to find some game inspiration. You watch kids playing,
     hear teenagers fantasize about space, adults work on theoretical rocket designs.

     Then it hits you. Your game is going to be about a child, who builds a 
     spaceship to fly to the moon. But you don't know what genre of game
     you want to make. Should you decide on your own, or leave it to chance?
     """)
     set_context('outchoice')


start()