import time
import cutie
from MainCharacter import MainCharacter
from ClearScreen import  ClearScreen

def continue_():
    c = input('\nPress anything to continue.')
    


print("""

###         ##  #####  ##      #####    #####       ###     ###      #####  |
 ##        ##   ##     ##     ##       ##   ##     ## ##   ## ##     ##     |
  ##      ##    #####  ##    ##       ##     ##   ##   ## ##   ##    #####  |
   ## ## ##     ##     ##     ##       ##   ##   ##     ###     ##   ##     |
    ##  ##      #####  ######  #####    #####   ##               ##  #####  O              
    
    \n""")


name = input('\nWhat is your name?:')
time.sleep(1.2)
gender = input("\nWhat gender are you?: ")

player = MainCharacter(name = name, gender=gender)
Denner = MainCharacter(name = 'Denner', gender = 'Male')

ClearScreen.clear_screen()







print(f'(confused self)==: You come to, your head feels like it is swirling, your thoughts are moving slow, you reach out to recall your name and barely grasp it.')
    
continue_()

print('\n'+player.name)

time.sleep(1.5)

print(f"""
({player.name})==: That's right, I was.... Where was I?""")

continue_()

print(f'\n(Unknown Voice)==: Hey, are you awake up there yet? Finally...')
continue_()






def ask_fate_question():
    user_choice = input('\n(Unknown Voice)==: I have a quick question for you, do you think you can change fate?')

    if user_choice.lower() == 'yes':
        time.sleep(0.8)
        print('\n(Unknown Voice)==: Many before you have had the same thought. Almost all of them failed.')
        player.brave = True
    elif user_choice.lower() == 'no':
        time.sleep(0.8)
        print('\n(Unknown Voice)==: Not one to fight against the odds, huh?')
    elif user_choice.lower() == 'maybe':
        time.sleep(0.8)
        print("\n(Unknown Voice)==: Either you're not one to make quick decisions or you haven't thought about this before.")
    else:
        time.sleep(0.8)
        print("\n(Unknown Voice)==: Answer 'Yes' or 'No', we don't have time for longer answers.")
        time.sleep(0.8)
        ask_fate_question()

ask_fate_question()
continue_()

print('''

\n({Denner.name})==: I guess.. This is a bit weird, but my name is Denner.

I have bad news and good news for you... for us really...

We both died.''')

continue_()

print('''
But because your species is especially powerful when it comes to psycic abilities and because my body wasn't
to badly damaged, they inserted your psycic essence into my body and now we share the same habitat. That is, my ugly, old ass
body. Sorry about that. unfortunately for you, I had the easy part, I get to remember all of my memories, you have to start 
over.

They say your innate personality will carry over but that you will not have strong memories of your past, only impressions. 
I'm getting ready to search for the person who killed both of us. Why they did it, I have no idea, but it just happens that I 
am a detective and you used to be a psycic forensic specialist. You know, speaking to the dead and feeling the emotions around
the areas of the crimes and such.''')