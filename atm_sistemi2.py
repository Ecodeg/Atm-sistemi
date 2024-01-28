bakiye=0

while True:
    ad=input("Adınızı giriniz: ")
    if ad=="":
        print("Boş bırakamazsınız!")
    else:
        break
    
while True:
    hesap_no=input("Hesap numaranızı yazınız: ")
    if hesap_no=="":
        print("Boş bırakamazsınız!")
    else:
        break

print(f"Sayın {ad} sisteme hoşgeldiniz.")

def para_yatır():
    global bakiye
    miktar=float(input("Para yatırmak istediğiniz miktarı yazınız: "))
    bakiye+=miktar
    print(f"Sayın {ad} hesabınıza {miktar} TL para yatırıldı yeni bakiyeniz: {bakiye}")


def para_cek():
    global bakiye
    miktar=float(input("Hesaptan çekmek istediğiniz miktarı yazınız: "))
    if bakiye>=miktar:
        bakiye-=miktar
        print(f"Sayın {ad} hesabınızdan {miktar} TL para çekildi yeni bakiyeniz: {bakiye}")
    else:
        print("Hesabınızda yeterli bakiye yoktur!")


def bakiye_sorgula():
    global bakiye
    print(f"Sayın {ad} hesabınızdaki güncel para: {bakiye} TL")


while True:
    print("1. Para Yatır")
    print("2. Para çek")
    print("3. Bakiye Sorgula")
    print("0. Çıkış")
    tercih=int(input("Lütfen yapmak istediğiniz işlemi seçiniz (0-3): "))

    if tercih==1:
        para_yatır()
    elif tercih==2:
        para_cek()
    elif tercih==3:
        bakiye_sorgula()
    elif tercih==0:
        print("Programdan çıkılıyor...")
        break
    else:
        print("Lütfen belirtilen aralıkta tercih yapınız!")




