# x = 10
# y = 50
# y,x=x,y
# print(x, y)
# x=[1,2,3,4,5,6,7,8,9,10]
# y=x
# x[2]=0
# print(y)
def knows(a, b):
    known = {0: [1, 2], 1: [2, 3], 2: [3]}
    d = known.get(a)
    if d is None:
        return False
    if b in d:
        return True
    return False
print(knows(3,1))



