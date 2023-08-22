from tkinter import *
import tkinter.messagebox
from tkinter import font
import datetime as dt
from tabulate import tabulate
import csv
import plotly.express as px
months=['jan','feb','mar','apr','may','jun','jul','sept','oct','nov','dec']
years={'2022','2023','2024','2025','2026'}
days=[31,28,31,30,31,30,31,31,30,31,30,31]
org = Tk()
b1 = PhotoImage(file='button1.png')
b2 = PhotoImage(file='button2.png')
b3 = PhotoImage(file='button3.png')
b4 = PhotoImage(file='button4.png')
b5 = PhotoImage(file='button5.png')
b6 = PhotoImage(file='button6.png')
def bar(cls,amt,title):
    fig = px.bar(x=cls, y=amt, title= title)
    fig.show()
def graphs(values,date,title):
    fig = px.line(x = date, y = values, title= title)
    fig.show()    
def month():
    def done():
        global months, years, b6        
        choose = vr.get()
        currenty = str(dt.datetime.now()).split()[0].split('-')[0]
        currentm = (((str(dt.datetime.now()).split())[0]).split('-'))[1]
        currentd = (((str(dt.datetime.now()).split())[0]).split('-'))[2]
        m_name = months[int(currentm) - 1]        
        if choose=='By Month':
            newWindow_4 = Toplevel(newWindow_1)
            newWindow_4.configure(bg= 'black')
            newWindow_4.title("Months")
            newWindow_4.geometry('569x800')
            frameCnt = 44
            frames = [PhotoImage(file='love-stars-2.gif',format = f'gif -index {i}') for i in range(frameCnt)]
            def update(ind):
                frame = frames[ind]
                ind += 1
                if ind == frameCnt:
                    ind = 0                
                try:
                    label.configure(image=frame)
                except Exception as e:
                    print(e)                    
                newWindow_4.after(100, update, ind)
            label = Label(newWindow_4)
            label.place(x=0,y=0)
            newWindow_4.after(0,update,0)         
            vr_1 = StringVar(newWindow_4)
            vr_1.set( "--select year--" )
            vr_2 = StringVar(newWindow_4)
            vr_2.set( "--select month--" )
            menu = OptionMenu(newWindow_4, vr_2 ,*months )
            menu.place(x=69,y=200)
            menu_1=OptionMenu(newWindow_4, vr_1,*years)
            menu_1.place(x=300,y=200)
            def m_graph():
                currentm = vr_2.get()
                currenty = vr_1.get()
                file = open(f'{currentm.title()}, {currenty}.csv','r',newline='')
                reader = csv.reader(file)
                l=[]
                d={}
                for i in reader:
                    if i[0]!='Category':
                        l.append((i[1],i[2]))
                for j in l:
                    if j[1] not in d:
                        d[j[1]]=0
                for k in d:
                    for x in l:
                        if x[1]==k:
                            d[k]+=int(x[0])
                dates=[]
                for p in list(d.keys()):
                    dates.append((p.split('/'))[0])
                graphs(values = list(d.values()), date = dates, title = f'{currentm.title()}, {currenty}')            
            btn = Button(newWindow_4,text='Enter',image=b6,bg='#0c0c0c',command = m_graph)
            btn.config(relief=FLAT)
            btn.place(x=200,y=400)
            menu.config(width=12)
            menu.config(height=2)
            menu.config(bg='#08dcdd')
            menu_1.config(width=12)
            menu_1.config(height=2)
            menu_1.config(bg='#08dcdd')
            font_s = font.Font(family='Helvetica', size=16)
            menu.config(font=font_s)
            menu_1.config(font=font_s)
            drop=newWindow_4.nametowidget(menu.menuname)
            drop.config(font=font_s)
            drop1=newWindow_4.nametowidget(menu_1.menuname)
            drop1.config(font=font_s)        
        elif choose=='By Category':            
            file=open(f'{m_name.title()}, {currenty}.csv','r',newline='')
            reader=csv.reader(file)
            l=[]
            d={}
            for i in reader:
                if i[0]!='Category':
                    l.append((i[0],i[1]))
            for j in l:
                if j[0] not in d:
                    d[j[0]]=0
            for k in d:
                for x in l:
                    if x[0]==k:
                        d[k]+=int(x[1])
            bar(cls=list(d.keys()),amt=list(d.values()),title=f'{m_name.title()}, {currenty}')
    global b6
    list1=['By Month','By Category']
    newWindow_1 = Toplevel(org)
    newWindow_1.configure(bg= 'black')
    newWindow_1.title("Display Selection")
    newWindow_1.geometry('569x800')
    frameCnt = 44
    frames = [PhotoImage(file='love-stars-2.gif',format = f'gif -index {i}') for i in range(frameCnt)]
    def update(ind):
        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0        
        try:
            label.configure(image=frame)
        except Exception as e:
            print(e)            
        newWindow_1.after(100, update, ind)
    label = Label(newWindow_1)
    label.place(x=0,y=0)
    newWindow_1.after(0,update,0)    
    vr = StringVar(newWindow_1)
    vr.set( "--select--" )
    menu = OptionMenu(newWindow_1, vr ,*list1 )
    menu.place(x=150,y=200)    
    btn = Button(newWindow_1,text='Enter',image=b6,bg='#0c0c0c',command= done)
    btn.config(relief=FLAT)
    btn.place(x=200,y=400)
    menu.config(width=15)
    menu.config(height=2)
    menu.config(bg='#08dcdd')
    font_s = font.Font(family='Helvetica', size=20)
    menu.config(font=font_s)
    drop=newWindow_1.nametowidget(menu.menuname)
    drop.config(font=font_s)
