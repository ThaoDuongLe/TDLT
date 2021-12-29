#Lê Dương Thảo K214061745
#Bài tập tính doanh thu bán điện thoại
def nhap_soluong():
    ip13 = int(input("Số lượng Iphone 13 bán được :"))
    sl_ip13.append(ip13)
    ip13pro = int(input("Số lượng Iphone 13 Pro bán được :"))
    sl_ip13pro.append(ip13pro)
    promax = int(input("Số lượng Iphone 13 Pro Max bán được :"))
    sl_promax.append(promax)
    mini = int(input("Số lượng Iphone Mini bán được :"))
    sl_mini.append(mini)
    return(sl_ip13, sl_ip13pro,sl_promax,sl_mini)
def doanhthu_cuoingay(sl,gia):
    doanh_thu=sum(sl)*gia
    return doanh_thu
"""ip13=10 ip13pr=20 ip13prm=30 ipmn=40"""
sl_ip13=[]
sl_ip13pro=[]
sl_promax=[]
sl_mini=[]
a=str.lower(input("Bắt đầu bán ? Rồi/chưa :"))
while a=='rồi' :
    nhap_soluong()
    b= input("Đơn hàng mới? (có/không)")
    if b=='không':
        c=doanhthu_cuoingay(sl_ip13,10)
        print("Tông tiền bán Iphone 13 là",c, "000 đồng")
        d=doanhthu_cuoingay(sl_ip13pro,20)
        print("Tổng tiền bán Iphone 13 Pro là",d, "000 đồng")
        e=doanhthu_cuoingay(sl_promax,30)
        print("Tổng tiền bán Iphone 13 Pro Max là",e, "000 đồng")
        f=doanhthu_cuoingay(sl_mini,40)
        print("Tổng tiền bán Iphone Mini là",f, "000 đồng")
        print("Tổng doanh thu của hôm nay là :" , c+d+e+f , "000 đồng")
        break

