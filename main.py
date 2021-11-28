
global number
import threading
from tkinter import *



root = Tk()
root.title("Converter")
large_font = ('Verdana',15)

#Pencere ilk açıldığında karş
frame1Text = "8"
frame2Text = "10"
frame3Text = "16"

#Aşağıdaki değişkenler sayı sistemleri için geçerli sayılar
hexDictionary = { 10: "A", 11:"B", 12:"C", 13:"D", 14:"E", 15:'F', 'A': 10, 'B':11
                  , 'C':12, 'D':13, 'E':14, 'F':15}
binaryNumbers = ["0", "1", ""]
octalNumbers = ["0","1","2","3","4","5","6","7", ""]
hexNumbers = ["0", "1", "2","3","4","5","6", "7", "8", "9", "A" ,"B","C","D","E","F", ""]

#Çevirilecek sayının doğru değerlerde girildiğini kontrol eden fonksiyon
def control():
    while True:
        #Hangi tabandan çevirileceğini alıyoruz
        system = clicked.get()

        #Anlık olarak girilen sayıyı alıyoruz ve basamaklara bölüyoruz
        numbers = list(str(inputSelected.get()))

        #Sistem ikilikse
        if system == "Binary":
            #Girilen sayının basamaklarını tek tek alıyoruz
            for i in numbers:

                #Eğer girilen sayı mevcut taban için uygun olan sayılarla eşleşmiyorsa arkaplanı kırmızı yapıyoruz.
                if i not in binaryNumbers:
                    inputSelected.configure(bg="red")

                #Değerler normalse arkaplanı beyaz yapıyoruz.
                else:
                    inputSelected.configure(bg="white")

        #Yukarıdaki işlemleri diğer tabanlar için kontrol ediyoruz
        elif system == "Octal":
            for i in numbers:
                if i not in octalNumbers:
                    inputSelected.configure(bg="red")
                else:
                    inputSelected.configure(bg="white")
        elif system == "Hex":
            for i in numbers:
                if i not in hexNumbers:
                    inputSelected.configure(bg="red")
                else:
                    inputSelected.configure(bg="white")
        elif system =="Decimal":
            for i in numbers:
                if not i.isnumeric():
                    inputSelected.configure(bg="red")
                else:
                    inputSelected.configure(bg="white")



# onluk tabandan ikilik tabana çevirme fonksiyonu
def decimalToBinary(number):

    result = ""
    number = int(number)
    # Sayı 1 olana kadar bölüyoruz
    while (number >= 1):

        #Sonuçta kullanmak için mevcut sayıdan kalanı kaydediyoruz
        remainder = number % 2

        #Kalanı aldıktan sonra sayıyı 2 ye bölüyoruz
        number = number // 2

        #Kalan olarak aldığımız sayıyı uç uca ekliyoruz
        result = str(remainder) + result

    #Sonucu geri dönderiyoruz
    return result


#onluk tabandan sekizlik tabana çevirme fonksiyonu
#decimalToBinary fonksiyonu için yapılanlar tekrar ediliyor
def decimalToOctal(number):
    result = ""
    number = int(number)
    while (number >= 1):
        remainder = number % 8
        number = number // 8
        result = str(remainder) + result
    return result


#onluk tabandan onaltılık tabana çevirme fonksiyonu
#decimalToBinary fonksiyonu için yapılanlar tekrar ediliyor
def decimalToHex(number):
    result = " "
    number = int(number)
    while ((number) >= 1):
        remainder = number % 16
        number = number // 16
        if remainder > 9:
            remainder = hexDictionary[remainder]
        result = str(remainder) + result
    return result

