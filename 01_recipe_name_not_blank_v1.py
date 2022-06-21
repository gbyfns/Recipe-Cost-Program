'''
component 1 - recipe name not blank
v1 - ask for recipe name and check it isn't blank, give error msg for blank name
GF 2022
'''

# functions go here

def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error_message)


# main routine
recipe_name = not_blank("Recipe name: ",
                        "this cant be blank")
