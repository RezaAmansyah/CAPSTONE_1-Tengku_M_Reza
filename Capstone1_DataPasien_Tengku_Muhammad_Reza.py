import os 
import datetime as dt
import openpyxl
import csv
from tabulate import tabulate
sistem_operasi = os.name

match sistem_operasi:
    case 'nt':os.system('cls')


database = {
    'P001' : {
        'nama':'Ahmad Sauri',
        'usia':37,
        'gender':'Pria',
        'tujuan':'Poli Umum',
        'penyakit':'Diabetes',
        'tanggal_daftar':dt.date(2023,8,15)        
    },
    'P002' : {
        'nama':'Fatima Dewi',
        'usia':23,
        'gender':'Wanita',
        'tujuan':'Poli Gigi',
        'penyakit':'Sakit Gigi',
        'tanggal_daftar':dt.date(2023,8,11)
    },
    'P003':{
        'nama':'Sultan La Ode',
        'usia':13,
        'gender':'Pria',
        'tujuan':'Poli Anak',
        'penyakit':'Demam',
        'tanggal_daftar':dt.date(2023,9,23)
    },
    'P004':{
        'nama':'Alexander Graham Bell',
        'usia':53,
        'gender':'Pria',
        'tujuan': None,
        'penyakit':'Demam',
        'tanggal_daftar':dt.date(2023,9,23)
    }
}

#-------------------function------------------



#-------------------------------Read Function--------------------------------
def main_read():


    while True:
        try:
            print('='*80)
            print(f'{"Lihat Report Data Passien":^80}')
            print('='*80)
            print('Silahkan Pilih Jenis Report')
            print(f'1. Lihat Report Seluruh Data\n2. Report Data Tertentu\n3. Filter Data Pasien')
            print('4. Sorting Data Pasien\n5. Mencari Data Yang terdapat Kolom Yang Kosong')

            user_main_read = input('Silahkan Input (1-5) e untuk kembali ke menu utama: ').lower()
            if user_main_read == '1':
                read_all()
            elif user_main_read == '2':
                read_one(database)
            elif user_main_read == '3':
                main_filter()
            elif user_main_read == '4':
                sorting_pasien()
            elif user_main_read == '5':
                read_null_data()
            elif user_main_read == 'e':
                print('Program Report Data Pasien Selesai')
                break
            else:
                print('Input Tidak Valid')
                
           
        except Exception as e:
            print('User Input Tidak Valid',e)

def read_all():
    '''
    Fungsi ini untuk membaca seluruh data dalam tabel
    '''

    table_data = []
    for key,value in database.items():

        ID = key

        NAMA = value['nama']
        USIA = value['usia']
        GENDER = value['gender']
        TUJUAN = value['tujuan']
        PENYAKIT = value['penyakit']
        TANGGAL = value['tanggal_daftar']
        table_data.append([ID,NAMA,USIA,GENDER,TUJUAN,PENYAKIT,TANGGAL])

    print(tabulate(table_data, headers=['ID', 'Nama', 'Usia', 'Gender', 'Tujuan', 'Penyakit', 'Tanggal Daftar'],
               tablefmt='fancy_grid')) #jika ingin menggunakan streamlit = st.table


         
def read_one(database):
    '''
    Fungsi ini membaca hanya satu data saja berdasarkan ID yang dimasukkan pengguna
    '''
    print('='*80)
    print('Silahkan Cari Data Pasien Berdasarkan [ID/Nama/Poli] [1/2/3]: ')
    print('='*80)
    # read_all()

    user_read = input('Silahkan Pilih (ID/Nama/Poli) (1/2/3) : ').lower() #input user untuk mencari data pasien
    if user_read == '1': #if untuk ID
        user_id_pasien = input('Silahkan Masukan ID Pasien: ').title() #input user untuk mencari ID
        for key, value in database.items():
            if user_id_pasien == key:
                ID = key
                NAMA = value['nama']
                USIA = value['usia']
                GENDER = value['gender']
                TUJUAN = value['tujuan']
                PENYAKIT = value['penyakit']
                TANGGAL = value['tanggal_daftar']
                data = [[ID, NAMA, USIA, GENDER, TUJUAN, PENYAKIT, TANGGAL]]
                print(tabulate(data, headers=['ID', 'Nama', 'Usia', 'Gender', 'Tujuan', 'Penyakit', 'Tanggal Daftar'],
                               tablefmt='fancy_grid'))
                break
        else:
            print('Data Pasien Tidak Ada')
    
    elif user_read =='2':
        nama_pasien = input('Silahkan Masukan Nama Pasien: ').title() #input user untuk mencari nama
        for key, value in database.items():
            if nama_pasien == value['nama']:
                ID = key
                NAMA = value['nama']
                USIA = value['usia']
                GENDER = value['gender']
                TUJUAN = value['tujuan']
                PENYAKIT = value['penyakit']
                TANGGAL = value['tanggal_daftar']
                data = [[ID, NAMA, USIA, GENDER, TUJUAN, PENYAKIT, TANGGAL]]
                print(tabulate(data, headers=['ID', 'Nama', 'Usia', 'Gender', 'Tujuan', 'Penyakit', 'Tanggal Daftar'],
                               tablefmt='fancy_grid'))
                break
        else:
            print('Data Pasien Tidak Ada')
    
    elif user_read == '3':
        
        print('='*80)
        print('1. Poli Umum | 2. Poli Anak | 3. Poli Gigi | 4. Poli Obgin | 5. Poli Bedah')
        print('='*80)
        poli_pasien = input('Silahkan Masukan Poli Tujuan: ')   
        data_poli = {
            '1' : 'Poli Umum',
            '2' : 'Poli Anak',
            '3' : 'Poli Gigi',
            '4' : 'Poli Obgin',
            '5' : 'Poli Bedah'
        }
        # if poli_pasien not in ['1','2','3','4','5']:
        #     print('Tidak Ada poli Yang di sebutkan')
        #     print('Masukan Poli Yang Benar')
        found = False    
        data_kosong = []
        poli_pasien = data_poli[poli_pasien]
        for ID, value in database.items():
            if poli_pasien == value['tujuan']:
                found = True
                poli = [ID]+list(value.values())
                data_kosong.append(poli)
                print(tabulate(data_kosong,headers=['ID', 'Nama', 'Usia', 'Gender', 'Tujuan', 'Penyakit', 'Tanggal Daftar'],
                               tablefmt='fancy_grid'))
        if not found:
            print('Data Tidak Di Temukan')
                




