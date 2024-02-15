# Kullanıcıdan iki sınav bilgisi ve bir performans notu alın.
Name=input("İsminizi Girin: ")
print("Merhabalar {0} Ortalama Hesaplamaya Hoşgeldiniz".format(Name))
number1 =input("1.Sayiyi Girin: ")
number2 =input("2.Sayiyi Girin: ")
performansnotu =float(number1)+float(number2)
A=2
Divide=float(performansnotu)/float(A)

if  Divide <=50:
    print ("malesef başarisiz oldunuz")

elif Divide >=50:
    print("Tebrikler başardiniz")
    
    