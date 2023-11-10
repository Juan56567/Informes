import mysql.connector
import bcrypt
import os
import getpass

while True:
    try:
        host = input("Host: ")
        user = getpass.getpass("User: ")
        adminPassword = getpass.getpass("Password: ")
        port = getpass.getpass("Ingrese el puerto")
        database = getpass.getpass("Database: ")

        config = {
            "host": host,
            "user": user,
            "password": adminPassword,
            "database": database,
        }


        conexion = mysql.connector.connect(**config)
        cursor = conexion.cursor()
        print("Conexion exitosa")
        os.system("cls")
        while True:
            newUser = input("Nuevo usuario: ")
            name = input("Nombre: ")
            rol = input("Rol:")
            newpassword = getpass.getpass("Password: ")
            confirmPass = getpass.getpass("Confirmar password: ")

            if newpassword == confirmPass:
                salt = bcrypt.gensalt() 
                hashedpass = bcrypt.hashpw(newpassword.encode('utf-8'),salt)
                hashedpass = hashedpass.decode('utf-8')
                print(hashedpass)
                cursor.execute(f"INSERT INTO users (user,password,name,rol) VALUES ('{newUser}', '{hashedpass}', '{name}', '{rol}')")
                conexion.commit()
                conexion.close()
                print("Ok")
                break
        break     
    except Exception as e:
        print(e)    


#INSERT INTO usuarios (nombre, edad, correo) VALUES ('Juan Pérez', 25, 'juan@example.com');
