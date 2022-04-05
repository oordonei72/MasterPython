import sqlite3
from sqlite3 import Error
from model.personal import Personal


class PersonalDao:
    def create(conn):
        try:
            sql = """ CREATE table if not exists Personal(
                id integer primary key,
                nombre varchar(100) not null,
                apellido varchar(100) not null,
                fecha_nac date,
                sueldo real);"""
            cursor = conn.cursor()
            cursor.execute(sql)

        except Error as e:
            print(e)
            wait = input('****** Error: pulse una tecla  *****')

    def insertar(conn, empleado):
        sql = """insert into personal (nombre,apellido,fecha_nac,sueldo)
                 values (?,?,?,?);"""

        try:
            cursor = conn.cursor()
            parametros = (empleado.nombre, empleado.apellido,
                          empleado.fecha_nac, empleado.sueldo)
            cursor.execute(sql, parametros),
            conn.commit()
            wait = input('*****  Registro Agregado ****')

        except Error as e:
            print(e)
            wait = input('******  pulse una tecla para continuar... *****')

    def listar(conn):
        sql = """ select * from Personal"""
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            print("             LISTADO DE LA TABLA PERSONAL")
            print("========================================================")
            print("\tcodigo\tnombre\tapellido\tfecha Nac.\tSueldo B")
            print("========================================================")
            rows = cursor.fetchall()
            for row in rows:
                print("\t"+str(row[0])+"\t"+row[1]+"\t" +
                      row[2]+"\t"+str(row[3])+"\t"+str(row[4]))
            print("")
            wait = input(
                "** Mensaje: Pulse cualquier tecla para continuar....**")

        except Error as e:
            print(e)
            wait = input("Error: Pulse una tecla para continuar...")

    def buscar(conn, id):
        try:
            sql = "select * from personal where id=?"
            cursor = conn.cursor()
            cursor.execute(sql, (id,))
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(e)
            wait = input("Error: Pulse una tecla para continuar...")

    def actualizar(conn, id, personal):
        sql = """update personal set nombre = ?,
                                    apellido=?,
                                    fecha_nac=?,
                                    sueldo=?
                                    where id=?
        """
        try:
            cursor = conn.cursor()
            parametro = (personal.nombre, personal.apellido,
                         personal.fecha_nac, personal.sueldo, id)
            cursor.execute(sql, parametro)
            conn.commit()
            wait = input(
                '** Registro Actualizad-pulse cualquier tecla para continuar...**')
                
        except Error as e:
            print(e)
            wait = input("Error: Pulse una tecla para continuar...")

    def eliminar(conn, id):
        sql = "DELETE FROM personal WHERE id=?"
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
        wait = input("  ***** Registro borrado *****")
