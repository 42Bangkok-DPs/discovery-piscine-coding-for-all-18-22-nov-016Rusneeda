#!/usr/bin/env python3
def greetings(name="noble stranger"):
  """ฟังก์ชันแสดงข้อความต้อนรับ"""
  if not isinstance(name, str):
    print("Error! It was not a name.")
  else:
    print(f"Hello, {name}!")

if __name__ == "__main__":
  greetings("Alexandra")
  greetings("Wil")
  greetings()
  greetings(42)
  

""" คำสั่งที่ใช้ และผลลัพธ์
 ./greetings_for_all.py | cat -e
Hello, Alexandra.$
Hello, Wil.$
Hello, noble stranger.$
Error! It was not a name.$
"""