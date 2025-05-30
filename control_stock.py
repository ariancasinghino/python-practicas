import datetime


def mostrar_menu():
    print("1- Cargar Productos\n")
    print("2- Registrar Ventas\n")
    print("3- Reporte Productos con poco Stock\n")
    print("4- Guardar los datos en archivo\n")
    print("5- Salir\n")
    
def carga_producto(libro):
    producto = input("Inserte el nombre del producto. ").title()
    categoria = input("Inserte la categoía del producto. ").title()
    stock_inicial = float(input("Ingrese el stock inicial. "))
    if producto not in libro:
        libro[producto] = {"categoria": categoria, "stock": stock_inicial}
        print(f"Se registro el producto: {producto}, en la categoría: {categoria}, con un stock inicial de: {stock_inicial}")

    else:
        respuesta = input("El producto ya esta registrado, desea modificar el stock inicial (s/n)?. ")
        if respuesta == "s":
            nuevo_stock_incial = float(input("Ingrese el nuevo stock inicial. "))
            libro[producto]["stock"] = nuevo_stock_incial
            print(f"El producto: {producto}, se le actualizo su stock inicial a: {nuevo_stock_incial}")
        else:
            print("No se registraron cambios.")


def registrar_ventas(libro):
    producto_vendido = input("Que producto se vendio. ").title()
    if producto_vendido in libro:
        venta = float(input("Cual es la cantidad de la venta?. "))
        if libro[producto_vendido]["stock"] >= venta:
            libro[producto_vendido]["stock"] -=  venta
            print(f"Se vendio {venta} de {producto_vendido}")
        else:
            print("Error: La venta supera el stock. Pruebe nuevamente.")


def reporte_poco_stock(libro):
    for producto, datos in libro.items():
        if datos["stock"] < 5:
            print(f"{producto} tiene {datos['stock']} unidades\n")

def guardar_datos(libro):
    fecha = datetime.date.today().strftime("%Y-%m-%d")
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    with open(f"reporte_{fecha}.txt", "w") as archivo:
        archivo.write(f"Reporte generado el {fecha} a las {hora}\n")
        if libro:
            for producto, datos in libro.items():
                stock = datos["stock"]
                categoria = datos["categoria"]
                archivo.write(f"{producto}: {stock} unidades - Categoría: {categoria}\n")
        else:
            archivo.write("No hay datos para guardar.\n")


def main():
    libro = {}
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion.isdigit():
            opcion = int(opcion)
            if opcion == 1:
                carga_producto(libro)
            elif opcion == 2:
                registrar_ventas(libro)
            elif opcion == 3:
                reporte_poco_stock(libro)
            elif opcion == 4:
                guardar_datos(libro)
            elif opcion == 5:
                print("Hasta luego")
                break
            else:
                print("Opción inválida, intente de nuevo.")
        else:
            print("Por favor ingrese un número válido.")

if __name__ == "__main__":
    main()