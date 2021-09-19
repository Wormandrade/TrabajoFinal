#1.- Dado el siguiente  diagrama de clases en UML, programar las respectivas clases en python.
# Observaciones: 
# 1.- Tomar en consideracion la herrencia entre cada una de las clases según el diagrama.
# 2.- Las clases que no tienen atributos o métodos, implementar al menos con el constructo por defecto y sobreescribir el método "__str__"

#Superclases
class Persona():
    #Constructor
    def __init__(self, email, direccion, telefono):
        self.__email = email
        self.__direccion = direccion
        self.__telefono = telefono

    def __str__(self):
        return f'Objeto Persona : {self.__email} {self.__direccion} {self.__telefono}'

    #Getters y Setters
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, correo):
        self.__email = correo
    
    @property
    def direccion(self):
        return self.__direccion
    
    @direccion.setter
    def direccion(self, direc):
        self.__direccion = direc
    
    @property    
    def telefono(self):
        return self.__telefono
    
    @telefono.setter
    def telefono(self, fono):
        self.__telefono = fono
    
class Personal():
    #Constructor
    def __init__(self, nombres, apellidos, fecha_contrato):
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__fecha_contrato = fecha_contrato

    def __str__(self):
        return f'Objeto Personal : {self.__nombres} {self.__apellidos} {self.__fecha_contrato}'

    #Getters y Setters
    @property
    def nombres(self):
        return self.__nombres
    
    @nombres.setter
    def nombres(self, nombres):
        self.__nombres = nombres
    
    @property
    def apellidos(self):
        return self.__apellidos
    
    @apellidos.setter
    def apellidos(self, apellidos):
        self.__apellidos = apellidos
    
    @property    
    def fecha_contrato(self):
        return self.__fecha_contrato

    @fecha_contrato.setter
    def fecha_contrato(self, fecha_contrato):
        self.__fecha_contrato = fecha_contrato

class Fisica(Persona):
    #Constructor
    def __init__(self, email, direccion, telefono, dni):
        super().__init__(email, direccion, telefono)
        self.__dni = dni
        
    def __str__(self):
        return f'Objeto Fisica : Superclase: Persona, atributo DNI: {self.__dni}' 
    
    #Getters y Setters
    @property    
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni


class Juridica(Persona):
    #Constructor
    def __init__(self, email, direccion, telefono, cif):
        super().__init__(email, direccion, telefono)
        self.__cif = cif

    def __str__(self):
        return f'Objeto Juridica : Superclase: Persona, atributo CIF: {self.__cif}'
    
    #Getters y Setters
    @property    
    def cif(self):
        return self.__cif

    @cif.setter
    def cif(self, cif):
        self.__cif = cif

class Veterniario(Personal):
    #Constructor
    def __init__(self, nombres, apellidos, fecha_contrato):
        super().__init__(nombres, apellidos, fecha_contrato)
    
    def __str__(self):
        return f'Objeto Veterinario : Superclase: Personal'

class Auxiliar(Personal):
    #Constructor
    def __init__(self, nombres, apellidos, fecha_contrato):
        super().__init__(nombres, apellidos, fecha_contrato)
    
    def __str__(self):
        return f'Objeto Auxiliar : Superclase: Personal'

class ElementoHistorico():
    def __str__(self):
        return f'Objeto ElementoHistorico'

class Animal():
    #Constructor
    def __init__(self, tipo, nombre, edad):
        self.__tipo = tipo
        self.__nombre = nombre
        self.__edad = edad
    
    def __str__(self):
        return f'Objeto Animal : tipo: {self.__tipo}, nombre: {self.__nombre}, edad: {self.__edad}'
    
    #Getters y Setters
    @property    
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo
    
    @property    
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property    
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__nombre = edad

class Historico():
    #Contructor
    def __init__(self, ref_historico):
        self.__ref_historico = ref_historico
    
    def __str__(self):
        return f'Objeto Historico : referencia historico: {self.__ref_historico}'
    
    #Getters y Setters
    @property    
    def ref_historico(self):
        return self.__ref_historico

    @ref_historico.setter
    def ref_historico(self, ref_histor):
        self.__ref_historico = ref_histor
    
class Diagnostico():
    #Contructor
    def __init__(self, fecha, descripcion):
        self.__fecha = fecha
        self.__descripcion = descripcion
    
    def __str__(self):
        return f'Objeto Diagnostico : fecha: {self.__fecha}, descripcion: {self.__descripcion}'
    
    #Getters y Setters
    @property    
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha

    @property    
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self.__descripcion = descripcion

class Factura():
    #Contructor
    def __init__(self, ref_factura):
        self.__ref_factura = ref_factura
    
    def __str__(self):
        return f'Objeto Factura : referencia factura: {self.__ref_factura}'

    #Getters y Setters    
    @property    
    def ref_factura(self):
        return self.__ref_factura
    
    @ref_factura.setter
    def ref_factura(self, ref_fac):
        self.__ref_factura = ref_fac

class ElementoFactura():
    #Contructor
    def __init__(self, elemento, precio, cantidad):
        self.__elemento = elemento
        self.__precio = precio
        self.__cantidad = cantidad
    
    def __str__(self):
        return f'Objeto Elemento factura : elemento: {self.__elemento}, precio: {self.__precio}, cantidad: {self.__cantidad}'

    #Getters y Setters    
    @property    
    def elemento(self):
        return self.__elemento
    
    @elemento.setter
    def elemento(self, elemen):
        self.__elemento = elemen
    
    @property    
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, costo):
        self.__precio = costo
    
    @property    
    def cantidad(self):
        return self.__cantidad
    
    @cantidad.setter
    def cantidad(self, unidades):
        self.__cantidad = unidades