def read_null_data():
    '''
    Fungsi untuk mencari null value
    '''

    print('='*80)

    print(f"{'Program Untuk Mencari Kolom Null':^80}")
    user_null = input('Apakah Anda Ingin Mencari Data Dengan nilai kosong (y/n) : ').lower()
    if user_null == 'y':

        for ID, value in database.items():
            for id_nested, value_nested in value.items():
                null_data = []
                if value_nested is None:
                    null_data.append([ID,value['nama'],value['usia'],
                                      value['gender'],value['tujuan'],value['penyakit'],value['tanggal_daftar']])
                    print(tabulate(null_data, headers=['ID', 'Nama', 'Usia', 'Gender', 'Tujuan', 'Penyakit', 'Tanggal Daftar'],
                                   tablefmt='fancy_grid')) 
#----------------------------------Filter Function-----------------------------------------#
def main_filter():
    while True:
        try:
            print('='*80)
            print(f'{"Filter Data Passien":^80}')
            print('='*80)
            print('Silahkan Pilih Jenis Filter')
            print(f'1. Filter Berdasarkan Gender\n2. Filter Berdasarkan Umur')


            user_main_filter = input('Silahkan Input (1-2) e untuk kembali ke Report Data Pasien: ').lower()
            if user_main_filter == '1':
                filter_gender(database)
            elif user_main_filter == '2':
                filter_umur(database)
            elif user_main_filter == 'e':
                print('Program Filter Data Pasien Selesai')
                break
            else:
                print('Input Tidak Valid')

        except Exception as e:
            print('User Input Tidak Valid',e)

def filter_gender(database):
    '''
    Fungsi Filter Dengan Gender
    '''
    while True:
        print('='*80)
        user_filter = input('Silahkan Masukan Gender (pria/wanita): ')
        print('='*80)

        filtered_data = []
        gender_found = False
        for key, value in database.items():
            ID = key
            NAMA = value['nama']
            USIA = value['usia']
            GENDER = value['gender']
            TUJUAN = value['tujuan']
            PENYAKIT = value['penyakit']
            TANGGAL = value['tanggal_daftar']

            if user_filter.lower() == GENDER.lower():  # Membandingkan gender secara case-insensitive
                filtered_data.append([ID, NAMA, USIA, GENDER, TUJUAN, PENYAKIT, TANGGAL])
                gender_found = True

        if filtered_data:
            print(tabulate(filtered_data, headers=['ID', 'Nama', 'Usia', 'Gender', 'Tujuan', 'Penyakit', 'Tanggal Daftar'],
                           tablefmt='fancy_grid'))
            break
        else:
            print('Gender Tidak Ditemukan/Penulisan Salah')
        is_done = input('Apakah anda ingin mengkahiri filter gender(y/n): ').lower()
        if is_done == 'y':
            print('Program Selesai Terima Kasih')
        

def filter_umur(database):
    '''
    Fungsi Filter Terhadap umur
    '''
    while True:
        print('='*80)
        print('Filter Pasien Berdasarkan Umur (1. Di Atas 50 | 2. Di Bawah 50)')
        user_filter = input('Silahkan Masukan Pilihan Anda (1 | 2): ')
        print('='*80)
        filtered_data = []
        if user_filter == '1':
            for key, value in database.items():
                ID = key
                NAMA = value['nama']
                USIA = value['usia']
                GENDER = value['gender']
                TUJUAN = value['tujuan']
                PENYAKIT = value['penyakit']
                TANGGAL = value['tanggal_daftar']

                if value['usia'] >= 50:
                    # print('Program Bisa')
                    filtered_data.append([ID, NAMA, USIA, GENDER, TUJUAN, PENYAKIT, TANGGAL])
            print(tabulate(filtered_data, headers=['ID', 'Nama', 'Usia', 'Gender', 'Tujuan', 'Penyakit', 'Tanggal Daftar'],
                   tablefmt='fancy_grid'))
            break
        elif user_filter == '2':
            for key, value in database.items():
                ID = key
                NAMA = value['nama']
                USIA = value['usia']
                GENDER = value['gender']
                TUJUAN = value['tujuan']
                PENYAKIT = value['penyakit']
                TANGGAL = value['tanggal_daftar']

                if value['usia'] < 50:
                    # print('Program Bisa')
                    filtered_data.append([ID, NAMA, USIA, GENDER, TUJUAN, PENYAKIT, TANGGAL])
            print(tabulate(filtered_data, headers=['ID', 'Nama', 'Usia', 'Gender', 'Tujuan', 'Penyakit', 'Tanggal Daftar'],
                   tablefmt='fancy_grid'))
            break

        else:
            print('Input Tidak Valid')

        is_done = input('Apakah Anda Ingin Mengakhiri Program (y/n): ').lower()
        if is_done == 'y':
            print('Program Selesai Terima Kasih')
        


