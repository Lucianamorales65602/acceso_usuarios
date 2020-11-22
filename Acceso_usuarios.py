import sqlite3
from sqlite3 import Error
import time
import re

def crear_conexion(db_file):
    """crea una conexion a una base de datos SQLite
        especificada por db_file
        :param db_file: database file
        :return : Connection object or None
        """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def crear_tablas(conn):
    """crea una tabla mediante los campos de crear_tabla_sql
    :param create_table_sql: a CREATE TABLE statement
    :param conn: Connection object
    :return:
    """

    sql_crea_tabla_usuarios = """ CREATE TABLE IF NOT EXISTS usuarios (
                                    usuarioID integer PRIMARY KEY,
                                    nombre text NOT NULL,
                                    Apaterno text,
                                    Amaterno text,
                                    telefono integer,
                                    correo text,
                                    ciudad text,
                                    Fnacimiento datetime,
                                    nivel integer,
                                    password text,
                                    user_name text
                                ); """


    sql_crea_tabla_roles = """ CREATE TABLE IF NOT EXISTS roles (
                                    rolID integer PRIMARY KEY,
                                    nivelID int NOT NULL,
                                    funcionID integer,
                                    FOREIGN KEY (nivelID) REFERENCES usuarios (usuarioID),
                                    FOREIGN KEY (funcionID) REFERENCES funciones (funcionID)                                    
                                ); """

    sql_crea_tabla_funciones = """ CREATE TABLE IF NOT EXISTS funciones (
                                    funcionID integer PRIMARY KEY,
                                    nombre integer NOT NULL,
                                    atributo text NOT NULL
                                ); """

    sql_query_inserta_admin = '''INSERT INTO usuarios(nombre,Apaterno,Amaterno,telefono,correo,ciudad,Fnacimiento,nivel,password,user_name)
                                 VALUES(?,?,?,?,?,?,?,?,?,?) '''

    sql_query_inserta_roles = '''INSERT INTO roles(nivelID,funcionID)
                                  VALUES(?,?) '''

    sql_query_inserta_funciones = '''INSERT INTO funciones(nombre,atributo)
                                     VALUES(?,?) '''

    try:
        c = conn.cursor()
        c.execute(sql_crea_tabla_usuarios)
        c.execute(sql_crea_tabla_roles)
        c.execute(sql_crea_tabla_funciones)

        sqlite_select_query = """SELECT * FROM usuarios"""
        c.execute(sqlite_select_query)
        records = c.fetchall()
        #print("Total registros en usuarios: ", len(records))
        if(len(records) == 0):
            print("Registrando parámetros iniciales....")
            print("Capture los datos para el admin  **")
            error_nombre = 1
            while(error_nombre == 1):
                nombre = input("Nombre: ")
                if(len(nombre) <= 30):
                    error_nombre = 0
                else:
                    print("Sólo 30 caracteres")
                    error_nombre = 1
            Apaterno = input("Apellido Paterno: ")
            Amaterno = input("Apellido Materno: ")
            error_tel = 1
            while(error_tel == 1):
                telefono = input("Teléfono (10 números): ")
                if(telefono.isdigit()):
                    if(len(telefono) != 10):
                        print("Deben ser 10 dígitos!!")
                        error_tel = 1
                    else:
                        error_tel = 0
                else:
                    print("Sólo números!!")
                    error_tel = 1
            error_correo = 1
            while (error_correo == 1):
                correo = input("Correo: ")
                if(re.match('^[(a-z0-9\\_\\-\\.)]+@[(a-z0-9\\_\\-\\.)]+\\.[(a-z)]{2,15}$',correo.lower())):
                    error_correo = 0
                else:
                     print ("Teclea un correo válido")
                     error_correo = 1            
            correo = input("Correo: ")
            ciudad = input("Ciudad: ")
            error_fecha = 1
            while(error_fecha == 1):
                Fnacimiento = input("Fecha de Nacimiento (dd/mm/yyyy): ")
                if validateDateEs(Fnacimiento):
                    error_fecha = 0
                else:
                    print("Fecha incorrecta")
                    error_fecha = 1            
            nivel = "1"
            password = input ("Password: ")
            user = "admin"
            tupla = (nombre,Apaterno,Amaterno,telefono,correo,ciudad,Fnacimiento,nivel,password,user)
            c.execute(sql_query_inserta_admin,tupla)
            conn.commit()
            print("Registro exitoso!!")

        sqlite_select_query = """SELECT * FROM roles"""
        c.execute(sqlite_select_query)
        records = c.fetchall()
        #print("Total registros en roles: ", len(records))
        if(len(records) == 0):
            print("Registrando parámetros iniciales....")
            tupla = ("1","1")
            c.execute(sql_query_inserta_roles,tupla)
            conn.commit()
            tupla = ("1","2")
            c.execute(sql_query_inserta_roles,tupla)
            conn.commit()
            tupla = ("1","3")
            c.execute(sql_query_inserta_roles,tupla)
            conn.commit()
            tupla = ("1","4")
            c.execute(sql_query_inserta_roles,tupla)
            conn.commit()
            tupla = ("1","5")
            c.execute(sql_query_inserta_roles,tupla)
            conn.commit()
            tupla = ("1","6")
            c.execute(sql_query_inserta_roles,tupla)
            conn.commit()            
            tupla = ("2","1")
            c.execute(sql_query_inserta_roles,tupla)
            conn.commit()
            tupla = ("2","2")
            c.execute(sql_query_inserta_roles,tupla)
            conn.commit()
            tupla = ("2","3")
            c.execute(sql_query_inserta_roles,tupla)
            conn.commit()
            tupla = ("2","4")
            c.execute(sql_query_inserta_roles,tupla)
            conn.commit()
            tupla = ("2","5")
            c.execute(sql_query_inserta_roles,tupla)
            conn.commit()
            tupla = ("2","6")
            c.execute(sql_query_inserta_roles,tupla)
            conn.commit()            
            tupla = ("3","6")
            c.execute(sql_query_inserta_roles,tupla)
            conn.commit()
            print("Registro exitoso!!")


        sqlite_select_query = """SELECT * FROM funciones"""
        c.execute(sqlite_select_query)
        records = c.fetchall()
        #print("Total registros en funciones: ", len(records))
        if(len(records) == 0):
            print("Registrando parámetros iniciales....")
            tupla = ("1","Crear")
            c.execute(sql_query_inserta_funciones,tupla)
            conn.commit()
            tupla = ("1","Listar")
            c.execute(sql_query_inserta_funciones,tupla)
            conn.commit()
            tupla = ("1","Modificar")
            c.execute(sql_query_inserta_funciones,tupla)
            conn.commit()
            tupla = ("1","Eliminar")
            c.execute(sql_query_inserta_funciones,tupla)
            conn.commit()
            tupla = ("1","Filtrar")
            c.execute(sql_query_inserta_funciones,tupla)
            conn.commit()
            tupla = ("1","Desplegar")
            c.execute(sql_query_inserta_funciones,tupla)
            conn.commit()
            tupla = ("2","Desplegar")
            c.execute(sql_query_inserta_funciones,tupla)
            conn.commit()
            tupla = ("3","Desplegar")
            c.execute(sql_query_inserta_funciones,tupla)
            conn.commit()
            tupla = ("4","Desplegar")
            c.execute(sql_query_inserta_funciones,tupla)
            conn.commit()
            tupla = ("5","Desplegar")
            c.execute(sql_query_inserta_funciones,tupla)
            conn.commit()
            print("Registro exitoso!!")
            

    except Error as e:
        print(e)        

