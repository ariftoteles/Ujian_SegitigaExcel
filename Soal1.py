class uraiRajutKata:      
    def urai(self,kata):
        self.kata = kata
        kata2 = ''
        kata3 = ''
        for j in self.kata:
            kata2 += j
            kata3 += kata2
        return kata3
    def rajut(self,kata):
        self.kata = kata
        lenKata = len(self.kata)
        pola = []
        for i in range(100):
            x = i*(i+1)/2
            pola += [int(x)]
        if lenKata in pola:
            x = pola.index(lenKata)
            y = lenKata - x
        return self.kata[(y)::]
x = uraiRajutKata()
print(x.urai('Code'))
print(x.rajut('CCoCodCode'))