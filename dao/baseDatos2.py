import sqlite3
from sqlite3 import Error
from model.areas import Areas

class Areasdao:
    def create(conn):
        try:
            sql="""create table if not exists areas(
                id integer PRIMARY KEY,
                descri varchar(100) not null,
                estado varchar(1)
            )
            """
            cursor = conn.cursor()
            cursor.execute(sql)

        except Error as e:
            print(e)
            wait=input('**** Error - digite cualquier tecla para continuar..')

    def insertar(conn,areasdao):
        sql = """insert into areas (descri,estado)
        values (?,?) """
        try:
            parametro = (areasdao[0],areasdao[1])
            cursor = conn.cursor()
            cursor.execute(sql,parametro)
            conn.commit()
            wait=input('** Registro agregado **')
        except Error as e:
            print(e)
            wait=input('** Error ..pulse cualquier tecla para continuar..')

    def actualizar(conn,id,areas):
        sql = """update areas set descri = ?,
                                    estado=?
                                    where id=?
        """
        try:
            cursor = conn.cursor()
            parametro = (areas.descri,areas.estado, id)
            cursor.execute(sql, parametro)
            conn.commit()
            wait = input(
                '** Registro Actualizad-pulse cualquier tecla para continuar...**')
                
        except Error as e:
            print(e)
            wait = input("Error: Pulse una tecla para continuar...")

    def buscar(conn,id):
        try:
            sql="select * from areas where id=?"
            cursor = conn.cursor()
            cursor.execute(sql,(id,))
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(e)
            wait=input("Error: Pulse una tecla para continuar...")

    def listar(conn):
        try:
            sql="select * from areas"
            cursor=conn.cursor()
            cursor.execute(sql)
            rows=cursor.fetchall()
            print("\t\t ================================")
            print("\t\t      Listado de tabla areas")
            print("\t\t codigo  Descripcion    Estado")
            print("\t\t ================================")
            for row in rows:
                print("\t\t\t"+str(row[0])+"\t"+row[1]+"\t"+row[2])
            wait=input("*** pulse cualquier tecla para continuar..")
        except Exception as e:
            print(e)
            wait=input("Error.. pulse cualquier tecla para continuar..")

    def eliminar(conn, id):
        sql = "DELETE FROM areas WHERE id=?"
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
        wait = input("  ***** Registro borrado *****")