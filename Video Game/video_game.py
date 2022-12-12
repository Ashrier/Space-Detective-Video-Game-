import time
import cutie
from MainCharacter import MainCharacter
from ClearScreen import  ClearScreen
from Locations import Locations

def continue_():
    c = input('\nPress Enter to continue.')
    


print("""

###         ##  #####  ##      #####    #####       ###     ###      #####  |
 ##        ##   ##     ##     ##       ##   ##     ## ##   ## ##     ##     |
  ##      ##    #####  ##    ##       ##     ##   ##   ## ##   ##    #####  |
   ## ## ##     ##     ##     ##       ##   ##   ##     ###     ##   ##     |
    ##  ##      #####  ######  #####    #####   ##               ##  #####  O              
    
    \n""")


name = input('\nWhat is your name?:')
time.sleep(1.2)

player = MainCharacter(name = name)
denner = MainCharacter(name = 'Denner')

ClearScreen.clear_screen()







print(f'(confused self)==: You come to, your head feels like it is swirling,\n your thoughts are moving slow, you reach out to recall your name and barely grasp it.')
    
continue_()

print('\n'+player.name)

time.sleep(1.5)

print(f"""
({player.name})==: That's right, I was.... Where was I?""")

continue_()

print(f'\n(Unknown Voice)==: Hey, are you awake up there yet? Finally...')
continue_()






def ask_fate_question():
    user_choice = input('\n(Unknown Voice)==: I have a quick question for you, do you think you can change fate?\n')

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

print(f'''

\n({denner.name})==: I guess.. This is a bit weird, but my name is Denner.

I have bad news and good news for you... for us really...

We both died.''')

continue_()

print(f'''
\n({denner.name})==: But because your species is especially powerful when it comes to psycic abilities and because my body wasn't to badly damaged, they inserted your psycic essence into my body and now we share the same habitat. That is, my ugly, old assbody. Sorry about that. unfortunately for you, I had the easy part, I get to remember all of my memories, you have to start over.

They say your innate personality will carry over but that you will not have strong memories of your past, only impressions. I'm getting ready to search for the person who killed both of us. Why they did it, I have no idea, but it just happens that I am a detective and you used to be a psycic forensic specialist. You know, speaking to the dead and feeling the emotions around the areas of the crimes and such.''')

continue_()

print(f'''
\n({denner.name})==: Well, I've been up for 2 hours already and my body is good to go. 'Thank you nano-healing gel.'-denner tries to think this privately to himself. I've been assigned this case on the account of me being the only detective on this space station. The boss tried to put Jurmand on this!.''')

if cutie.prompt_yes_or_no('Would like to try to remember Jurmand?'):
    options = [
        "Of course I don't remember! I just woke up 2 minutes ago and you've just been spouting off stuff!",
        "Yea, good guy.",
        "Jurmand? Like that giant earth norse lizard tale?? It is real?!?!",
        "No."
    ]
    # Names which are captions and thus not selectable
    captions = []
    # Get the name
    option = options[cutie.select(options, caption_indices=captions, selected_index=0)]
    if option == options[0]:
        print(f'\n({denner.name})==: Of course, I am sorry.')
    if option == options[2]:
        print(f"\n({denner.name})==: Ehh, I guess his dandruff can make it look like he sheds a bit, but no he is not Jormangander.") 
    if option == options[1] or option == options[3]:
        print(f"\n({denner.name})==: Being of few words huh?")

continue_()

print(f'''
\n({denner.name})==: Well, the best thing to do now is move on, we have a killer on the loose and we don't know who it is. We do think that we were unfortunate bystanders. 7 other people were killed in the blast and part of the hubs oxygen transport system was damaged too. Engineering has repairs underway and the families of the deceased are or have been notified. I think we have only been out one day (miracles of current day surgery huh). I say we go to the hub and talk to the forensic bots there and see what has been found, or we can go the precinct in the hub first and see what the footage captured.''')

Locations.hub()

if player.solved_case == False:
    print('\nYou did not solve the case and the space station blows up.')
else:
    print('\nYou solved the case and saved the space station!')