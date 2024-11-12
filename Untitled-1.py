class Contacto:
    """
    Clase que representa un contacto con nombre y correo electrónico.
    """
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f"Contacto: {self.nombre}, Email: {self.email}"

class ListaContactos:
    """
    Clase que gestiona una lista de contactos con métodos para insertar,
    eliminar y enviar mensaje a los contactos.
    """
    def __init__(self):
        self.contactos = []  # Lista vacía para almacenar contactos

    def insertar_contacto(self, contacto):
        """
        Inserta un nuevo contacto en la lista.
        
        Parámetros:
        - contacto (Contacto): Objeto de tipo Contacto a insertar en la lista.
        """
        self.contactos.append(contacto)
        print(f"{contacto.nombre} ha sido añadido a la lista de contactos.")

    def eliminar_contacto(self, nombre):
        """
        Elimina un contacto de la lista por su nombre.
        
        Parámetros:
        - nombre (str): Nombre del contacto a eliminar.
        """
        for i, contacto in enumerate(self.contactos):
            if contacto.nombre == nombre:
                del self.contactos[i]
                print(f"{nombre} ha sido eliminado de la lista de contactos.")
                return
        print(f"Contacto con nombre {nombre} no encontrado en la lista.")

    def enviar_mensaje(self, nombre, mensaje):
        """
        Envía un mensaje a un contacto específico.
        
        Parámetros:
        - nombre (str): Nombre del contacto al que se enviará el mensaje.
        - mensaje (str): El mensaje a enviar.
        """
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                print(f"Enviando mensaje a {contacto.email}: {mensaje}")
                return
        print(f"Contacto con nombre {nombre} no encontrado en la lista.")
        
    def mostrar_contactos(self):
        """
        Muestra todos los contactos en la lista.
        """
        print("Lista de contactos:")
        for contacto in self.contactos:
            print(contacto)