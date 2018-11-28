shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopping_list:
    if item == 'spam':
        print("Fuck " + item)
        continue  # goes to the next item in the for loop
    print("Buy " + item)

meal = ["egg", "bacon", "spam", "sausages"]
for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break  # leaves the current loop
else:  # runs if loop not broken out of
    nasty_food_item = ''
    print("I'll have a plate of that, then, please.")

if nasty_food_item:
    print("Can't I have anything without spam in it?")