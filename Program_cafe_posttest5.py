list_menu = {'menu' : "Nasi goreng : Rp 15.000",
             "menu2" : "Ayam kremes : Rp 17.000",
             "menu3" : "Mie ayam : Rp 13.000",
             "menu4" : "Bakso : Rp 13.000",
             "menu5" : "Soto ayam : Rp 12.000",
             "menu6" : "Es teh : Rp 5.000",
             "menu7" : "Teh hangat : Rp 5.000",
             "menu8" : "Es jeruk : Rp 7.000",
             "menu9" : "Jeruk hangat :  7.000"
             }
#'''
def tampil():
    index = 1
    for mmenu in list_menu :
        print(str(index)+". " + list_menu[mmenu])
        index= index+1


def tambah():
    mmenu = input("masukkan menu yang ingin ditambahkan: ")
    list_menu.update({'menu10':mmenu})
    tampil()

def ubah():
    tampil()
    urutan = int(input("masukkan index: "))
    menu_baru = input("masukkan menu baru: ")
    if urutan == 1:
            list_menu['menu'] = menu_baru
            tampil()
    if urutan == 2:
            list_menu['menu'] = menu_baru
            tampil()
    if urutan == 3:
            list_menu['menu'] = menu_baru
            tampil()
    if urutan == 4:
            list_menu['menu'] = menu_baru
            tampil()
    if urutan == 5:
            list_menu['menu'] = menu_baru
            tampil()
    if urutan == 6:
            list_menu['menu'] = menu_baru
            tampil()
    if urutan == 7:
            list_menu['menu'] = menu_baru
            tampil()
    if urutan == 8:
            list_menu['menu'] = menu_baru
            tampil()
    if urutan == 9:
            list_menu['menu'] = menu_baru
            tampil()
    if urutan == 10:
            list_menu['menu'] = menu_baru
            tampil()
    else:
        print("angka yang anda masukkan salah!")

        

def hapus():
    tampil()
    urutan = int(input("masukkan index: "))
    if urutan == 1:
        del list_menu['menu']
        tampil()
    elif urutan == 2:
        del list_menu['menu']
        tampil()
    elif urutan == 3:
        del list_menu['menu']
        tampil()
    elif urutan == 4:
        del list_menu['menu']
        tampil()
    elif urutan == 5:
        del list_menu['menu']
        tampil()
    elif urutan == 6:
        del list_menu['menu']
        tampil()
    elif urutan == 7:
        del list_menu['menu']
        tampil()
    elif urutan == 8:
        del list_menu['menu']
        tampil()
    elif urutan == 9:
        del list_menu['menu']
        tampil()
    elif urutan == 10:
        del list_menu['menu']
        tampil()
    else:
        print("angka yang anda masukkan salah!")



def menu():
    print("==========================")
    print("[1] Tampilkan menu")
    print("[2] Tambah menu")
    print("[3] Ubah menu")
    print("[4] Hapus menu")
    print("[5] Keluar")
    print("==========================")

    kode = input("masukan kode: ")
    if kode == "1":
        tampil()
    elif kode == "2":
        tambah()
    elif kode == "3":
        ubah()
    elif kode == "4":
        hapus()
    elif kode == "5":
        print("Terima kasih!")
    else :
        print("kode yang anda masukkan salah!")

while(True):
    menu()





