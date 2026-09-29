import math
def convert_temperature(value, unit):
    if unit == 'C':
        return (value * 9/5) + 32
    elif unit == 'F':
        return (value - 32) * 5/9
    else:
        return "Unit tidak valid"

print("=== KONVERSI SUHU ===")

print("25°C =", convert_temperature(25, 'C'), "°F")
print("77°F =", convert_temperature(77, 'F'), "°C")

circle_area = lambda r: math.pi * r**2

print("\n=== LUAS LINGKARAN ===")

jari_jari = 7
print("Jari-jari =", jari_jari)
print("Luas lingkaran =", circle_area(jari_jari))