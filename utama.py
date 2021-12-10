import os
import json
import time

def loaddata (arg1):
    print ('proses .......')
    time.sleep(1)
    os.system('cls')
    with open ('db.json','r') as opd :
        tmp = json.load(opd)
        print('-'*80)
        print('%-2s | %-30s | %-12s | %-10s'%('#','Nama','Nim','Status'))
        for idx, item in enumerate(tmp):
            print('%-2s | %-30s | %-10s | %-7s'%(idx,item['nama'],item['nim'],item[arg1]))
        print('-'*80)
        inputan = input('masukkan no mahasiswa untuk mengecek status selengkapnya / enter untuk kembali ')
        if inputan != "":
            loaddatarnc(int(inputan),arg1)
        elif inputan == "" :
            menu(arg1)
        else:
            print('keyword error')
def loaddatassw():
    print ('proses .......')
    time.sleep(1)
    os.system('cls')
    with open ('db.json','r') as opd :
        tmp = json.load(opd)
        print('-'*60)
        print('%-2s | %-30s | %-12s '%('#','Nama','Nim'))
        for idx, item in enumerate(tmp):
            print('%-2s | %-30s | %-10s '%(idx,item['nama'],item['nim']))
        print('-'*60)
def loaddatarnc(arg1,arg2):
    print ('proses....')
    time.sleep(1)
    os.system('cls')
    with open ('db.json','r') as op:
        tmp = json.load(op)
        print ('Nama Mahasiswa ',tmp[arg1]['nama'])
        print ('status pembayaran semester satu    ', tmp[arg1]['st1'])
        print ('status pembayaran semester dua     ', tmp[arg1]['st2'])
        print ('status pembayaran semester tiga    ', tmp[arg1]['st3'])
        print ('status pembayaran semester empat   ', tmp[arg1]['st4'])
        print ('status pembayaran semester lima    ', tmp[arg1]['st5'])
        print ('status pembayaran semester enam    ', tmp[arg1]['st6'])
        print ('status pembayaran semester tujuh   ', tmp[arg1]['st7'])
        print ('status pembayaran semester delapan ', tmp[arg1]['st8'])
        inp = input("--- enter untuk kembali ---")
        if inp == "" :
            loaddata(arg2)
def showdata(arg1):
    print ('proses .......')
    time.sleep(1)
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
    while True:
        showdata(arg1)
        with open ('db.json','r')as opdb:
            tmp = json.load(opdb)
            print ('UKT 1 Semester Rp 4.500.000')
            inputan = int(input('masukkan no mahasiswa : '))
            inp1 = int(input('Nominal Uang Yang dibayarkan : '))
            rumus = inp1 - 4500000
            if inp1 >= 4500000:
                print('kembalian =', rumus)
                tmp [inputan][arg1]="lunas"
            else:
                print ('uang yang dibayarkan kurang dari nominal')
        with open('db.json', 'w') as f:
            f.write(json.dumps(tmp))
        inp = input('apakah masih ada lagi? [y/t]').lower()
        if inp == 'y':
            continue
        elif inp == 't':
            break 
        else:
            print('keyword error')
def tambah():
    while True:
        os.system('cls')
        loaddatassw()
        nama = input('masukkan nama : ')
        nim = input('masukkan nim : ')
        tmp = {"nama":nama,"nim":nim,"st1":"Belum Lunas","st2":"Belum Lunas","st3":"Belum Lunas","st4":"Belum Lunas","st5":"Belum Lunas","st6":"Belum Lunas","st7":"Belum Lunas","st8":"Belum Lunas",}
        with open ('db.json','r')as crjs:
            sem = json.load(crjs)
        sem.append(tmp)    
        with  open ('db.json','w') as crjs :
            json.dump(sem,crjs)
        loaddatassw()
        inps = input('apakah ada lagi ? [y/t] ')
        if inps == 'y':
            continue
        elif inps == 't':
            break
        else:
            print('keyword error')
def hapus():
    while True:
        os.system('cls')
        loaddatassw()
        inputan = int(input('masukkan no mahasiswa : '))
        with open ('db.json','r') as ldb :
            tmp = json.load(ldb)
        tmp.pop(inputan)
        with open ('db.json','w') as delete :
            json.dump(tmp,delete)
        loaddatassw()   
        inps = input('apakah ada lagi ? [y/t] ')
        if inps == 'y':
            continue
        elif inps == 't':
            break
        else:
            print('keyword error')
def menu(arg1):
    print ('proses .......')
    time.sleep(1)
    os.system('cls')
    while True :
        os.system('cls')
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
            pembayaran(arg1)
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
menuawal()