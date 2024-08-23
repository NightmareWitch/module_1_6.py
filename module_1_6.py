from typing import Set

my_dict = {'Roma': 2008, 'Misha': 2017, 'Leonid': 2019, 'Liza': 2022}
print(my_dict)
print(my_dict.get('Liza'))
print(my_dict.get('Nikolay', 'Такого имени нет'))
my_dict.update({'Igor' : 2013, 'Angelina' : 2007})
print(my_dict)
deleted_name = my_dict.pop('Leonid')
print(my_dict)
print('Deleted Name' , deleted_name)
#Множества
my_set = {1,1,1,'kivi',5,5,5,'cats',73, (4,2,7)}
print(my_set)
print(my_set.add(8))
print(my_set.add('mouse'))
print(my_set)
print(my_set.remove('cats'))
print(my_set)