#----------------------------------Create Function-----------------------------------------#
def main_create():


    while True:
        try:
            print('='*80)
            print(f"{'Menu Tambah Data Pasien':^80}")
            print('='*80)
            print('Silahkan Pilih Jenis Tambah')
            print(f'1. Tambah Satu Data\n2. Tambah Banyak Data\n3. Sorting Data Pasien')
            print('4. Filter Data Pasien')
            user_main_create = input('Silahkan Input (1-4) e untuk kembali ke menu utama: ')
            if user_main_create == '1':
                create_one()
            elif user_main_create == '2':
                create_many(database)
            elif user_main_create == '3':
                sorting_pasien()
            elif user_main_create == '4':
                main_filter()
            elif user_main_create == 'e':
                print('Program Report Data Pasien Selesai')
                break
            else: 
                print('Input Tidak Valid')


        except Exception as e:
            print('User Input Tidak Valid',e)
            
        

def create_one():
    '''
    Fungsi untuk menambahkan satu Data Pasien
    '''
    while True:
        table_data = []
        for key,value in database.items():
            ID = key
            NAMA = value['nama']
            USIA = value['usia']
            GENDER = value['gender']
            TUJUAN = value['tujuan']
            PENYAKIT = value['penyakit']
            TANGGAL = value['tanggal_daftar']
            table_data.append([ID,NAMA,USIA,GENDER,TUJUAN,PENYAKIT,TANGGAL])
        print(tabulate(table_data, headers=['ID', 'Nama', 'Usia', 'Gender', 'Tujuan', 'Penyakit', 'Tanggal Daftar'],
               tablefmt='fancy_grid'))

        database_template = {

            'nama':'nama panjang',
            'usia':00,
            'gender':'JK',
            'tujuan':'poli',
            'penyakit':'sakit apa',
            'tanggal_daftar':dt.date(1111,1,11)
        }
        print('='*80)
        ID = input('Masukan ID Pasien: ').title()
        
        if ID in database:
            print(f'data pasien dengan ID {ID} Sudah ada')
            print('SIlahkan Masukan ID baru')
            continue
        else:
            data_kosong = dict.fromkeys(database_template.keys()) #template dictionary untuk mengambik keys nya saja 
            while True:  #while untuk validasi nama
                data_kosong['nama'] = input('Masukan Nama Pasien : ').title()

                if data_kosong['nama'].isdigit():
                    print('Nama Tidak Boleh Angka')
                    continue
                else:
                    data_kosong['nama'] = data_kosong['nama']
                    break
            while True: #while true untuk usia
                data_kosong['usia'] = (input('Masukan Usia Pasien : '))
                if data_kosong['usia'].isdigit():
                    data_kosong['usia'] = int(data_kosong['usia'])
                    break
                else:
                    print('Usia Pasien Harus Angka')
                    continue
            while True:    #while True untuk gender
                data_kosong['gender'] = input('Masukan Gender Pasien (pria/wanita): ').title()
                if data_kosong['gender'] not in ['Pria','Wanita']:
                    print('Input Untuk Gender Tidak Valid')
                    continue
                else:
                    data_kosong['gender'] = data_kosong['gender']
                    break
            while True:    #while Tru untuk Poli
                print(' Poli Umum | Poli Anak | Poli Gigi | Poli Obgin | Poli Bedah')
                data_kosong['tujuan'] = input('Masukan Poli tujuan Pasien: ').title()
                if data_kosong['tujuan'] not in ['Poli Umum','Poli Anak','Poli Gigi','Poli Obgin','Poli Bedah']:
                    print('Input untuk Poli Tidak Valid. Masukan input Seperti di Atas')
                    continue
                else:
                    data_kosong['tujuan'] = data_kosong['tujuan']
                    break
            while True:   #while True untuk Keluhan Pasien 
                data_kosong['penyakit'] = input('Masukan Keluhan/Penyakit Pasien: ').title()
                if data_kosong['penyakit'].isdigit():
                    print('Data Keluhan/Penyakit Pasien Tidak Boleh Angka')
                    continue
                else:
                    data_kosong['penyakit'] = data_kosong['penyakit']
                    break

            tanggal_daftar = input("Masukkan Tanggal Pendaftaran (YYYY-MM-DD): ")
            tahun, bulan, hari = map(int, tanggal_daftar.split('-'))
            tanggal_daftar = dt.date(tahun, bulan, hari)

            data_kosong['tanggal_daftar'] = tanggal_daftar

            save = input('Apakah Anda Mau menyimpan nya (y/n): ').lower()
            if save == 'y':
                database.update({ID:data_kosong})
                print('Data Sudah Di simpan') 
            else:
                print('Data Tidak Di Save')
                break
            read_all()
        is_done = input('Tekan 1 untuk mengakhiri program dan tombol apapun untuk tambah lagi: ')
        if is_done == '1':
            break

def create_many(database):
    '''
    Fungsi untuk menaambahkan beberapa data sekaligus dengan flow
    user di minta memasukan berapa banyak data yang akan di add
    
    '''
    table_data = []
    for key,value in database.items():
        ID = key
        NAMA = value['nama']
        USIA = value['usia']
        GENDER = value['gender']
        TUJUAN = value['tujuan']
        PENYAKIT = value['penyakit']
        TANGGAL = value['tanggal_daftar']
        table_data.append([ID,NAMA,USIA,GENDER,TUJUAN,PENYAKIT,TANGGAL])
    print(tabulate(table_data, headers=['ID', 'Nama', 'Usia', 'Gender', 'Tujuan', 'Penyakit', 'Tanggal Daftar'],
           tablefmt='fancy_grid'))
    print('='*80)
    jumlah_pasien = int(input("Berapa banyak data yang ingin Anda tambahkan? "))
    
    for i in range(jumlah_pasien):
        ID = input("Masukkan ID Pasien (contoh: P004): ").title()
        if ID in database:
            print('data Sudah ada')
            break
        nama = input("Masukkan Nama Pasien: ").title()
        if nama.isdigit():
            print('Input Data Tidak Valid')
            break
        usia = int(input("Masukkan Usia Pasien: "))
        gender = input("Masukkan Gender Pasien (Pria/Wanita): ").title()
        print(' Poli Umum | Poli Anak | Poli Gigi | Poli Obgin | Poli Bedah')
        tujuan = input("Masukan Poli tujuan Pasien: ").title()
        penyakit = input("Masukan Keluhan/Penyakit Pasien: ").title()
        tanggal_daftar = input("Masukkan Tanggal Pendaftaran (YYYY-MM-DD): ")
        tahun, bulan, hari = map(int, tanggal_daftar.split('-'))
        tanggal_daftar = dt.date(tahun, bulan, hari)
        

        save = input('Apakah Anda Mau menyimpan nya (y/n): ').lower()
        if save == 'y':
            database[ID] = {
            'nama': nama,
            'usia': usia,
            'gender': gender,
            'tujuan': tujuan,
            'penyakit': penyakit,
            'tanggal_daftar': tanggal_daftar
            }
            print('Data Sudah Di simpan') 
        else:
            print('Data Tidak Di Save')
        
    read_all()

