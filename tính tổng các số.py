#K214061745_Lê Dương Thảo#
"""tính tổng n số đầu tiên"""
n = int(input("nhập số:"))
s = 0
def tongnso(tong):
  for i in range(n+1):
   tong+=i
  return tong
tong=tongnso(s)
print("tổng của", n, " số đầu tiên là :", tong)
"""tính tổng các số được nhập vào"""
m = int(input("bạn muốn tính tổng bao nhiêu số: "))
tong = 0
cac_so = []
for i in range(m):
 a=int(input("nhập số:"))
 cac_so.append(a)
def tong_so(s):
 for i in cac_so:
  s+=i
 return(s)
tong=tong_so(tong)
print(tong, " là tổng của", cac_so)