def add_data():
    global b4,b5
    newWindow_2 = Toplevel(org)
    newWindow_2.configure(bg= 'black')
    newWindow_2.title("input data screen")
    newWindow_2.geometry('569x800')
    frameCnt = 44
    frames = [PhotoImage(file='love-stars-2.gif',format = f'gif -index {i}') for i in range(frameCnt)]
    def update(ind):
        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0        
        try:
            label.configure(image=frame)
        except Exception as e:
            print(e)            
        newWindow_2.after(100, update, ind)
    label = Label(newWindow_2)
    label.place(x=0,y=0)
    newWindow_2.after(0,update,0)
    btn_1 = Button(newWindow_2,image=b4,bg='#171817',command = lambda:[message("Please enter you data in the Python shell"),input_budget()],text = 'input budget')
    btn_1.config(relief=FLAT)
    btn_1.place(x = 140,y = 200)
    btn_2 = Button(newWindow_2,image=b5,bg='#171817',command = lambda:[message("Please enter you data in the Python shell"),exp_input()],text = 'input expenditure')
    btn_2.config(relief=FLAT)
    btn_2.place(x = 90,y = 400)    
def get_advice():
    newWindow_3 = Tk()
    newWindow_3.configure(bg= 'black')
    newWindow_3.title("get advice screen")
    newWindow_3.geometry('400x500')
#    bg = PhotoImage(file = "Your_image.png")
    label1 = Label(newWindow_3)
    global months, days
    currenty = str(dt.datetime.now()).split()[0].split('-')[0]
    currentm = (((str(dt.datetime.now()).split())[0]).split('-'))[1]
    currentd = (((str(dt.datetime.now()).split())[0]).split('-'))[2]
    if currentd=='01':
        m_name = months[int(currentm)-2]        
    else:
        m_name = months[int(currentm)-1]
    try:
        file1 = open(f'{m_name}, {currenty}.csv','r')
        reader1 = csv.reader(file1)
        file2 = open(f'{m_name}, {currenty} budget.csv','r')
        reader2 = csv.reader(file2)
        spent=0
        budget=0
        date=0
        tot_days = days[months.index(m_name)]
        new={}
        new2={}
        cls=[]        
        for j in reader2:
            budget+=j['amount']
            new[(j['category'])]=0
            if j['priority']=='2':
                new2[(j['category'])]=0       
        for i in reader1:
            spent+=i['amount']
            if int(i['date'])>date:
                date=int(i['date'])
            for k in new:
                if new[k]==i['category']:
                    new[k]+=i['amount']
            for m in new2:
                if new2[k]==i['category']:
                    new2[k]+=i['amount']
        s1=('You spent {spent} out of your total budget of {budget} ie. {spent/budget*100}% of total budget\nin {date} days ie. {date/tot_days*100}% of the month')
        s2=('Your top 3 most expenditure categories are:')
        s3=''
        for x in sorted(zip(new.values(),new.keys()))[:-4:-1]:
            s3+=(f'{x[1]}: Amount= {x[0]}\n')
        s4=('Your top 3 most expenditure categories (Non-essential) are:')
        s5=''
        for y in sorted(zip(new2.values(),new2.keys()))[:-4:-1]:
            s5+=(f'{y[1]}: Amount= {y[0]}\n')
        xyz=f'{s1}\n{s2}\n{s3}\n-x-\n{s4}\n{s5}'
        lbl = Label(newWindow_3,text = xyz, font=('Arial',14),bg='black',fg='white').pack()
    except FileNotFoundError:
        message('Insufficient data for analysis.')
        newWindow_3.destroy()    
