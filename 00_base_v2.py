'''
program to calculate cost of serving sizes for recipes
base component
v1 - set up the skeleton of the program, test the functions are called as required
v2 - add not_blank function
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
    return response



# function to calculate cost to make
def cost_to_make():
    print("cost to make")

# function to calculate total cost of meal
def cost_of_meal():
    print("cost of meal")

# function to calculate cost per serving
def cost_per_serving():
    print("cost per serving")

# ✭✭✭✭✭✭✭✭✭✭✭ set up all lists and constants ✭✭✭✭✭✭✭✭✭✭✭

thisdict =	{
  "flour": 3.5,
  "sugar": 3,
  "milk": 2.5
}
x = thisdict["flour"]
x = (125/1500)*x
print("the cost of the flour will be ${:.2f}".format(x))

# ✭✭✭✭✭✭✭✭✭✭✭ main routine ✭✭✭✭✭✭✭✭✭✭✭

# introduction
print("✭✭✭✭✭✭✭✭RECIPE COST PROGRAM✭✭✭✭✭✭✭✭")
print("")
print("Welcome to my program")

print("")
print("")


# get recipe name
recipe_name = not_blank("Please enter a recipe name: ",
                        "Sorry - this cant be blank, "
                        "Please enter your recipe name")
print(recipe_name)

