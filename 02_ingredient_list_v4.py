'''
component 2 - ingredient list
v1 - ask for ingredient, check in dict and calculate cost of ingredient
v2 - error message displayed when wrong ingredient entered
v3 - stop program when 'xxx' is entered
v4 - add items to list, check ingredients in list, error message for incorrect input and program stops for "xxx" input
calculate cost of ingredient and total cost of each ingredient
GF 2022
'''

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
#main routine *******************
recipe = ["flour","sugar","milk"]
items_list = ['flour', 'sugar', 'milk']
item_weight = [1500, 1500, 1000]
item_cost = [3.5,4.5,2.5]
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

 # pull the weight out of ingredient_list



  # start of loop

# initialise loop so that it runs at least once
#error_message = ("this is not an integer")

while True:

    ingredient = input("enter ingredient: ")
    #cost = amount/ingredient_weight*ingredient_price
    #ingredient = input("enter ingredient: ")


    if ingredient == "xxx":
        print(*ingredient_list)
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
    print("the cost of the " + ingredient + " will be ${:.2f}".format(cost))
    print("________________")
    print()



