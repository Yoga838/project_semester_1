import os
import json

def loaddata (arg1):
    os.system('cls')
    with open ('db.json','r') as opd :
        tmp = json.load(opd)
        print('-'*80)
        print('%-2s | %-30s | %-12s | %-10s'%('#','Nama','Nim','Status'))
        for idx, item in enumerate(tmp):
            print('%-2s | %-30s | %-10s | %-7s'%(idx,item['nama'],item['nim'],item[arg1]))
        print('-'*80)
def pembayaran (arg1):
    os.system('cls')
    loaddata(arg1)
    with open ('db.json','r')as opdb:
        tmp = json.load(opdb)
        inputan = int(input('masukkan no mahasiswa : '))
        tmp [inputan][arg1]="lunas"
    with open('db.json', 'w') as f:
        f.write(json.dumps(tmp))
    loaddata(arg1)
def tambah():
    os.system('cls')
    loaddata("st1")
    nama = input('masukkan nama : ')
    nim = input('masukkan nim : ')
    tmp = {"nama":nama,"nim":nim,"st1":"Belum Lunas","st2":"Belum Lunas","st3":"Belum Lunas","st4":"Belum Lunas","st5":"Belum Lunas","st6":"Belum Lunas","st7":"Belum Lunas","st8":"Belum Lunas",}
    with open ('db.json','r')as crjs:
        sem = json.load(crjs)
    sem.append(tmp)    
    with  open ('db.json','w') as crjs :
        json.dump(sem,crjs)
    loaddata("st1")
def hapus():
    loaddata('st1')
    inputan = int(input('masukkan no mahasiswa : '))
    with open ('db.json','r') as ldb :
        tmp = json.load(ldb)
    tmp.pop(inputan)
    with open ('db.json','w') as delete :
        json.dump(tmp,delete)
    loaddata('st1')   
def menu():
    while True :
        menu = """
        1.Tampilkan Data
        2.Pembayaran Ukt
        3.Menambah Siswa 
        4.Menghapus Siswa 
        5.exit
        """
        print (menu)
        inputan = int(input('masukkan Pilihan : '))
        if inputan == 1 :
            loaddata1()
        elif inputan == 2 :
            pembayaran1()
        elif inputan == 3 :
            tambah()
        elif inputan == 4 :
            hapus()
        elif inputan == 5 :
            exit()

def pembayaran1():
    os.system('cls')
    print("Pilih Semester")
    menu = """
    1.semester 1
    2.semester 2
    3.semester 3
    4.semester 4
    5.semester 5
    6.semester 6
    7.semester 7
    8.semester 8
    """
    
    print(menu)
    choice = input('Menu: ')
    if choice=='1':
        pembayaran('st1')
    elif choice=='2':
        pembayaran('st2')
    elif choice=='3':
        pembayaran('st3')
    elif choice=='4':
        pembayaran('st4')
    elif choice=='5':
        pembayaran('st5')
    elif choice=='6':
        pembayaran('st6')
    elif choice=='7':
        pembayaran('st7')
    elif choice=='8':
        pembayaran('st8')
    else:
        pass

def loaddata1():
    os.system('cls')
    print("Pilih Semester")
    menu = """
    1.semester 1
    2.semester 2
    3.semester 3
    4.semester 4
    5.semester 5
    6.semester 6
    7.semester 7
    8.semester 8
    """

    print(menu)
    choice = input('Menu: ')
    if choice=='1':
        loaddata('st1')
    elif choice=='2':
        loaddata('st2')
    elif choice=='3':
        loaddata('st3')
    elif choice=='4':
        loaddata('st4')
    elif choice=='5':
        loaddata('st5')
    elif choice=='6':
        loaddata('st6')
    elif choice=='7':
        loaddata('st7')
    elif choice=='8':
        loaddata('st8')
    else:
        pass

