import shelve

# blt = ['bacon', 'lettuce', 'tomato', 'bread']
# beansOnToast = ['beans', 'bread']
# scrambledEggs = ['eggs', 'butter', 'milk']
# pasta = ['pasta', 'cheese']
soup = ['tin of soup']

with shelve.open('recipes', writeback=True) as recipes:
    # recipes['blt'] = blt
    # recipes['beansOnToast'] = beansOnToast
    # recipes['scrambledEggs'] = scrambledEggs
    # recipes['pasta'] = pasta
    # recipes['soup'] = soup

    # tempList = recipes['blt']
    # tempList.append('butter')
    # recipes['blt'] = tempList
    #
    # tempList = recipes['pasta']
    # tempList.append('tomato')
    # recipes['pasta'] = tempList
    # recipes['soup'].append('croutons')
    recipes['soup'] = soup
    recipes.sync()
    soup.append('cream')

    for snack in recipes:
        print(snack, recipes[snack])