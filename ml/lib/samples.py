import pandas as pd

mapping = {
    'Time': 'DateTime',
    'ts': 'Time',
    'ax': 'Ax',
    'ay': 'Ay',
    'az': 'Az',
    'gx': 'Gx',
    'gy': 'Gy',
    'gz': 'Gz'
}


def collect(i):
    return pd.read_csv('data/tsv_50hz_20kg/'+str(i)+'.log', sep="\t")


def load_sample(file):
    df = pd.read_csv('data/csv_100hz_8kg/'+str(file)+'.csv', sep=";")
    df = df.rename(columns=mapping)
    return df