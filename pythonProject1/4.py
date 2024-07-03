import pandas as pd
import matplotlib.pyplot as plt

# 设置matplotlib使用中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 定义CSV文件的路径
file_path_erp_khxd = 'C:\\Users\\ooo\\Desktop\\project-2024-a-master\\data\\ERP_KHXD.csv'
file_path_erp_fhddx = 'C:\\Users\\ooo\\Desktop\\project-2024-a-master\\data\\ERP_FHDDX.csv'

# 读取第一个CSV文件
df_khxd = pd.read_csv(file_path_erp_khxd, encoding='gbk')

# 确保列名存在
if 'fhd_id' not in df_khxd.columns or 'sjfhdw' not in df_khxd.columns:
    print("ERP_KHXD.csv文件中缺少必要的列")
    exit()

# 转换sjfhdw列为数值型，并计算sjfhdw的总和
df_khxd['sjfhdw'] = pd.to_numeric(df_khxd['sjfhdw'], errors='coerce')
df_khxd_grouped = df_khxd.groupby('fhd_id')['sjfhdw'].sum().reset_index()
df_khxd_grouped.rename(columns={'sjfhdw': 'sjfhdw_sum'}, inplace=True)

# 读取第二个CSV文件
df_fhddx = pd.read_csv(file_path_erp_fhddx, encoding='gbk')

# 确保列名存在
if 'id' not in df_fhddx.columns or 'mc' not in df_fhddx.columns:
    print("ERP_FHDDX.csv文件中缺少必要的列")
    exit()

# 将fhd_id和id进行匹配，并将对应的mc和sjfhdw_sum组合在一起
merged_df = df_fhddx.merge(df_khxd_grouped, on='fhd_id', how='left')
merged_df.rename(columns={'fhd_id': 'id'}, inplace=True)

# 绘制柱状图
plt.figure(figsize=(10, 6))

# 过滤掉sjfhdw_sum为NaN的行
filtered_df = merged_df[merged_df['sjfhdw_sum'].notnull()]

# 创建柱状图
plt.bar(filtered_df['mc'], filtered_df['sjfhdw_sum'], color='blue')

# 设置x轴和y轴标签以及图表标题
plt.xlabel('名称 (mc)')
plt.ylabel('数据分户单位 (sjfhdw_sum)')
plt.title('柱状图：名称与数据分户单位')

# 显示x轴标签并旋转，使其更加清晰
plt.xticks(rotation=45)

# 自动调整子图参数
plt.tight_layout()

# 显示图表
plt.show()