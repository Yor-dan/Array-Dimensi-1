from prettytable import PrettyTable
index = []
value = []
emarr = []

def intro():
    menu = PrettyTable()
    menu.title = (f"Program Array Dimensi 1")
    menu.field_names = ([f"No.", f"======= Menu ======="])
    menu.add_rows(
        [
            [f"1.", f"Buat Array"],
            [f"2.", f"Tampilkan Array"],
            [f"3.", f"Nilai Max dan Min"],
            [f"4.", f"Cari Index atau Nilai"],
            [f"5.", f"Penjumlahan"],
            [f"6.", f"Pengurangan"],
            [f"7.", f"Modifikasi Array"],
            [f"0.", f"Keluar"],
        ]
    )
    menu.align = "l"
    print(menu)
   
def utama():
    intro()
    pth = input(f"Pilih Menu: ")
    if pth == f"1":
        arr()
    elif pth == f"2":
        tmp()
    elif pth == f"3":
        mix()
    elif pth == f"4":
        sch()
    elif pth == f"5":
        total()
    elif pth == f"6":
        kurang()
    elif pth == f"7":
        mdf()
    elif pth == f"0":
        cls()
    else:
        err()
        restart()

def restart():
    res = input(f"\nKembali ke Menu? (y/n): ")
    if res == f"y":
        utama()
    elif res == f"n":
        cls()
    else:
        err()
        restart()

def are():
    lp = 0
    if index[0] != 0:
        index[0] = 0

    for i in index[1:]:
        lp += 1
        if i - index[lp-1] != 1:
            index[i-1] = index[lp-1] + 1

def arr():
    try:
        itr = int(input(f"\nJumlah Index: "))
        spc()
        for i in range(0,itr):
            nilai = input(f"Masukkan Nilai Index ke {i}: ")
            x = int(i)
            y = int(nilai)
            index.append(x)
            value.append(y)
        print(f"\nArray Berhasil Dibuat!")
    except ValueError:
        err()

    restart()

def tmpb():
    if index == emarr:
        emy()
    else:
        lp = 0
        spc()
        tbl = PrettyTable([f"No.", f"Index", f"Nilai"])
        for i in index:
            lp += 1
            tbl.add_row([lp, index[i], value[i]])
        print(tbl)

def tmp():
    tmpb()
    restart()

def mix():
    spc()
    if index == emarr:
        emy()
    else:
        h = max(value)
        inx = value.index(h)
        l = min(value)
        inv = value.index(l)
        if h == l:
            print(f"Nilai Index Sama Rata! = {h}")
        else:
           print(f"Nilai Tertinggi: {h} berada pada Index: {inx}")
           print(f"Nilai Terendah: {l} berada pada Index: {inv}")

    restart()
    
def sch():
    if index == emarr:
        emy()
    else:
        find = False
        tsch = PrettyTable([f"Index", f"Nilai"])
        src = input(f"\nCari Index atau Nilai? (i/n): ")
        
        if src == f"i":
            try:
                ix = int(input(f"\nMasukan Index: "))
                if ix in index:
                    for i in index:
                        if ix == i:
                            tsch.add_row([index[i], value[i]])
                    print(tsch)
                else:
                    print(f"\nIndex Tidak Ditemukan!")
            except ValueError:
                err()

        elif src == f"n":
            try:
                inm = int(input(f"\nMasukan Nilai: "))
                for i in index:
                    if value[i] == inm:
                        find = True
                        tsch.add_row([i, inm])
                if find:
                    print(tsch)
                else:
                    print(f"\nNilai Tidak Ditemukan!")
            except ValueError:
                err()
                
        else:
            err()

    restart()

