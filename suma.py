class Operaciones:
    def suma(self, primerSumando, segundoSumando):
        return primerSumando + segundoSumando

if __name__ == '__main__':
    primerSumando = int(input("Ingrese el primer sumando: "))
    segundoSumando = int(input("Ingrese el segundo sumando: "))

    # Crear una instancia de la clase Operaciones
    operacion = Operaciones()
    print(f"{primerSumando} + {segundoSumando} = {operacion.suma(primerSumando, segundoSumando)}")
