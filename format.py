name = "Pınar"
surname= "Güzel"
age= "16"

# print(' My name is {} {}' .format(name,surname))
# print(' My name is {1} {0}' .format(name,surname))  # indekslerde verilen degerlere göre çıktı verir. yani önce güzel sonra pınar yazılır.
# print(' My name is {s} {n}' .format( n=name, s=surname)) #değişkenlere verilen isimleri parantez içine yazdıgımızda yukardaki işlem tekrarlanır.
# print(" My name is {} {}  She's {} years old. ".format( name, surname, "16")) # veya 16 yerine age yazılabilir.

# print(" My name is {} {}  She's {} years old. ".format( name, name, name))  # bu şekilde her parantes içine name bilgisi aktarılır.

result= 200/700 
# print( " the result is {}".format( result)) # float degerini str degerine çevirmemize bu .format ile gerek kalmadı.

# print( " the result is {r:1.3}".format( r=result)) # bu şekilde ondalık sayının belli bir kısmını aldık. 1 sayısı tamsayıdan önceki boşlugu 3 sayısı ondalıklı kısımı gösteriyor ve bu işlem ile ondalıklı sayısı en yakın sayıya yuvarlama işlemi yaptık.

print( f" My name is {name} {surname}  She's {age} years old. ") # başına f ekledigimizde parantezlerin içine eklemek istediklerimizi yazabiliriz.