İsim=(input("Lütfen İsminizi Giriniz:"))
print("Merhabalar {0} Ortalama Hesaplamaya Hoşgeldiniz".format(İsim))


Not1=int(input("İlk Sınav Notunuzu Giriniz:"))
Not2=int(input("İkinci Sınav Notunuzu Giriniz:"))
performans_notu=float(Not1) + float(Not2)
X=2
Divide=float(performans_notu)/float(X)

if Divide <=50:
    print("Maalesef  Başarısız Oldunuz!")
if Divide >=50:
    print("Tebrikler Başardınız!")