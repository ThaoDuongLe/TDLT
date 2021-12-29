#Lê Dương Thảo _ K214061745
# Bài tập tư vấn khối học
def tinhdiem_khoi(diem):
   A = diem[0] * 2 + diem[1] + diem[2]
   B = diem[5] * 2 + diem[0] + diem[2]
   C = diem[3] * 2 + diem[6] + diem[7]
   D = diem[5] * 2 + diem[4] + diem[0]
   return([A,"Khối A"],[B,"Khối B"],[C,"Khối C"],[D, "Khối D"])
def chon_khoi(khoi):
    n=max(khoi)
    return(n)
danhsachmon=["toán", "vật lý", "hóa học", "ngữ văn", "sinh học", "anh văn", " lịch sử", "địa lý"]
cacdiem =[]
for i in range(8):
    #nhập điểm của các môn vào
    diem=float(input(" Nhập điểm môn" +" "+str(danhsachmon[i]) +":"))
    while (diem<0) or(diem>10):
        # trường hợp nhập điểm không hợp lệ
        print("Bạn nhập sai mời nhập lại")
        diem = float(input("Nhập điểm vào"))
    cacdiem.append(diem)
diemso=tinhdiem_khoi(cacdiem)
khoi=chon_khoi(diemso)
print("Điểm cao nhất là", khoi[0],". Bạn nên học", khoi[1])



