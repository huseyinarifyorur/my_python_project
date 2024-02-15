while True:
    sayi = int(input("1 ile 5 arasında bir sayı girin: "))

    if sayi >= 1 and sayi <= 5:
        if sayi == 3:
            print("3 sayısı girildi ve döngü sona erdi.")
            break
        else:
            print(f"Girilen sayı: {sayi}")
    else:
        print("Geçersiz sayı. Lütfen 1 ile 5 arasında bir sayı girin.")
