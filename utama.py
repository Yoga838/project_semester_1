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
def pembayaran(arg1):
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
def menu(arg1):
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
            loaddata(arg1)
        elif inputan == 2 :
            pembayaran()
        elif inputan == 3 :
            tambah()
        elif inputan == 4 :
            hapus()
        elif inputan == 5 :
            exit()

def menuawal():
    os.system('cls')
    print("Pilih Semester")
    lists = """
    1.semester 1
    2.semester 2
    3.semester 3
    4.semester 4
    5.semester 5
    6.semester 6
    7.semester 7
    8.semester 8
    """
    
    print(lists)
    choice = input('Menu: ')
    if choice=='1':
        menu('st1')
    elif choice=='2':
        menu('st2')
    elif choice=='3':
        menu('st3')
    elif choice=='4':
        menu('st4')
    elif choice=='5':
        menu('st5')
    elif choice=='6':
        menu('st6')
    elif choice=='7':
        menu('st7')
    elif choice=='8':
        menu('st8')
    else:
        pass
