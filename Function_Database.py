# Definir función .max():

def custom_max(n1: int, n2: int):
    """
    Función creada manualmente para obtener el máximo de dos números enteros.

    Parameters
    ----------
    n1 : int
        Primer número a comparar.
    n2 : int
        Segundo número a comparar.

    Returns
    -------
    n : Devuelve el máximo de ambos valores.

    """
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    elif n1 == n2:
        raise Exception("Los valores no pueden ser iguales.")
    else:
        raise Exception("Ha ocurrido un error")

def max_de_tres(n1: int,n2: int,n3: int):
    """
    Defino el funcionamiento

    Parameters
    ----------
    n1 : TYPE
        DESCRIPTION.
    n2 : TYPE
        DESCRIPTION.
    n3 : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    n = custom_max(n1,n2)
    n_final = custom_max(n3,n)
    return n_final


def test_for_int(num):
    try:
        num = int(num)
        message = str(num) + " is an integer. Good job!"

    # this exception handles any entry that was NOT an integer
    except ValueError:
        message = "Error: You did not provide a whole number."
    return message

# ask for user input
response = input("Enter a number: ")
print(test_for_int(response))

def suma_indefnida(a,b,*numeros):
    suma = a+b
    for num in numeros:
        suma += num
    return suma

print(suma_indefnida(2,3,6,1,2))

def buildConfig(nombreApp,idApp,*config):
    body = {
        "nombreApp":nombreApp,
        "idApp":idApp,
        "roles":[],
        "permisos":[],
        }
    for args in config:
        print(args)
    print(body)

print(buildConfig("Caliapp",232,["admin","engineer"],["read","write","remove"]))

def buildConfig2(nombreApp,idApp,**config):
    body = {
        "nombreApp":nombreApp,
        "idApp":idApp,
        "roles":[],
        "permisos":[],
        }
    if config.get('roles'):
        body['roles'] = config.get('roles')
    if config.get('permisos'):
        body['permisos'] = config.get('permisos')

    # Otra forma de usar los if:
    # body['roles'] = config.get('roles') if config.get('roles') else None
    # body['permisos'] = config.get('permisos') if config.get('permisos') else None

    print(body)

print(buildConfig2("Caliapp",232,roles=["admin","engineer"],permisos=["read","write","remove"]))
























