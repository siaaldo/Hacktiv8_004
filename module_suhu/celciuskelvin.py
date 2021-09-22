def convertCandK ():
    '''Input 1 atau 2 untuk menjalankan pengubah suhu'''
    choose = input('Pilih 1 untuk pilih celcius to kelvin, atau 2 untuk sebaliknya : ')
    choose_inp = int(choose)
    if choose_inp == 1:
        suhuIn = int(input('Masukan Suhu dalam Celcius : '))
        suhuIn += 273.15
        print(f'berhasil ubah suhu ke kelvin menjadi {suhuIn} kelvin')
    elif choose_inp == 2:
        suhuIn = int(input('Masukan Suhu dalam Kelvin : '))
        suhuIn -= 273.15
        print(f'berhasil ubah suhu ke celcius menjadi {suhuIn} derajat celcius')
    else : print('Command tidak ditemukan')
