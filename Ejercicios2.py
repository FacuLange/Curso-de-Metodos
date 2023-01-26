class Usuario:
    __edad  = 0
    def  __init__(self, nombre):
        ##Metodo Constructor
        self.nombre = nombre

    def saludar(self , saludo):
        print(saludo + self.nombre)


@property  ##getter
def  edad(self):
    return self.__edad

class Empleado(Usuario):
    salario = 140000

    def modificar_salario(self,salario): ##Setter
        self.salario = salario

    def ver_salario(self):  ##Getter
        print(self.salario)

    def saludar(self):
        print ("Mi nombre  es:  "+self.nombre+"  y  gano: "+ str(self.salario) )

    

empleado =  Empleado("Facu")
empleado.edad =  20
print(empleado.edad)
