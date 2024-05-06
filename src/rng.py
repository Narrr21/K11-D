import os
import time

def random(a=48271, c=0, m=2**31-1, n=None, seed=None, numRange:list[int]=None) -> int:#C++11's minstd_rand
    # SPESIFIKASI
    # Menghasilkan suatu angka dari daerah hasil yang diinginkan (numRange)
    # KAMUS
    # a,c,m = int
    # x_prev = float
    # numRange = array of integer
    # ALGORITMA
    if seed is None: #iterasi pertama
        x0 = int(os.getpid() + time.time())
    else:
        x0 = seed
    if n is None:
        n = random(n=1, numRange=[2,10])
    for _ in range(n):
        x0 = (a * x0 + c) % m
    if numRange is None: #saat tidak dimasukkan daerah hasil yang diinginkan
        return x0
    else:
        return int((x0 / (m - 1)) * (numRange[1] - numRange[0]) + numRange[0])
