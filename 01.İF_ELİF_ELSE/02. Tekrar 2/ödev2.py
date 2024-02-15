Açı1=int(input("1.Açıyı Giriniz:"))
Açı2=int(input("2.Açıyı Giriniz:"))
Açı3=int(input("3.Açıyı Giriniz:"))

total=float(Açı1) + float(Açı2) + float(Açı3)
if total==180:
    print("{0} Bu Bir Üçgendir.".format(total))
if total <180:
    print("{0} Bu Bir Üçgen Değildir.".format(total))
if total >180:
    print("{0} Bu Bir Üçgen Değildir.".format(total))
    