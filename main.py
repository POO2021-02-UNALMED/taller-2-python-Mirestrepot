from typing import List


class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        colores = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in colores:
            self.color = color
        else:
                pass




class Auto:

    cantidadCreados=0

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo=modelo
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro

    def cantidadAsientos(self):

        cont=0

        for i in self.asientos:
            if i!= None:
                cont +=1
        return cont


    def verificarIntegridad(self):
            if self.asientos[0].registro == self.registro:
                if self.registro == self.motor.registro:
                    return print("Auto original")
                else:
                    return print("Las piezas no son originales")
            else:
                return print("Las piezas no son originales")

                
class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self,registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo=="electrico" or tipo=="normal":
            self.tipo=tipo
