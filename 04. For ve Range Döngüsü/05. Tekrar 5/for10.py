ifade = input("Bir ifade girin: ")
aranacak_harf = input("Aranacak harfi girin: ")

sayac = 0

for harf in ifade:
    if harf == aranacak_harf:
        sayac += 1
print(f"'{aranacak_harf}' harfi ifadede {sayac} kez bulunuyor.")
