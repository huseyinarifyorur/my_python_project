Number1=int(input("1.Sayiyi Giriniz: \n"))
Number2=int(input("2.Sayiyi Giriniz: \n"))
Number3=int(input("3.Sayiyi Giriniz: \n"))

Total=float(Number1)+float(Number2)+float(Number3)
if Total ==180:
    print("{0} Bu Bir Üçgendir".format(Total))
elif Total <180:
    print("{0} Bu Bir Üçgen Değildir".format(Total))
elif Total >180:
    print("{0} Bu Bir Üçgen Değildir".format(Total))
