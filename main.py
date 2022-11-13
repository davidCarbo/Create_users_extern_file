import pickle

class Persona():
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print(f'Se ha creado una persona con el nombre de {self.nombre}')

    # Esto lo que hace que se represente el objeto como una clase
    # (por eso lo podemos imprimir y leer bien más adelante)
    def __str__(self):
        return f'{self.nombre}, {self.genero}, {self.edad}'


class ListaPersonas():
    personas = []

    #Creamos esto aquí para que cada vez creemos una instancia de esta clase, se llame
    #al constructor y se cargue todo eso en la variable 'personas' de la instancia creada.
    #Luego para mostrarlo tenemos el método mostrar personas.
    def __init__(self):
        listaDePersonas = open('ficheroExterno', 'ab+')
        listaDePersonas.seek(0)

        try:
            self.personas = pickle.load(listaDePersonas)
            print(f'Se cargaron {len(self.personas)}')
        except:
            print('El fichero está vacío')
        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas = open('ficheroExterno', 'wb')
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostrarInfoFicheroExterno(self):
        print('La información del cichero externo es:')
        for p in self.personas:
            print(p)

miLista = ListaPersonas()
persona = Persona('Manolo', 'Masculino', 39)
miLista.agregarPersonas(persona)
miLista.mostrarPersonas()
