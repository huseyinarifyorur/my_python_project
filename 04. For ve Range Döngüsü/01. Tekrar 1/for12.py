while("True...") :
 New_Password = input("\nŞifrenizi giriniz: ")
 print("--"*20)
 New_Password_Again = input("Şifrenizi tekrar giriniz: ")


 if len(New_Password) == 8 or len(New_Password_Again) == 8 :
        if New_Password == New_Password_Again :
            print("Şifrenizi oluşturuldu ")
            break
 else : 
      print("Bir hata oldu lütfen tekrar deneyiniz")