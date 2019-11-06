import Pyro4
import base64
import json
import sys
import os

namainstance = sys.argv[1] or "fileserver"

def get_fileserver_object():
    uri = "PYRONAME:{}@localhost:7777" . format(namainstance)
    fserver = Pyro4.Proxy(uri)
    return fserver

if __name__=='__main__':
    f = get_fileserver_object()
    os.chdir(namainstance)
    path = os.getcwd()
    f.create(path, 'slide1.txt')
    f.update(path, 'slide1.txt', "wedusku")

    # f.create(path, 'slide1.txt')
    # f.update(path,'slide1.txt', content = open('FFF-slide1.txt','rb+').read())
    # f.create(path, 'slide2.pptx')
    # f.update(path,'slide2.pptx', content = open('FFF-slide2.pptx','rb+').read())
    # fuc = os.listdir()
    # print(f.list(path))
    # d = f.read(path,'slide1.pdf')
    # #kembalikan ke bentuk semula ke dalam file name slide1-kembali.pdf
    # open('slide1-kembali.pdf','w+b').write(base64.b64decode(d['data']))
    #
    # k = f.read(path,'slide2.pptx')
    # #kembalikan ke bentuk semula ke dalam file name slide2-kembali.pptx
    # open('slide2-kembali.pptx','w+b').write(base64.b64decode(k['data']))


