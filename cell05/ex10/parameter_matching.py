#!/usr/bin/env python3
import sys

if len(sys.argv) == 2:
    word = sys.argv[1]
    user_input = input(f"What was the parameter? ")
    if user_input == word:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")

    
"""?> ./parameter_matching.py
none
?> ./parameter_matching.py "Hello"
What was the parameter? Bonjour
Nope, sorry...
?> ./parameter_matching.py "Hello"
What was the parameter? Hello
Good job!
?>"""