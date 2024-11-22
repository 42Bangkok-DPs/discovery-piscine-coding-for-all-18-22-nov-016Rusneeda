#!/usr/bin/env python3
import sys

if len(sys.argv) > 1: #เช็คว่ามีตัวแปรส่งมาไหม
    print(sys.argv[1]) # ถ้ามีก็แสดงค่าตัวแรก
else:
    print("none") #ถ้าไม่มีให้แสดง ข้อมความnone

""" ใช้คำสั่ง
./aff_first_param.py | cat -e
none$
./aff_first_param.py "Code Ninja" "Numerique" "42" | cat -e
Code Ninja$ 
"""
