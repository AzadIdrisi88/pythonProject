# Using the cmp function
import functools as ft

def compare(x, y):


    return y-x


a = [1, 2, 3, 4, 5]
a.sort(key=ft.cmp_to_key(compare))
print(a)

