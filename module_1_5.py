immutable_var = 1, 2, 3, 'evgenij', True
print('immutable tuple:', immutable_var)
#immutable_var[1] = 12
#    ~~~~~~~~~~~~~^^^
#TypeError: 'tuple' object does not support item assignment
#кортеж не поддерживает обращение по элементам
mutable_list = [1, 2, 3, 4, 'stop', True]
print('Mutable list:', mutable_list)
mutable_list[3] = 100
mutable_list.append(False)
print('Mutable list modific_1:', mutable_list)
mutable_list.extend('gays')
print('Mutable list modific_2:', mutable_list)
mutable_list.remove(False)
print('Mutable list modific_3:', mutable_list)
#print(5 in mutable_list )
