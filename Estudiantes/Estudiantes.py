class Person:
    def __init__(self, firstname="Nombre", lastname="Apellido", email="Correo", phone="Teléfono"):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone
        
        print("Mi nombre es", self.firstname, self.lastname, "mi correo es", self.email, "y mi teléfono", self.phone)