#----------------------------------SORTING FUNCTION---------------------------------------
def sorting_pasien():
    '''
    fungsi untuk mengurutkan data pasien berdasarkan usia dan tanggal daftar
    '''
    while True:
        print('='*80)
        print('Silahkan Sorting Berdasarkan (Usia|Tanggal Daftar): ')
        print('='*80)

        user_sorting = input('Masukan Pilihan Anda (1. Usia | 2. Tanggal Daftar): ')
        if user_sorting == '1':
            print('Silahkan Urutkan Usia (1. Dari Termuda | 2. Dari Tertua): ')
            user_urut = input('Silahkan Masukan Inputan: ')
            if user_urut == '1': 
                sorted_database = dict(sorted(database.items(), key=lambda item: item[1]['usia']))

                # Menampilkan hasil pengurutan
                table_data = []
                for key,value in sorted_database.items():
                    ID = key
                    NAMA = value['nama']
                    USIA = value['usia']
                    GENDER = value['gender']
                    TUJUAN = value['tujuan']
                    PENYAKIT = value['penyakit']
                    TANGGAL = value['tanggal_daftar']
                    table_data.append([ID,NAMA,USIA,GENDER,TUJUAN,PENYAKIT,TANGGAL])
                print(tabulate(table_data, headers=['ID', 'Nama', 'Usia', 'Gender', 'Tujuan', 'Penyakit', 'Tanggal Daftar'],
                           tablefmt='fancy_grid'))
            elif user_urut == '2':
                sorted_database = dict(sorted(database.items(), key=lambda item: item[1]['usia'],reverse=True))

                # Menampilkan hasil pengurutan
                table_data = []
                for key,value in sorted_database.items():
                    ID = key
                    NAMA = value['nama']
                    USIA = value['usia']
                    GENDER = value['gender']
                    TUJUAN = value['tujuan']
                    PENYAKIT = value['penyakit']
                    TANGGAL = value['tanggal_daftar']
                    table_data.append([ID,NAMA,USIA,GENDER,TUJUAN,PENYAKIT,TANGGAL])
                print(tabulate(table_data, headers=['ID', 'Nama', 'Usia', 'Gender', 'Tujuan', 'Penyakit', 'Tanggal Daftar'],
                           tablefmt='fancy_grid'))

        elif user_sorting =='2':
            print('Silahkan Urutkan Tanggal Berdasarkan (1. Tanggal Terbaru | 2. Tanggal Terlampau)')
            user_tanggal = input('Silahkan Masukan Pilihan Anda: ')
            if user_tanggal == '1':
                sorted_database = dict(sorted(database.items(), key=lambda item: item[1]['tanggal_daftar'],reverse=True ))

                # Menampilkan hasil pengurutan
                table_data = []
                for key,value in sorted_database.items():
                    ID = key
                    NAMA = value['nama']
                    USIA = value['usia']
                    GENDER = value['gender']
                    TUJUAN = value['tujuan']
                    PENYAKIT = value['penyakit']
                    TANGGAL = value['tanggal_daftar']
                    table_data.append([ID,NAMA,USIA,GENDER,TUJUAN,PENYAKIT,TANGGAL])
                print(tabulate(table_data, headers=['ID', 'Nama', 'Usia', 'Gender', 'Tujuan', 'Penyakit', 'Tanggal Daftar'],
                           tablefmt='fancy_grid'))
            elif user_tanggal == '2':
                sorted_database = dict(sorted(database.items(), key=lambda item: item[1]['tanggal_daftar']))

                # Menampilkan hasil pengurutan
                table_data = []
                for key,value in sorted_database.items():
                    ID = key
                    NAMA = value['nama']
                    USIA = value['usia']
                    GENDER = value['gender']
                    TUJUAN = value['tujuan']
                    PENYAKIT = value['penyakit']
                    TANGGAL = value['tanggal_daftar']
                    table_data.append([ID,NAMA,USIA,GENDER,TUJUAN,PENYAKIT,TANGGAL])
                print(tabulate(table_data, headers=['ID', 'Nama', 'Usia', 'Gender', 'Tujuan', 'Penyakit', 'Tanggal Daftar'],
                           tablefmt='fancy_grid'))
            else:
                print('Tidak Ada Pilihan Tersebut')

        else:
            print('Input Tidak Valid Untuk Program Sorting')
            continue
            
        print('Tekan 1 untuk keluar Program dan tombol lainnya untuk lanjut')
        is_done = input('Silahkan masukan pilihan anda: ')
        if is_done == '1':
            print('Terima Kasih')
            break

