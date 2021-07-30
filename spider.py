from requests_html import HTMLSession
import pandas as pd

session = HTMLSession()#实例化一个请求
#请求网址
url = "https://weather.com/weather/tenday/l/f794497bed5fbf7b76e1c7bd05995b21b6cdb75e7493d3fa8bece770d92ae198"
r = session.get(url)#访问所请求的网址
results=[]#用来盛放结果的空列表
for i in range(0, 10):
    pathH = '#titleIndex' + \
        str(i)+' > div.DetailsSummary--temperature--1Syw3 > span'#根据网页内部找到高温所在地址
    pathL = '#titleIndex' + \
        str(i)+' > div.DetailsSummary--temperature--1Syw3 > span:nth-child(2) > span'#根据网页内部找到低温所在地址
    highV = r.html.find(pathH)
    lowV=r.html.find(pathL)#具体寻找
    results.append((list(highV)[0].text,list(lowV)[0].text))#将高温、低温打包加入结果列表中
for res in results:
    print(res)#测试列表内的数据
df=pd.DataFrame(results)#生成一个csv文件
df.columns=['最高气温','最低气温']#csv文件中的列名，和excel中的列表同理
print(df)#测试文件内容是否正常
df.to_csv('weather.csv',encoding='utf-8',index=False)#写入文件，文件名、编码方式、是否带有行号
# path = "#con-three-1 > ul > li > a"
# results = r.html.find(path)
# news=[]
# for result in results:
#     news.append((result.text,list(result.absolute_links)[0]))

# df=pd.DataFrame(news)
# df.columns=['新闻名称','新闻网址']
# print(df)
# df.to_csv('news.csv',encoding='utf-8',index=False)
