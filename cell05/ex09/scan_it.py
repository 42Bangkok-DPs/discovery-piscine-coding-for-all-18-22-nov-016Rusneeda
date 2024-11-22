#!/usr/bin/env python3
import sys
import re

# ตรวจสอบว่ามีพารามิเตอร์ 2 ตัวหรือไม่
if len(sys.argv) == 3:
    keyword, text = sys.argv[1], sys.argv[2]
    # นับจำนวนครั้งที่ keyword ปรากฏใน text โดยใช้ regular expression
    count = len(re.findall(keyword, text))
    print(count)
else:
    print("none")

"""
?> ./scan_it.py | cat -e
none$
?> ./scan_it.py "the" | cat -e
none$
?> ./scan_it.py "the" "the quick brown fox jumps over the lazy dog" | cat -e
2$
?>
"""