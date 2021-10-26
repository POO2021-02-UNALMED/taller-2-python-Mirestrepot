from typing import List


class Asiento:
    def __init__(self, color:str, precio:int, registro:int) -> None:
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color:str):
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

        contador=0

        for i in self.asientos:
            if i!= None:
                contador +=1
        return contador



    def verificarIntegridad(self):
        for i in self.asientos:
            if i!= None:
                if i.registro != self.registro or i.registro != self.motor.registro:
                    return print("Las piezas no son originales")
            
        return print  ("Auto original")

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
