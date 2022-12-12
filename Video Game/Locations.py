import cutie
class Locations:
    def hub():
        if cutie.prompt_yes_or_no('Would you like to head to the hub?'):

            options = [
                'Yes, take me to the hub',
                'No, I wish to complete the game.'
            ]

            captions = []
            option = options[cutie.select(options, caption_indices=captions, selected_index=0)]
