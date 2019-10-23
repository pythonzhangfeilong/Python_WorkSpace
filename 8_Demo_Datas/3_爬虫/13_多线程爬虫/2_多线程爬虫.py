import threading
from queue import Queue
class CrawlThread(threading.Thread):
    def __init__(self,threadName):
        # 继承父类属性的同时，并且拓展父类的属性
        super().__init__()
        self.threadName=threadName
        pass

    def run(self):
        pass


class ParseThread(threading.Thread):
    pass

def main():
    pageQueue=Queue()
    for i in range(1,14):
        pageQueue.put(i)

    crawlList=['采集1号','采集2号','采集3号']
    for var in crawlList:
        c=CrawlThread(var)
        c.start()
if __name__ == '__main__':
    main()