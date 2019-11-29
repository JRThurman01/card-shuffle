import pandas as pd
from matplotlib import pyplot as plt

df_summary=pd.DataFrame()

multiplier = 1000000
for i in range(0,8):
    for j in range(0,10):
        df = pd.read_csv('run3/result{}.csv' .format(i), delimiter=',', names=['Run Number', 'Hands', 'Tricks'], header=0, skiprows=multiplier*j +3, nrows= multiplier)
        df_summary = df_summary.append({'run range':i*10+j,'mean':df['Tricks'].mean(), 'max':df['Tricks'].max()}, ignore_index=True)
        print(i*10+j)

#print(df_summary)

plt.figure(figsize=(20,10))
plt.subplot(121)
plt.plot('run range', 'mean', data = df_summary, color='red' )
plt.subplot(122)
plt.plot('run range', 'max', data=df_summary, color = 'blue')
plt.legend()
plt.show()
