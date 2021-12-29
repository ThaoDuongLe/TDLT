#K214061745_Lê Dương Thảo#
"""tim uoc chung lon nhat cua hai so"""
a = int(input("nhập số a:"))
b = int(input("nhập số b:"))
n = min(a, b)
x = 0
for i in range( 1, n+1):
 if a % i == 0 and b % i == 0:
  x = i
if x!=1:
 print(x, 'la uoc chung lon nhat')
else:
 print("ước chung duy nhất là ",x)
# viết def
c = int(input("nhập số c:"))
d = int(input("nhập số d:"))
m = min(c, d)
def uocchung(s1,s2):
 n = min(s1,s2)
 x=0
 for i in reversed(range(1, n + 1)):
  if s1% i == 0 and s2% i == 0:
   x = i
   return(x)
print("ước chung lớn nhất là",uocchung(c,d))

