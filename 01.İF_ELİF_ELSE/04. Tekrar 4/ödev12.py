boy1=float(input("Boyunuzu giriniz:\n"))
boy2=float(input("Boyunuzu giriniz:\n"))
kilo=float(input("Kilonuzu giriniz:\n"))

vki=(float(boy1)*float(boy2)/float(kilo))


if vki <=18==25:
    print("Normal")
elif vki<=30:
    print("Kilolu")
elif vki<=35:
    print("Obez")
elif vki>35:
    print("Ciddi Obez")