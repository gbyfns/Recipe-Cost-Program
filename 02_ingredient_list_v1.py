'''
component 2 - ingredient list
v1 - ask for ingredient, check in dict and calculate cost of ingredient
GF 2022
'''

cake_recipe = ['flour', 'sugar', 'milk']

weight = float(1500)
amount = float(150)
price = 2.5

thisdict = {
  "flour": [2.5, 1500],
  "sugar": [3.5, 1500],
  "milk": [2.5, 1000]
}

#dictonary for cake recipe

print("✭✭✭✭✭ this program is in beta, please enter ingredients listed ✭✭✭✭✭")
print()
print("~~~~~~~")

for i in range(0, len(cake_recipe)):

    print(cake_recipe[i])

print("~~~~~~~")
print()
print("please type 'xxx' to stop entering ingredients")
print()


#cost = amount/weight*price

ingredient = input("enter ingredient: ")
amount = float(input("amount (in grams or litres): "))
ingredient_list = thisdict[ingredient]
weight = float(ingredient_list[1]) # pull the weight out of ingredient_list
price = (ingredient_list[0])

  # start of loop

# initialise loop so that it runs at least once


while True:

    cost = amount/weight*price

    if ingredient == "xxx":
        break
    else:
        print("the cost of the " + ingredient + " will be ${:.2f}".format(cost))
    print()
    ingredient = input("enter ingredient: ")
    amount = float(input("amount (in grams or litres): "))

