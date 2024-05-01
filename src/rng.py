import os
import time

class LCGPseudoRandomGenerator :
# Membuat variabel Pseudo Random Generator
    def __init__(self, a=48271, c=0, m=2**31-1, seed=None) -> int: #C++11's minstd_rand
        # SPESIFIKASI
        # Melakukan penghitungan nilai berdasarkan nilai sebelumnya bila ada menggunakan parameter seed
        # atau bila merupakan iterasi pertama akan mengambil data os dan time sebagai seed
        # KAMUS
        # a,c,m,seed = int
        # x_prev, x0 = float
        # ALGORITMA
        self.a = a
        self.c = c
        self.m = m

        if seed is None: #iterasi pertama
            self.x0 = int(os.getpid() + time.time())
        else:
            self.x0 = seed

        self.x_prev = (self.a * self.x0 + self.c) % self.m

    type Range = list[int]
    def generate(self, numRange:Range=None) -> int:
        # SPESIFIKASI
        # Menghasilkan suatu angka dari daerah hasil yang diinginkan (numRange)
        # KAMUS
        # a,c,m = int
        # x_prev = float
        # numRange = array of integer
        # ALGORITMA
        self.x_prev = (self.a * self.x_prev + self.c) % self.m
        if numRange is None: #saat tidak dimasukkan daerah hasil yang diinginkan
            return self.x_prev
        else:
            return int((self.x_prev / (self.m - 1)) * (numRange[1] - numRange[0]) + numRange[0])

random = LCGPseudoRandomGenerator()