def total():
    if index == emarr:
        emy()
    else:
        ttbl = PrettyTable()
        ttbl.title = f"Penjumlahan"
        ttbl.field_names = ([f"No", f"===== Menu ====="])
        ttbl.add_rows(
            [
                [f"1.", f"Jumlah (n) Index"],
                [f"2.", f"Total"],
                [f"0.", f"Kembali"],
            ]
        )
        ttbl.align = f"l"
        print(ttbl)
        pnj_pth = input(f"Pilih Menu: ")

        if pnj_pth == f"1":
            fp = False
            ipj = []
            npj = []
            nipj = []
            try:
                j_i = int(input(f"\nMasukan Jumlah Index: "))
                if j_i < 1:
                    err()
                else:
                    tmpb()
                    for i in range(0,j_i):
                        try:
                            trj = int(input(f"Masukan Index: "))
                            if trj in index:
                                fp = True
                                ipj.append(trj)
                                npj.append(value[trj])
                            else:
                                fp = False
                                print(f"\nIndex Tidak Ditemukan!")
                                break
                        except ValueError:
                            err()
                    if fp:
                        for i in ipj:
                            i = str(i)
                            i = f"Index({i})"
                            nipj.append(i)
                        spc()
                        print(*nipj, sep = " + ")
                        print(*npj, sep = " + ")
                        print(f"= {sum(npj)}")
            except ValueError:
                err()

        elif pnj_pth == f"2":
            tot = sum(value)
            print(f"\nTotal Penjumlahan Seluruh Nilai Array: \n= {tot}")

        elif pnj_pth == f"0":
            utama()

        else:
            err()

    restart()

def kurang():
    if index == emarr:
        emy()
    else:
        ttbl = PrettyTable()
        ttbl.title = f"Pengurangan"
        ttbl.field_names = ([f"No", f"======= Menu ======="])
        ttbl.add_rows(
            [
                [f"1.", f"Pengurangan (n) Index"],
                [f"2.", f"Total Pengurangan"],
                [f"0.", f"Kembali"],
            ]
        )
        ttbl.align = f"l"
        print(ttbl)
        pnj_pth = input(f"Pilih Menu: ")

        if pnj_pth == f"1":
            fp = False
            ipp = []
            npp = []
            nipp = []
            try:
                p_i = int(input(f"\nMasukan Jumlah Index: "))
                if p_i < 1:
                    err()
                else:
                    tmpb()
                    for i in range(0,p_i):
                        try:
                            trj = int(input(f"Masukan Index: "))
                            if trj in index:
                                fp = True
                                ipp.append(trj)
                                npp.append(value[trj])
                            else:
                                fp = False
                                print(f"\nIndex Tidak Ditemukan!")
                                break
                        except ValueError:
                            err()
                    if fp:
                        for i in ipp:
                            i = str(i)
                            i = f"Index({i})"
                            nipp.append(i)
                        spc()
                        print(*nipp, sep = f" - ")
                        print(*npp, sep = f" - ")
                        print(f"= {npp[0] - sum(npp[1:])}")
            except ValueError:
                err()

        elif pnj_pth == f"2":
            top = value[0] - sum(value[1:])
            print(f"\nTotal Pengurangan Seluruh Nilai Array: \n= {top}")

        elif pnj_pth == f"0":
            utama()

        else:
            err()

    restart()

def mdf():
    if index == emarr:
        emy()
    else:
        mtbl = PrettyTable()
        mtbl.title = f"Modifikasi Array"
        mtbl.field_names = ([f"No.", f"=== Menu ==="])
        mtbl.add_rows(
            [
                [f"1.", f"Tambah Index"],
                [f"2.", f"Hapus Index"],
                [f"3.", f"Hapus Array"],
                [f"0.", f"Kembali"],
            ]
        )
        mtbl.align = f"l"
        spc()
        print(mtbl)
        mdf_pth = input(f"Pilih Menu: ")

        if mdf_pth == f"1":
            try:
                nk = int(input(f"\nJumlah Index Baru: "))
                tmpb()
                spc()
                for i in range(0,nk):
                    i = int(i)
                    while i in index:
                        i += 1
                    else:
                        index.append(i)
                        nv = int(input(f"Masukan Nilai Index ke {i}: "))
                        index[i] = i
                        value.append(nv)
                print(f"\nIndex Baru Berhasil Ditambahkan!")
            except ValueError:
                err()

        elif mdf_pth == f"2":
            tmpb()
            try:
                hix = int(input(f"Hapus Index: "))
                if hix in index:
                    index.remove(hix)
                    value.remove(value[hix])
                    print(f"\nIndex Berhasil Dihapus")
                    if len(index) > 0:
                        are()
                else:
                    print(f"\nIndex Tidak Ditemukan!")
            except ValueError:
                err()

        elif mdf_pth == f"3":
            index.clear()
            value.clear()
            print(f"\nArray Dihapus!")

        elif mdf_pth == f"0":
            utama()

        else:
            err()

    restart()

def emy():
    print(f"\nArray Kosong!")

def err():
    print(f"\nInput Tidak Valid!")

def cls():
    print(f"\nProgram Ditutup!")

def spc():
    print(f"")

utama()