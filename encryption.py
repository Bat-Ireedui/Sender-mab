import cv2
import string
import os


# Хэрэгтэй хувьсагч нараа зарлах
dict1 = {}
dict2 = {}
for i in range(255):
    dict1[chr(i)]=i
    dict2[i]=chr(i)
#Эхний dict1 нь ASCII объектуудыг тус тусын
#id-ийн хамт түлхүүр болгон хадгалах бол
#dict1 нь ижил төстэй ажлыг гүйцэтгэдэг боловч эсрэгээрээ функцтэй.
img = cv2.imread("test_image.jpeg") #Зургаа уншиж авах
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
print(f"Height: {height}, Width: {width}, Number of channels: {channels}")
# Урт, Өндөр болон channel буюу 3 байвал RGB 2 байвал Grayscale гэж үзэж байгаа юм

# Encryption
key = input("Шинэ нууц үгээ хийнэ үү: ")
text = input("Зурганд нуух үгээ хийнэ үү : ")
kl=0
x = 0 # Анхны утга 0 оноож өгөх
y = 0 # Анхны утга 0 оноож өгөх
z = 0 # Анхны утга 0 оноож өгөх
l=len(text)
for i in range(l):
    print('i=',i)
    print('text=',text[i])
    print('key=',key[kl])
    print('dict1=',dict1[text[i]])
    print('dict2=',dict1[key[kl]])
    xor = dict1[text[i]] ^ dict1[key[kl]]
    print('xor=', xor);
    img[x, y, z] = dict1[text[i]] ^ dict1[key[kl]]
    print('img=', img[x, y, z])
    y = y+1
    x = x+1
    print('kl+1 = ', kl);

    kl = (kl+1)%len(key)

    
cv2.imwrite("encrypted_img.jpeg", img) 
os.system("encrypted_img.jpeg")
print("Encryption амжилттай.")


# Decryption
kl=0
x = 0 #Анхны утга 0 оноож өгөх
y = 0 #Анхны утга 0 оноож өгөх
z = 0 #Анхны утга 0 оноож өгөх
ch = int(input("\n1-г оруулж decryption-ийг эхлүүлнэ уу : "))
if ch == 1:
    key1=input("\n\nНууц үгээ оруулна уу : ")
    decrypt=""
    if key == key1 :
            for i in range(l):
                decrypt+=dict2[img[x, y,z] ^ dict1[key[kl]]]
                y = y+1
                x = x+1
                kl = (kl+1)%len(key)
                print("Нуусан үг нь : ", decrypt)
    else:
         print("Нууц үг нь таарахгүй байна.")
else:
    print("Exiting the code...")

   
