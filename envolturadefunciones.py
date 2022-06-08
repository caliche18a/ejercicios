def suma (v1=0,v2=0):
    return v1 + v2

def operacion(funcion,v1=0,v2=0):
    return funcion(v1=0,v2=0)

funcion_suma = suma
resultado = operacion(funcion_suma,10,20)
print(resultado)