import pandas as pd
import os
import matplotlib.pyplot as plt

# 设置matplotlib的字体，以支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为SimHei
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 定义一个函数来安全地读取CSV文件
def safe_read_csv(file_path, encoding='utf-8'):
    try:
        df = pd.read_csv(file_path, encoding=encoding, dtype=object, low_memory=False)
        # 检查并转换'sjfhdw'列为数值类型
        if 'sjfhdw' in df.columns:
            df['sjfhdw'] = pd.to_numeric(df['sjfhdw'], errors='coerce')
        return df
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return None

# 检查文件是否存在
def check_file_exists(file_path):
    if not os.path.isfile(file_path):
        print(f"文件 {file_path} 不存在")
        exit()


# 尝试使用不同的编码读取文件的函数
def read_csv_with_encoding(file_path, encodings):
    for encoding in encodings:
        try:
            print(f"尝试使用 {encoding} 编码读取文件...")
            return pd.read_csv(file_path, encoding=encoding, dtype=str)
        except UnicodeDecodeError as e:
            print(f"使用 {encoding} 编码失败: {e}")
            continue
    print("所有编码尝试失败")
    exit()

# 定义文件路径
file_paths = {
    'ERP_KHXD': 'E:\\Desktop\\shixunpoject\\shixun2\\project-2024-a-master\\data\\ERP_KHXD.csv',
    'ERP_FHDXX': 'E:\\Desktop\\shixunpoject\\shixun2\\project-2024-a-master\\data\\ERP_FHDXX.csv',
    'ERP_KHXX': 'E:\\Desktop\\shixunpoject\\shixun2\\project-2024-a-master\\data\\ERP_KHXX.csv'
}

# 检查所有文件是否存在
for file_path in file_paths.values():
    check_file_exists(file_path)
# 通用的主处理函数
def process_csv_files(file_path1, file_path2, key_column, value_column):
    # 读取两个CSV文件
    df1 = safe_read_csv(file_path1)
    df2 = safe_read_csv(file_path2)

    # 检查文件是否读取成功
    if df1 is None or df2 is None:
        print("读取文件失败，请检查文件路径和格式。")
        return

    # 确保必要的列存在
    if key_column not in df1.columns or value_column not in df1.columns:
        print(f"必要的列在文件中不存在。需要的列是：'{key_column}' 和 '{value_column}'。")
        return

    # 转换 value_column 列为数值类型，非数值转换为 NaN
    df1[value_column] = pd.to_numeric(df1[value_column], errors='coerce')

    # 按 key_column 分组求和 value_column
    summed_df1 = df1.groupby(key_column)[value_column].sum().reset_index(name=f'{value_column}_sum')

    # 确保求和后的列是数值类型
    if summed_df1[f'{value_column}_sum'].dtype == 'object':
        summed_df1[f'{value_column}_sum'] = summed_df1[f'{value_column}_sum'].astype(float)

    # 选择 value_column 总和前五的 key_column
    top5_index = summed_df1.nlargest(5, f'{value_column}_sum')[key_column]

    # 从第一个CSV中筛选出前五的 key_column 对应的 value_column 总和
    top5_values = summed_df1.loc[summed_df1[key_column].isin(top5_index)]

    # 在第二个CSV中筛选 'id' 与 key_column 相同的行，并获取 'khqc'
    matched_df2 = df2[df2['id'].isin(top5_index)][['id', 'khqc']]

    # 合并 'khqc' 和 value_column 总和
    result_df = pd.merge(matched_df2, top5_values, left_on='id', right_on=key_column, how='inner')

    # 重置索引，从1开始
    result_df = result_df.reset_index(drop=True)

    # 删除 'id' 和 key_column 列
    result_df = result_df.drop(columns=['id', key_column])

    # 按 value_column 总和降序排列
    result_df = result_df.sort_values(f'{value_column}_sum', ascending=False)

    # 在生成最终结果后，添加新的一列 'Rank'
    result_df['Rank'] = range(1, len(result_df) + 1)

    # 重新排序列，将 'Rank' 放在第一位
    cols = ['Rank'] + [col for col in result_df.columns if col != 'Rank']
    result_df = result_df[cols]

    return result_df

# 调用主处理函数，处理 sjfhze 数据
result_df_sjfhze = process_csv_files(
    'E:\\Desktop\\shixunpoject\\shixun2\\project-2024-a-master\\data\\ERP_KHXD.csv',
    'E:\\Desktop\\shixunpoject\\shixun2\\project-2024-a-master\\data\\ERP_KHXX.csv',
    'khxx_id', 'sjfhze'
)

