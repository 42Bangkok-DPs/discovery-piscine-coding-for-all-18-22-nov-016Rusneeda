#!/usr/bin/env python3
import sys

# ตรวจสอบว่ามีพารามิเตอร์ 1 ตัวหรือไม่
if len(sys.argv) == 2:
    # ถ้ามีพารามิเตอร์ 1 ตัว ให้แปลงเป็นตัวอักษรใหญ่และแสดงผล
    print(sys.argv[1].upper())
else:
    # ถ้าจำนวนพารามิเตอร์ไม่เท่ากับ 1 ให้แสดง 'none'
    print("none")
    
"""  ใช้คำสั่ง
./upcase_it.py | cat -e
none$
?> ./upcase_it.py "initiation" | cat -e
INITIATION$
?> ./upcase_it.py 'This exercise is quite easy!' | cat -e
THIS EXERCISE IS QUITE EASY!$
"""