def alta_registro_usuario(conn,tupla):
    

    sql = '''INSERT INTO usuarios(nombre,Apaterno,Amaterno,telefono,correo,ciudad,Fnacimiento,nivel,password,user_name)
             VALUES(?,?,?,?,?,?,?,?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql,tupla)
    conn.commit()
    return cur.lastrowid

def actualiza_registro_usuario(conn,tupla):
    """
    update priority, begin_date, and end_date of a task
    :param conn:
    :param task:
    :return: project_id
    """
    sql = ''' UPDATE usuarios
              SET nombre = ?,
                  Apaterno = ?,
                  Amaterno = ?,
                  telefono = ?,
                  correo = ?,
                  ciudad = ?,
                  Fnacimiento = ?,
                  password = ?,
                  user_name = ?
              WHERE usuarioID = ?'''

    cur = conn.cursor()
    cur.execute(sql,tupla)
    conn.commit()

def borrar_usuario(conn,id):
    """
    Delete a task by task id
    :param conn: Connection to the SQLite database
    :param id: id of the task
    :return:
    """

    sql = 'DELETE FROM usuarios where usuarioID = ?'
    cur = conn.cursor()
    cur.execute(sql,(id,))
    conn.commit()

def borrar_todos_los_usuarios(conn):
    """
    Delete all rows in the tasks table
    :param conn: Connection to the SQLite database
    :return:
    """

    sql = 'DELETE from usuarios'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def Leer_tabla_usuarios(conn,sqlite_select_query):
    try:
        sqliteConnection = conn 
        cursor = sqliteConnection.cursor()
        #print("Conectado a SQLite")

        #sqlite_select_query = """SELECT * FROM usuarios"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total de usuarios: ", len(records))
        print("Imprimiendo cada usuario: ")
        for row in records:
            print("Id: ", row[0])
            print("Nombre: ", row[1])
            print("Apellido Paterno: ", row[2])
            print("Apellido Materno: ", row[3])
            print("Teléfono: ", row[4])
            print("Correo : ", row[5])
            print("Ciudad : ", row[6])
            print("Fecha de Nacimiento : ", row[7])
            print("Nivel : ", row[8])
            print("\n")

        cursor.close()

        
    except sqlite3.Error as error:
        print("Falla al leer los datos de la BD de SQLite", error)

    #finally:
        #if(sqliteConnection):
            #sqliteConnection.close()
            #print("La conexión SQLite se cerró ")

def buscar_usuario(conn,clave,sqlite_select_query):
    try:
        sqliteConnection = conn 
        cursor = sqliteConnection.cursor()
        #print("Conectado a SQLite")

        #sqlite_select_query = """SELECT password FROM usuarios WHERE user_name = ?"""
        cursor.execute(sqlite_select_query,(clave,))
        psw = cursor.fetchall()
        if (psw):
            return psw
        else:
            return "Falso"
        
        #cursor.close()
        
    except sqlite3.Error as error:
        print("Falla al leer los datos de la BD de SQLite", error)

    #finally:
        #if(sqliteConnection):
            #sqliteConnection.close()
            #print("La conexión SQLite se cerró ")


def validateDateEs(date):
    """
    Funcion para validar una fecha en formato:
        dd/mm/yyyy, dd/mm/yy, d/m/yy, dd/mm/yyyy hh:mm:ss, dd/mm/yy hh:mm:ss, d/m/yy h:m:s
    """
    for format in ['%d/%m/%Y', '%d/%m/%y', '%d/%m/%Y %H:%M:%S', '%d/%m/%y %H:%M:%S']:
        try:
            result = time.strptime(date, format)
            return True
        except:
            pass
    return False


def main():
    database = r"C:\sqlite\db\accesos.db"

    #Crea la conexion a la base de datos
    conn = crear_conexion(database)
    if conn is None:
        print("Error! no se pudo crear la conexión a la base de datos. ")
    else:
        salir = ""
        intentos = 0
        while(salir != "S" and salir != "s"):
            #intentos = 0
            while (intentos < 3 ):
                crear_tablas(conn)
                user = input("Captura usuario para accesar: ")
                clave = input("Captura Contraseña: ")
                sql = """SELECT password,nivel FROM usuarios WHERE user_name = ?"""
                user_bd = buscar_usuario(conn,user,sql)
                if(user_bd == "Falso"):
                    print("Usuario incorrecto, intenta nuevamente !")
                    intentos += 1
                else:
                    if(user_bd[0][0] == clave):
                        print("Acceso correcto")
                        nivel = user_bd[0][1]
                        print("Nivel: ",nivel)
                        nivel_usuario = nivel
                        sql = """SELECT atributo FROM funciones INNER JOIN roles on funciones.funcionID = roles.funcionID WHERE roles.nivelID = ?"""
                        funciones = buscar_usuario(conn,nivel,sql)
                        x=1
                        for row in funciones:
                            print(x,": ", row[0])
                            x+=1
                        opcion = input("Selecciona una opción: ")
                        if(opcion.isdigit()):
                            if ((int(opcion) >= 1) and (int(opcion) <= x-1)):
                                funcion = funciones[int(opcion)-1][0]
                                if(funcion == "Listar" or funcion == "Desplegar"):
                                    sql = """SELECT * FROM usuarios"""
                                    Leer_tabla_usuarios(conn,sql)
                                if(funcion == "Eliminar"):
                                    id = input("Captura id de Usuario: ")
                                    sql =  """SELECT * FROM usuarios WHERE usuarioID = ?"""
                                    existe_usuario = buscar_usuario(conn,id,sql)
                                    if(existe_usuario != "Falso"):
                                        sql = """SELECT * FROM usuarios WHERE usuarioID = """ + str(id)
                                        Leer_tabla_usuarios(conn,sql)
                                        borrar = input("Está seguro de borrar ? : (S/s)")
                                        if(borrar == 'S' or borrar =='s'):
                                            borrar_usuario(conn,int(id))
                                    else:
                                        print("Id de usuario incorrecto!!")
                                if(funcion == 'Crear'):
                                    error_nombre = 1
                                    while(error_nombre == 1):
                                        nombre = input("Nombre: ")
                                        if(len(nombre) <= 30):
                                            error_nombre = 0
                                        else:
                                            print("Sólo 30 caracteres")
                                            error_nombre = 1
                                    Apaterno = input("Apellido Paterno: ")
                                    Amaterno = input("Apellido Materno: ")
                                    error_tel = 1
                                    while(error_tel == 1):
                                        telefono = input("Teléfono (10 números): ")
                                        if(telefono.isdigit()):
                                            if(len(telefono) != 10):
                                                print("Deben ser 10 dígitos!!")
                                                error_tel = 1
                                            else:
                                                error_tel = 0
                                        else:
                                            print("Sólo números!!")
                                            error_tel = 1
                                    error_correo = 1
                                    while (error_correo == 1):
                                        correo = input("Correo: ")
                                        if re.match('^[(a-z0-9\\_\\-\\.)]+@[(a-z0-9\\_\\-\\.)]+\\.[(a-z)]{2,15}$',correo.lower()):
                                            error_correo = 0
                                        else:
                                            print ("Teclea un correo válido")
                                            error_correo = 1
                                    ciudad = input("Ciudad: ")
                                    error_fecha = 1
                                    while(error_fecha == 1):
                                        Fnacimiento = input("Fecha de Nacimiento (dd/mm/yyyy): ")
                                        if validateDateEs(Fnacimiento):
                                            error_fecha = 0
                                        else:
                                            print("Fecha incorrecta")
                                            error_fecha = 1
                                    #print(nivel_usuario)
                                    if(nivel_usuario == 1):
                                        nivel_user = 2
                                    if(nivel_usuario == 2):
                                        nivel_user = 3
                                    user_temporal = input("Nombre usuario: ")
                                    sql = """SELECT user_name FROM usuarios WHERE user_name = ?"""
                                    existe_user = buscar_usuario(conn,user_temporal,sql)
                                    while(existe_user != "Falso"):
                                        print("Ya existe el nombre de usuario.. captura uno diferente. ")
                                        user_temporal = input("Nombre usuario: ")
                                        sql = """SELECT user_name FROM usuarios WHERE user_name = ?"""
                                        existe_user = buscar_usuario(conn,user_temporal,sql)
                                    user = user_temporal
                                    password = input ("Password: ")
                                    #print(nivel_user)
                                    tupla = (nombre,Apaterno,Amaterno,telefono,correo,ciudad,Fnacimiento,nivel_user,password,user)
                                    alta_registro_usuario(conn,tupla)
                                
                                if(funcion == 'Modificar'):
                                    id = input("Captura id de Usuario: ")
                                    sql = """SELECT usuarioID FROM usuarios WHERE usuarioID = ?"""
                                    existe_ID = buscar_usuario(conn,int(id),sql)
                                    if(existe_ID != "Falso"):
                                        error_nombre = 1
                                        while(error_nombre == 1):
                                            nombre = input("Nombre: ")
                                            if(len(nombre) <= 30):
                                                error_nombre = 0
                                            else:
                                                print("Sólo 30 caracteres")
                                                error_nombre = 1
                                        Apaterno = input("Apellido Paterno: ")
                                        Amaterno = input("Apellido Materno: ")
                                        error_tel = 1
                                        while(error_tel == 1):
                                            telefono = input("Teléfono (10 números): ")
                                            if(telefono.isdigit()):
                                                if(len(telefono) != 10):
                                                    print("Deben ser 10 dígitos!!")
                                                    error_tel = 1
                                                else:
                                                    error_tel = 0
                                            else:
                                                print("Sólo números!!")
                                                error_tel = 1
                                        error_correo = 1
                                        while (error_correo == 1):
                                            correo = input("Correo: ")
                                            if re.match('^[(a-z0-9\\_\\-\\.)]+@[(a-z0-9\\_\\-\\.)]+\\.[(a-z)]{2,15}$',correo.lower()):
                                                error_correo = 0
                                            else:
                                                print ("Teclea un correo válido")
                                                error_correo = 1
                                        ciudad = input("Ciudad: ")
                                        error_fecha = 1
                                        while(error_fecha == 1):
                                            Fnacimiento = input("Fecha de Nacimiento (dd/mm/yyyy): ")
                                            if validateDateEs(Fnacimiento):
                                                error_fecha = 0
                                            else:
                                                print("Fecha incorrecta")
                                                error_fecha = 1
                                        user_temporal = input("Nombre usuario: ")
                                        sql = """SELECT user_name FROM usuarios WHERE user_name = ?"""
                                        existe_user = buscar_usuario(conn,user_temporal,sql)
                                        while(existe_user != "Falso"):
                                            print("Ya existe el nombre de usuario.. captura uno diferente. ")
                                            user_temporal = input("Nombre usuario: ")
                                            sql = """SELECT user_name FROM usuarios WHERE user_name = ?"""
                                            existe_user = buscar_usuario(conn,user_temporal,sql)
                                        user = user_temporal
                                        password = input ("Password: ")
                                        tupla = (nombre,Apaterno,Amaterno,telefono,correo,ciudad,Fnacimiento,password,user,int(id))
                                        actualiza_registro_usuario(conn,tupla)
                                    else:
                                        print("Id de usuario no existe!!")
                            else:
                                print("Opción incorrecta!!")
                        else:
                            print("Opción incorrecta !!")
                    else:
                        print("Acceso denegado")
                        intentos += 1
                    #salir = input("Teclea (S/s) para salir ..")
            time.sleep(5)
            salir = input("Teclea (S/s) para salir ..")
            intentos = 0
           
        



if __name__ == '__main__':
    main()