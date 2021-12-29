#K214061745_Lê Dương Thảo#
#------------------------------------------------------
"""nhap va tinh tu, mau cua phan so"""
tu=0
mau=1
n = int(input("so phan so :"))
for i in range(1, n+1):
  ps = []
  ps.append(int(input(" nhap tu so", )))
  ps.append(int(input(" nhap mau so", )))
  tu = ps[0]*mau+tu*ps[1]
  mau = ps[1]*mau
"""rut gon phan so"""
n = min(tu, mau)
x = 0
for i in range(2, n+1):
 if tu % i == 0 and mau% i == 0:
  x = i
  tu= tu//x
  mau = mau//x
print("ket qua la :", tu,"/",mau, )