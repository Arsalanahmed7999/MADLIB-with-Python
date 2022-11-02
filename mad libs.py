while True:
    properNoun = input("Enter a Person's name: \n ")
    noun = input("Enter a Noun(place): \n ")
    adjective = input("Enter an adjective: \n ")
    pronoun = input("Enter a pronoun: \n")
    verb = input('Enter a verb(action): \n')

    print('***********************************************************')
    print()

    print(f'Yesterday, {properNoun} went to {noun}, it was a {adjective} place.\n On the way {properNoun} was a {adjective} animal.\n Once {pronoun} got to the destination, it was a more {adjective} place.\n Tomorrow we will {verb} in the {noun} as well.')
    print()
    print('***********************************************************')

    newStory = input('You want to create another mab libs? (yes/no): \n')
    if(newStory=='no'):
        break

