import os
import base64
import shutil

class FileServer(object):
    def __init__(self):
        pass

    def create_return_message(self,kode='000',message='kosong',data=None):
        return dict(kode=kode,message=message,data=data)

    def syncserver(self,path='',path2='',nama='',event=""):
        os.chdir(path2)
        fuc = [x for x in os.listdir() if os.path.isdir(x)]
        os.chdir(path)
        for y in fuc:
            print(y)
            if(y is not ".idea" and y is not "__pycache__" and y is not "fileserver1"):
                dir2 = path2 + "\\" + y
                if(event == "notdel"):
                    shutil.copy2(nama,dir2)
                elif(event == "del"):
                    os.remove(dir2 + "\\" + nama)

    def list(self, path=''):
        os.chdir(path)
        print("list ops")
        try:
            daftarfile = []
            for x in os.listdir():
                if x[0:4]=='FFF-':
                    daftarfile.append(x[4:])
            return self.create_return_message('200',daftarfile)
        except:
            return self.create_return_message('500','Error')

    def create(self, path='', name=''):
        os.chdir(path)
        nama = "FFF-{}" . format(name)
        print("create ops {}" . format(nama))
        try:
            if os.path.exists(name):
                return self.create_return_message('102', 'OK','File Exists')
            f = open(nama,'wb',buffering=0)
            f.close()
            os.chdir("..")
            path2 = os.getcwd()
            self.syncserver(path,path2,nama,"notdel")
            return self.create_return_message('100','OK')
        except:
            return self.create_return_message('500','Error')
    def read(self, path='', name=''):
        os.chdir(path)
        nama='FFF-{}' . format(name)
        print("read ops {}" . format(nama))
        try:
            f = open(nama,'r+b')
            contents = f.read().decode()
            f.close()
            return self.create_return_message('101','OK',contents)
        except:
            return self.create_return_message('500','Error')
    def update(self,path='',name='',content=''):
        os.chdir(path)
        nama='FFF-{}' . format(name)
        print("update ops {}" . format(nama))

        if (str(type(content))=="<class 'dict'>"):
            content = content['data']
        try:
            f = open(nama,'w+b')
            f.write(content.encode())
            f.close()
            os.chdir("..")
            path2 = os.getcwd()
            self.syncserver(path, path2, nama, "notdel")
            return self.create_return_message('101','OK')
        except Exception as e:
            return self.create_return_message('500','Error',str(e))

    def delete(self,path='',name='filename000'):
        os.chdir(path)
        nama='FFF-{}' . format(name)
        print("delete ops {}" . format(nama))

        try:
            os.remove(nama)
            os.chdir("..")
            path2 = os.getcwd()
            self.syncserver(path, path2, nama, "del")
            return self.create_return_message('101','OK')
        except:
            return self.create_return_message('500','Error')



if __name__ == '__main__':
    k = FileServer()
    print(k.create('f1'))
    print(k.update('f1',content='wedusku'))
    print(k.read('f1'))
#    print(k.create('f2'))
#    print(k.update('f2',content='wedusmu'))
#    print(k.read('f2'))
    print(k.list())
    #print(k.delete('f1'))
