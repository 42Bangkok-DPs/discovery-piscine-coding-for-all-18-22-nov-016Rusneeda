#!/usr/bin/env python3
multiplier = 0
while multiplier <= 10:
    print(f"Table de {multiplier}:", end=" ")
    multiplicand = 0
    while multiplicand <= 10:
      product = multiplier * multiplicand
      print(f"{product:3}", end="")
      multiplicand += 1
    print()
    multiplier += 1