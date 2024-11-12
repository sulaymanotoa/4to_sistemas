# Definimos la clase Mensaje
class Mensaje:
    # Método constructor: se ejecuta automáticamente cuando creamos un objeto de esta clase
    def __init__(self, contenido):
        self.contenido = contenido  # Atributo que almacena el contenido del mensaje
        self.enviado = False        # Atributo que indica si el mensaje ha sido enviado

    # Método para enviar el mensaje
    def enviar(self):
        if not self.enviado:
            self.enviado = True
            print(f"Mensaje enviado: {self.contenido}")
        else:
            print("El mensaje ya ha sido enviado.")
    
    # Método para modificar el contenido del mensaje
    def modificar(self, nuevo_contenido):
        if not self.enviado:
            self.contenido = nuevo_contenido
            print(f"Mensaje modificado: {self.contenido}")
        else:
            print("No se puede modificar un mensaje ya enviado.")
    
    # Método para eliminar el mensaje
    def eliminar(self):
        if self.enviado:
            print("No se puede eliminar un mensaje ya enviado.")
        else:
            self.contenido = None
            print("Mensaje eliminado.")

# Ejemplo de uso de la clase Mensaje
mensaje1 = Mensaje("Hola, este es un mensaje de prueba.")  # Creamos un objeto de la clase Mensaje

mensaje1.enviar()          # Enviamos el mensaje
mensaje1.modificar("Nuevo contenido")  # Intentamos modificar el mensaje
mensaje1.eliminar()         # Intentamos eliminar el mensaje
