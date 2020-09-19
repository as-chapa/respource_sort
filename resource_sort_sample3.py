### pandasで特定の範囲で絞り込んで最大値を取得する
import pandas as pd


def extract_from_date(df, from_date: str, to_date: str):
    return df.query('@from_date < date < @to_date')

FILENAME = 'sample2.csv'
df = pd.read_csv(FILENAME)
print(df)

# お試し用の記述（備忘のため残す）
# df_out = df[(df['cpu'] > 10) & (df['date'] > '2020/9/22 11:00')]
# print(df_out)

# print(df.query('cpu > 10 and "2020/9/22 11:20" > date > "2020/9/22 11:00"'))

a = "2020/9/22 11:00"
b = "2020/9/22 11:20"
df_out2 = extract_from_date(df, a, b)
print(df_out2['cpu'].max())