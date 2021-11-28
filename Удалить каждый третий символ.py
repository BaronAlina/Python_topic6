s = input()
a = ''
for c in range(len(s)):
    if c % 3 != 0:
        a = a + s[c]
print(a)
