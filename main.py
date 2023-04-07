class Transaction:
        
    def __init__(self):
        self.tabel = []


    def add_item(self, nama_item=0, jumlah_item=0, harga_item=0):
        """method untuk menambahkan serta menampilkan item yang dibeli

        parameter:
        nama_item(str) = nama item yang dibeli
        jumlah_item(int) = jumlah item yang dibeli
        harga_item(int) = harga item per item yang dibeli

        hasil:
        isi dari parameter dimasukan pada variabel pembelian_dengan_harga.
        variabel pembelian_dengan_harga di tambahkan pada atribut self.tabel.
        menampilkan item yang dibeli
        """
        pembelian_dengan_harga = [nama_item, jumlah_item, harga_item, jumlah_item*harga_item]

        self.tabel.append(pembelian_dengan_harga)

        self.tabel_tanpa_harga = [(data[0],data[1],data[2]) for data in self.tabel]

        print(f"Item yang dibeli {self.tabel_tanpa_harga}")


    def update_item_name(self, nama_item, update_nama_item):
        """method untuk mengganti nama item

        parameter:
        nama_item(str) = nama item yang ingin diganti
        update_nama_item(str) = nama item baru yang ingin dimasukkan

        hasil:
        menampilkan tabel dengan setelah update nama item
        """
        for i in self.tabel:
            if i[0] == nama_item:
                i[0] = update_nama_item
                print("update nama item berhasil")
                self.check_order()
    
    def update_item_qty(self, nama_item, update_jumlah_item):
        """method untuk mengganti jumlah item

        parameter:
        nama_item(str) = nama item yang dari jumlah item ingin diganti
        update_jumlah_item(int) = jumlah item baru yang ingin dimasukkan

        hasil:
        menampilkan tabel dengan setelah update jumlah item
        """
        for i in self.tabel:
            if i[0] == nama_item:
                i[1] = update_jumlah_item
                i[3] = update_jumlah_item*i[2]
        print("update jumlah item berhasil")
        self.check_order()

    def update_item_price(self, nama_item, update_harga_item):
        """method untuk mengganti harga item

        parameter:
        nama_item(str) = nama item yang dari harga item ingin diganti
        update_harga_item(int) = jumlah harga item baru yang ingin dimasukkan

        hasil:
        menampilkan tabel dengan setelah update harga item
        """
        for i in self.tabel:
            if i[0] == nama_item:
                i[2] = update_harga_item
                i[3] = update_harga_item*i[1]
        print("update harga item berhasil")
        self.check_order()

    def delete_item(self, nama_item):
        """method untuk menghapus salah satu item

        parameter:
        nama_item(str) = baris dari item pembelian yang ingin dihapus

        hasil:
        menampilkan tabel dengan setelah menghapus salah satu item pembelian
        """
        for i in self.tabel:
            if i[0]== nama_item:
                self.tabel.remove(i)
        self.check_order()
        print('\n')

    def reset_transaction(self):
        """method untuk menghapus seluruh item pembelian

        hasil:
        menampilkan tabel setelah dihapus secara keseluruhan
        """
        self.tabel.clear()
        self.check_order()
        print('Semua item berhasil di delete!')
        print('\n')

    def check_order(self):
        """method untuk mengecek apakah ada kekosongan input
        fungsi untuk menampilkan tabel item pembelian

        hasil:
        menampilkan hasil pengecekan
        menampilkan tabel item pembelian
        """
        try:
            for i in self.tabel:
                if (i[0]==0) or (i[1]==0) or (i[2]==0):
                    raise Exception("Terdapat Kesalahan input data")
            from tabulate import tabulate
            print(tabulate(self.tabel, headers=["item", "jumlah item", "harga/item", "harga_total"]))
            print("\n") 
            
        except Exception as e:
            print(e)
            
    def total_price(self):
        """method untuk menghitung total harga setelah diberi potongan diskon

        hasil:
        menampilkan item pembelian beserta total harga setelah dipotong diskon
        """
        item = [(i[0], i[1], i[2]) for i in self.tabel]
        print(f'item yang dibeli {item}')
        total = sum([harga[3] for harga in self.tabel])
       
        if total <= 200_000:
            total_harga = total*1
            print(f'total belanja yang harus dibayarkan Rp. {float(total_harga)}')
            print('\n')
        elif total <= 300_000:
            total_harga = total*0.95
            print("anda mendapat diskon sebesar 5%")
            print(f'total belanja yang harus dibayarkan Rp. {float(total_harga)}')
            print('\n')
        elif total <= 500_000:
            print("anda mendapat diskon sebesar 8%")
            total_harga = total*0.92
            print(f'total belanja yang harus dibayarkan Rp. {float(total_harga)}')
            print('\n')
        else:
            total_harga = total*0.9
            print("anda mendapat diskon sebesar 10%")
            print(f'total belanja yang harus dibayarkan Rp. {float(total_harga)}')
            print('\n')
    






















