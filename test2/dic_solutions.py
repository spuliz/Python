a=['this','is',]
item_to_replace = 'is'
replacement_value = 'was'
indices_to_replace = [i for i,x in enumerate(a) if x==item_to_replace]
indices_to_replace [0, 5, 10]
 for i in indices_to_replace:
...     a[i] = replacement_value
...
 a
[6, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6]

