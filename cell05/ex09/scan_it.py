#!/usr/bin/env python3
import sys
import re

if len(sys.argv) == 3:
    keyword,text = sys.argv[1], sys.argv[2]
    
    count = len(re.findall(keyword, text))
    print(count)
else:
    print("none")

""" คำสั่งโจทย์
?> ./scan_it.py | cat -e
none$
?> ./scan_it.py "the" | cat -e
none$
?> ./scan_it.py "the" "the quick brown fox jumps over the lazy dog" | cat -e
2$
?>
"""