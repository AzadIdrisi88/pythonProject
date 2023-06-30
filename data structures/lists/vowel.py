a = ["apple", "mango", "orange", "cat", "deer",'aam']


def countVowels(x):
    vowels = "aeiou"
    count = 0
    x = x.lower()
    for ch in x:
        if ch in vowels:
            count += 1
    return -count


print(a)
a.sort(key=countVowels)
print(a)
