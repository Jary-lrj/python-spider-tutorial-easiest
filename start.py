import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 用来让柱状图显示中文的代码
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

'''
data = pd.read_csv("D:\\A_vsCodeProjects\\vsCodePython\\Project2\\info.csv")#读取要处理的表格数据
x=data['name']
y=data['salary']#x、y分别代表图的横纵坐标
plt.barh(x,y,color="#67C23A")#水平柱状图，因为可能存在没法显示完全的问题
for i,v in zip(data['name'],data['salary']):#在柱状图上标注每个柱的具体数据
    plt.text(v,i,v)
plt.grid()#在背景上添加格子
plt.show()#显示图像
'''

'''
#竖直柱状图用来统计测试数据中姓名与工资的关系
data = pd.read_csv("D:\\A_vsCodeProjects\\vsCodePython\\Project2\\info.csv")#读取要处理的表格数据
plt.bar(data['name'],data['salary'],color="#409EFF")#x和y轴分别为姓名和工资来反映关系
plt.xlabel('姓名')#横坐标名称
plt.ylabel('工资')#纵坐标名称
for x,y in enumerate(data['salary']):
    plt.text(x,y+100,'%s'%y,ha='center')
plt.grid()
plt.show()
'''

'''
#折线图用来统计测试接下来十日内武威市预报气温变化情况
data=pd.read_csv('D:\\A_vsCodeProjects\\vsCodePython\\Project2\\weather.csv')#读取要处理的表格数据
x=range(1,11)#设置x轴坐标为天数
plt.plot(x,data['最高气温'],'-',color='#F56C6C',label="单日最高气温")#画出单日最高气温折线
plt.plot(x,data['最低气温'],'-',color='#409EFF',label="单日最低气温")#画出单日最低气温折线
plt.title('武威市近10天内气温变化趋势示意图')#图表标题
plt.xlabel('日期')#图标横坐标名称
plt.ylabel('气温/华氏度')#图标纵坐标名称
for a,b in zip(x,data['最高气温']):#显示最高气温图线每个点的数值
    plt.text(a,b,b,ha='center',va='bottom')
for c,d in zip(x,data['最低气温']):#显示最低气温图线每个点的数值
    plt.text(c,d,d,ha='center',va='bottom')
plt.legend()#显示图例
plt.grid(True)#背景显示网格
plt.show()#显示图线
'''

'''
x=np.linspace(-1,1,100)#在-1到1范围内绘制100个点，点数越多曲线越平滑
y1=x#标准正比例函数
y2=x**2#标准二次函数

plt.plot(x,y1)#绘制函数图像
plt.plot(x,y2)#绘制函数图像
plt.grid(True)#显示网格
plt.show()#显示图像
'''

places=['凉州区','古浪县','天祝县','民勤县']#标签名称 
gdp=[314.43,56.26,45.75,72.02]#实际数据
#饼图绘制
plt.pie(gdp,labels=places,autopct="%1.2f%%",colors=['#409EFF','#67C23A','#F56C6C','#E6A23C'])
plt.legend()#显示图例
plt.title('2019年武威市各地区GDP饼状图')#图表名称
plt.show()#显示图表