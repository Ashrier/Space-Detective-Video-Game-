import time
import cutie
from MainCharacter import MainCharacter
from ClearScreen import  ClearScreen

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
        print('(Dennis)==: Of course, I am sorry.')
