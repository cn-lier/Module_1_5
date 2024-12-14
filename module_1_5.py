Immutable_var = 30, 'string', True, 4.7
print(Immutable_var)
#Immutable_var[0] = 3 Попытка изменить элементы кортежа в Python приведет к ошибке.
#print(Immutable_var) Кортежи в Python являются неизменяемыми (Immutable) структурами данных.
# TypeError: 'tuple' object does not support item assignment
Mutable_list = [15, 2024, "Python", False]
print(Mutable_list)
Mutable_list[1] = 2025
Mutable_list[2] = "Happy new year"
print(Mutable_list)