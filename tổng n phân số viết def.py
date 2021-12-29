#k214061745 Lê Dương Thảo
#tính tổng n phân số
n=int(input("Số phân số muốn tính tổng"))
tong_ps=[0,1]
def tongps(ps1,ps2):
    tong=[0,1]
    tong[0]=ps1[0]*int(ps2[1])+ps1[1]*int(ps2[0])
    tong[1]=ps1[1]*int(ps2[1])
    return (tong)
def toigian(ps_ch_toigian):
    n = min(ps_ch_toigian)
    for i in reversed(range(1,n+1)):
     if ps_ch_toigian[0]% i == 0 and ps_ch_toigian[1]% i == 0:
      x = i
      tu= ps_ch_toigian[0]//x
      mau = ps_ch_toigian[1]//x
      return (tu,mau)
for i in range(n):
    print("Nhập phân số thứ ", i+1)
    a=input("Nhập phân số: " )
    ps=a.split("/")
    tong_ps=tongps(tong_ps,ps)
ketqua=toigian(tong_ps)
print("ket qua la ", ketqua[0] ,"/", ketqua[1])







