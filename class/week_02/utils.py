import pandas as pd
import numpy as np

def freq_profile(df:pd.DataFrame) -> pd.DataFrame:
    """freq_profile Create a frequency profile for messy datasets

    Args:
        df (pd.DataFrame): Some raw or tidy data frame

    Returns:
        pd.DataFrame: frequency profile of the input dataset 
    """
    d = []
    columns = df.columns
    for col in columns: 
        if np.issubdtype(df[col].dtype,np.number):
            vc = df[col].value_counts(bins=5).sort_index().reset_index()
            if df[col].isnull().sum()>0:
                vc = vc.append(dict(zip(vc.columns,
                                        [np.nan,df[col].isnull().sum()]))
                               ,ignore_index=True)
        else:
            vc = df[col].value_counts(dropna=False).sort_index().reset_index()
        vc.columns=['Value','Freq']
        vc['Precent']= vc.Freq/df.shape[0]
        vc = pd.concat({col: vc.set_index('Value')},axis=0)
        d.append(vc)
    return pd.concat(d)