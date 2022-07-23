# Вычислить число pi c заданной точностью d Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

d = 0.001
roundPi = round(math.pi, int(-math.log10(d)))
print(f"{d = }, π = {roundPi}")
