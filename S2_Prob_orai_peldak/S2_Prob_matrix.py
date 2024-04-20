import random

def creat_matrix(size):
    matrix=[]
    for i in range(size):
        row=[]
        for i in range(size):
            row.append(0)
        matrix.append(row)
    return matrix  

def print_matrix(matrix):
    for row in matrix:
        sz=""
        for cell in row:
            sz+=str(cell)+" "
        print(sz)

def set_data(matrix, size, dc):
    for i in range(dc):
        row=random.randint(0,size-1)
        col=random.randint(0,size-1)
        matrix[row][col]=data=random.randint(1,9)

def ritka_matrix(matrix,size):
    count=0
    for row in matrix:
        for col in row:
            if col!=0:
                count+=1
    print('A mátrix "20%"-a ', (size*size*0.2))
    print('Az elhelyezett számok száma: ',count)
    return count<(size*size*0.2)

while True:
    size=int(input("kérem adja meg a mátrix méretét: "))
    if size>0:
        break

while True:
    dc=int(input("kérem adja meg az értékkel ellátott elemek számát: "))
    if dc>0:
        break

m=creat_matrix(size)
set_data(m,size,dc)
print('Mátrix: ')
print(m)
print('Ritka mátrix? ',ritka_matrix(m,size))
