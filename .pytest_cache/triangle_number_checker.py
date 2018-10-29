import pandas as pd

def calculate_sum(int, layers=1):
    result = 0

    for j in range(1,int+1):
        if layers ==1:
            result+=j
        else:
            result+=calculate_sum(j, layers-1)
        #print(result)
    return result

print(calculate_sum(4,3))



# df = pd.DataFrame()
# for i in range(1,10):
#     for j in range(1,3):
#         df = df.append({'i':i,
#                              'j':j,
#                              'ratio': calculate_sum(i, j)/ i**j
#                              }, ignore_index=True)
#
# print(df)