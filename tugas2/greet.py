import os

class Func(object):
    def __init__(self):
        pass
    def pingpong(self, hostip=''):
        cek = os.system("ping -c 1 %s" % hostip)
        if cek == 0:
            print("active!")
        else:
            print("inactive!")
            exit()
#    def get_greet(self, name=''):
#      lucky_number = random.randint(1, 100000)
#      return "Hello {}, this is your lucky number {}".format(name, lucky_number)
    def createfile(self,name=''):
        path = os.getcwd()
        file = open(path + '/' + name, 'w')
        file.close()
        return "%s dibuat" % name

    def readfile(self,name=''):
        path = os.getcwd()
        try:
            file = open(path + '/' + name, 'r')
        except FileNotFoundError:
            return "file tidak ada"
        return file.read()

    def listfile(self):
        path = os.getcwd()
        return(os.listdir(path))

    def editfile(self,name='',content=''):
        path = os.getcwd()
        try:
            file = open(path + '/' + name, 'w+')
        except FileNotFoundError:
            return "file tidak ada"
        file.write(content)
        file.close()
        return self.readfile(name)

    def deletefile(self,name=''):
        path = os.getcwd()
        try:
            os.remove(path + '/' + name)
        except FileNotFoundError:
            return "file tidak ada"
        return "hapus selesai"


if __name__ == '__main__':
    _run = Func()
