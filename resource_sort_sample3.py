### pandasで特定の範囲で絞り込んで最大値を取得する
import pandas as pd


def extract_from_date(df, from_date: str, to_date: str):
    return df.query('@from_date <= date <= @to_date')

FILENAME = 'sample2.csv'
df = pd.read_csv(FILENAME)
print(df)

# お試し用の記述（備忘のため残す）
# df_out = df[(df['cpu'] > 10) & (df['date'] > '2020/9/22 11:00')]
# print(df_out)

a = "2020/9/20 11:00"
b = "2020/9/20 11:20"
df_out2 = extract_from_date(df, a, b)

print(df_out2.head(1)['cpu'])
print(df_out2['cpu'].max())
print(df_out2.sort_values('cpu', ascending=False))
