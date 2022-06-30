'''
program to calculate cost of serving sizes for recipes
base component
v1 - set up the skeleton of the program, test the functions are called as required
GF 2022
'''

# import library ✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭

# set up functions ✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭

# function to ask for recipe and give error for blank

def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error_message)

# function to calculate cost to make
def cost_to_make():
    print("cost to make")

# function to calculate total cost of meal
def cost_of_meal():
    print("cost of meal")

# function to calculate cost per serving
def cost_per_serving():
    print("cost per serving")

# main routine
recipe_name = not_blank("Recipe name: ",
                        "Sorry - this cant be blank, "
                        "Please enter your recipe name")
