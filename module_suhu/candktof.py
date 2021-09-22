def converttoF():
    '''input 1 atau 2 untuk menjalankan pengubah suhu'''
    choose = int(input('Converter suhu dari celcius atau kelvin menjadi farenheit, pilih 1 dari celcius dan 2 dari kelvin : '))
    if choose == 1:
        suhuIn = int(input('Masukan suhu dalam celcius'))
        suhuIn = (suhuIn*9/5) + 32
        print(f'konversi suhu berhasil !\nSuhu menjadi {suhuIn} fahrenheit')
    elif choose == 2:
        suhuIn = int(input('Masukan suhu dalam kelvin'))
        suhuIN = ((suhuIn - 273.15)*9/5) + 32
        print(f'konversi suhu berhasil!\nSuhu berhasil diubah menjadi {suhuIn} fahrenheit')
    else : print('command tidak ditemukan')