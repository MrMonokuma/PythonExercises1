def lunes(prec1):
    precioTotal= prec1-(prec1*0.1)
    return precioTotal

def martes(prec1):
    precioTotal= prec1-(prec1*0.05)
    return precioTotal

def miercoles(prec1):
    precioTotal= prec1-(prec1*0.03)
    return precioTotal

def jueves(prec1):
    precioTotal= prec1-(prec1*0.01)
    return precioTotal

def viernes(prec1):
    precioTotal= prec1-(prec1*0.07)
    return precioTotal

def sabado(prec1):
    precioTotal= prec1
    return precioTotal

def domingo(prec1):
    precioTotal= prec1-(prec1*0.01)
    return precioTotal

def default():
   return "Opción invalida"


def descuentoProducto(dia,precio):
    switch = {
        "l": lunes(precio),
        "m": martes(precio),
        "M": miercoles(precio),
        "j": jueves(precio),
        "v": viernes(precio),
        "s": sabado(precio),
        "d": domingo(precio),
    }
    return switch.get(dia,default)

def main():
    dia = input("Ingrese el día en que se realizará la compra: ")
    precio = int(input("Ingrese el precio del producto: "))
    print("El precio total de su producto es: ", descuentoProducto(dia,precio), "$")

if __name__ == '__main__':
    main()