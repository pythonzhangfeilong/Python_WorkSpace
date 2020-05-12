"""
@File    : 1_Text公式.py
@Time    : 2020/5/8 2:57 下午
@Author  : FeiLong
@Software: PyCharm
"""
from matplotlib import pyplot

def run():
    fig=pyplot.figure()

    ax=fig.add_subplot(111)

    ax.set_xlim([1,7])
    ax.set_ylim([1,5])

    ax.text(2,4,r'$ \alpha_i \beta_j \pi \lambda \omega $',size=25)
    ax.text(4,4,r'$ \sin(0)=\cos(\frac{\pi}{2}) $',size=25)
    ax.text(2,2,r'$ \lim_{x \rightarrow y} \frac{1}{x^3} $',size=25)
    ax.text(4,2,r'$ \sqrt[4]{x}=\sqrt{y} $',size=25)




    pyplot.show()
run()












