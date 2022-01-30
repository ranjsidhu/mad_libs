# ask user for input
amount_of_goes = input("How many times would you like to play? ")

# error handling function to check if an integer is/not entered
def type_of_input():
    try:
        int(amount_of_goes)
        type_int = True
    except ValueError:
        type_int = False
    
    return type_int

while not type_of_input():
    print("Enter an integer number")
    amount_of_goes = input("How many times would you like to play? ")

# pre-determined sentences and inputs within for loop
def concatenation():
    for i in range(int(amount_of_goes)):
        adj_1 = input("Enter an adjective:  ")
        clr_1 = input("Enter a colour:  ")
        size_1 = input("Enter a size:  ")
        flvr_1 = input("Enter a flavour:  ")
        adj_clr = input("Enter an adjective and a colour e.g. soft blue:  ")
        noun_1 = input("Enter a noun:  ")
        verb_1 = input("Enter a verb:  ")
        family_1 = input("Enter a family member's name:  ")
        clth_1 = input("Enter an item of clothing:  ")
        verb_2 = input("Enter a verb:  ")
        animal = input("Enter an animal:  ")
        face = input("Enter a facial body part:  ")

        # concatenation
        print(f'Have you ever had a pimple? Boy, are they {adj_1}! They are {clr_1} and {size_1} and will explode like a {flvr_1} volcano! Sometimes they pop, and {adj_clr} goo pours out. Use a soft {noun_1} to clean up the mess, and be sure to always {verb_1} your pimples over your {family_1}\'s {clth_1}. Be careful not to {verb_2} your pimple too hard, though...it may hurt like a {animal}\'s horn to the {face}.')

        print("-"*100)

concatenation()