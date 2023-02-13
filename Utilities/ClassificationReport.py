import pandas as pd
from sklearn.metrics import classification_report

def Classification_Report(y_test, y_pred):
    n=len(y_test.unique())
    report = [ classification_report(y_test, y_pred).split('\n')[i] for i in range(n+7) if len(classification_report(y_test,y_pred).split('\n')[i]) !=0 ]

    df_report = pd.DataFrame()
    for i in range(n+1):
      l = pd.DataFrame(report[i].split())
      df_report = pd.concat([df_report, l ],axis=1, ignore_index=True)

    df_report2 = pd.DataFrame()
    for i in [-1,-2]:
      s = []
      d = []
      for j in report[i].split():
          if j.isalpha():
            s.append(j)

          else:
            d.append(j)

      l = pd.DataFrame([" ".join([str(k) for k in s])] + d).T

      df_report2 = pd.concat([df_report2, l ])

    temp = pd.concat([df_report.T, df_report2],ignore_index=True)
    col = [i for i in temp.iloc[:1,:].values[0] if type(i)==str]
    temp.set_index(0,inplace=True)
    temp.columns = col
    temp = temp.iloc[1:,:]
    temp = temp.reset_index()
    cr = temp.rename(columns={0:'class'})

    return cr