bagaj=int(input("Lütfen Valiz (Kg) Bilginizi Giriniz:"))

if bagaj <=20:
    print("Ek Bir Ücret Alma")
else:

    ek_ucret= (bagaj - 20 ) *10
    print("Fazla Bagaj Hakkı İçin", ek_ucret ,"TL Ödemelisiniz.")
    