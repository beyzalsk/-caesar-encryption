
keylistesi = ["A","B","C","D","E","F","G","H","I","J",\
    "K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] #Şifrelemek için kullanacağımız harfler

# Bu fonksiyonuz kullanıcıdan şifrelenmesini istediği kelimeyi alıyoruz
def sifregiris():
    sifre = input("\n\n\n Şifrelenmesini istediğiniz Kelimeyi Giriniz\n Kelime: ")
    for i in sifre:
        if i.upper() not in (keylistesi or " "):

            return -1
        else:
            return sifre

# Bu fonksiyonumuzda kullanıcıdan bir key (öteleme miktarı) istiyoruz
# Keyimizi de 1-30 arasında seçilecek şekilde ayarlıyoruz
def keygiris():

    key = input("\nLütfen 1-30 arası bir sayı giriniz \nKey: ")
    if key.lower() == 'GERİ':
        return -2
    elif int(key) not in range(0,31):
        print("\nLütfen sayı giriniz geri dönmek istiyorsanız geri yazabilirsiniz")
        return -1
    else:
        return int(key)

# Bu fonksiyonda alınan kelimeyi bir diziye atar
def sifreIndex(sifregiris):

    sifre = sifregiris # Alınan kelimeyi şifrelenmiş olan kelimeye atar
    sifrelenmis = [] # Şifrelemiş kelimenin her bir harfinin tutulduğu dizidir.


    for alfabe in sifre:

        if alfabe != " ": #Kelimede boşluk olup olmadığını kontrol ediyoruz
            for keyalfabe in range(0,len(keylistesi )): #Bu alfabadeki harflerin ilk başta yazdığımız keylisetesindeki harflere eşit olup omadığını kontrol ediyoruz.

# eşit ise diziye eklenir eşit değilse eşit olana kadar yenilemeye devam eder.
                if alfabe.upper() == keylistesi [keyalfabe]:
                    sifrelenmis.append(keyalfabe)
        elif alfabe == " ": #Boşluk var ise alfabaye boşluk olarak eklenir
            sifrelenmis.append(" ")
        else:
            return None
    return  sifrelenmis

# Bu fonksiyonda şifrelemeyi yapıyoruz
def cöz( sifrelenmis, key):

    cöz= [] #Şifrenlenmiş kelimeyi bu diziye ekler

    for sfr in  sifrelenmis:

        if sfr !=" ": #Dizide boşuk var mı yok mu kontrol ediliyor

            if (sfr -key) < 0:
                sfr  = 26+(sfr -key)
                cöz.append(sfr )
            elif (sfr -key) >= 0: # Key 0dan büyükse kelime şifrenlenmesi iç,n kullanılır
                sfr -=key
                cöz.append(sfr )

        elif sfr  == " ":
            cöz.append(" ")
        else:
            return None
    return cöz


def islem(cöz):
    kelime = ""
    for sfr  in cöz:
        if sfr != " ": #Şifrelenmiş kelime kontrol sonrası alfabeye eklenir
            alfabe = keylistesi [sfr ]
            kelime+=alfabe
        elif sfr  == " ": #boşluk kontrolü
            kelime+= sfr #boşluk diziye eklenir
    return kelime

# Bu fonskiyonda büyük küçük harfe bakıyoru
# Büyük küçük harf olarak doğru şifrelenmiş kelimeyi bu diziye ekliyoruz
def kontrol(cözülmüskelime, kodlanacakkelime):

    kelime=""
    for sfr in range(0,len(cözülmüskelime)):
        if kodlanacakkelime[sfr ]==kodlanacakkelime[sfr ].lower(): # eğerki harfler büyük ise küçük harfe döndürülüp diziye kelenir
            kelime+=cözülmüskelime[sfr ].lower()

        else:
            kelime+=cözülmüskelime[sfr ]
    return kelime


def menü():
    try:
        while True:

            kullanici= int(input("1) Şifreleme \n2) Çıkış \n Seçim Yapınız: ")) #Kullanıcıdan İşlem Yapması için Girdi İstiyoruz
            if kullanici in (1,2):
                return kullanici
            else:
                print("Invalid Input")
    except:
        print("Invalid input")

def control():
    input("ANA MENÜYE DÖN")
    return

# Main Method
def main():
    while True:
        kullanici = menü()
        if kullanici == 1: #Kullanici 1i seçtiyse sifregirise yönlendiriyor sizden bir kelime
            kontrol1 = sifregiris()
            if kontrol1 == -1:
                control()
                continue
            while True:
                kontrol2 = keygiris()  #İkinci olarak key istiyor ve keygiris
                if kontrol2== -1:
                    continue
                elif kontrol2== -2:
                    break
                else:
                    sfIndex = sifreIndex(kontrol1)
                    keIndex = cöz(sfIndex, kontrol2)
                    stringi = islem(keIndex)
                    final = kontrol(stringi, kontrol1)
                    print("\nŞifrelenmiş Kelime {}".format(final))
                    control()
                    break


        if kullanici == 2:

            break


if __name__ == "__main__":
    main()