#----------------------------------UPDATE FUNCTION-----------------------------------------
def main_update():
    '''
    Fungsi Utama Menu Update
    '''


    while True:
        try:
            print('='*80)
            print(f"{'Menu Update Data Pasien':^80}")
            print('='*80)
            print('Silahkan Pilih Jenis Tambah')
            print(f'1. Update Satu Kolom Data Berdasarkan ID Pasien\n2. Update Satu Baris Data Pasien')
            print('3. Update Kolom Kosong Data Pasien\n4. Sorting Data Pasien')
            user_main_update = input('Silahkan Input (1-4) e kembali ke menu utama: ').lower()
            if user_main_update == '1':
                update_one_col()
            elif user_main_update == '2':
                update_many_col()
            elif user_main_update == '3':
                update_null_data()
            elif user_main_update == '4':
                sorting_pasien()
            elif user_main_update == 'e':
                print('Program Update Data Pasien Selesai')
                break
            else:
                print('Input Tidak Valid')

        except Exception as e:
            print('User Input Tidak Valid',e)

def update_one_col():
    '''
    Fungsi Untuk Mengupdate Satu Kolom Data diri pasien berdasarkan id pasien
    '''
    table_data = []
    for key,value in database.items():
        ID = key
        NAMA = value['nama']
        USIA = value['usia']
        GENDER = value['gender']
        TUJUAN = value['tujuan']
        PENYAKIT = value['penyakit']
        TANGGAL = value['tanggal_daftar']
        table_data.append([ID,NAMA,USIA,GENDER,TUJUAN,PENYAKIT,TANGGAL])
    print(tabulate(table_data, headers=['ID', 'Nama', 'Usia', 'Gender', 'Tujuan', 'Penyakit', 'Tanggal Daftar'],
               tablefmt='fancy_grid')) 


    while True:
        print('='*80)
        ID = input('Silahkan Pilih ID Pasien Yang akan Di Update: ').title()
        if ID in database:
            print(f'ID Pasien {ID} ada di database. Pilih Kolom Yang akan anda Update')
            print('='*20)
            print(f'1. Ubah Nama Pasien\n2. Ubah Usia Pasien\n3. Ubah Gender Pasien ')
            print(f'4. Ubah Poli Pasien\n5. Ubah Keluhan Pasien\n6. Ubah Tanggal Daftar Pasien')
            user_input_update = input('Masukan Nama Kolom Pilihan Anda: ').lower()
            if user_input_update == '1':
                while True:
                    nama_baru = input('Masukan Nama Baru Pasien: ').title()
                    if nama_baru.isdigit():
                        print('Nama Tidak Boleh Angka')
                        continue
                    else:
                        save_i = input('Apakah anda ingin Menyimpan (y/n): ').lower()
                        if save_i == 'y':
                            database[ID]['nama'] = nama_baru
                            read_all()
                            break
                        else:
                            print('Data Tidak Di Simpan')
                            break
            elif user_input_update == '2':
                while True:
                    usia_baru = (input('Masukan Usia Baru Pasien: '))
                    if usia_baru.isdigit():
                        usia_baru = int(usia_baru)
                        break
                    else:
                        print('Anda Harus Memasukan Angka')
                        continue
                save_i = input('Apakah anda ingin Menyimpan (y/n): ').lower()
                if save_i == 'y':
                    database[ID]['usia'] = usia_baru
                    read_all()
                    break
                else:
                    print('Data Tidak Di Simpan')
                    break
            elif user_input_update == '3':
                while True:  
                    gender_baru = input('Masukan Gender Baru Pasien: ').title()
                    if gender_baru.isdigit():
                        print('Gender Tidak Boleh Angka')
                        continue
                    else:
                        save_i = input('Apakah anda ingin Menyimpan (y/n): ').lower()
                        if save_i == 'y':
                            database[ID]['gender'] = gender_baru
                            read_all()
                            break
                        else:
                            print('Data Tidak Di Simpan')
                            break
            elif user_input_update == '4':
                while True:
                    tujuan_baru = input('Masukan Poli Baru Pasien: ').title()
                    if tujuan_baru.isdigit():
                        print('Poli Tidak Boleh Angka cth: (Poli Anak)')
                        continue
                    else:
                        save_i = input('Apakah anda ingin Menyimpan (y/n): ').lower()
                        if save_i == 'y':
                            database[ID]['tujuan'] = tujuan_baru
                            read_all()
                            break
                        else:
                            print('Data Tidak Di Simpan')
                            break
            elif user_input_update == '5':
                while True:
                    penyakit_baru = input('Masukan Keluhan Baru Pasien: ').title()
                    if penyakit_baru.isdigit():
                        print('Penyakit Tidak Boleh Angka')
                        continue
                    else:
                        save_i = input('Apakah anda ingin Menyimpan (y/n): ').lower()
                        if save_i == 'y':
                            database[ID]['penyakit'] = penyakit_baru
                            read_all()
                            break
                        else:
                            print('Data Tidak Di Simpan')
                            break
            elif user_input_update == '6':
                tanggal_daftar = input("Masukkan Tanggal Pendaftaran (YYYY-MM-DD): ")
                tahun, bulan, hari = map(int, tanggal_daftar.split('-'))
                tanggal_daftar = dt.date(tahun, bulan, hari)
                save_i = input('Apakah anda ingin Menyimpan (y/n): ').lower()
                if save_i == 'y':
                    database[ID]['tanggal_daftar'] = tanggal_daftar
                    read_all()
                    break
                else:
                    print('Data Tidak Di Simpan')
                    break
            else:
                print('Input Tidak Valid')

        else:
            print('Data ID Pasien Tidak Di Temukan') 
        is_done = input('Tekan 1 untuk mengakhiri selesai program dan tombol apapun untuk update kembali: ').lower()
        if is_done == '1':
            break 


