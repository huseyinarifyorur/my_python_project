n1=int(input("İlk Sayiyi Giriniz:"))
n2=int(input("İkinci Sayiyi Giriniz:"))

total=1

for i in  range(1,n1 + n2):
  total += i
divide = total /i
print(divide)