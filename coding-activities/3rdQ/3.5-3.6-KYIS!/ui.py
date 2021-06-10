from bst_dictionary import binary_search_tree as bst

valid_choices = "123"
filler = "--------------------------------"
tree = bst()

def display_slang():
    print("LIST OF SLANGS:")
    print(filler)
    tree.display()
    input("Press Enter key to go back to Main Menu.")

def search_slang():
    print("SEARCH SLANG:")
    print(filler)
    slang=input("What slang are you searching for?: ")
    if bst.verify(tree, slang.upper()) == False:
        print(filler)
        print("Sorry, this slang is not in the dictionary...")
    else:
        bst.search(tree, slang.upper())
    input("Press Enter key to go back to Main Menu.")

def add_slang():
    print("ADD NEW SLANG:")
    print(filler)
    slang = input("What's the internet slang?: ")
    if bst.verify(tree, slang.upper()) == True:
        print(filler)
        print("The slang already exists in the dictionary!")
    else:
        meaning = input("What does the slang mean?: ")
        usage = input("What is it used for?: ")
        bst.add(tree, slang.upper(),meaning,usage)
        print(filler)
        print("Successfully added new slang to the dictionary!")
    input("Press Enter key to go back to Main Menu.")

def invalid_choice():
    print("Your input does not match any of the choices!")
    print(filler)
    choice=input("Enter choice: ")
    print(filler)
    if choice not in valid_choices:
        invalid_choice()

    elif choice == "1":
        display_slang()
        
    elif choice == "2":
        search_slang()

    else:
        add_slang()

while True:
    print(filler)
    print("KNOW YOUR INTERNET SLANGS!")
    print(filler)
    print("MAIN MENU:")
    print("1. Slang A-Z")
    print("2. Search Slang")
    print("3. Add New Slang")
    print(filler)
    choice=input("Enter choice: ")
    print(filler)
    if choice not in valid_choices:
        invalid_choice()

    elif choice == "1":
        display_slang()

    elif choice == "2":
        search_slang()

    else:
        add_slang()
