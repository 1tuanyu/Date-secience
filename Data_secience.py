import os
import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

os.chdir("G:\\python\\Date secience\\csv")
DAU = pd.DataFrame(pd.read_csv('G:\\python\\Date secience\\csv\\section3-dau.csv'))
DPU = pd.DataFrame(pd.read_csv('G:\\python\\Date secience\\csv\\section3-dpu.csv'))
INSTALL = pd.DataFrame(pd.read_csv('G:\\python\\Date secience\\csv\\section3-install.csv'))

DAU_INSTALL = pd.merge(INSTALL, DAU, how='outer',on=['user_id', 'app_name'])
API = pd.merge(DAU_INSTALL, DPU, how="outer", on=['user_id', 'app_name', 'log_date'])
API = API.fillna(value=0)
API = DataFrame(API, columns=['app_name','user_id', 'log_date', 'install_date', 'payment']).sort_values(by=["user_id", "log_date"])
API['log_date'] = API['log_date'].replace(0, "2013-00")
API['log_month'] = API['log_date'].map(lambda x :str(x).split('-')[0]+'-'+str(x).split('-')[1])
API['install_month'] = API['install_date'].map(lambda x :str(x).split('-')[0]+'-'+str(x).split('-')[1])
AP = list(API['payment'].groupby(API['log_month']).sum())[1:3]
NP = list(API['payment'].groupby(API['install_month']).sum())[2:]

months = ['2013-06', '2013-07']
xs = [i for i, _ in enumerate(months)]
plt.bar(xs, NP)
plt.ylabel('game payment')
plt.xticks([i for i, _ in enumerate(months)], months)
plt.title('date anynise')
plt.show()

#print(API[API['install_date'] > '2013-4']) #返回日期大于13-04的列
#print(API.ix[1]) 用索引返回列



