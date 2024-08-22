my_dict = {'Vasya': 159, 'Petr': 160, 'Kolya': 170}
print('Dict:', my_dict)
print('Height:', my_dict['Kolya'])
print('Not existing value:', my_dict.get('Anton'))
my_dict.update({'Anna': 140, 'Andrej': 180})
print('Modified dictionary_1:', my_dict)
# my_dict['Anna']=140
# my_dict['Andrej']= 180
a = my_dict.pop('Anna')
print('Deleted value:', a)
print('Modified dictionary_2:', my_dict)
print()
my_set = {1, 2, 3, 9, 34, 1, 'pop', 'hit', False, 'pop', (9, 5, 7)}
print('Set:',my_set)
my_set.update({345, 'hjk'})
print('Modified set_1:',my_set)
my_set.discard('pop')
print('Modified set_2:',my_set)