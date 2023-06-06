# write a program to find the frequency of elements in a list. eg-a=[1,2,1,1,3,3], the output will be  1:3, 2:1, 3:2.
# d = {9: 99}
# print(d.get(9,))
k = 3
l = [1, 2, 3, 4, 5, 3, 3, 2, 2, 1, 1, 4, 4, 4, 1, 3, 3, 5, 5, 2, 2, 2, 2]
frequencies = {}
for x in l:
    frequencies[x] = frequencies.get(x, 0) + 1
    if frequencies[x] >= k:
        print(x)
        break

# h=max(frequencies.values())
# print("high=",h)

# frequencies += 1
# frequencies[x] = currentfrequency
# print(frequencies)
print(frequencies)
