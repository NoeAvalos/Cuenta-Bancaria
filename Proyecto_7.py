#La clase Persona tiene dos atributos: nombre y apellido. Estos atributos se inicializan
# a través del método __init__ que es un método especial que se llama automáticamente
#cuando se crea un objeto de esta clase. Este método recibe dos parámetros: 
#nombre y apellido que se asignan a los atributos correspondientes usando la palabra clave self.
class Persona:
    def __init__(self, nombre,apellido):
        self.nombre = nombre
        self.apellido =apellido
#la clase Cliente hereda de Persona y además tiene dos nuevos atributos: numero_cuenta y balance. En su método __init__, se 
# llama al método __init__ de la clase Persona usando la función super() y se le pasan los mismos parámetros que recibió Cliente.
# Después, se asignan los nuevos atributos.
class Cliente(Persona):
    def __init__(self,nombre,apellido,numero_cuenta,balance=0):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
 #El método __str__ es otro método especial 
 # que devuelve una representación en forma de cadena del objeto. En este caso, devuelve una cadena con el nombre, apellido, número de cuenta y balance del cliente.
    def __str__(self):
        return f"Nombre y apellido: {self.nombre} {self.apellido}, numero de cuenta: {self.numero_cuenta}, balance: {self.balance}"
    #Los métodos depositar y retirar permiten depositar y retirar
    #  dinero de la cuenta del cliente, respectivamente. En el caso del método retirar, se verifica que haya suficiente saldo antes de realizar la operación.
    def depositar(self, deposito):
        self.balance+=deposito
        print(f"Dinero depositado")

    def retirar(self, retiro):
        if self.balance >= retiro:
            self.balance-= retiro
            print("Dinero retirado")
        else:
            print("No tienes fondos")
#Por último, la función cliente_nuevo pide al usuario que ingrese su nombre, apellido y número de cuenta para crear un nuevo objeto de la clase Cliente.
# La función inicio crea un objeto Cliente llamando a cliente_nuevo, y luego entra en un ciclo que permite al usuario depositar o retirar dinero
# de su cuenta hasta que decida finalizar la operación.

    
def cliente_nuevo():
    nombre_cliente= input("Ingrese su nombre: ")
    apellido_cliente= input("Ingrese su apellido: ")
    num_cuenta_cliente= input("Ingrese su numero de cuenta: ")
    cliente= Cliente(nombre_cliente,apellido_cliente,num_cuenta_cliente)
    return cliente

def inicio():
    mi_cliente= cliente_nuevo()
    print(mi_cliente)
    continua = 0
    while continua != "S": 
        continua = input("Elija una opcion:  D para depositar, R para retirar, S para finalizar la operacion")
        if continua == "D":
            monto_deposito= int(input("Ingrese su monto a depositar:" ))
            mi_cliente.depositar(monto_deposito)
        elif continua == "R":
            monto_retiro= int(input("Ingrese un monto a retirar: "))
            mi_cliente.retirar(monto_retiro)
        print(mi_cliente)
    print("Ha finalizado la operacion")


inicio()

    