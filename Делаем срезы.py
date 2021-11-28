s=input()
cin=0
c=""
for c in s:
    cin+=1
    if cin==3:
        print(c)
    if cin==len(s)-1:
        print(c)
print(s[0:5])
print(s[0:len(s)-2])
cin=0
for c in s:
    cin+=1
    if cin%2!=0:
        print(c, end='')
#print('\n')
print(sep='')
cin=0
for c in s:
    if cin%2!=0:
        print(c, end='')
    cin+=1
print(sep='')
print(s[::-1])
print(s[::-2])
cin=0
for c in s:
    cin+=1
print(cin)
