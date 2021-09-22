def convertfromF ():
    '''input 1 atau 2 untuk menjalankan pengubah suhu'''
    suhuIn = int(input('Masukin Suhu dalma Fahrenheit : '))
    choose = int(input('Converter Suhu dari fahrenheit, ketik 1 untuk mengubah ke celcius dan 2 untuk mengubah ke kelvin : '))
    if choose == 1 :
        suhuIn = (suhuIn - 32) * 5/9
        print(f'Konversi suhu berhasil !\nsuhu menjadi {suhuIn} celcius')
    elif choose == 2:
        suhuIn = (suhuIn-32)*5/9+273.15
        print(f'Konversi Suhu Berhasil !\nsuhu menjadi {suhuIn} kelvin')
    else : print('ccommand tidak ditemukan')