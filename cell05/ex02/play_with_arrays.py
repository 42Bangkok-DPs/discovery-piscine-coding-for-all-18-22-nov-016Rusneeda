#!/usr/bin/env python3
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

new_array = []
for num in original_array:
    if num > 5:
        new_array.append(num + 2)

print("Original array:", original_array)
print("New array:", new_array)

#ใช้คำสั่ง  ./play_with_arrays.py | cat -e ในการรันไฟล์
# เหมือน ex01 แต่อันนี้ให้แสดงเฉพาะตัวเลขที่มากกว่า 5แล้ว+2