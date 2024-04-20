# 3. tananyag
# 5. feladat 
# Ritka mátrix 3 soros reprezentacio, ne a 0 legyen a leggyakoribb elem.

class hsrep: #osztály létrehozása, hogy a sor oszlop értéket egybe #tudjuk kezelni.
    rowindex=[]
    colindex=[]
    datas=[]
    defdata=0  #!!!alapértelmezett adat, de megváltoztathatja lenteb, csak egy változóba jegyeztetjük meg, h ne tároljuk sokszor

    # Megkeresi, hogy az adott sor oszlop -on van-e már adat, ha igen visszatér az indexével
    def find_index(self,row,col): #self-önmaga. objektumok #használatához mindig ezel kezdjük. Megkapja a sorindexet, #oszlopindexet és a datat.
        for i in range(len(self.rowindex)):
            if self.rowindex[i]==row and self.colindex[i]==col:
                return i
        return -1

    def set_defdata(self,a):   #!!!!!beállítja az alapértelmezett értéket, mi legyne a 0 helyett
        self.defdata=a
       
# Tárol egy értéket a mátrix megadott sorába, oszlopába
    # de csak akkor, ha még ott nem volt érték helyezve, azaz először find megkeresi, hogy van-e már ott érték, ha nincs akkor append bővít, különben felülír
    def set_data(self,row,col,data): 
        # set data , megkapsa melyik sor melyik oszlpban melyik adatot kell tárolni.
# Írjuk át úgy, hogy ha már van ezen a helyen elem akkor 
#írja felül
        x=self.find_index(row,col) # Van-e adat ebben a sorban és  #oszlopban?
        if x==-1: # ha nem szerepel még a ritkamátrixban akkor tárolunk
            self.rowindex.append(row) # rowindexet bővítjül
            self.colindex.append(col) # oszlopindexet bővítjük
            self.datas.append(data) # értékkel bővít
        else: # különben felülírunk
            self.datas[x]=data
        pass            

    # eltávolít ja a megadott helyen lévő értéket
    # kétféle megoldás: 
    # - megkeressük és nullát írunk (nem hatákony tárolás szempontjából)
    # - megrekessük és kivesszük a tömbökből
    def remove_data(self,row,col):
        # self.set_data(row,col,0) # 1. megoldás, kinullázzuk.
        # 2. megoldás
        x=self.find_index(row,col)
        if x!=-1: # ha tényleg van érték a megadott sor6/oszlop-on, akkor kivesszük a tömbökből
            del self.rowindex[x]
            del self.colindex[x]
            del self.datas[x]
        pass

    # !!!!!!Kiolvas egy datatot a megadott sorból, oszlopból
    def get_data(self,row,col):
        for i in range(len(self.rowindex)):
            if self.rowindex[i]==row and self.colindex[i]==col:
                return self.datas[i]
        return self.defdata # !!!!!!!!!!Nem 0-val alapértelmezett adattal érünk vissza

    # kiírja a háromsoros reprezentációs mátrixot
    def print_repl_matrix(self):
        print(" ".join(str(cell) for cell in self.rowindex))
        print(" ".join(str(cell) for cell in self.colindex))
        print(" ".join(str(cell) for cell in self.datas))
      #Maskent
	#    print(self.rowindex)
	#    print(self.colindex)
	#	print(self.datas)

    # megjeleníti a ritkamátrixot
    def print_rmatrix(self):
        N=max(max(self.rowindex),max(self.colindex))
        print(N)
        for i in range(N+1):
            sz=""
            for j in range(N+1):
                sz=sz+str(self.get_data(i,j))+" "
            print(sz)
        pass

#Főprogi rm-ritka mátrix létrehozása
rm=hsrep()
rm.set_defdata(9)  # !!!!!!!!!!alapértelmezett érték beállítás
rm.set_data(2,3,5) #2.sorindex 3. oszlopindex tárolja az 5 értéket (3 sor 4 oszlop <- 5)
rm.set_data(1,3,6)
rm.set_data(1,4,7)
rm.set_data(2,2,8)

print('Három soros reprezentáció:')
rm.print_repl_matrix()

print(rm.get_data(2,2)) #Kiolvas index: 2 sor 2 oszlopoindexből
print(rm.get_data(2,3))
print(rm.get_data(1,1))

rm.print_rmatrix()

print()

rm.remove_data(1,3)
rm.print_repl_matrix()

