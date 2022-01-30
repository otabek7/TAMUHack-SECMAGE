# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 11:41:30 2022

@author: mavlo
"""
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from PIL import *
import random
import datetime as dt
import os, sys
from tkinter import ttk
global finalmessage

#import "C:\Users\mavlo\Documents\decrypter"

root = Tk()
root.title("SECMAGE")
root.geometry('1900x800')

canvas = Canvas(root, width = 380, height = 120)      
canvas.place(x = 300, y=0)


img = PhotoImage(file="d133c2fc811a4247a758ccec0024b9f3.png")      
canvas.create_image(0,0, anchor=NW, image=img)

        
lbl_enc=Label(root, text="To encrypt: enter your message in the text box,\nopen a picture to encrypt into, and click encrypt!", fg='black', bg= "#F0F0F0", font=("Trebuchet MS Bold", 12))
lbl_enc.place(x=30, y=150)

lbl_dec=Label(root, text="To decrypt: open a picture to decrypt and click decrypt!", fg='black', bg="#F0F0F0", font=("Trebuchet MS Bold", 12))
lbl_dec.place(x=30, y=340)

root.iconbitmap("lets_encrypt_logo_icon_145110.ico")
root.configure(background='#F0F0F0')




def text_input():
   global entry
   string = entry.get()
    #Initialize a Label to display the User Input
   return string

#Create an Entry widget to accept User Input
entry = Entry(root, width= 25)
entry.focus_set()
entry.place(x=450, y=158)



def encrypt_option():
    
    def file_picker():
        global my_image
        root.filename = filedialog.askopenfilename(initialdir = "C:/Users/mavlo/Documents", title = "Select A File", filetypes = (("png files", "*.png"), ("all files", "*.*"), ("jpg files", "*.jpg")))
        #my_label = Label(root, text = root.filename).pack() # not sure if we need to display the working directory on the screen
        image = Image.open(root.filename, "r")
        width,height = image.size
        if (width and height) <=199:
            resize_image = image.resize((width//2, height//2))
            img = ImageTk.PhotoImage(resize_image)
            label1 = Label(image=img)
            label1.image = img
            label1.place(x=760, y=150)
    
        elif (width and height) >200 and (width and height) <299:
            resize_image = image.resize((width//3, height//3))
            img = ImageTk.PhotoImage(resize_image)
            label1 = Label(image=img)
            label1.image = img
            label1.place(x=760, y=150)
    
        elif (width and height) >300 and (width and height) <399:
            resize_image = image.resize((width//4, height//4))
            img = ImageTk.PhotoImage(resize_image)
            label1 = Label(image=img)
            label1.image = img
            label1.place(x=760, y=150)
       
        else:
            resize_image = image.resize((width//5, height//5))
            img = ImageTk.PhotoImage(resize_image)
            label1 = Label(image=img)
            label1.image = img
            label1.place(x=760, y=150)

        label2 = Label(root, text="Image has been saved in your working directory", fg='black', bg="#ee9b00", font=("Trebuchet MS Bold", 10))
        label2.place(x=440, y=260)
        return root.filename
    def FileChecker(filename):
        slash = "\ ".strip()
        filenameNew = filename.replace("/", slash)
        fileNameList = filenameNew.split(slash)        
        for i in range(len(fileNameList)):
            if ((".jpg" in fileNameList[i]) or (".png" in fileNameList[i])):
                filename1 = fileNameList[i].split(".")
                
                root = filenameNew.replace(fileNameList[i],"")
                return root, (filename1[0] + "(1)")
    
    def OpenFile(filename):
        canvas = Image.open(open.FileName, 'r')
        width, height = canvas.size
        pixelList = canvas.load()
        return pixelList, canvas.size
    
    def RandomizerSeed():
        currentTime = dt.datetime.now()
        timeSeed = currentTime.strftime("%m%d%y%H%M")
        return timeSeed
    
    def SeedLengthEncoder(timeSeed, pixelList, message):
        timeSeedString = str(timeSeed)
        print(message)
        for i in range(len(timeSeed)):
            pixelRGB = pixelList[i, 0] 
            RGBValue = str(pixelRGB[1] // 10)
            
            if pixelRGB[1] < 250:
                pixelList[i, 0] = (pixelRGB[0], int(RGBValue + timeSeedString[i]), pixelRGB[2])
            else:
                pixelList[i, 0] = (pixelRGB[0], 240 + int(timeSeedString[i]), pixelRGB[2])
    
        messageLen = str(len(message))
        messageLenNew = messageLen
        
        while len(messageLenNew) < 5:
            messageLenNew = "0" + messageLenNew
        
        for i in range(len(messageLenNew)):
            pixelRGB = pixelList[11 + i, 0] 
            RGBValue = str(pixelRGB[1] // 10)
    
            if pixelRGB[1] < 250:
                pixelList[11 + i, 0] = (pixelRGB[0], int(RGBValue + messageLenNew[i]), pixelRGB[2])
            else:
                pixelList[11 + i, 0] = (pixelRGB[0], 240 + int(messageLenNew[i]), pixelRGB[2])
    
    # Randomizer
    def RandomizerMessage(pixelList, seed, canvasSize, message):
        random.seed(int(seed))
        sizeX = canvasSize[0]
        sizeY = canvasSize[1]
        
        keyEncrypt = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, 
                      "7":7, "8":8, "9":9, " ":10, "a":11, "b":12, "c":13, 
                      "d":14, "e":15, "f":16, "g":17, "h":18, "i":19, "j":20, 
                      "k":21, "l":22, "m":23, "n":24, "o":25, "p":26, "q":27, 
                      "r":28, "s":29, "t":30, "u":31, "v":32, "w":33, "x":34, 
                      "y":35, "z":36}
        specialEncrypt = {"!":1,'"':2,"#":3,"$":4,"%":5,"&":6,"'":7,"(":8,")":9,"*":10,"+":11,",":12,
                          "-":13,".":14,"/":15,":":16,";":17,"<":18,"=":19,">":20,"?":21,"@":22,"[":23,
                          "]":24,"^":25,"_":26,"`":27,"{":28,"}":29,"~":30}
        cordList = []
        for character in message: 
            isUsed = False
            xVal = 0
            yVal = 0
            while isUsed == False:
                xVal = random.randint(1, sizeX-2)
                yVal = random.randint(3, sizeY-2)
                cordChecker = str(xVal) + str(yVal)
                if cordChecker not in cordList:
                    isUsed = True
                    cordList += [cordChecker]
            # Clone
            pixelRGBVal = pixelList[xVal, yVal]           
            # special character checker
            if character in specialEncrypt:
                specialValue = True
            else:
                specialValue = False
            if ((specialValue == True) or (character.lower() not in keyEncrypt)):
                if pixelRGBVal[2] >= 128:
                    try:
                        value = specialEncrypt[character]
                    except:
                        value = 14
                    newRGBVal = (pixelRGBVal[0], pixelRGBVal[1], (pixelRGBVal[2] - value))
                else:
                    try:
                        value = specialEncrypt[character]
                    except:
                        value = 14
                    newRGBVal = (pixelRGBVal[0], pixelRGBVal[1], (pixelRGBVal[2] + value))
                        
            elif ((specialValue == False) and (pixelRGBVal[1] >= 128)):
                upperCaseTest = character.isupper()
                if character.lower() in keyEncrypt:
                    try:
                        value = keyEncrypt[character.lower()]
                    except:
                        value = 10
                else:
                        value = 10
                        
                if (upperCaseTest == False):
                    newRGBVal = (pixelRGBVal[0], (pixelRGBVal[1] - value), pixelRGBVal[2])
                elif (pixelRGBVal[0] > 253):
                    newRGBVal = (pixelRGBVal[0] - 1, (pixelRGBVal[1] - value), pixelRGBVal[2])
                else:
                    newRGBVal = (pixelRGBVal[0] + 1, (pixelRGBVal[1] - value), pixelRGBVal[2])
            else:
                upperCaseTest = character.isupper()
                try:
                    value = keyEncrypt[character.lower()]
                except:
                    value = specialEncrypt["."]
    
                if (upperCaseTest == False):
                    newRGBVal = (pixelRGBVal[0], (pixelRGBVal[1] + value), pixelRGBVal[2])
                elif (pixelRGBVal[0] > 253):
                    newRGBVal = (pixelRGBVal[0] - 1, (pixelRGBVal[1] + value), pixelRGBVal[2])
                else:
                    newRGBVal = (pixelRGBVal[0] + 1, (pixelRGBVal[1] + value), pixelRGBVal[2])
                
            # Write clone and new color
            pixelList[xVal, yVal] = newRGBVal
            pixelList[xVal - 1, yVal] = pixelRGBVal
    
    
    # Main that calls everything
    def main():
        # From GUI        
        FileName = file_picker()
        root, newFileName = FileChecker(FileName)
        canvas = Image.open(FileName, 'r')
        width, height = canvas.size
        pixelList = canvas.load()
        canvasSize = canvas.size
                
        # Later overwrite with GUI
        message = str(text_input())
            
        # Seed
        timeSeed = RandomizerSeed()
        SeedLengthEncoder(timeSeed, pixelList, message)
        
        # randomizer
        RandomizerMessage(pixelList, timeSeed, canvasSize, message)
        canvas.save(root + newFileName + ".png")
    main()    
    
finalmessage = ""
    



def getSeed(im):
    seed = ""
    img = im.load()
    for i in range(10):
        pix = img[i,0]
        bValue = pix[1]
        seed += str(bValue % 10)
    seed = int(seed)
    return seed

def getLength(im):
    img = im.load()
    messageLength = ""
    for i in range(5):
        pix = img[i+11, 0]
        bValue = pix[1]
        messageLength += str(bValue % 10)
    messageLength = int(messageLength)
    return messageLength
    
def getMessage(im, seed, messageLength):
    message = ""
    img = im.load()
    random.seed(seed)
    sizeX, sizeY = im.size
    cordList = []
    codeKey = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:" ",
               11:"a", 12:"b", 13:"c", 14:"d", 15:"e", 16:"f", 17:"g", 18:"h", 19:"i", 20:"j",
               21:"k", 22:"l", 23:"m", 24:"n", 25:"o", 26:"p", 27:"q", 28:"r", 29:"s", 30:"t",
               31:"u", 32:"v", 33:"w", 34:"x", 35:"y", 36:"z"}
    
    specialKey = {1:"!",2:'"', 3:"#", 4:"$", 5:"%", 6:"&", 7:"'", 8:"(", 9:")", 10:"*",
                  11:"+", 12:",", 13:"-", 14:".", 15:"/", 16:":", 17:";", 18:"<", 19:"=", 20:">",
                  21:"?", 22:"@", 23:"[", 24:"]", 25:"^", 26:"_", 27:"`", 28:"{", 29:"}", 30:"~"}
    
    for i in range(messageLength):  
        isUsed = False
        xVal = 0
        yVal = 0
        while isUsed == False:
            xVal = random.randint(1, sizeX-2)
            yVal = random.randint(3, sizeY-2)
            cordChecker = str(xVal) + str(yVal)
            if cordChecker not in cordList:
                isUsed = True
                cordList += [cordChecker]
                
        clonePix = img[xVal - 1, yVal]
        changedPix = img[xVal, yVal]
        redDiff = abs(changedPix[0] - clonePix[0])
        greenDiff = abs(changedPix[1] - clonePix[1])
        blueDiff = abs(changedPix[2] - clonePix[2])

        myChar = ""
        try:
            if blueDiff > 0:
                myChar += specialKey[blueDiff]
                #print(blueDiff)
            else:
                myChar += codeKey[greenDiff]
                #print(greenDiff)
            if redDiff > 0:
                myChar = myChar.upper()
        except:
            myChar = "."
        message += myChar
        
    finalmessage = message
    return message

def mainer():
    im = getImage()
    seed = getSeed(im)
    messageLength = getLength(im)
    message = getMessage(im, seed, messageLength)
    global finalmessage 
    finalmessage = "The message was:", message   
    label2 = Label(root, text = finalmessage, fg='black', bg="#ee9b00", font=("Trebuchet MS Bold", 10)) # Rather than image chosen, state what the message was
    label2.place(x=610, y=340)
        #return("The message was:", finalmessage)
        
        #lbl_deca=Label(message, fg='black', bg="#F0F0F0", font=("Trebuchet MS Bold", 12))
        #lbl_deca.place(x=300, y=340)
def getImage():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir = "/Documents", title = "Select A File", filetypes = (("png files", "*.png"), ("all files", "*.*"), ("jpg files", "*.jpg")))
    #my_label = Label(root, text = root.filename).pack() # not sure if we need to display the working directory on the screen
    image = Image.open(root.filename, "r")
    width,height = image.size
    if (width and height) <=199:
        resize_image = image.resize((width//2, height//2))
        img = ImageTk.PhotoImage(resize_image)
        label1 = Label(image=img)
        label1.image = img
        label1.place(x=620, y=300)
    elif (width and height) >200 and (width and height) <299:
        resize_image = image.resize((width//3, height//3))
        img = ImageTk.PhotoImage(resize_image)
        label1 = Label(image=img)
        label1.image = img
        label1.place(x=620, y=300)
    elif (width and height) >300 and (width and height) <399:
        resize_image = image.resize((width//4, height//4))
        img = ImageTk.PhotoImage(resize_image)
        label1 = Label(image=img)
        label1.image = img
        label1.place(x=620, y=300)
    elif (width and height) >400 and (width and height) <499:
        resize_image = image.resize((width//3, height//3))
        img = ImageTk.PhotoImage(resize_image)
        label1 = Label(image=img)
        label1.image = img
        label1.place(x=620, y=300)
    
    
    return image
        
    
my_btn_oencrypt=Button(root, text="Open File to Encrypt", fg='black', bg="#219ebc", command = encrypt_option)
my_btn_oencrypt.place(x=618, y=158)

#my_btn_encrypt=Button(root, text="Encrypt", fg='black', bg="#0a9396", command = encrypt_option)
#my_btn_encrypt.place(x=680, y=160)


my_btn_decrypt=Button(root, text="Open File to Decrypt", fg='black', bg="#219ebc", command = mainer)
my_btn_decrypt.place(x=480, y=340)




root.mainloop()