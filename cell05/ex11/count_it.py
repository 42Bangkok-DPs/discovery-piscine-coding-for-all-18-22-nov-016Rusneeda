#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    print("parameters:")
    for arg in sys.argv[1:]:
        print(f"{arg}: {len(arg)}")
else:
    print("none")

""" คำสั่งที่ใช้ในการรัน
?> ./count_it.py | cat -e
none$
?> ./count_it.py "Game" "of" "Thrones" | cat -e
parameters: 3$
Game: 4$
of: 2$
Thrones: 7$
?>"""
