import pandas as pd

def Num_of_Words_in_String(text):
    str1 = text.strip() 
    index = 0
    count = 0
    while index < len(str1):
        while str1[index] != " ": 
            index += 1
            if index == len(str1):
                break
        count += 1 
        if index == len(str1): 
            break
        while str1[index] == " ": 
            index += 1
    return count

def Check_Content_Len(dataset, col_name):
    df_sum_len = pd.DataFrame(columns=['{col_name}_length'.format(col_name=col_name)])
    for index, row in dataset.iterrows():
            content_len = Num_of_Words_in_String(row[col_name])
            df_sum_len = df_sum_len.append({'{col_name}_length'.format(col_name=col_name):content_len}, ignore_index=True)
    return df_sum_len