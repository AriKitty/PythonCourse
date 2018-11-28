import shelve

with shelve.open('bike2') as bike:
    # bike['make'] = 'Honda'
    # bike['model'] = '250 Dream'
    # bike['color'] = 'red'
    # bike['engineSize'] = 250

    del bike['enginSize']

    for key in bike:
        print(key)

    print('=' * 40)
    print(bike['engineSize'])
    # print(bike['enginSize'])
    print(bike['color'])