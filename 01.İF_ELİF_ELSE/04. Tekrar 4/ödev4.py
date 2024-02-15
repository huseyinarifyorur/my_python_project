ürün1=int(input("Birinci ürünün fiyatını giriniz:\n"))
ürün2=int(input("İkinci ürünün fiyatını giriniz:\n"))
 
toplam_fiyat=(int(ürün1)+int(ürün2))

if toplam_fiyat<=200:
 print("Ödemeniz gereken tutar",toplam_fiyat)

elif toplam_fiyat>=200:
  print("İndirimden sonra ödenecek tutar",toplam_fiyat/3)
 

