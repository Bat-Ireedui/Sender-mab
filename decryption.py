import cv2
import string
import os


# Declaring the essential Characters
dict1 = {}
dict2 = {}
for i in range(255):
    dict1[chr(i)]=i
    dict2[i]=chr(i)
# print(dict1)
# print(dict2)
# Reading and analyzing our image
img = cv2.imread("test_image.jpeg")
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
print(f"Height: {height}, Width: {width}, Number of channels: {channels}")


# Encryption
key = input("Enter Your Secret Key : ")
text = input("Enter text to hide In the Image : ")
kl=0
tln=len(text)
x = 0 # No of rows
y = 0 # no of columns
z = 0 # plane selection
l=len(text)
for i in range(l):
    img[x, y, z] = dict1[text[i]] ^ dict1[key[kl]]
    y = y+1
    x = x+1
    x = (x+1)%3
    kl = (kl+1)%len(key)
    
cv2.imwrite("encrypted_img.jpeg", img) 
os.system("encrypted_img.jpeg")
print("Data Hiding in Image completed successfully.")


# Decryption
kl=0
tln=len(text)
x = 0 # No of rows
y = 0 # no of columns
z = 0 # plane selection
ch = int(input("\nEnter 1 to extract data from Image : "))
if ch == 1:
    key1=input("\n\nRe-enter secret key to extract text : ")
    decrypt=""
if key == key1 :
        for i in range(l):
            decrypt+=dict2[img[x, y,z] ^ dict1[key[kl]]]
            y = y+1
            x = x+1
            x = (x+1)%3
            kl = (kl+1)%len(key)
print("Encrypted text was : ", decrypt)
    else:
        print("Enter Key doesn't match the original records.")
else:
    print("Exiting the code...")
