#####socket协议
# TCP面向连接的通信协议
# UDP无线连接的协议（容易丢包，成本低，但是速度快）
# 建立连接:三次握手
'''
1.第一次握手:建立连接。
     	客户端发送连接请求报文，将SYN=1，随机产生seq=x,客户端进入SYN_SEND状态，等待服务器的确认。
2.第二次握手:服务器收到SYN报文段。
     	服务器收到客户端的SYN报文段，需要对这个SYN报文段进行确认，设置ACK=x+1，同时自己还发送SYN请求SYN=1，序列号seq=y；服务器端将上述所有信息放到一个报文段(即SYN+ACK)中，一并发给客户端，此时服务器进入SYN_RECV状态。
3.第三次握手:客户端收到服务器的SYN+ACK报文段。
     	将序列号seq=y+1，向服务器发送ACK报文段，这个报文段发送完毕后，客户端与服务器端都进入ESTABLISHED状态，完成TCP三次握手。
'''
# 断开连接：四次挥手
'''
1.第一次挥手
  client设置seq和ACK，向server发送FIN报文段，此时client进入FIN_WAIT_1状态，表示主机1没有数据要发送给server了。
2.第二次挥手
•server收到了client发送的FIN报文段，向client回一个ACK报文段，ACK=seq+1；client进入FIN_WAIT_2状态；server告诉client，我“同意”你的关闭请求。 
3.第三次挥手
   server向client发送FIN报文段，请求关闭连接，同时server进入CLOSE_WAIT状态； 
4.第四次挥手
• client收到server发送的FIN报文段，向server发送ACK报文段，然后client进入TIME_WAIT状态；server收到client的ACK报文段以后，就关闭连接；此时，client等待2MSL后依然没有收到回复，则证明Server端已正常关闭，那好，client也可以关闭连接了。 
注：FIN是用来扫描保留的端口，发送一个FIN包（或者是任何没有ACK或SYN标记的包）到目标的一个开放的端口，然后等待回应。许多系统会返回一个复位标记。

TCP和UDP对比：
1.基于连接与无连接；
2.对系统资源的要求（TCP较多，UDP少）；
3.UDP程序结构较简单；
4.流模式与数据报模式 ；
5.TCP保证数据正确性，UDP可能丢包，TCP保证数据顺序，UDP不保证。
'''





















