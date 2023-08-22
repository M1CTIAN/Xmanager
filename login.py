from cryptography.fernet import Fernet
import csv
import pickle
import app
with open('untitled.key','rb') as pwd_file:
    key = pwd_file.read()
def encrypt(l,key,file):
    x=Fernet(key)
    l1=pickle.dumps(l)
    encrypted = x.encrypt(l1)
    with open(file,'wb') as f1:
        f1.write(encrypted)
def decrypt(file,key):
    x=Fernet(key)
    with open(file,'rb') as f:
        encrypted = f.read()
    text = x.decrypt(encrypted)
    a=text.decode('utf-8')
    l= a.split('\r\n')
    l1=[]
    for i in l:
        try:
            l1.append([i.split(',')[0],i.split(',')[1]])
        except:
            continue
    return l1
def strongpswd(x):
    size=False
    caps=False
    lower=False
    num=False
    special=False
    s='[@_!#$%^&*()<>?/\|}{~:]'
    if len(x)>8:
        size=True
    for i in x:
        if i.isdigit():
            num=True
        elif i.islower():
            lower=True
        elif i.isupper():
            caps=True
        elif i in s:
            special=True
    total=caps and lower and num and special and size
    if total==True:
        return True
    else:
        return False
with open('untitled.key','rb') as pwd_file:
    key = pwd_file.read()
login_file = 'test.csv'
def login(file,key):
    done1=False
    while done1==False:
        ask=input('Create new ID (1) / Log-in existing ID (2): ')
        if ask=='1':
            x=decrypt(file,key)            
            while True:
                user = input('Enter Username: ')
                for i in x:
                    if i[0]==user:
                        print('Username already taken. Try again.')
                        break
                else:
                    break       
            while True:
                pswd=input('Enter Strong Password (must contain lowercase, uppercase, numbers and special characters and must be at least 8 characters):\n')
                if strongpswd(pswd):
                    break
                else:
                    print('Weak Password')
            x.append([user,pswd])
            encrypt(x,key,file)
            break
        elif ask=='2':
            tries=3
            x=decrypt(file,key)
            done=False
            while tries>0 and done==False:
                print(f'Tries left: {tries}')
                user2=input('Enter Username: ')
                pswd2=input('Enter Password: ')
                for j in x:
                    if user2==j[0] and pswd2==j[1]:
                        done=True
                tries-=1               
            if done==True:
                print('Login Successful.')
                done1=True
                app.start()
            elif done==False:
                print('Invalid Credentials.')
        else:
            print('Invalid Option.')
login('login_enc.csv',key)
