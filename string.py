name = "Pınar"
surname= "Güzel"
age= "16"

name2="irem"

surname2= "Güzel"
age2= "18"

print("My name is sister "+name2+" " +surname2 + "  and \nShe is "+ age2+" years old." )

# age int türünden bir deger taşımasına rağmen str olarak gösterdik ancak int türünden deger taşımasını istersek print içerisini 
# print("My name is sister "+name2+" " +surname2 + "  and she is "+ str (age2)+" years old." )
#str (age2) şeklinde değiştirmemiz gerekir. bu şekilde yaparsak age tanımlı oldugu degeri "tırnak " ile yazmamıza gerek kalmaz.

# \n= cümleyi bir alt satıra taşır.

# yazdırmak istediğimiz degeri bir fonksiyona aktarırsak print içinde bu fonksiyonu yazdıgımızda print içindeki degerin eşitliğini ekrana girecektir. 


gretting ="My name is little sister "+name+" " +surname + " and she is "+ age+" years old."
print(gretting )

# egr dizi olarak tanımlarsak
# print(gretting[0]) yazdıgımızda ekrana "M" degeri gözükecektir.
# eger dizi olarak tanımlamak istersek bu şekilde yapmamız yeterlidir.
# peki burda gretting isimli fonksiyonun kaç karakterli oldugunu ögrenmek isteseydik ne yapmamız gerekirdi?
# o zamanda print(len(gretting)) yazarsak bu fonksiyonda kaç karakter oldugunu söyleyecektir.

print(gretting[0])
print(len(gretting))

# son karakteri ekranda görmek istediğimizde 

lenght =len(gretting)

print(gretting[ lenght-1]) # lenght -1 olarak tanımlamamız gerekir. çünkü dizi degerleri 0 dan başlamaktadır. veya;

print(gretting[-1])   # şeklindene bulabiliriz. bu şekilde ekranda "." görünür.

print( gretting [2:5])  # bu şekilde gretting ifadesinin 2. indeksinden başla 5. indeksinde dur 2 ve 5 arasındaki degerleri ekranda gözükür.


print( gretting[3:])     # burada dizinin 3. indeksinden son karaktere kadar gösterilir.

print(gretting [:18])    # baştan 18. karaktere kadar yazar ve 18. karaterde keser.

print (gretting [2:40:4])  # 2.karakterden başla ve 40 kadar gir ancak her 4 karakterde bir alma


