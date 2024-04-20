class hsrep:
    rowindex=[]
    colindex=[]
    datas=[]

def find_index(hsm:hsrep, row:int, col:int)->int:
    for i in range(len(hsm.rowindex)):
        if hsm.rowindex[i]==row and hsm.colindex[i]==col:
            return i
    return -1

def set_data(hsm:hsrep, row, col, data):
    x=find_index(hsm, row, col)
    if x==-1:
        hsm.rowindex.append(row)
        hsm.colindex.append(col)
        hsm.datas.append(data)
    else:
        hsm.datas[x]=data

def remove_data(hsm:hsrep, row, col):
    x=find_index(hsm, row, col)
    if x!=-1:
        del hsm.rowindex[x]
        del hsm.colindex[x]
        del hsm.datas[x]

def get_data(hsm:hsrep, row, col):
    x=find_index(hsm, row, col)
    if x!=-1:
        return hsm.datas[x]
    return 0

def print_repr_matrix(hsm:hsrep):
    print(" ".join(str(cell) for cell in hsm.rowindex))
    print(" ".join(str(cell) for cell in hsm.colindex))
    print(" ".join(str(cell) for cell in hsm.datas))

def print_matrix(hsm:hsrep):
    N=max(max(hsm.rowindex), max(hsm.colindex))
    print('Mátrix méret: ',N+1)
    for i in range(N+1):
        sz=""
        for j in range(N+1):
            sz+=str(get_data(hsm,i,j))+"  "
        print(sz)

#főprogi
rm=hsrep()
set_data(rm,0,1,2)
set_data(rm,1,0,1)
set_data(rm,1,2,7)
set_data(rm,2,0,5)
set_data(rm,3,2,9)

print("Reprezentációs mátrix")
print_repr_matrix(rm)
print("Mátrix")
print_matrix(rm)

remove_data(rm, 1, 2)
print_matrix(rm)




