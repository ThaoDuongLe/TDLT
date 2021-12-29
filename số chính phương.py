#kiểm tra 1 số có phải số chính phương
n = int(input("số muốn kiểm tra :"))
flag =0
for i in range(n):
 if (n ==i*i):
     flag=1
if (flag==1):
    print(n, " là số chính phương")
else: print(n, "không là số chính phương")

"""Kỹ thuật cắm cờ là kỹ thuật đơn giản nhất, nó giúp bạn kiểm soát các trường hợp quan trọng.
Bạn sẽ lưu giá trị flag luôn luôn là một con số mặc định nào đó, thường là 0. Với các trường hợp đặc biệt khác, 
ta lưu giá trị nó làm các con số khác nhau để tiện cho việc xử lý.
Ví dụ như ở đây, tôi muốn kiểm tra đây có phải là số nguyên tố hay không. Tôi cài đặt 1 biến flag = 0,
 số đang kiểm tra là số x, khi x không phải là số nguyên  tố thì flag = 1. 
 Sau đó dựa vào biến flag mà tôi quyết định có in ra màn hình."""