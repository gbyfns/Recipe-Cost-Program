'''
program to calculate cost of serving sizes for recipes
base component
v1 - set up the skeleton of the program, test the functions are called as required
v2 - add not_blank function
v3 - add second component
GF 2022
'''


# set up functions ✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭✭

#int checker funcion

def int_checker(amount_question, error_message):

        #amount = int(input("please enter amount:"))

        x = True
        while x == True:

            try:
                int_num = int(input(amount_question))
                x = False
            except:
                print(error_message)

            ingredient_list.append(int_num)
        return(int_num)

        returned_num = int_checker("please enter an amount in grams: ", "sorry - this is not an integer ")


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

# ✭✭✭✭✭✭✭✭✭✭✭ set up all lists and constants ✭✭✭✭✭✭✭✭✭✭✭

thisdict =	{
  "flour": 3.5,
  "sugar": 3,
  "milk": 2.5
}
#x = thisdict["flour"]
#x = (125/1500)*x
#print("the cost of the flour will be ${:.2f}".format(x))

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
#print(recipe_name)
print()

#main routine *******************
recipe = ["flour","sugar","milk"]
items_list = ['flour', 'sugar', 'milk']
item_weight = [1500, 1500, 1000]
item_cost = [3.5, 4.5, 2.5]
#hard coded lists ***************


#ingredient_weight = float(1500)
#ingredient_weight = float(1500)
#amount = float(150)
#ingredient_price = 2.5
#ingredient_price = 2.5

thisdict = {
  "flour",
  "sugar",
  "milk"
}

#dictonary for cake recipe hard coded

print("✭✭✭✭✭ this program is in beta, please enter ingredients listed ✭✭✭✭✭")
print()
print("~~~~~~~")

#for i in range(recipe):


print(*recipe, sep="\n")

print("~~~~~~~")
print()
print("please type 'xxx' to stop entering ingredients")
print()


#cost = amount/weight*price

ingredient = " "
#amount = 0
ingredient_list = [] #list to append user
total_costs = []


 # pull the weight out of ingredient_list



  # start of loop

# initialise loop so that it runs at least once
#error_message = ("this is not an integer")

while True:

    ingredient = input("enter ingredient: ")

    #cost = amount/ingredient_weight*ingredient_price
    #ingredient = input("enter ingredient: ")

    if ingredient == "xxx":

        #total_costs.append(cost)
        total_price = sum(total_costs)
        print()
        print("the total price to make " + recipe_name + " is ${:.2f}".format(total_price))
        break

    if ingredient in recipe:
        print()

        #for i in ingredient_list:
            #print(i)                   #for when enter 'xxx'


        #amount = input("please enter an integer:")
    else:
        print("error - please enter ingredient in the list")
        print()
        #ingredient = input("enter ingredient: ")

    if ingredient in recipe:
        ingredient_list.append(ingredient)
        amount = float(input("amount (in grams or litres): "))
        ingredient_list.append(amount)



        #ingredient = input("enter ingredient: ")

    #amount = input("please enter an integer:")


    if ingredient not in recipe:

        continue


    idx = ingredient_list.index(ingredient)
    price = item_cost[idx]
    weight = item_weight[idx]

    cost = amount/weight*price


#main
#check that the int checker is called and returns a number

    #returned_num = int_checker("please enter an amount in grams: ", "sorry - this is not an integer ")


    print()
    #print(*ingredient_list, sep = "\n")
    total_costs.append(cost)
    print("the cost of the " + ingredient + " will be ${:.2f}".format(cost))
    print("________________")
    print()

