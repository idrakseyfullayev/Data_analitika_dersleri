import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('gold.csv').tail(15)

tarixler = pd.to_datetime(df['Date'], format = '%Y-%m-%d')
yuxari_qiymetler = df['High']
asagi_qiymetler = df['Low']

fiq1, ox1 = plt.subplots()
fiq2, ox2 = plt.subplots()

ox1.plot_date(tarixler, yuxari_qiymetler, linestyle = 'solid', label='Yuxarı qiymət')
ox2.plot_date(tarixler, asagi_qiymetler, linestyle = 'solid', label='Aşağı qiymət')

fiq1.autofmt_xdate()
fiq2.autofmt_xdate()

ox1.legend()

ox1.set_title('Qızılın yuxarı qiymətləri')
ox2.set_xlabel('Tarixlər')
ox1.set_ylabel('Qiymətlər')

ox2.legend()

ox2.set_title('Qızılın aşağı qiymətləri')
ox2.set_xlabel('Tarixlər')
ox2.set_ylabel('Qiymətlər')

plt.show()