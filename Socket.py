from socket import *
import time
from openpyxl import load_workbook

index = 0
# 返回当前日期，时间
def Time_Obtain():
    Local_Time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    for index in range(len(Local_Time)):
        if(Local_Time[index]==' '):
            Date = Local_Time[0:index]
            Time = Local_Time[index+1:]
    return Date ,Time,Local_Time
    
def decode(message):
    Date,Time,Local_Time = Time_Obtain()
    d_0 = {0:"障碍",1:"停止",10:"终止"}
    d_1 = {0:"卸货完毕",1:"装货完毕",10:"无操作"}
    d_2 = ("A","B","C","D","E","F","G","H")
    if len(message) == 8:
        message_header = message[:4]    #校验位
        message_flag_0 = message[4:6]   #终止，停止，障碍
        message_flag_1 = message[6:8]   #装、卸货
        global index
        if(int(message_header) == 1111 ):
            if(int(message_flag_0) == 0 ):
                print(Local_Time,d_0[int(message_flag_0)])
            elif(int(message_flag_0) == 10):
                print("完成时间:",Local_Time)
            else:
                print(Local_Time,d_1[int(message_flag_1)])
    elif len(message) == 1:
        d_3 = {0:"有货",1:"没货"}
        print("出发时间:",Local_Time,d_3[int(message)])
    elif len(message) == 2:
        print(Local_Time,"停止于{}仓".format(d_2[index]))
        print("装卸中…………")
        index = index + 1

def Excel_Init():
    wb = load_workbook("Report.xlsx")
    sheet = wb["Sheet1"]
    sheet["A{}".format(1)] = "日期"
    sheet["B{}".format(1)] = "时间"
    sheet["C{}".format(1)] = "地点"
    sheet["D{}".format(1)] = "装货/卸货"
    wb.save("Report.xlsx")

# def Excel_Input():
    

if __name__ == "__main__":
    Excel_Init()
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(("",8080))
    serverSocket.listen(5)
    print("Socket server success")
    clientSocket,clientInfo = serverSocket.accept() # 链接
    print("Connection success")
    while True:
        recvData = clientSocket.recv(1024)
        # print(recvData)
        decode(recvData)
# clientSocket.close()
# serverSocket.close()
    
