import Pyro4
import Pyro4.errors
import os
import time
uri = "PYRONAME:greetserver@localhost:7777"
hostip = "127.0.0.1"
# def test_with_ns():
#    gserver = Pyro4.Proxy(uri)
#    print(gserver.get_greet('ronaldo'))

def listcommand():
    print("Command yang ada: \n- create \n- edit \n- read \n- list \n- delete")

if __name__=='__main__':
    while True:
        listcommand()
        command = input("ketik command: ").lower()
        cek = os.system("ping -c 1 %s" % hostip)
        if cek == 0:
            print("active!")
        else:
            print("inactive!")
            exit()
        if command == 'create':
            naming = input("nama file: ")
            p = Pyro4.Proxy(uri)
            print(p.createfile(naming))
        elif command == 'edit':
            naming = input("nama file: ")
            content = input("isi: ")
            p = Pyro4.Proxy(uri)
            print(p.editfile(naming,content))
        elif command == 'read':
            naming = input("nama file: ")
            p = Pyro4.Proxy(uri)
            print(p.readfile(naming))
        elif command == 'list':
            path = os.getcwd()
            print(os.listdir())
        elif command == 'delete':
            naming = input("nama file: ")
            p = Pyro4.Proxy(uri)
            print(p.deletefile(naming))
        else:
            print("command tidak ada. Coba yang ada!")

