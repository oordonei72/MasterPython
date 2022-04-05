from re import A
import sqlite3

from model.personal import Personal
from model.areas import Areas
from utilidades.librerias import *
from dao.baseDatos import PersonalDao
from dao.baseDatos2 import Areasdao


if __name__=='__main__':

    try:
        conn =sqlite3.connect('mybasedatos.db')
        PersonalDao.create(conn)
        Areasdao.create(conn)
        sw=True
        while sw:
            opc=menu()
            if opc==1:
                sw_op1=True
                while sw_op1:
                    opc1=submenu('Tabla de Empleados')
                    if opc1==1:
                        lista_datos =insertar()
                        empleado = Personal(lista_datos[0],lista_datos[1],lista_datos[2],lista_datos[3])
                        PersonalDao.insertar(conn,empleado)
                    elif opc1==2:
                        idEliminar=int(input("Ingrese codigo a Actualizar: "))
                        datos= PersonalDao.buscar(conn,idEliminar)
            
                        print('Deseas modificar el: (si no desas dejar en blanco):')
                        for dat in datos:
                            nomb=input('nombre ['+dat[1]+' ]:')
                            ape=input('apellido['+dat[2]+' ]:')
                            fec=input('Fecha nac['+dat[3]+' ]:')
                            suel=int(input('Sueldo Basico:'+str(dat[4])))
                        if nomb=="":
                            nomb=dat[1]
                        if ape=="":
                            ape=dat[2]
                        if fec=="":
                            fec=dat[3]
                        if suel=="":
                            suel=dat[4]


                        empleado_modificar = Personal(nomb,ape,fec,suel)
                        PersonalDao.actualizar(conn,idEliminar,empleado_modificar)

                
                    elif opc1==3:
                        limpiar_pantalla()
                        PersonalDao.listar(conn)
                    elif opc1==4:
                        id_eliminar = int(input("ingrese el codigo a Eliminar: "))
                        PersonalDao.eliminar(conn,id_eliminar)
                    elif opc1==5:
                        sw_op1=False
            elif opc==2:
                
                sw_op2=True
                while sw_op2:
                    opc2=submenu('Tabla de Areas')
                    if opc2==1:
                       
                        listaIng = pedir_datos_area()
                        Areasdao.insertar(conn,listaIng)
                    elif opc2==2:
                        idEliminar=int(input("Ingrese codigo a Actualizar: "))
                        datos= Areasdao.buscar(conn,idEliminar)
            
                        print('Deseas modificar el: (si no desas dejar en blanco):')
                        for dat in datos:
                            descri=input('Descripcion ['+dat[1]+' ]:')
                            estado=input('Estado['+dat[2]+' ]:')
                            
                        if descri=="":
                            descri=dat[1]
                        if estado=="":
                            estado=dat[2]
                        
                        area_modificar = Areas(descri,estado)
                        Areasdao.actualizar(conn,idEliminar,area_modificar)

                
                    elif opc2==3:
                        limpiar_pantalla()
                        Areasdao.listar(conn)
                    elif opc2==4:

                        id_eliminar = int(input("ingrese el codigo a Eliminar: "))
                        print(Areasdao.buscar(conn,id_eliminar))
                        sw_resp=True
                        while sw_resp:
                            resp=input("¿Estas seguro de eliminar[Si/No]?:")
                            if (resp=="Si" or resp=="si" or resp=="No" or resp=="no"):
                                sw_resp=False

                        if (resp=="Si" or resp=="si"):
                            Areasdao.eliminar(conn,id_eliminar)


                    elif opc2==5:
                        sw_op2=False
            elif opc==3:
                sw=False
    except Exception as e:
        print(e)
    finally:
        conn.close