# =========================================
# =========== Polimorfismo ================
# =========================================
# Sin herencia estricta.

class PDF:
    def abrir(self):
        print("Abriendo un archivo PDF...")
        
class Word:
    def abrir(self):
        print("Abriendo un archivo de Word...")
        
def lector_de_archivos(archivo):
    print("Iniciando el lector de archivos...")
    archivo.abrir()
    
doc1 = PDF()
doc2 = Word()

lector_de_archivos(doc1)
lector_de_archivos(doc2)