# Write a program that takes as input a list of dates and then sorts
a = [[2, 4, 2020], [5, 4, 2023], [7, 4, 2017], [4, 2, 2021]]
import functools as ft


def compare(date1, date2):
    y1 = date1[2]
    y2 = date2[2]
    if y1 != y2:
        return y1 - y2
    m1 = date1[1]
    m2 = date2[1]
    if m1 != m2:
        return m1 - m2
    d1 = date1[0]
    d2 = date2[0]
    if d1 != d2:
        return d1 - d2
    return 0


a.sort(key=ft.cmp_to_key(compare))

print(a)
