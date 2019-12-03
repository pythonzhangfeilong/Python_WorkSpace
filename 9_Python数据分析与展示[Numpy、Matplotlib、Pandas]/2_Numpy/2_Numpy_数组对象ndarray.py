# Numpy的底层实现使用C实现的

# 1、n维数组对象：ndarray
"""
数组对象可以去掉元素间的运算所需要的循环，使一维向量更像单个数据
设置专门的对象，经过优化，可以提升这类应用的运算的速度
科学计算中，一个维度所有数据的类型往往是相同的
"""

# 2、ndarray是一个多维数组对象，有俩部分构成：
"""
实际的数据
描述这些数据的原数据（数据维度，数据类型等）

ndarray数组一般要求所有元素类型相同，数组下标从0开始
"""

# 3、ndarray使用
"""
numpy.array()生成一个ndarray数组

ndarray在程序中的别名是array

numpy.array()输出成[]形式，元素由空格分割

轴（axis）：保存数据维度
秩（rank）:轴的数量
"""

# 4、ndarray 对象属性：
"""
.ndim：    即轴的数量或维度的数量 
.shape：   数组的维度，对于矩阵，n 行 m 列 
.size：    数组元素的总个数，相当于hape 中 n*m 的值 
.dtype：   ndarray 对象的元素类型 
.itemsize: ndarray 对象中每个元素的大小，以字节为单位 
.flags:    ndarray 对象的内存信息 
.real:     ndarray 元素的实部 
.imag:     ndarray 元素的虚部 
.data:     包含实际数组元素的缓冲区，由于一般通过数组的索引获取元素，所以通常不需要使用这个属性。
"""

# 5、ndarray实例
"""
In [1]: import numpy                                                                                                                      

In [2]: a=numpy.array([[0,1,2,3,4],[5,6,7,8,9]])                                                                                          

In [3]: a.ndim                                                                                                                            
Out[3]: 2

In [4]: a.shape                                                                                                                           
Out[4]: (2, 5)

In [5]: a.size                                                                                                                            
Out[5]: 10

In [6]: a.dtype                                                                                                                           
Out[6]: dtype('int64')

In [7]: a.itemsize                                                                                                                        
Out[7]: 8

"""

# 6、ndarray数据元素类型
"""
名称	        描述
bool_	    布尔型数据类型（True 或者 False）
int_	    默认的整数类型（类似于 C 语言中的 long，int32 或 int64）
intc	    与 C 的 int 类型一样，一般是 int32 或 int 64
intp	    用于索引的整数类型（类似于 C 的 ssize_t，一般情况下仍然是 int32 或 int64）
int8	    字节（-128 to 127）
int16	    整数（-32768 to 32767）
int32	    整数（-2147483648 to 2147483647）
int64	    整数（-9223372036854775808 to 9223372036854775807）
uint8	    无符号整数（0 to 255）
uint16	    无符号整数（0 to 65535）
uint32	    无符号整数（0 to 4294967295）
uint64	    无符号整数（0 to 18446744073709551615）
float_	    float64 类型的简写
float16	    半精度浮点数，包括：1 个符号位，5 个指数位，10 个尾数位
float32	    单精度浮点数，包括：1 个符号位，8 个指数位，23 个尾数位
float64	    双精度浮点数，包括：1 个符号位，11 个指数位，52 个尾数位
complex_	complex128 类型的简写，即 128 位复数
complex64	复数，表示双 32 位浮点数（实数部分和虚数部分）
complex128	复数，表示双 64 位浮点数（实数部分和虚数部分）
numpy       的数值类型实际上是 dtype 对象的实例，并对应唯一的字符，包括 np.bool_，np.int32，np.float32，等等。
"""









