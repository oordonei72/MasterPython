def limpiar_pantalla():
    import platform
    import os
    if platform.system()=='windows':
        os.system('cls')
    else:
        os.system('clear')
def menu():
    limpiar_pantalla()
    print('\t********************************')
    print('\t     mantenimiento de Tablas')
    print('\t================================')
    print('\t[1] Tabla de Empleados')
    print('\t[2] Tabla de areas')
    print('\t[3] Salir')
    print('\t================================')
    op1 = int(input('\tElija una opcion:'))
    return(op1)

def submenu(titulo):
    limpiar_pantalla()
    print('\t***********************************')
    print(f'\t            {titulo}')
    print('\t===================================')
    print('\t[1] Insertar')
    print('\t[2] Actualizar')
    print('\t[3] Listar')
    print('\t[4] Borrar')
    print('\t[5] volver')
    print('\t===========================')
    op2 = int(input('\tElija una opcion:'))
    return (op2)
    
def insertar():
    try:
       # conn = sqlite3.connect('mybasedatos.db')
        limpiar_pantalla()
        print('\t****************************************')
        print('\t[1] Ingresar un Registro')
        print('\t*****************************************')
        nombre = input('\tNombre:')
        apellido = input('\tApellidos:')
        fechaNac = input('\tfecha Nacimiento:')
        sueldo = input('\tSueldo Basico:')
        return [nombre,apellido,fechaNac,sueldo]
       

    except Exception as e:
        print(e)
       
def pedir_datos_area():
    try:
        limpiar_pantalla()
        print('\t****************************************')
        print('\t[1] Ingresar un Registro')
        print('\t*****************************************')
        descripcion = input('\tDescripción:')
        estado = input('\tEstado [1]activo [2] inactivo:')
        
        return [descripcion,estado]
    except Exception as e:
        print(e)
        wait=input('** Error..pulse cualquier tecla para continuar...') 
