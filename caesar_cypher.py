alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

def caesar(text,shift,direction):
  def decrypt(text, shift):
    a=[]
    b=0
    c=[]
    d=""
    for i in range(0,len(text)):
      if text[i] not in alphabet:
       c.append(text[i]) 
      else:
        a.append(text[i])
        b=alphabet.index(a[i])
        c.append(alphabet[b-shift])
    d=''.join(c)
    print(f"The decoded text is {d}")
  def encrypt(text, shift):
    a=[]
    b=0
    c=[]
    d=""
    for i in range(0,len(text)):
      if text[i] not in alphabet:
       c.append(text[i]) 
      else:
        a.append(text[i])
        b=alphabet.index(a[i])
        c.append(alphabet[b+shift])
    d=''.join(c)
    print(f"The encoded text is {d}")
  if direction=="encode":
    encrypt(text,shift)
  elif direction=="decode":
    decrypt(text,shift)
  
    
c=""
a=0
while a==0:
  print(logo)
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  if direction=="encode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift= shift%26
    caesar(text,shift,direction)
  elif direction=="decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift= shift%26
    caesar(text,shift,direction)
  else:
    print("Wrong Input")
  c=input("If you want to continue enter 'yes', if you want to exit enter 'no' :\n").lower()
  if c=="yes":
    a=0
  elif c=="no":
    a=1
  else:
    print("Wrong input exiting the program")
    a=1

