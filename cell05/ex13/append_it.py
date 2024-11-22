#!/usr/bin/env python3
import sys
def append_ism(word):
  """เพิ่มคำว่า 'ism' ต่อท้ายคำที่รับมา ถ้ายังไม่ลงท้ายด้วย 'ism'"""
  if not word.endswith('ism'):
    return word + 'ism'
  return word

if len(sys.argv) > 1:
  for word in sys.argv[1:]:
    result = append_ism(word)
    if result != word:
      print(result)
else:
  print("none")


""" คำสั่งในโจทย์
?> ./append_it.py | cat -e
none$
?> ./append_it.py "parallel" "egoism" "human" | cat -e
parallelism$
humanism$
?>
"""