#ikilik tabandan onluk tabana çevirme fonksiyonu
def binaryToDecimal(number):
    #Girilen sayıyı basamak basamak liste olarak kaydediyoruz
    number = list(str(number))

    #Başlangıç sonucu 0
    result = 0

    #İlk basamak değeri x üzeri 0 olduğu için kuvveti (basamak sayısı -1) olarak başlatıyoruz
    pows = len(number) - 1

    #Tüm basamakları tek tek dolaşıyoruz
    for i in number:
        i = int(i)

        #Sonucu basamak değeri * ve ikinin kuvvetlerini çarparak buluyoruz, her basamak değerlerini topluyoruz
        result += i * (pow(2, pows))

        #Bir sonraki basamak için kuvveti bir azaltıyoruz
        pows -= 1

    #Sonucu geri dönderiyoruz
    return result



#ikilik tabanı sekizlik tabana çevirme fonksiyonu
def binaryToOctal(number):
    #ikilik tabanı öncelikte onluk tabana çeviriyoruz
    number = binaryToDecimal(number)

    #Onluk tabana çevirdiğimiz sayıyı sekizlik tabana çeviriyoruz
    number = decimalToOctal(number)

    #Sonucu geri dönderiyoruz
    return number


#ikilik tabanı onaltılık tabana çevirme fonksiyonu
#Yukarıda bulunan fonksiyondaki adımları tekrar ediyoruz
def binaryToHex(number):
    number = binaryToDecimal(number)
    number = decimalToHex(number)
    return number


#sekizlik tabanı ikilik tabana çevirme fonksiyonu
def octalToBinary(number):
    #sekizlik tabanı öncelikle onluk tabana çeviriyoruz.
    number = octalToDecimal(number)

    #çevirdiğimiz onluk sayıyı ikilik tabana çeviriyoruz
    number = decimalToBinary(number)

    #sonucu geri dönderiyoruz
    return number

#Sekizlik tabandan onluk tabana çevirme fonksiyonu
def octalToDecimal(number):
    number = list(str(number))
    result = 0
    pows = len(number) - 1
    for i in number:
        i = int(i)
        result += i * (pow(8, pows))
        pows -= 1
    return result

def octalToHex(number):
    number = octalToDecimal(number)
    number = decimalToHex(number)
    return number

def hexToBinary(number):
    number = hexToDecimal(number)
    number = decimalToBinary(number)
    return number

def hexToOctal(number):
    number = hexToDecimal(number)
    number = decimalToOctal(number)
    return number

#onaltılık tabanı onluk tabana çevirme fonksiyonu
def hexToDecimal(number):
    number = list(number)
    result = 0
    pows = len(number) - 1
    for i in number:

        #Eğer gelen değer sayı değilse sözlükten o harfin karşılığını buluyoruz
        if not i.isnumeric():
            i = hexDictionary[i]
        result += int(i) * (pow(16, pows))
        pows -= 1
    return result






##Aşağıdaki toAll fonksiyonları ikilik sistemleri kutulara gönderen fonksiyonları içeriyor
def binaryToAll(number):

    inputFrame1.insert(0, binaryToOctal(number))
    inputFrame2.insert(0, binaryToDecimal(number))
    inputFrame3.insert(0, binaryToHex(number))

def octalToAll(number):
    inputFrame1.insert(0, octalToBinary(number))
    inputFrame2.insert(0, octalToDecimal(number))
    inputFrame3.insert(0, octalToHex(number))

def decimalToAll(number):
    inputFrame1.insert(0, decimalToBinary(number))
    inputFrame2.insert(0, decimalToOctal(number))
    inputFrame3.insert(0, decimalToHex(number))

def hexToAll(number):
    inputFrame1.insert(0, hexToBinary(number))
    inputFrame2.insert(0, hexToOctal(number))
    inputFrame3.insert(0, hexToDecimal(number))


#Çevirilecek tabana göre sonuç kutularını düzenleyen fonksiyonlar
def configureText(system):
    if system == "Binary":
        #ikilik tabandan çevirme yapacağımız için sonuçlar 8,10,16 tabanlarından sonuç alacağız
        frame1.configure(text=8)
        frame2.configure(text=10)
        frame3.configure(text=16)
    elif system == "Octal":
        frame1.configure(text=2)
        frame2.configure(text=10)
        frame3.configure(text=16)
    elif system == "Decimal":
        frame1.configure(text=2)
        frame2.configure(text=8)
        frame3.configure(text=16)
    else:
        frame1.configure(text=2)
        frame2.configure(text=8)
        frame3.configure(text=10)