def update_many_col():
    '''
    Fungsi untuk mengupdate satu Data Pasien dengan seluruh kolom
    '''
    while True:
        # print('Silahkan untuk mengupdate data pasien')
        table_data = []
        for key,value in database.items():
            ID = key
            NAMA = value['nama']
            USIA = value['usia']
            GENDER = value['gender']
            TUJUAN = value['tujuan']
            PENYAKIT = value['penyakit']
            TANGGAL = value['tanggal_daftar']
            table_data.append([ID,NAMA,USIA,GENDER,TUJUAN,PENYAKIT,TANGGAL])
        print(tabulate(table_data, headers=['ID', 'Nama', 'Usia', 'Gender', 'Tujuan', 'Penyakit', 'Tanggal Daftar'],
               tablefmt='fancy_grid'))

        database_template = {

            'nama':'nama panjang',
            'usia':00,
            'gender':'JK',
            'tujuan':'poli',
            'penyakit':'sakit apa',
            'tanggal_daftar':dt.date(1111,1,11)
        }
        print('='*80)
        print('Silahkan Update Berdasarkan ID Pasien / Nama Pasien')
        user_update = input('Tekan (1 | 2) untuk ID Pasien / Nama Pasien: ')
        if user_update == '1':
            data_kosong = dict.fromkeys(database_template.keys()) #template dictionary untuk mengambik keys nya saja 
            ID = input('Masukan ID Pasien: ').title()             #update berdasarkan ID pasien
            if ID in database:
                print('data Terdapat di database update bisa di lanjut')
            
                data_kosong['nama'] = input('Masukan Nama Pasien : ').title()
                if data_kosong['nama'].isdigit():
                    print('Nama Tidak Boleh Angka')
                    break
                data_kosong['usia'] = int(input('Masukan Usia Pasien : '))
                data_kosong['gender'] = input('Masukan Gender Pasien (pria/wanita): ').title()
                print(' Poli Umum | Poli Anak | Poli Gigi | Poli Obgin | Poli Bedah')
                data_kosong['tujuan'] = input('Masukan Poli tujuan Pasien: ').title()
                data_kosong['penyakit'] = input('Masukan Keluhan/Penyakit Pasien: ').title()
                tanggal_daftar = input("Masukkan Tanggal Pendaftaran (YYYY-MM-DD): ")
                tahun, bulan, hari = map(int, tanggal_daftar.split('-'))
                tanggal_daftar = dt.date(tahun, bulan, hari)

                data_kosong['tanggal_daftar'] = tanggal_daftar


                save = input('Apakah Anda Mau menyimpan nya (y/n): ').lower()
                if save == 'y':
                    database.update({ID:data_kosong})
                    print('Data Sudah Di simpan') 
                else:
                    print('Data Tidak Di Save')
                    break
                read_all()
            else:
                print('Data Tidak Di Temukan. Silahkan Coba Lagi')
                break

        elif user_update == '2': 
            nama_pasien = input('Silahkan Cari Nama Pasien : ').title()
            found = False
            for ID, data_pasien in database.items():
                if data_pasien['nama'] == nama_pasien:
                    found = True
                    print('Data Terdapat di database update bisa di lanjut.') #perhatikan ID nya belum di rubah

                    data_kosong = dict.fromkeys(database_template.keys()) #template dictionary untuk mengambil keys nya saja 

                    data_kosong['nama'] = input('Masukkan Nama Baru Pasien : ').title()
                    data_kosong['usia'] = int(input('Masukkan Usia Baru Pasien : '))
                    data_kosong['gender'] = input('Masukkan Gender Pasien (pria/wanita): ').title()
                    data_kosong['tujuan'] = input('Masukkan Poli Baru Tujuan Pasien: ').title()
                    data_kosong['penyakit'] = input('Masukkan Keluhan/Penyakit Pasien: ').title()
                    tanggal_daftar = input('Masukkan Tanggal Pendaftaran (YYYY-MM-DD): ')
                    tahun, bulan, hari = map(int, tanggal_daftar.split('-'))
                    tanggal_daftar = dt.date(tahun, bulan, hari)
                    data_kosong['tanggal_daftar'] = tanggal_daftar
                    save = input('Apakah Anda ingin menyimpannya? (y/n): ').lower()
                    if save == 'y':
                        database[ID] = data_kosong
                        print('Data Sudah Disimpan') 
                    else:
                        print('Data Tidak Disimpan')
                       
                    read_all()
                    break
            if not found:
                print('Data Pasien Tidak Ditemukan')
                


        is_done = input('Tekan 1 untuk mengakhiri program dan tombol apapun untuk lanjut: ')
        if is_done == '1':
            print('Program Update Data Pasien Selesai. Terima Kasih !!! ')
            break 

def update_null_data():
    '''
    Fungsi untuk mengupdate null value
    '''

    print('='*80)

    print(f"{'Program Untuk Mengupdate Kolom Null':^80}")
    user_null = input('Apakah Anda Ingin Mencari Data Dengan nilai kosong (y/n) : ').lower()
    if user_null == 'y':

        for ID, value in database.items():
            for id_nested, value_nested in value.items():
                null_data = []
                if value_nested is None:
                    null_data.append([ID,value['nama'],value['usia'],
                                      value['gender'],value['tujuan'],value['penyakit'],value['tanggal_daftar']])
                    print(tabulate(null_data, headers=['ID', 'Nama', 'Usia', 'Gender', 'Tujuan', 'Penyakit', 'Tanggal Daftar'],
                                   tablefmt='fancy_grid')) 
                    
        user_update_null = input('Apakah Anda Ingin mengupdate Data Kosong(y/n): ').lower()
        if user_update_null == 'y':
            for ID, value in database.items():
                for key, val in value.items():
                    val_found = False
                    if val is None:
                        val_found = True
                        user_input_update = input(f'Masukan nilai untuk {key} Pada ID {ID}: ').title()
                        user_confirm_update = input('Apakah Anda yakin akan mengupdate data(y/n): ').lower()
                        if user_confirm_update =='y':
                            database[ID][key] = user_input_update
                            read_all()
                        else:
                            print('Data Tidak di Update')
                if val_found:
                    print('Tidak ada Kolom Kosong')


