import os
import random 
import string
import time
Nama = 'Muhammad Robitul Anam'
NIM  = '212410102067'
Prodi = "Teknologi Informasi"
Instansi = "Universitas Jember"
def cooltrik_str(arg, letter):
    j = 0
    word = ''
    word2 = ''
    while not word2 == arg :
        for i in range(j,len(arg)):
            if arg[j] in string.ascii_uppercase:
                word += random.choice(string.ascii_uppercase + ' ')
                if word == arg[j]:
                    j += 1
                    word2 += word
            elif arg[j] in string.ascii_lowercase:
                word += random.choice(string.ascii_lowercase + ' ')
                if word == arg[j]:
                    j += 1
                    word2 += word
            else :
                word2 += ' '
                j += 1
        print(letter + ' ' + word2 + word)
        word = ''
        os.system('clear')
        
    return letter + ' ' + word2
def cooltrik_int(arg, letter):
    j = 0
    word = ''
    word2 = ''
    while not word2 == arg :
        for i in range(j,len(arg)):
            word += str(random.randint(0,9))
            if word == arg[j]:
                j += 1
                word2 += word
        print(letter + ' ' + word2 + word)
        word = ''
        os.system('clear')
        
    return letter + ' ' + word2

print(cooltrik_str(Nama,"Nama saya : " ))
print(cooltrik_int(NIM, "NIM saya :"))
print(cooltrik_str(Prodi,"Prodi : "))
print(cooltrik_str(Instansi , " Instansi : "))
print("Wow sabar sekali anda")