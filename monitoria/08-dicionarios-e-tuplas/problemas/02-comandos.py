'''
https://panda.ime.usp.br/pensepy/static/pensepy/11-Dicionarios/dicionarios.html
'''

'''
>>> d = {'apples': 15, 'bananas': 35, 'grapes': 12}
>>> d['banana']
>>> d['oranges'] = 20
>>> len(d)
>>> 'grapes' in d
>>> d['pears']
>>> d.get('pears', 0)
>>> fruits = d.keys()
>>> fruits.sort()
>>> print(fruits)
>>> del d['apples']
>>> 'apples' in d
'''

def add_fruit(inventory, fruit, quantity=0):
    inventory[fruit] = quantity
    return inventory

new_inventory = {}
add_fruit(new_inventory, 'strawberries', 10)
test('strawberries' in new_inventory, True)
test(new_inventory['strawberries'], 10)
add_fruit(new_inventory, 'strawberries', 25)
test(new_inventory['strawberries'] , 35)
