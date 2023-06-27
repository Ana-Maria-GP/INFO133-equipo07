import os
in_user     = input("Usuario    : ")
os.system(f"mysqldump -u {in_user} -p COLOMBIA > Proyecto_colombia.sql")
print("Dump created successfully")