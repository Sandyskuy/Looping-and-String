#!/usr/bin/env python
# coding: utf-8

# In[3]:


a = 0 #inisialisasi sesuai awalan fibonacci
b = 1 #inisialisasi sesuai awalan fibonacci

for i in range(11): #jumlah baris yang akan ditampilkan
    for j in range(i): #mencetak bilangan pada setiap baris
        if j == 0: #mengecek bilangan tersebut awal (a) atau bukan
            print(a, end=" ") #mencetak bilangan awal
        elif j == 1: #jika bukan bilangan awal maka bilangan kedua (b) 
            print(b, end=" ") #mencetak bilangan kedua
        else:
            c = a + b
            a = b
            b = c
            #bilangan dicetak melalui rumus ini
            print(c, end=" ")
    print(" ")
    #menghitung kembali dari awal
    a = 0
    b = 1


# In[ ]:





# In[ ]:



        


# In[ ]:




