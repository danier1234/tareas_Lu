info={} #diccionario
class video_juego: # clase
    nombre = ""
    monedas = 0
    vidas = 3
    tamaño = "pequeño"
    mundo = 1
    nivel = 1
    disparos=0
    Max_mone=100
    
    def __init__(self,nombre,monedas,vidas,tamaño,mundo,nivel): #metodo contructor 
        self.nombre=nombre
        self.monedas=monedas
        self.vidas=vidas
        self.tamaño=tamaño
        self.mundo=mundo
        self.nivel=nivel
    
    #def setmundos(self): #fincuion para cambiar mundo
     #   if (self.vidas>0):
      #      if(self.mundo <=8):
       #         if self.nivel==4:
        #            self.mundo = self.mundo + 1
         #           self.nivel = 1
          #          if(self.mundo >=9):
           #             self.mundo = 1
            #            self.nivel= 1
    
    def setnivel(self): #funcion para cambiar nivel y mundos 
        if(self.vidas>0):
            self.nivel = self.nivel + 1
            if(self.nivel >4):
                self.nivel = 1
                self.mundo = self.mundo + 1
                if self.mundo>=9:
                    self.mundo=1
                    self.nivel=1
      
                    
   
    def sethomgocre(self): #funcion para creser
        self.tamaño="grande"
        
    def setflor(self): #funcion para recoher flor y disparar
        if(self.vidas>0):
            if self.tamaño=="grande":
                if(self.vidas>0 and self.tamaño=="grande"):
                    self.disparos=self.disparos + 1
                    return self.disparos
    
    def setmonedas(self): #funcion para recoger monedas
        if(self.vidas>0):
            self.monedas=self.monedas + 10
            if(self.monedas== 100 ):
                self.vidas= self.vidas+1
    
            elif(self.monedas >=100 ):
                self.monedas = 10
            
    def setincidente_sen(self): #funcion para incidente sencillo
        if(self.vidas>0):
            if self.tamaño=="pequeño":
                self.vidas=self.vidas -1
            elif self.tamaño=="grande":
                self.tamaño="pequeño"
    
    def setincidente_gra(self): #funcion para incidente complicado
        if (self.vidas>0):
            self.vidas = self.vidas -1
            self.tamaño="pequeño"
            
    def sethomgovid(self): #funcion para recoger hongo de vida
        if(self.vidas>0):
            self.vidas = self.vidas +1
    
    def setreiniciar(self): #funcion para reiniciar 
        if(self.vidas==0):
            self.monedas=0
            self.vidas=3
            self.tamaño="pequeño"
            self.disparos=0
            self.mundo=1
            self.nivel=1
            
def mostrar(): #funcion para mostrar
    for elem in listaP:
        print("nombre:",elem.nombre)
        print("monedas:",elem.monedas)
        print("vidas:",elem.vidas)
        print("tamaño:",elem.tamaño)
        print("disparos:",elem.disparos)
        print("mundo:",elem.mundo)
        print("nivel:",elem.nivel)

def res(): #funcnion para elegir personaje y crear el objeto
    print("1. mario")
    print("2. luigi")
    nom=int(input("ingrese una opcion:"))
    if nom==1:
        nombre="mario"
    elif nom==2:
        nombre="luigi"
    monedas=0
    vidas=3
    tamaño="pequeño"
    mundo=1
    nivel=1
    id = int(len(listaP)) + 1  
    info[id]={
        "id":id,
        "nombre":nombre,
        "monedas":monedas,
        "vidas":vidas,
        "tamaño":tamaño,
        "mundo":mundo,
        "nivel":nivel,
        "disparo":0
    }  
    jugador=video_juego(nombre,monedas,vidas,tamaño,mundo,nivel)
    listaP.append(jugador)
    return jugador
listaP=[]
op=0
while True: #menu
    print("1. elegir personaje")
    print("2. cambiar nivel")
    print("3. recoger hongo de crecimiento")
    print("4. recoger flor y disparar")
    print("5. recoger monedas")
    print("6. incidente sencillo")
    print("7. incidente complicado")
    print("8. recoger hongo de vida")
    print("9. reiniciar")
    print("10. salir")
    op=int(input("ingrese una opcion:"))

    if op==1:
        per=res()
        mostrar()
        
    #if (op==2):
      #  per.setmundos()
      #  mostrar()
        
    elif(op==2):
        per.setnivel()
        mostrar()
        
    elif(op==3):
        per.sethomgocre()
        mostrar()
        
    elif(op==4):
        per.setflor()
        mostrar()
        
    elif(op==5):
        per.setmonedas()
        mostrar()
    
    elif(op==6):
        per.setincidente_sen()
        mostrar()
        
    elif(op==7):
        per.setincidente_gra()
        mostrar()
        
    elif(op==8):
        per.sethomgovid()
        mostrar()
        
    elif(op==9):
        per.setreiniciar()
        mostrar()
        
    elif(op>=10):
        print("Gracias por jugar")
        break
        