#------------------------------------DELETE FUNCTION--------------------------------------
def main_delete():
    '''
    Fungsi Utama Menu Delete
    '''


    while True:
        try:
            print('='*80)
            print(f"{'Menu Delete Data Pasien':^80}")
            print('='*80)
            print('Silahkan Pilih Jenis Delete')
            print(f'1. Delete Satu Data Pasien\n2. Delete Banyak Data Pasien')
            print('3. Delete Kolom Tertentu Dari Data Pasien\n4. Hapus Seluruh Data')
            user_main_delete = input('Silahkan Input (1-4) e for exit: ').lower()
            if user_main_delete == '1':
                delete_one()
            elif user_main_delete == '2':
                delete_many_col()
            elif user_main_delete == '3':
                delete_col_tertentu()
            elif user_main_delete == '4':
                delete_all()
            elif user_main_delete == 'e':
                print('Program Delete Data Pasien Selesai')
                break
            else:
                print('Input Tidak Valid')

        except Exception as e:
            print('User Input Tidak Valid',e)

def delete_one():
    '''
    fungsi ini di gunakan untuk menghapus salah satu data pasien yang ada didalam database
    '''
    table_data = []
    for key,value in database.items():
        ID = key
        NAMA = value['nama']
        USIA = value['usia']
        GENDER = value['gender']
        TUJUAN = value['tujuan']
        PENYAKIT = value['penyakit']
        TANGGAL = value['tanggal_daftar']
        table_data.append([ID,NAMA,USIA,GENDER,TUJUAN,PENYAKIT,TANGGAL])
    print(tabulate(table_data, headers=['ID', 'Nama', 'Usia', 'Gender', 'Tujuan', 'Penyakit', 'Tanggal Daftar'],
               tablefmt='fancy_grid')) 

    print('='*80)
    print('SIlahkan Hapus Data Pasien Berdasarkan (ID/Nama Pasien)')
    user_hapus = input('Tekan 1 untuk ID | Tekan 2 untuk Nama Pasien : ').lower()
    if user_hapus == '1':
        ID = input('Masukan Data Pasien yang akan di hapus berdasarkan ID: ').title()
        if ID in database:
            print(f'ID {ID} Terdapat di Database. Data dapat di Hapus')
            user_delete = input(f'Apakah Anda ingin menghapus data pasien {ID} (y/n): ').lower()
            if user_delete == 'y':
                del database[ID]
                print(f'\nData Pasien Dengan ID {ID} telah berhasil dihapus\n')
            else:
                print(f'Data Pasien Dengan ID {ID} Tidak di hapus') 
        else:
            print('data Tidak Di temukan')

    elif user_hapus == '2':
        nama_pasien = input('Silahkan Cari Nama Pasien : ').title()
        found = False
        delete_key = []
        for ID, data_pasien in database.items():
            if data_pasien['nama'] == nama_pasien:
                found = True
                print(f'Data {nama_pasien} Di temukan. Data Bisa Di Hapus')
                user_nama_hapus = input(f'Apakah Anda Yakin Ingin Menghapus Data {nama_pasien} (y/n): ').lower()
                if user_nama_hapus == 'y':
                    delete_key.append(ID)
                else:
                    print('Data Tidak DI hapus')

        if not found:
            print('Data Tidak Di temukan')

        for key in delete_key:
            del database[key]

    read_all()


def delete_many_col():
    '''
    Fungsi ini di gunakan untuk menghapus banyak baris data pasien di database
    '''
    table_data = []
    for key,value in database.items():
        ID = key
        NAMA = value['nama']
        USIA = value['usia']
        GENDER = value['gender']
        TUJUAN = value['tujuan']
        PENYAKIT = value['penyakit']
        TANGGAL = value['tanggal_daftar']
        table_data.append([ID,NAMA,USIA,GENDER,TUJUAN,PENYAKIT,TANGGAL])
    print(tabulate(table_data, headers=['ID', 'Nama', 'Usia', 'Gender', 'Tujuan', 'Penyakit', 'Tanggal Daftar'],
               tablefmt='fancy_grid')) 
    
    jumlah_data = int(input('Berapa Jumlah Data yang akan anda hapus: '))
    list_delete = []
    for i in range(jumlah_data):
        user_delete_many = input(f'Masukan ID Pasien ke {i+1}: ').title()
        list_delete.append(user_delete_many)
        # print(list_delete)

    for data in list_delete:
        if data in database:
            print(f'Data Pasien {data} Ada di Database')
            user_confirm = input('Apakah Anda Ingin Menghapus Data Tersebut(y/n): ').lower()
            if  user_confirm == 'y':
                del database[data]
                user_display = input('Apakah Anda Ingin Menampilkan Data(y/n): ').lower()
                if user_display == 'y':
                    read_all()
            else:
                print(f'Data Pasien {data} Tidak Di hapus')
                

        else:
            print(f'Data Pasien {data} Tidak Ada di Database')

