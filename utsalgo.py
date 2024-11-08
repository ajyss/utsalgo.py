from datetime import datetime

class Barang:
    def __init__(self, kode, nama, harga):
        self.kode = kode
        self.nama = nama
        self.harga = harga

class ItemKeranjang:
    def __init__(self, barang, jumlah):
        self.barang = barang
        self.jumlah = jumlah
        self.subtotal = barang.harga * jumlah

class Keranjang:
    def __init__(self):
        self.items = []
        
    def tambah_barang(self, barang, jumlah):
        # Cek apakah barang sudah ada di keranjang
        for item in self.items:
            if item.barang.kode == barang.kode:
                item.jumlah += jumlah
                item.subtotal = item.barang.harga * item.jumlah
                return
        
        # Jika barang belum ada, tambahkan sebagai item baru
        item_baru = ItemKeranjang(barang, jumlah)
        self.items.append(item_baru)
    
    def tampilkan_daftar(self):
        print("\nDaftar Belanja:")
        print("=" * 50)
        print("Kode\tNama\t\tHarga\tJumlah\tSubtotal")
        print("-" * 50)
        for item in self.items:
            print(f"{item.barang.kode}\t{item.barang.nama}\t\t{item.barang.harga}\t{item.jumlah}\t{item.subtotal}")
    
    def hitung_total(self):
        return sum(item.subtotal for item in self.items)

class Kasir:
    def __init__(self):
        self.keranjang = Keranjang()
        # Daftar barang yang tersedia (simulasi database)
        self.daftar_barang = {
            "01": Barang("01", "Beras 1kg", 15000),
            "02": Barang("02", "Gula 1 kg", 7000),
            "03": Barang("03", "Minyak 2 liter", 20000),
            "04": Barang("01", "Obat nyamuk 1 pack", 5000),
            "05": Barang("02", "Golda Coffe", 3000),
            "06": Barang("03", "Air Mineral", 3700),
            "07": Barang("01", "Cocacola", 5000),
            "08": Barang("02", "Pocari Sweat", 6000),
            "09": Barang("03", "Sprite", 5000),
        }
    
    def tambah_ke_keranjang(self, kode_barang, jumlah):
        if kode_barang in self.daftar_barang:
            barang = self.daftar_barang[kode_barang]
            self.keranjang.tambah_barang(barang, jumlah)
            print(f"Berhasil menambahkan {jumlah} {barang.nama} ke keranjang")
        else:
            print("Barang tidak ditemukan!")
    
    def cetak_struk(self):
        print("\n" + "=" * 50)
        print("STRUK BELANJA")
        print("Tanggal:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("=" * 50)
        
        self.keranjang.tampilkan_daftar()
        
        total = self.keranjang.hitung_total()
        print("-" * 50)
        print(f"Total Belanja: Rp {total}")
        print("=" * 50)
        print("Terima kasih telah berbelanja!")
        print("=" * 50)

# Contoh penggunaan
def main():
    kasir = Kasir()
    
    while True:
        print("\nMenu:")
        print("1. Tambah Barang")
        print("2. Lihat Keranjang")
        print("3. Cetak Struk")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == "1":
            print("\nDaftar Barang Tersedia:")
            for kode, barang in kasir.daftar_barang.items():
                print(f"{kode} - {barang.nama} (Rp {barang.harga})")
            kode = input("Masukkan kode barang: ")
            jumlah = int(input("Masukkan jumlah: "))
            kasir.tambah_ke_keranjang(kode, jumlah)
            
        elif pilihan == "2":
            kasir.keranjang.tampilkan_daftar()
            print(f"Total: Rp {kasir.keranjang.hitung_total()}")
            
        elif pilihan == "3":
            kasir.cetak_struk()
            
        elif pilihan == "4":
            print("Terima kasih!")
            break
            
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()