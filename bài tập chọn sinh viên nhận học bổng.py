#Lê Dương Thảo K214061745
#Chọn 5 sinh viên nhận học bổng
cac_mon=["môn 1", "môn 2","môn 3","môn 4", "môn 5"]
tin_chi=[2,3,4,5,6]
n=int(input("số sinh viên :"))
ds_drl=[]
ds_cuoicung=[]
def nhap_diem():
    ds_diem = []
    diem_mon=float(input("Nhập điểm "+ cac_mon[j]+":"))
    ds_diem.append(diem_mon)
    return(ds_diem)
def tb_1_mon(diem, tc,tin_chi):
    for k in range(len(cac_mon)):
      tong=round(diem[k] *tc/sum(tin_chi),2)
      return (tong)
def diem_tb_sv(tong,drl):
    tb=round(sum(tong)+drl*0.2,2)
    return tb
for i in range(n):
    ten_sv=input("Tên sinh viên:")
    drl=float(input("Điểm rèn luyện:"))
    ds_drl.append(drl)
    ds_diem_1sv = []
    for j in range(len(cac_mon)):
        m=nhap_diem()
        a=tb_1_mon(m, tin_chi[j], tin_chi)
        ds_diem_1sv.append(a)
    b=diem_tb_sv(ds_diem_1sv,ds_drl[i])
    print("Điểm trung bình là ", b)
    diem_sv=[b,ten_sv]
    ds_cuoicung.append(diem_sv)
    print(ds_cuoicung)
sap_xep=sorted(ds_cuoicung, reverse= True)
print("5 Sinh viên được nhận học bổng là :",sap_xep[0:5])