#!/usr/bin/env python
# coding: utf-8

# In[2]:


nama = input("Masukkan nama anda: ") #menginputkan nama

#untuk menghitung nama dengan awalan 0
jumlah_huruf = 0
jumlah_vokal = 0
jumlah_konsonan = 0

for huruf in nama: #perulangan
    if huruf != '\n' and huruf.isalpha(): #pengecekan
        jumlah_huruf += 1 #menghitung jumlah huruf
        if huruf in ['a', 'i', 'u', 'e', 'o', 'A','I', 'U', 'E', 'O']: #untuk mengecek vokal
            jumlah_vokal += 1 #jika merupakan vokal maka akan dihitung jumlah vokal
        else:
            jumlah_konsonan += 1 #jika bukan akan dihitung jumlah konsonan

#untuk mencetak hasil perhitungan
print("jumlah huruf : ", jumlah_huruf)
print("jumlah vokal : ", jumlah_vokal)
print("jumlah konsonan : ", jumlah_konsonan)                     
                     


# In[ ]:




