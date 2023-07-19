# Genera una pequeña aplicación, para registrar un usuario en memoria o base
# de datos. Tendrás que tener una clase en un fichero repository, donde haya
# diferentes métodos (add, get … ).
# La aplicación tendrá dos puntos de entrada:
# - “/create/user” à Creación de usuario
# Ejemplo: POST à /créate/user/1/pepe/25
# - “/user/id” à Obtención de usuario
# Ejemplo: GET à /user/1


from usuario import User
from repository import solicitudes


if __name__ == '__main__':
    query_usuario = solicitudes()

    lista_datos_memoria = query_usuario.data
    w = query_usuario.print_data(lista_datos_memoria)
    print(w)
    print("Por favor indique si desea INSERTAR, ELIMINAR, SELECCIONAR, usuarios aleatorios en memoria o TERMINAR borrando todo:")
    encendido = "off"
    while encendido == "off":
        decision = input("Que desea hacer:")
        match decision:
            case "INSERTAR":
                num_añadir = int(input("Cuantos datos aleatorios desea añadir:"))
                for i in range(0,num_añadir):
                    usuario_definicion = [i, 'Wilson', 'Forero', 20 + i,  f'Wilson{i}@gmail.com']
                    query_usuario.add(usuario_definicion)

                print(f"Se añadieron {num_añadir} usuarios en memoria")
            case "SELECCIONAR":
                for i in range(0, 5):
                    print(query_usuario.get(i))
            case "TERMINAR":
                encendido = "on"
                print("Se ha borrado todos los usuarios en memoria")
            case _:
                print("El comando no se reconoce, solo puede escribir INSERTAR, ELIMINAR, SELECCIONAR o TERMINAR:")

