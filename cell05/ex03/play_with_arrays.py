#!/usr/bin/env python3
my_list = [2, 8, 9, 48, 8, 22, -12, 2]
unique_list = []

for num in my_list:
    if num not in unique_list:
        unique_list.append(num)

print(unique_list)

#ใช้คำสั่งนี้ในการรันไฟล์ ./play_with_arrays.py | cat -e
# แสดงตัวเลขที่ไม่ซ้ำในอาเรย์