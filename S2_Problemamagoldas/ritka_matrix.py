# 3. feladat 
# Írjon algoritmust, ami eldönti egy mátrixról, hogy ritkamátrix-e! Ritkamátrixnak tekintsünk egy mátrixot, 
# ha a nullától különböző elemek aránya 20% alatt van!
# Kérje be, hogy hányszor hányas mátrixot szeretne, mennyi véletlenszerűen választott számot akar benne elhelyezni

import random

# megjeleníti a mátrixot
def print_matrix(matrix):
#    for row in matrix: #soronként
#        print(" ".join(str(cell) for cell in row))
# row-egy sor értékei, cell vltozóval végigmegy a row értékein és #azt teszi be, szöveggé alakítva összefűzi.

        for row in matrix:
            sz=""
            for cell in row:
                sz=sz+str(cell)+" "
            print(sz)

# létrehoz egy 0-ákat tartalmazó mátrixot
def create_matrix(size):
#    matrix = [[0 for _ in range(size)] for _ in range(size)]
    matrix=[]
    for i in range(size):
       row=[]   #sor
       for j in range(size):
          row.append(0)
       matrix.append(row)    # row=[0,0,0,…]
    
    return matrix

# Feltölti a mtárixot körülbelül dc darab adattal
def set_data(matrix,size,dc):
    for i in range(dc):
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        data=random.randint(1,9)
        matrix[row][col]=data

def ritkamatrix(matrix,size): # Igazzal v hamissal tér vissza
    db=0
    for row in matrix:
        for col in row:
            if col!=0:
                db=db+1
    print(size*size*0.2)
    print(db)
    return db<size*size*0.2

#Főprogi
size = int(input("Adja meg a mátrix méretét: "))
dc = int(input("Adja meg az elhelyezendő adatok számát: "))
# pl. 8 akkor 8 számot elhelyez, többit 0-ával tölti ki

# ha a nullától különböző elemek aránya 20% alatt van!
#Mar kész a ritkamatrixban() Ha (melemsz=size*size)*0,2>= dc akkor print(’Ritkamátrix’) # #különben print(’Nem ritka mátrix’)  

m=create_matrix(size)
set_data(m,size,dc)
print_matrix(m)
print(ritkamatrix(m,size))  # True akkor ritka, False nem ritka mátrix
