from socket import *

def Socket_client():
    try:
        client = socket() #定义协议类型,相当于生命socket类型,同时生成socket连接对象
        client.connect(('192.168.1.3',8000))
        while True:
            msg = input(">>>").strip()
            if len(msg) ==0:
                continue
            client.send(msg.encode("utf-8"))
            data = client.recv(1024)#这里是字节1k
            print("recv:>",data.decode())
        client.close()
    except ConnectionError as ex:
        print(ex)
 
if __name__ == "__main__":
    Socket_client()
