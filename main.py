def print_params(a=1, b='string', c=True):
    print(a, b, c)

print_params()

values_list = [5, 4, 'three']
values_dict = {'a':1, 'b':'hello', 'c':False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['test', 3.14]

print_params(*values_list_2, 42)