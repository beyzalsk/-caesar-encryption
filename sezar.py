def sifreleme(a,key): #Şifreleme yapıyoruz
    s=''
    for i in kelime: #Kullıcıdan aldığımız string ifadenin harflerini tek tek dönüyor
        if i in k:
            index1=k.index(i)+key
            if(index1>=len(k)): #Kelimenin harflerinden küçük olanları alıyoruz ve sayısı küçük harflerden fazla ise
                index1-=len(k) #Harflerin eksiğini alıyoruz
            s=s+k[index1]
        elif i in b: #Kelimenin harflerinden büyük olanları alıyoruz ve ve sayısı büyük harflerden fazla ise
            index1=u.index(i)+key #Harflerin eksiğini alıyoruz
            if(index1>=len(b)):
                index1-=len(b)
            s=s+b[index1]
    return(s) #Küçük ve büyük harflerin hepsini e değişkenine attık ve e değişkenini döndürüyoruz

def sifrecozme(a,key): #Şifre çözümlemesi yapıyoruz
    c=''
    for i in kelime: #Kullanıcıdan aldığımız string ifadenin harflerini tek tek dönüyor
        if i in k: # Harflerin içinde büyük olanlarda işlem yapıyoruz
            index1=k.index(i)-key #Her harften keyi çıkararak geri geliyoruz
            c=c+k[index1]
        elif i in b:
            index1=b.index(i)-key
            c=c+b[index1]
    return(c) #Küçük ve büyük harflerin hepsini d değişkenine attık ve e değişkenini döndürüyoruz
while(True):
 se=int(input(" 1 Şifreleme - 2 Şifre Çözme :   ")) #Kullanıcadan yapmak istediği işlem için girdi alıyoruz. 1 ise şifreleme 2 ise şifre çözme
 k=list(chr(a) for a in range(ord('a'),ord('a')+26)) #Küçük harflerin listesi
 b=list(chr(a) for a in range(ord('A'),ord('A')+26)) #Büyük harflerin listesi
 key=2 #keyi kendi otomatik atıyoruz
 if se==1:
    kelime=input("Şifrelenmesini İstediğiniz Kelimeyi Yazınız:  ") # Kullanıcan şifreleme işlemi için girdi olarak string bir ifade istiyoruz
    s=sifreleme(kelime,key) # Şifreleme fonksiyonunu çağırıyoruz ve buna parametre olarak kullanıcıdan aldığımız string ifade ile key değerini veriyoruz.
    print("Şifrelenmiş Kelime: ",s) #Bi üst satırda yaptığımız işlemi e değişkenine atadık ve bunu yazdırdık.
    break;
 elif se==2:
    kelime=input("Çözümlemek İstediğiniz Kelimeyi Yazınız ")
    c=sifrecozme(kelime,key)
    print("Çözümlenmiş Kelime: ",c)
    break;
 else:
    print("Lütfen geçerli bir giriş yapınız")
    continue


