import pandas as pd
import numpy as np
new_data = pd.read_csv(r'D:\\A_vsCodeProjects\\vsCodePython\\news.csv')
new_data.rename(columns={'新闻名称':'新闻标题','新闻网址':'新闻网页'},inplace=True)
print(new_data)

