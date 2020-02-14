import xlsxwriter

def segitigaExcel(kata):
    kata = kata.replace(' ','')
    pola = []
    for i in range(len(kata)):
        x = i*(i+1)/2
        pola += [int(x)]
    if len(kata) not in pola:
        print('Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola')
    else :
        book = xlsxwriter.Workbook('SegitigaKata.xlsx')
        sheet = book.add_worksheet()
        for i in range(pola.index(len(kata))):
            k = 0
            for j in range (pola[i],pola[i+1]):
                sheet.write(i,k,kata[j])
                k += 1
        book.close()
segitigaKata('Purwadhika')
segitigaExcel('Purwadhika Startup and Coding School @BSD')
# segitigaExcel('kode')
segitigaExcel('kode python')
# segitigaExcel('Lintang')
