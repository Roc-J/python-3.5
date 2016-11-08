#4-2.py
import math
#利用栈实现大整数加法

#栈的实现
#主函数入口
if __name__=="__main__":

    #输入两个加数
    add1 = input("请输入第一个加数:")
    add2 = input("请输入第二个加数:")
    #建立建立加数栈1、加数栈2和结果栈
    add1List = []
    add2List = []
    result = []
    #加数1和加数2按照由高位到低位分别入栈
    for s in add1:
        add1List.append(ord(s)-ord('0'))
    for s in add2:
        add2List.append(ord(s)-ord('0'))
    tmp=0
    while len(add1List)>0 and len(add2List)>0:  #栈1和栈2均非空时执行循环
        tmp += add1List.pop() + add2List.pop()  #取栈1和栈2的栈顶相加，存入临时变量tmp
        #栈1弹出栈顶
        #栈2弹出栈顶
        result.append(tmp%10)#将tmp除以10的余数压入结果栈
        tmp = math.floor(tmp/10) #取tmp除以10的商，结果只能为0和1,1代表有进位
    if tmp:  #最高位相加后若有进位则将进位结果压入结果栈
        result.append(tmp)

    #结果输出
    res = ""
    while len(result)>0:
        res += str(result.pop())
    print("%d与%d相加的结果是:%d" % (int(add1),int(add2),int(res)))