def print_params(a=1, b='string', c=True):
    print(a, b, c)

print_params()
print_params(2, 'brrr')
print_params('skr', None, 2.4)
# print_params(3, 5, 3, 6) # ошибка
print_params(b = 25)
print_params(c = [1, 2, 3])


values_list = [5, 4, 'three']
values_dict = {'a':1, 'b':'hello', 'c':False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['test', 3.14]

print_params(*values_list_2, 42)