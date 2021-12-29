#Lê Dương Thảo K214061745
#Bài tập tính doanh thu bán điện thoại  viết lại
def tien_banduoc(sl,gia):
    tong_tien=str(sl*gia)
    return tong_tien
def tong_sl_1loai(themvao):
    sl=0
    sl=sl+themvao
    return sl
cac_loai={'Iphone 13':10,'Iphone 13 Pro':20,'Iphone Pro Max':30,'Iphone Mini':40}
gia=[10,20,30,40]
print("Các loại điện thoại: Loại 1:Iphone 13 - Loại 2:Iphone 13 Pro - Loại 3:Iphone Pro Max - Loại 4:Iphone Mini")
a=str.lower(input("Bắt đầu bán ? Rồi/chưa :"))
while a== 'rồi' :
    sl_ban = []
    ip13 = []
    ip13pro=[]
    ippromax=[]
    ipmini=[]
    dt=cac_loai.get(input("Loại điện thoại bán được:"))
    if dt==10:
     sl13 = int(input("Số lượng:"))
     ip13.append(sl13)
    elif dt==20:
     sl13pro = int(input("Số lượng:"))
     ip13pro.append(sl13pro)
    elif dt==30:
     slpromax= int(input("Số lượng:"))
     ippromax.append(slpromax)
    else:
     slmini = int(input("Số lượng:"))
     ipmini.append(slmini)
    b= input("Đơn hàng mới? (có/ko)")
    if b== 'ko':
        print("Tông tiền bán ", cac_loai.setdefault(), "là" , tien_banduoc(sl,cac_loai[1]), "000 đồng")

        print("Tổng doanh thu của hôm nay là :"   "000 đồng")
        break
