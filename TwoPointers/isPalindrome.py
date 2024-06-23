string = "abcdcba"
length = len(string) - 1
i = 0
j = length
mid = length//2

while (i <= mid and j >= mid):
    if (string[i] != string[j]):
        print(False)
        break
    i += 1
    j -= 1
else:
    print(True)