def input_budget():
    global months
    currenty = str(dt.datetime.now()).split()[0].split('-')[0]
    currentm = (((str(dt.datetime.now()).split())[0]).split('-'))[1]
    currentd = (((str(dt.datetime.now()).split())[0]).split('-'))[2]    
    if currentd=='01':
        print(f'Welcome! Enter the budget details for {(months[int(currentm)-1]).title()}, {currenty}')
        name = f'{(months[int(currentm)-1]).title()}, {currenty}'
    elif currentd!='01' and int(currentm)<12:
        print(f'Welcome! Enter the budget details for {(months[int(currentm)]).title()}, {currenty}')
        name = f'{(months[int(currentm)]).title()}, {currenty}'
    elif currentd!='01' and int(currentm)==12:
        print(f'Welcome! Enter the budget details for Jan, {int(currenty)+1}')
        name = f'Jan, {int(currenty)+1}'       
    b_csv = open(f'{name} budget.csv','w+',newline='')
    run=True
    classes=[]
    writer = csv.writer(b_csv)
    writer.writerow(['Category','Amount','Priority'])        
    while run:
        c=input('Enter new category (type "done" after storing all categories): ')
        if c.lower()=='done':
            run=False
        else:
            classes.append(c)
    for i in classes:
        while True:
            print(f'Entry for Category {i}')
            while True:
                amt = input('Enter amount allotted (No decimal values, integers only): ')
                imp = input(f'Is {i} category essential or non-essential (1/2):')
                print(f'Category: {i}, amount allotted: {amt}, priority: {imp}\n# Priority(1)= Essential; Priority(2)= Non-Essential')
                cont = input('Confirm response (y/n)')
                if cont.lower()=='y':
                    break
            if amt.isdigit()==True and (imp=='1' or imp=='2'):
                writer.writerow([i,int(amt),imp])
                break
            else:
                print('Incorrect Entry. Try Again.')
    b_csv.close()
    b1_csv = open(f'{name} budget.csv','r',newline='')
    reader=csv.reader(b1_csv)
    l1=[]
    for j in reader:
        if j[0]!='Category':
            if j[2]=='1':
                a='Essential'
            elif j[2]=='2':
                a='Non-essential'        
            l1.append([j[0],j[1],a])
            print(tabulate(l1,headers=['Category','Amount','Priority'],showindex='always',tablefmt='psql'))  
    b1_csv.close()
    print('\nEntries recorded.')
def input_expenditure(e_csv):
    global months
    currenty = str(dt.datetime.now()).split()[0].split('-')[0]
    currentm = (((str(dt.datetime.now()).split())[0]).split('-'))[1]
    currentd = (((str(dt.datetime.now()).split())[0]).split('-'))[2]
    print(f'Entry for {months[int(currentm)-1]}, {currenty}')
    writer = csv.writer(e_csv)
    writer.writerow(['Category','Amount','DD/MM/YYYY'])
    while True:
        while True:
            cls = input('Enter Category: ')
            amt = input('Enter amount spent: ')
            if amt.isdigit():
                writer.writerow([cls,int(amt),f'{currentd}/{currentm}/{currenty}'])
                break
            else:
                print('Invalid input.')
                break
        d=input('Continue adding entries? (y/n)')
        if d.lower()=='n':
            break
def exp_input():
    global months
    currenty = str(dt.datetime.now()).split()[0].split('-')[0]
    currentm = (((str(dt.datetime.now()).split())[0]).split('-'))[1]
    currentd = (((str(dt.datetime.now()).split())[0]).split('-'))[2]
    m_name = months[int(currentm) - 1]    
    file=open(f'{(m_name).title()}, {currenty}.csv','a+',newline='')
    input_expenditure(file)
    file.close()
def message(txt):
    tkinter.messagebox.showinfo("Message",  txt)
def start():
    global months, years, days, org, b1, b2, b3, b4, b5, b6
    org.configure(bg = 'black')
    org.title('Expenditure manager')
    org.geometry("569x800")
    frameCnt = 44
    frames = [PhotoImage(file='love-stars.gif',format = f'gif -index {i}') for i in range(frameCnt)]
    def update(ind):
        frame = frames[ind]
        ind += 1
        if ind == frameCnt:
            ind = 0
        label.configure(image=frame)
        org.after(100, update, ind)
    label = Label(org)
    label.pack()
    org.after(0, update, 0)
    button_1 = Button(org,image=b1,bg='#171817',command = month, text = 'VIEW MONTHS')
    #button_1.config(font = ('Porter',19,'bold'), height = 2, width = 15,relief = GROOVE)
    button_1.config(relief=FLAT)
    button_1.place(x = 180,y = 100)
    button_2 = Button(org,image=b2,bg='#141416',command = add_data, text = 'add data')
    #button_2.config(font = ('Porter',19,'bold'), height = 2, width = 15,relief = GROOVE)
    button_2.config(relief=FLAT)
    button_2.place(x = 180,y = 300)
    button_3 = Button(org,image=b3, bg='#090809',command = get_advice, text = 'GET ADVICE')
    #button_3.config(font = ('Porter',19,'bold'), height = 2, width = 15,relief = GROOVE)
    button_3.config(relief=FLAT)
    button_3.place(x = 180,y = 500)
    mainloop()
