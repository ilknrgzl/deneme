f=open("users.txt","r")

d={}
for i in f:
    a=i.split(".")
    print(a)
    isim=[0]
    sifre=[1]
    sifre:sifre.replace("\n","")
    d[isim]=sifre

count=0
while (count<3):
 loginAd=input("İsminizi giriniz: ")
 loginSıfre=input("Şifrenizi giriniz: ")
if (loginAd in d.keys()) and (d[loginAd == loginSıfre]):
    print("Giriş Başarılı l")
else:
    print("Giriş başarısız l")