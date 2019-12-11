# 1、Numpy向csv文件写入数据，函数savetx()
"""
    numpy.savetxt(fraem,array,fmt='%.18e',delimiter=None)
    frame   文件、字符串或产生器，可以是.gz或.bz2的压缩文件
    array   存入文件的数组
    fmt     写入文件的格式，例如：%d,%.2f,%.18e
    delimiter   分割字符串，默认是任何空格
"""

# 2、把csv文件读取到Numpy对象中
"""
    numpy.loadtxt(fram,dtype=np.float,delimiter=None,unpack=Flase)
    frame   文件、字符串或产生器，可以是.gz或.bz2的压缩文件
    dtype   数据类型
    delimiter   分割字符串，默认是任何空格
"""

# 3、csv文件的局限性
"""
csv只能有效的存取一维、二维数组
numpy.savetxt()和numpy.loadtxt()只能有效存取一维、二维叔祖

"""



























