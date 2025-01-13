i = "0"
Hesapisim = "x"
Hesaplar = {}
Hesaplar["placeholder"]=0
###########################################################
def HesapKontrol(n):
    for x in Hesaplar:
        if n == x:
            return True
    Hesaplar[n]=0
    return False
#########################################
def HesapKontrol2(n):
    for x in Hesaplar:
        if n == x:
            print("")
            return True
    print("")
    print("Hesap Bulunamadı.")
    print("")
    Menu()
###########################################################
def ParaUygunluk(para2):
    if para2 < 0:
        print("")
        print("Para Miktarı Olarak Negatif Girilemez.")
        print("")
        return False
    elif para2 == 0:
        print("")
        print("Para Miktarını 0 Dışında Bir Sayı Giriniz.")
        print("")
        return False
    elif para2 > 0:
        print("")
        print("İşlemizi Başarıyla Gerçekleştirilmiştir.")
        print("")
        return True
    else:
        print("")
        print("Para Miktarı Olarak Sayı Girmeniz Gerekmektedir.")
        print("")
        return False
##########################################################
def BakiyeSorgulayıcı(m):
    for x in Hesaplar:
        if m == x:
            return False
    return True        
##########################################################
def Paraİşlemeri(isim2,para):
    Hesaplar[isim2] += para
#########################################################
def Parayükle():
    boo3 = False
    print("")
    print("Para Yüklemek İstediğiniz Hesabın İsmini Girin.")
    print("")
    isim = input()
    HesapKontrol2(isim)
    print("Yüklemek İstediğiniz Miktarı Girin.")
    print("")
    para = float(input())
    boo3 = ParaUygunluk(para)
    if boo3 == True:
        Paraİşlemeri(isim,para)
        Menu()
    else:
        Menu()
###########################################################
def Paraçek():
    print("")
    print("Para Çekmek İstediğiniz Hesabın İsmini Girin.")
    print("")
    isim = input()
    HesapKontrol2(isim)
    print("Çekmek İstediğiniz Miktarı Girin.")
    print("")
    para = float(input())
    if para>(Hesaplar[isim]):
        print("")
        print("Hesabınızda Yeterli Bakiye Yoktur")
        print("")
        Menu()
    boo3 = ParaUygunluk(para)
    if boo3 == True:
        para *= -1
        Paraİşlemeri(isim,para)
        Menu()
    else:
        Menu()
##########################################################
def Hesap():
    Boo = True
    print("")
    print("Hesap ismini giriniz.")
    print("")
    Hesapisim=input()
    Boo = HesapKontrol(Hesapisim)
    if Boo == True:
        print("")
        print("Bu Hesap Zaten Mevcut")
        print("")
        Menu()
    else:
        print("")
        print("Hesabınız Başarıyla Oluşturulmuştur")
        print("")
        Menu()
########################################################
def Bakiye():
    Boo2 = True
    print("")
    print("Bakiyesini Sorgulamak İstediğiniz Hesabın İsmini Giriniz.")
    print("")
    Hesapisim = input()
    Boo2 = BakiyeSorgulayıcı(Hesapisim)
    if Boo2 == True:
        print("")
        print("Hesap Mevcut Değil")
        print("")
        Menu()
    else:
        print("")
        print("Bakiyeniz:",Hesaplar[Hesapisim])
        print("")
    Menu()
######################################################
def Menu():
    print("------Banka------")
    print("1.Hesap Oluştur")
    print("2.Bakiye Sorgula")
    print("3.Para yükle")
    print("4.Para Çek")
    print("Lütfen 1-4 arasında bir sayı giriniz.")
    print("")
    i = input()
    if i == "1":
        Hesap()
    elif i == "2":
        Bakiye()
    elif i == "3":
        Parayükle()
    elif i == "4":
        Paraçek()
    else:
        print("")
        print("Geçerli Bir Sayı Giriniz.")
        print("")
        Menu()

##########################################################
Menu()