# 调用主处理函数，处理 sjfhdw 数据
result_df_sjfhdw = process_csv_files(
    'E:\\Desktop\\shixunpoject\\shixun2\\project-2024-a-master\\data\\ERP_KHXD.csv',
    'E:\\Desktop\\shixunpoject\\shixun2\\project-2024-a-master\\data\\ERP_KHXX.csv',
    'khxx_id', 'sjfhdw'
)

# 打印结果
if isinstance(result_df_sjfhze, pd.DataFrame) and not result_df_sjfhze.empty:
    print("实际发货总额前五的公司按发货总额降序排列：")
    print(result_df_sjfhze.to_string(index=False))
else:
    print("处理过程中出现错误或结果为空。")

if isinstance(result_df_sjfhdw, pd.DataFrame) and not result_df_sjfhdw.empty:
    print("实际发货吨位前五的公司按发货吨位降序排列：")
    print(result_df_sjfhdw.to_string(index=False))
else:
    print("处理过程中出现错误或结果为空。")
# 设置matplotlib的字体，以支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为SimHei
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 定义文件路径
file_path = 'E:\\Desktop\\shixunpoject\\shixun2\\project-2024-a-master\\data\\ERP_KHXD.csv'

# 尝试读取CSV文件，使用GBK编码，设置low_memory=False以处理混合类型数据
try:
    data = pd.read_csv(file_path, encoding='utf-8', low_memory=False)
except Exception as e:
    print(f"读取文件时发生错误: {e}")
    exit()

# 检查'hyfs'和'sjfhdw'列是否存在
if 'hyfs' not in data.columns or 'sjfhdw' not in data.columns:
    print("CSV文件中缺少'hyfs'或'sjfhdw'列。")
    exit()

# 将'hyfs'列转换为数值类型，非数值转换为NaN，然后转换为整数
data['hyfs'] = pd.to_numeric(data['hyfs'], errors='coerce').fillna(0).astype(int)

# 将'sjfhdw'列转换为数值类型，非数值转换为NaN，然后转换为浮点数
data['sjfhdw'] = pd.to_numeric(data['sjfhdw'], errors='coerce').fillna(0).astype(float)

# 根据'hyfs'的值分组并计算'sjfhdw'列的总和
land_transport_sum = data[data['hyfs'] == 0]['sjfhdw'].sum()
sea_transport_sum = data[data['hyfs'] == 1]['sjfhdw'].sum()



# 定义CSV文件的路径
file_path_erp_khxd = 'E:\\Desktop\\shixunpoject\\shixun2\\project-2024-a-master\\data\\ERP_KHXD.csv'
file_path_erp_fhddx = 'E:\\Desktop\\shixunpoject\\shixun2\\project-2024-a-master\\data\\ERP_FHDXX.csv'
check_file_exists(file_path_erp_khxd)
check_file_exists(file_path_erp_fhddx)
# 读取并处理ERP_KHXD.csv文件
df_khxd = safe_read_csv(file_path_erp_khxd)
df_khxd['sjfhdw'] = pd.to_numeric(df_khxd['sjfhdw'], errors='coerce', downcast='float')
df_khxd_grouped = df_khxd.groupby('fhd_id')['sjfhdw'].sum().reset_index()
df_khxd_grouped.rename(columns={'sjfhdw': 'sjfhdw_sum'}, inplace=True)

# 读取并处理ERP_FHDDX.csv文件
df_fhddx = safe_read_csv(file_path_erp_fhddx)

# 确保合并键'id'和'fhd_id'存在
assert 'id' in df_fhddx.columns, "'id'列在ERP_FHDDX.csv中不存在"
assert 'fhd_id' in df_khxd_grouped.columns, "'fhd_id'列在ERP_KHXD.csv中不存在"

# 合并两个DataFrame
merged_df = pd.merge(df_fhddx, df_khxd_grouped, left_on='id', right_on='fhd_id', how='left')

# 过滤掉sjfhdw_sum为NaN的行
filtered_df = merged_df.dropna(subset=['sjfhdw_sum'])

sizes = [land_transport_sum, sea_transport_sum]  # 这些数据需要在使用前定义
labels = ['陆运', '海运']

# 创建一个图形窗口，并设置大小
plt.figure(figsize=(16, 8))

# 第一幅图：柱状图
plt.subplot(1, 2, 1)  # 1行2列的第一个位置
plt.bar(filtered_df['mc'], filtered_df['sjfhdw_sum'], color='blue')
plt.xlabel('名称')
plt.ylabel('吨位')
plt.title('仓库码头发货总吨位')
plt.xticks(rotation=45)
plt.tight_layout()

# 第二幅图：饼状图
plt.subplot(1, 2, 2)  # 1行2列的第二个位置
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('运输方式分布')
plt.axis('equal')  # 确保饼状图是圆形的

# 显示所有图表
plt.show()