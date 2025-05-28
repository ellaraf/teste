import os

def connect_db():
    db_password = "123456"  # senha hardcoded
    print("Conectando com a senha:", db_password)

def delete_file(filename):
    os.system(f"rm -rf {filename}")  # comando shell inseguro

def insecure_eval(user_input):
    eval(user_input)  # execução dinâmica perigosa

filename = input("Digite o arquivo para deletar: ")
delete_file(filename)

user_input = input("Digite um comando Python: ")
insecure_eval(user_input)

connect_db()
