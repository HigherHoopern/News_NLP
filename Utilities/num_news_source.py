from collections import Counter
import pandas as pd

def News_Source_Num(dataset,col_source_name,num_most_common):
    source_name = dataset[col_source_name]
    c= pd.DataFrame(Counter(source_name).most_common(num_most_common))
    c = c.set_index(c.columns[0])
    return c