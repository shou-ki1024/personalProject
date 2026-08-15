
import shutil
import sys

ascii_art = """
        ██╗      ██████╗  ██████╗██╗  ██╗    ██╗███╗   ██╗██╗██╗██╗           
        ██║     ██╔═══██╗██╔════╝██║ ██╔╝    ██║████╗  ██║██║██║██║           
        ██║     ██║   ██║██║     █████╔╝     ██║██╔██╗ ██║██║██║██║           
        ██║     ██║   ██║██║     ██╔═██╗     ██║██║╚██╗██║╚═╝╚═╝╚═╝           
        ███████╗╚██████╔╝╚██████╗██║  ██╗    ██║██║ ╚████║██╗██╗██╗           
        ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝    ╚═╝╚═╝  ╚═══╝╚═╝╚═╝╚═╝           
                                                                              
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗███████╗██████╗ ██╗██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝██╔════╝██╔══██╗██║██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗█████╗  ██████╔╝██║██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║██╔══╝  ██╔══██╗╚═╝╚═╝
   ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║███████╗██║  ██║██╗██╗
   ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝


"""

def cetak_ascii_responsif(art):
    # Ambil lebar terminal saat ini
    lebar_terminal = shutil.get_terminal_size().columns
    
    # Pecah ASCII art menjadi baris-baris terpisah
    baris_art = art.splitlines()
    
    # Cari tahu berapa lebar (jumlah karakter) baris terpanjang dari ASCII art Anda
    lebar_art_maksimal = max(len(baris) for baris in baris_art) if baris_art else 0
    
    # Cek apakah terminal cukup luas untuk menampilkan ASCII art
    if lebar_art_maksimal > lebar_terminal:
        # Jika terminal terlalu kecil, Anda bisa mengecilkan teks atau memberi peringatan
        print("[Peringatan: Terminal terlalu kecil untuk menampilkan ASCII art]\n")
        # Tetap cetak apa adanya (atau potong jika terpaksa)
        for baris in baris_art:
            print(baris[:lebar_terminal])
    else:
        # Hitung sisa ruang kosong dan bagi 2 untuk mendapatkan margin kiri (agar presisi di tengah)
        margin_kiri = (lebar_terminal - lebar_art_maksimal) // 2
        spasi_pembatas = " " * margin_kiri
        
        # Cetak setiap baris ASCII art dengan tambahan margin di kirinya
        for baris in baris_art:
            print(spasi_pembatas + baris)

# Jalankan fungsi
cetak_ascii_responsif(ascii_art)
