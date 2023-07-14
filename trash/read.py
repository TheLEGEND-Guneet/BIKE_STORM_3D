import pickle
def read():
    file=open('subscription.dat','rb')
    try:
        while True:
            dic=pickle.load(file)
            print(dic)
    except EOFError:
        file.close()
def write():
    file=open('subscription.dat','wb')
    file.close()
read()
#write()