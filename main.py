import csv
def add():
    f = open ("Olympic.csv","w", newline = '')
    cw = csv.writer(f)
    cw.writerow(['Sno.','Name','Sex','Age','Country','Sport',
                 'Type of medal won'])
    ans = 'y'
    while ans == 'y':
        sno = int(input("Enter player ID:"))
        n = input("Name of the player:")
        s = input('Sex of the player:')
        age = int(input("Age of the player:"))
        c = input("Enter country of the player:")
        sp = input('Sport played:')
        m = input('Type of medal won:')
        l = [sno,n,s,age,c,sp,m]

        cw.writerow(l)
        ans = input("Want to enter more records? (y/n)..")
    f.close()
    
def display():
     with open("Olympic.csv", 'r', newline = '') as f:
         read=csv.reader(f)
         for i in read:
             print(i)

def name():
    f=open('Olympic.csv','r',newline='')
    reader=csv.reader(f)
    n=input('Enter name of the player to be searched in the record:')
    for row in reader:
        if n == row[1] :
            print('Record found successfully!!')
            print(row)
            break
    else:
        print('Record not found.')

   
def sex():
    f=open('Olympic.csv','r',newline='')
    reader=csv.reader(f)
    sex=input('Enter the gender to be searched (F/M):')
    for row in reader:
        if row[2]==sex:
            print('Record found successfully!!')
            print(row)
    else:
            print('Record not found.')


def country():
    f=open('Olympic.csv','r',newline='')
    reader=csv.reader(f)
    n=input('Enter the country to be searched in the database:')
    for row in reader:
        if row[4] ==n:
            print('Record found successfully!!')
            print(row)
            break
    else:
            print('Record not found.')

def sport():
    f=open('Olympic.csv','r',newline='')
    reader=csv.reader(f)
    n=input('Enter sport to be searched in the database:')
    for row in reader:
        if row[5] ==n:
            print('Record found successfully!!')
            print(row)
            break
    else:
            print('Record not found.')


def medal():
    f=open('Olympic.csv','r',newline='')
    reader=csv.reader(f)
    n=input('Enter the type of medal to be searched in the database:')
    for row in reader:
         if row[5]==n:
             print('Record found successfully!!')
             print('row')
             break
    else:
         print('Record not found!!')




def update():
    f = open ("Olympic.csv","a", newline = '')
    cw = csv.writer(f)
    cw.writerow(['Sno.','Name','Sex','Age','Country','Sport',
                 'Number of medals won'])
    
    sno = int(input("Enter player ID:"))
    n = input("Name of the player:")
    s = input('Sex of the player:')
    age = int(input("Age of the player:"))
    sp = input('Sport played:')
    m= input('Type of medal won:')
    l = [sno,n,s,age,sp,m]
    cw.writerow(l)
    f.close()



while True:

    print("MENU:")
    print("Choose the task to be performed.")
    print('''1.Add records to the database.\n2.Display the records.
3.Search a record.\n4.Update the record.\n5.Exit''')
    n = int(input("Enter your choice of the task to be performed"))

    if n == 1:
        add()
    elif n == 2:
       display()
    elif n == 3:
      while True:
        print("MENU:")
        print("Choose the task to be performed.")
        print('''1.Search by name.\n2.Search by gender. \n3.Search by country.
4.Search by sport.\n5.Search by type of medals.\n6.Exit this command.''')
        x = int(input("Enter your choice of the task to be performed"))
        if x == 1:
            name()
        elif x == 2:
            sex()
        elif x == 3:
            country()
        elif x == 4:
            sport()
        elif x == 5:
            medal()
        elif x == 6:
            print("Terminating this command.")
            break
        else:
            print("Invalid choice. Enter again...")
    elif n == 4:
        update()
    elif n == 5:
        print("Terminating the program!!!")
        break
    else:
        print("Invalid choice entered. Enter again...")











     




