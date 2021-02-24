websitesi ="http://www.ilknurgüzel.com"
course ="Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

#1- 'course ' karakter dizisinde kaç karakter bulunmaktadır?

result =len(course)
length= len(websitesi)
#2- 'website' içerisinden www karakterlerini alın 
result = websitesi[7:10]

#3- 'website' içerisinden com karakterini alın

result= websitesi[22:25]
result=websitesi [length-3:length]
#4- 'course' içerisinde ilk 15 ve son 15 karakterini alın
result = course[0:15]
result= course[:15]
result=course[-15:]

#5-'course' ifadesindeki karakterleri tersten yazdırın

result= course[::-1]

s= '12345' *5
print(s[::5])

# yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdıralım.
#'Benim adım İrem Güzel, Yaşım 18 ve mesleğim ögrenci.'
name, surname, age, job= 'irem', 'güzel', 18, 'öğrenci'
result= "beni adım "+ name+ " "+ surname+", Yaşım "+ str(age )+ " ve mesleğim "+job
result='Benim adım {0} {1}, Yaşım {2} ve mesleğim {3}.'.format(name,surname,age,job)


print(result)