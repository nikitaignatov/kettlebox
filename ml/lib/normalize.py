import math


def acc_scalar2(df):
    df['Axs'] = (df['Ax'].apply(lambda x: (x+4.0)/8.0))
    df['Ays'] = (df['Ay'].apply(lambda x: (x+4.0)/8.0))
    df['Azs'] = (df['Az'].apply(lambda x: (x+4.0)/8.0))
    df['Gxs'] = (df['Gx'].apply(lambda x: (x+500.0)/1000.0))
    df['Gys'] = (df['Gy'].apply(lambda x: (x+500.0)/1000.0))
    df['Gzs'] = (df['Gz'].apply(lambda x: (x+500.0)/1000.0))


def acc_scalar(df):
    df['Axs'] = (df['Ax'].apply(lambda x: math.sqrt(x**2)/4))
    df['Ays'] = (df['Ay'].apply(lambda x: math.sqrt(x**2)/4))
    df['Azs'] = (df['Az'].apply(lambda x: math.sqrt(x**2)/4))
    df['Gxs'] = (df['Gx'].apply(lambda x: math.sqrt(x**2)/500.0))
    df['Gys'] = (df['Gy'].apply(lambda x: math.sqrt(x**2)/500.0))
    df['Gzs'] = (df['Gz'].apply(lambda x: math.sqrt(x**2)/500.0))


def magnitude(df):
    ax2 = df['Ax']**2
    ay2 = df['Ay']**2
    az2 = df['Az']**2
    am2 = ax2 + ay2 + az2

    gx2 = df['Gx']**2
    gy2 = df['Gy']**2
    gz2 = df['Gz']**2
    gm2 = gx2 + gy2 + gz2

    df['Am'] = am2.apply(lambda x: math.sqrt(x)/4)
    df['Gm'] = gm2.apply(lambda x: math.sqrt(x)/500)

    #df['Pitch']=         math.atan2(df['Ay'][index],df['Az'][index])
    #   math.atan2(-df['Ax'][index], math.sqrt(df['Ay'][index]**2 +(df['Az'][index] **2)))


def frequency(df):
    df['Time_Delta_ms'] = (df['Time']-df['Time'].shift()
                           ).fillna(1000).astype(int)
    df['Hz'] = (1000/df['Time_Delta_ms']).astype(int)


def unique_labels(df):
    return df['Activity'].unique()
