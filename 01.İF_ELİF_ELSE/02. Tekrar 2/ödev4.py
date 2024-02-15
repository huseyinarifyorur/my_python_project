ürün1=int(input("İlk Ürün Fıyatını Giriniz:"))
ürün2=int(input("İkinci Ürün Fiyatını Giriniz:"))

total= float(ürün1) + float(ürün2)
 
if total <=200:
  print("Ödenecek Tutar",total)
 
elif total >=200:
  print("İndirimli Tutar", total/3)

