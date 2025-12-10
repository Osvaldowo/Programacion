# ===============================
# ========= Encapsulado =========
# ===============================
# En Python, los atributos privados se definen
# utilizando un doble guion bajo (__) al inicio del nombre del atributo.

class CuenntaBancaria:
    def __init__(self, titular, saldo_inicial):
        
        self.titular = titular # Atributo público
        
        self.__saldo = saldo_inicial  # Atributo privado
        
    def ver_saldo(self):
        
        return self.__saldo  # Acceso controlado al atributo privado
    
cuenta = CuenntaBancaria("Oswiwi", 1000)

print(f"Titular: {cuenta.titular}")
print(f"Saldo inicial: {cuenta.ver_saldo()}")


