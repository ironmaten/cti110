 # Jonathan Maten
 # 30 September 2024
 # P2LAB1
 # This program processes certain formulas for circles

import math
print('What is the radius of the circle?', end = " ")

radius = float(input())
print('')

diameter = radius * 2
circumference = 2 * math.pi * radius
area = math.pi * radius * radius

print('The diameter of the circle is', f'{diameter:.1f}')
print('')
print('The circumference of the circle is', f'{circumference:.2f}')
print('')
print('The area of the circle is', f'{area:.3f}')