#4-3.py

#利用队列实现重复密钥加密法

#队列的实现

#主函数入口
if __name__=='__main__':
    #密钥列表
    List = [1,2,3,4,5,0,-1,-2,-3,-4,-5]
    #输入待加密原文
    string = input("请输入待加密的原文:")
    #加密字符串
    str_encode=""
    #解密字符串
    str_decode=""
    #加密队列和解密队列
    eList = []
    dList = []
    #加密过程实现，包括从队列中取密钥值、进行加密和将用完的密钥值放入队列
    for c in string:
    	value = List.pop(0)
    	List.append(value)
    	eList.append(value)
    	dList.append(value)
    	str_encode += chr(ord(c)+value)
    #解密过程实现，包括从队列中取密钥值、进行解密和将用完的密钥值放入队列
    for c in str_encode:
    	value = dList.pop(0)
    	str_decode += chr(ord(c)-value)
	#输出过程
    print("加密后的密文为：%s" %str_encode)
    print("解密后的原文为：%s" %str_decode)