##Anlık olarak girilen değeri döndüren fonksiyon
def getNumber():
    return  inputSelected.get()

#Calculate butonu için kullanılan fonksiyon
def calculate():

    #Açılır menüden seçilen tabanı alıyoruz
    system = clicked.get()

    #Tabana göre sonuç kutularını değiştiriyoruz
    configureText(system)

    #Tüm kutuları temizliyoruz
    delete()

    #Girilen sayıyı alıyoruz
    number = getNumber()

    if system == "Binary":
        binaryToAll(number)
    elif system == "Octal":
        octalToAll(number)
    elif system == "Decimal":
        decimalToAll(number)
    else:
        #onaltılık taban harf içerebileceği için string olarak yolluyoruz
        hexToAll(str(number))


#Tüm kutuları temizleyen fonksiyon
def delete():
    inputFrame1.delete(0, END)
    inputFrame2.delete(0, END)
    inputFrame3.delete(0, END)



#Ana kutumuz
mainFrame = LabelFrame(root, text = "Number Calculator", padx = 10, pady= 10)
mainFrame.pack(padx=10, pady=10)

#Sayı sistemlerinden birini seçip değer gireceğimiz kutu
selectFrame = LabelFrame(mainFrame, text = "Select From", width = 670, height = 70 )
selectFrame.pack()

#selectFrame kutusunun üst kısmındaki öğeleri koyacağımız kutu
topFrame = LabelFrame(selectFrame)
topFrame.pack(padx = 10, pady = 10)

#Açılır menümüzün kodları
clicked = StringVar()
#Default olarak İkilik sistemde başlatıyoruz
clicked.set("Binary")
drop = OptionMenu(topFrame, clicked, "Binary", "Octal", "Decimal", "Hex")
drop.pack(side = LEFT)

#Değer alacağımız kutu
inputFrame = LabelFrame(topFrame, width = 565, height = 70 )
inputFrame.pack(side = RIGHT, padx = 10)
inputSelected = Entry(inputFrame, width = 39, bg = "white", fg = "black",font=large_font )
inputSelected.pack(padx= 20, pady = 20)

#selectFrame kutusnun alt kısmı, sadece Calculate butonunu ekleyeceğiz
botFrame = LabelFrame(selectFrame)
botFrame.pack(padx = 10 , pady = 10)



#Butonu sağa kaydırmak için boş bir label

emptyItem = Button(botFrame, text = "Clear", command = delete, width = 35, height = 1 )
emptyItem.pack(side = LEFT, padx=5)


#Calculate butonumuz
buttonCalculate = Button(botFrame, text = "Calculate", command = calculate, width = 35, height = 1 )
buttonCalculate.pack(side = RIGHT, padx = 5)


#1. Kutu
frame1 = LabelFrame(mainFrame, text =frame1Text, width = 850, height = 70)
frame1.pack(padx = 10, pady = 10)
inputFrame1 = Entry(frame1, width = 50, bg ="white", fg ="black", font=large_font)
inputFrame1.grid(padx= 10, pady = 20)


#2. kutu
frame2 = LabelFrame(mainFrame, text =frame2Text, width = 850, height = 70)
frame2.pack(padx = 10, pady = 10)
inputFrame2 = Entry(frame2, width = 50, bg ="white", fg ="black", font=large_font)
inputFrame2.grid(padx= 10, pady = 20)

#3. kutu
frame3 = LabelFrame(mainFrame, text =frame3Text, width = 850, height = 70)
frame3.pack(padx = 10, pady = 10)
inputFrame3 = Entry(frame3, width = 50, bg ="white", fg ="black", font=large_font)
inputFrame3.grid(padx= 10, pady = 20)

#veri girişi yaptığımız sürekli olarak kontrol ediyoruz
t1 = threading.Thread(target=control)
t1.start()

root.mainloop()

