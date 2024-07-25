import pandas as pd

# 創建舊的 DataFrame
df_old = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'value': ['A', 'B', 'C', 'D']
})

# 創建新的 DataFrame
df_new = pd.DataFrame({
    'id': [3, 4, 5, 6],
    'value': ['C', 'D', 'E', 'F']
})

# 找出重疊數據
df_overlap = pd.merge(df_old, df_new, on='id')
print("重疊數據：")
print(df_overlap)

# 移除重疊數據
df_new_unique = df_new[~df_new['id'].isin(df_overlap['id'])]
print("移除重疊數據後的新 DataFrame：")
print(df_new_unique)