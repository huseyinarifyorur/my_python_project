üçgen1=float(input("Birinci değeri giriniz:\n"))
üçgen2=float(input("İkinci değeri giriniz:\n"))
üçgen3=float(input("Üçüncü değeri giriniz:\n"))


if üçgen1 == üçgen2 == üçgen3:
    print("Eşkenar üçgendir")
if üçgen1 == üçgen2:
    print("İkizkenar üçgendir")
else:
    print("Çeşitkenar üçgendir")