def delete_col_tertentu():
    '''
    fungsi ini utk menghapus kolom tertentu di ID Pasien
    '''
    table_data = []
    for key,value in database.items():
        ID = key
        NAMA = value['nama']
        USIA = value['usia']
        GENDER = value['gender']
        TUJUAN = value['tujuan']
        PENYAKIT = value['penyakit']
        TANGGAL = value['tanggal_daftar']
        table_data.append([ID,NAMA,USIA,GENDER,TUJUAN,PENYAKIT,TANGGAL])
    print(tabulate(table_data, headers=['ID', 'Nama', 'Usia', 'Gender', 'Tujuan', 'Penyakit', 'Tanggal Daftar'],
               tablefmt='fancy_grid')) 
    
    print('='*80)
    print('Menghapus satu nilai dalam sebuah kolom')
    user_delete_col = input('SIlahkan Masukan ID Pasien: ').title()
    if user_delete_col in database:
        print(f'Data Pasien Dengan ID {user_delete_col} Ada Di Database')
        print('Silahkan Pilih Kolom Yang akan di hapus')
        print('1. nama\n2. usia\n3. gender\n4. Poli Pasien')
        print('5. keluhan pasien\n6. tanggal pendaftaran')
        user_input_for_delete = input('Masukan Pilihan Anda: ')
        if user_input_for_delete == '1':
            database[user_delete_col]['nama'] = None
            read_all()
        elif user_input_for_delete == '2':
            database[user_delete_col]['usia'] = None
            read_all()
        elif user_input_for_delete == '3':
            database[user_delete_col]['gender'] = None
            read_all()
        elif user_input_for_delete == '4':
            database[user_delete_col]['tujuan'] = None
            read_all()
        elif user_input_for_delete == '5':
            database[user_delete_col]['penyakit'] = None
            read_all()
        elif user_input_for_delete == '6':
            database[user_delete_col]['tanggal_daftar'] = None
            read_all()
    else:
        print(f'Data Pasien {user_delete_col} Tidak Terdapat Di Database')

    print('Program Delete Kolom Tertentu Selesai!!') 


def delete_all():
    '''
    Fungsi Ini untuk menghapus seluruh Data di Database
    '''
    table_data = []
    for key,value in database.items():
        ID = key
        NAMA = value['nama']
        USIA = value['usia']
        GENDER = value['gender']
        TUJUAN = value['tujuan']
        PENYAKIT = value['penyakit']
        TANGGAL = value['tanggal_daftar']
        table_data.append([ID,NAMA,USIA,GENDER,TUJUAN,PENYAKIT,TANGGAL])
    print(tabulate(table_data, headers=['ID', 'Nama', 'Usia', 'Gender', 'Tujuan', 'Penyakit', 'Tanggal Daftar'],
               tablefmt='fancy_grid')) 
    print('='*80)
    user_delete_all = input('Apakah Anda Yakin Ingin Menghapus Seluruh Data Pasien (y/n): ').lower()

    if user_delete_all == 'y':
        database.clear()
        print('Database Sudah Di hapus')
        read_all()
    else:
        print('Database Tidak Jadi di Hapus')
        read_all()  

#------------------------------------EXPORT FUNCTION---------------------------------------
def main_export():
    '''
    Fungsi Untuk Export Data Pasien 
    '''
    while True:
        try:
            print('='*80)
            print(f"{'Export Data Passien':^80}")
            print('='*80)
            print('Silahkan Pilih Jenis File yang akan di Export')
            print(f'1. CSV File | 2. Excel File')
            user_export = input('Silahkan Input (1-2) e kembali ke menu utama: ').lower()
            if user_export == '1':
                export_to_csv(database)
            elif user_export == '2':
                export_to_excel(database)
            elif user_export == 'e':
                print('Program Export Data Pasien Selesai. Terima Kasih')
                break
            else:
                print('Input Tidak Valid')

            # match user_export:
            #     case '1': export_to_csv(database)
            #     case '2': export_to_excel(database)
            #     case 'e':
            #         print('Program Export Data Pasien Selesai. Terima Kasih')
            #         break
        except Exception as e:
            print('User Input Tidak Valid',e)



def export_to_excel(database):
    '''
    Fungsi Untuk mengexport database ke excel
    '''
    filename = input('Masukan Nama File dalam format excel(hallo.xlsx): ')
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['ID', 'Nama', 'Usia', 'Gender', 'Tujuan', 'Penyakit', 'Tanggal Daftar'])

    for id_pasien, data_pasien in database.items():
        ws.append([
            id_pasien,
            data_pasien['nama'],
            data_pasien['usia'],
            data_pasien['gender'],
            data_pasien['tujuan'],
            data_pasien['penyakit'],
            data_pasien['tanggal_daftar'].strftime('%Y-%m-%d')  # Format tanggal 
        ])

    wb.save(filename)
    print('Database Sudah Di export. Terima Kasih !!!')



def export_to_csv(database):
    '''
    fungsi untuk export database ke CSV file
    '''
    filename = input('Masukan Nama File dalam format CSV(hallo.csv): ')
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['ID', 'Nama', 'Usia', 'Gender', 'Tujuan', 'Penyakit', 'Tanggal Daftar']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for id_pasien, data_pasien in database.items():
            writer.writerow({
                'ID': id_pasien,
                'Nama': data_pasien['nama'],
                'Usia': data_pasien['usia'],
                'Gender': data_pasien['gender'],
                'Tujuan': data_pasien['tujuan'],
                'Penyakit': data_pasien['penyakit'],
                'Tanggal Daftar': data_pasien['tanggal_daftar']
            })
        print('Database Sudah DI Export. Terimakasih!!!')
#==========================================================================================
#==================================MAIN APP PROGRAM========================================
#==========================================================================================



while True:
    try:
        print('='*90)
        print(f"{'Data Pasien Rumah Sakit Al Istriham':^90}")
        print('='*90)

        print('Silahkan Pilih Menu Di Bawah')
        print('1. Report Data Pasien\n2. Tambah Data Pasien\n3. Update Data Pasien')
        print('4. Hapus Data Pasien\n5. Export Data Pasien\n6. Exit Program')
        user_input = int(input('Silahkan Masukan Pilihan Anda: '))
        if user_input == 1 :
            main_read()
        elif user_input == 2:
            main_create()
        elif user_input == 3:
            main_update()
        elif user_input == 4:
            main_delete()
        elif user_input == 5:
            main_export()
        elif user_input == 6:
            print('Program Selesai. Terimakasih Sudah Menggunakan Aplikasi Kami!!!')
            break
        else:
            print('Input Tidak Valid')

    except Exception as e:
        print('Pilihan Menu Tidak Valid',e)
