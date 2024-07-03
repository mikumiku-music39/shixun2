import pandas as pd
import os
import matplotlib.pyplot as plt

# 定义CSV文件的路径
file_path_erp_khxd = 'E:\\Desktop\\shixunpoject\\shixun2\\project-2024-a-master\\data\\ERP_KHXD.csv'
file_path_erp_fhddx = 'E:\\Desktop\\shixunpoject\\shixun2\\project-2024-a-master\\data\\ERP_FHDXX.csv'

# 检查文件是否存在
def check_file_exists(file_path):
    if not os.path.isfile(file_path):
        print(f"文件 {file_path} 不存在")
        exit()

check_file_exists(file_path_erp_khxd)
check_file_exists(file_path_erp_fhddx)

# 设置matplotlib使用中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 尝试使用不同的编码读取文件的函数
def read_csv_with_encoding(file_path, encodings):
    for encoding in encodings:
        try:
            print(f"尝试使用 {encoding} 编码读取文件...")
            # 对于混合类型的列，我们指定它们为字符串类型
            return pd.read_csv(file_path, encoding=encoding, dtype=str)
        except UnicodeDecodeError as e:
            print(f"使用 {encoding} 编码失败: {e}")
            continue
    print("所有编码尝试失败")
    exit()

encodings_to_try = ['gbk', 'utf-8', 'utf-8-sig', 'ISO-8859-1']

# 读取并处理ERP_KHXD.csv文件
df_khxd = read_csv_with_encoding(file_path_erp_khxd, encodings_to_try)
df_khxd['sjfhdw'] = pd.to_numeric(df_khxd['sjfhdw'], errors='coerce', downcast='float')
df_khxd_grouped = df_khxd.groupby('fhd_id')['sjfhdw'].sum().reset_index()
df_khxd_grouped.rename(columns={'sjfhdw': 'sjfhdw_sum'}, inplace=True)

# 读取并处理ERP_FHDDX.csv文件
df_fhddx = read_csv_with_encoding(file_path_erp_fhddx, encodings_to_try)

# 确保合并键'id'和'fhd_id'存在
assert 'id' in df_fhddx.columns, "'id'列在ERP_FHDDX.csv中不存在"
assert 'fhd_id' in df_khxd_grouped.columns, "'fhd_id'列在ERP_KHXD.csv中不存在"

# 合并两个DataFrame
merged_df = pd.merge(df_fhddx, df_khxd_grouped, left_on='id', right_on='fhd_id', how='left')

# 过滤掉sjfhdw_sum为NaN的行
filtered_df = merged_df.dropna(subset=['sjfhdw_sum'])

# 绘制柱状图
plt.figure(figsize=(12, 8))
plt.bar(filtered_df['mc'], filtered_df['sjfhdw_sum'], color='blue')
plt.xlabel('名称 ')
plt.ylabel('吨位')
plt.title('仓库码头发货总吨位')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()