import pandas as pd

# 定义一个函数来安全地读取CSV文件
def safe_read_csv(file_path, encoding='gbk'):
    try:
        df = pd.read_csv(file_path, encoding=encoding, dtype=object, low_memory=False)
        # 检查并转换'sjfhdw'列为数值类型
        if 'sjfhdw' in df.columns:
            df['sjfhdw'] = pd.to_numeric(df['sjfhdw'], errors='coerce')
        return df
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return None

# 主处理函数
def process_csv_files(file_path1, file_path2):
    # 读取两个CSV文件
    df1 = safe_read_csv(file_path1)
    df2 = safe_read_csv(file_path2)

    # 检查文件是否读取成功
    if df1 is None or df2 is None:
        print("读取文件失败，请检查文件路径和格式。")
        return

    # 确保 'khxx_id' 和 'sjfhdw' 列存在
    if 'khxx_id' not in df1.columns or 'sjfhdw' not in df1.columns:
        print("必要的列在文件中不存在。")
        return

    # 按 'khxx_id' 分组求和 'sjfhdw'
    summed_df1 = df1.groupby('khxx_id')['sjfhdw'].sum().reset_index(name='sjfhdw_sum')

    # 选择 'sjfhdw_sum' 前五的 'khxx_id'
    top5_index = summed_df1.nlargest(5, 'sjfhdw_sum')['khxx_id']

    # 从第一个CSV中筛选出前五的 'khxx_id' 对应的 'sjfhdw_sum'
    top5_sjfhdw = summed_df1.loc[summed_df1['khxx_id'].isin(top5_index)]

    # 在第二个CSV中筛选 'id' 与 'khxx_id' 相同的行，并获取 'khqc'
    matched_df2 = df2[df2['id'].isin(top5_index)][['id', 'khqc']]

    # 合并 'khqc' 和 'sjfhdw_sum'
    result_df = pd.merge(matched_df2, top5_sjfhdw, left_on='id', right_on='khxx_id', how='inner')

    # 重置索引，从1开始
    result_df = result_df.reset_index(drop=True)

    # 删除 'id' 和 'khxx_id' 列
    result_df = result_df.drop(columns=['id', 'khxx_id'])

    # 按 'sjfhdw_sum' 降序排列
    result_df = result_df.sort_values('sjfhdw_sum', ascending=False)

    # 在生成最终结果后，添加新的一列 'Rank'
    result_df['Rank'] = range(1, len(result_df) + 1)

    # 重新排序列，将 'Rank' 放在第一位
    cols = ['Rank'] + [col for col in result_df.columns if col != 'Rank']
    result_df = result_df[cols]

    return result_df

# 调用主处理函数
result_df = process_csv_files(
    'C:\\Users\\ooo\\Desktop\\project-2024-a-master\\data\\ERP_KHXD.csv',
    'C:\\Users\\ooo\\Desktop\\project-2024-a-master\\data\\ERP_KHXX.csv'
)

# 打印结果
if isinstance(result_df, pd.DataFrame) and not result_df.empty:
    print("实际发货吨位前五的公司按发货吨位降序排列：")
    print(result_df.to_string(index=False))
else:
    print("处理过程中出现错误或结果为空。")