print("MENU")
print("CHỌN 1 ĐỂ CÀI NHẮC NHỞ DEADLINE")
print("CHỌN 2 ĐỂ HỌC TẬP VỚI POMODORO ")
print("CHỌN 0 ĐỂ KẾT THÚC")

from datetime import datetime
import time
today = datetime.now()
hour = today.hour
minute = today.minute
second = today.second
day = today.day
month = today.month
year = today.year
print("NGÀY GIỜ HIỆN TẠI LÀ",day,"/",month,"/",year," ",hour,":",minute)
ch = int(input("nhập lựa chọn của bạn: "))
""" LỰA CHỌN 0"""
if ch==0:
    print("! CHƯƠNG TRÌNH ĐÃ KẾT THÚC !")
""" LỰA CHỌN 1"""
if ch==1:
    def changetime(gio, phut, giay):
        t = gio * 60 * 60 + phut * 60 + giay
        return (t)

    ds_deadline = []
    flag = 0
    while True:
        if flag == 1:
            break
        deadline = []
        thoigian_thongbao = []
        thoigian_deadline = []
        ten = input('Nhập tên deadline: ')
        deadline.append(ten)
        ngay_dl, thang_dl, nam_dl = map(int, input('Nhập ngày theo format (nn/tt/nnnn): ').split('/'))
        gio_dl, phut_dl, giay_dl = map(int, input('Nhập giờ theo format (hh:mm:ss)').split(':'))
        ghichu = input('Nhập ghi chú:')
        deadline.append(ghichu)
        thoigian_tb = input('Nhập giờ bạn muốn nhắc nhở hàng ngày:').split(':')
        deadline.append(thoigian_tb)
        thoigian_deadline.append(nam_dl)
        thoigian_deadline.append(thang_dl)
        thoigian_deadline.append(ngay_dl)
        thoigian_deadline.append(gio_dl)
        thoigian_deadline.append(phut_dl)
        thoigian_deadline.append(giay_dl)
        deadline.append(thoigian_deadline)
        ds_deadline.append(deadline)
        choice = str(input('Bạn có muốn thêm deadline không? (có/ko) '))
        if choice == "có":
            print(ds_deadline)
            continue
        else:
            while True:
                if flag == 1:
                    break
                thoigianhientai = datetime.now().time()
                gio_hientai = thoigianhientai.hour
                phut_hientai = thoigianhientai.minute
                giay_hientai = thoigianhientai.second
                for i in range(len(ds_deadline)):
                    t1 = changetime(gio_hientai, phut_hientai, giay_hientai)
                    t2 = changetime(int(ds_deadline[i][2][0]), int(ds_deadline[i][2][1]), int(ds_deadline[i][2][2]))
                    deadlinene = datetime(int(ds_deadline[i][3][0]),int( ds_deadline[i][3][1]), int(ds_deadline[i][3][2]),
                                          int(ds_deadline[i][3][3]), int(ds_deadline[i][3][4]), int(ds_deadline[i][3][5]))
                    if flag == 1:
                        break
                    print('Bạn có deadline thứ', i + 1, ':')
                    if datetime.now() < deadlinene:
                        print('Thời gian còn lại', deadlinene - datetime.now())
                    if datetime.now() > deadlinene:
                        print('Đã trễ', datetime.now()-deadlinene)
                    if t1 == t2:
                        print('Bạn có deadline vào lúc', deadlinene)
                        print('Ghi chú: ', ds_deadline[i][1])
                        thoat = input('Bạn có muốn thoát chương trình nhắc nhở deadline không? (có/ko)')
                        if thoat == 'có':
                            flag = 1
                            break
                        if thoat == 'ko':
                            continue
                    time.sleep(1)

    ch = int(input("bạn còn muốn làm gì nữa không? Nhập lựa chọn của bạn: "))
""" lỰA CHỌN 2"""
if ch==2:
    print("Chào mừng bạn đến với Pomodoro")
    def cong_viec(): # lời nhắc: tên công việc
        print("Công việc của hôm nay là gì?")
        cong_viec=str(input("Hãy nhập ông việc mà bạn muốn làm: "))
        return(cong_viec)

    tgian=input("Nhập 'start' khi bạn muốn bắt đầu công việc:")
    def pomodoro(): #bắt đầu chạy pomodoro
        import time
        if tgian=='start':
         print("Hãy bắt đầu làm việc thôi !")
         print(cong_viec())
         for i in range(4): # pomodoro có 4 phiên làm việc
             t = 25*60
             while t :
                 min = t // 60
                 sec = t % 60
                 print(min,":", sec)
                 time.sleep(1) #dùng hàm spleep để trì hoãn thức thi trong 1 giây ---> để đếm ngược thời gian
                 t -= 1 # t giảm dần
             print("Hết giờ rồi") #playsound
             print("Hãy nghỉ ngơi 5 phút nhé:")
             t = 5*60
             while t: #các giải thihcs giống với phần trên
                 min = t // 60
                 sec = t % 60
                 print(min,":",sec)
                 time.sleep(1)
                 t -= 1
             print("Đã hết 5 phút nghỉ ngơi, hãy bắt đầu làm việc tiếp nào!") #playsound

        a = input("Nếu bạn đã hoàn thành công việc hãy nhập 'xong':")
        if a == 'xong':
            print("Bạn đã hoàn thành công việc đặt ra cho hôm nay ! Rât tốt ")
    pomodoro( )
    lua_chon=input("Nhập 'restart'để bắt đầu Pomodoro mới Hoặc nhập 'end' để kết thúc học cùng Pomodoro:")
    if lua_chon=='restart':
        cong_viec( )
        pomodoro( )
    else :
        print("Pomodoro của hôm nay đã kết thúc!")
    ch = int(input("bạn còn muốn làm gì nữa không? Nhập lựa chọn của bạn: "))