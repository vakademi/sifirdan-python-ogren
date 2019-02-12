# Kendini Sına - Çözüm !
"""
Vize %30
Final %70

85-100 -> A
70-84  -> B
55-69  -> C
45-54  -> D
25-44  -> E
0-24   -> F

Sonucu hem puan, hem de harf olarak veriniz.
"""

vize = int(input("Vize Sonucunu Giriniz: "))
final = int(input("Final Sonucunu Giriniz: "))

sonuc = (vize * .30) + (final * .70)

if sonuc >= 85:
    harf = "A"
elif sonuc >= 70:
    harf = "B"
elif sonuc >= 55:
    harf = "C"
elif sonuc >= 45:
    harf = "D"
elif sonuc >= 25:
    harf = "E"
else:
    harf = "F"

print("Sonuç: ", sonuc, "Harf Değeri", harf)
