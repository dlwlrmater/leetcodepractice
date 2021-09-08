s = "A man, a plan, a canal: Panama"
s1 = filter(str.isalnum,s)
s2 = ''.join(list(s1))
s2 =s2.casefold().lower()
l = len(s2)
l1 = l // 2
a = 0
for i in range(l1):
    if s2[i] == s2[l-1-i]:
        a +=1
if l1 ==a:
    print(True)
else:
    print(False)