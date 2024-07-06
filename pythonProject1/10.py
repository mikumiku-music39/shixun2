import os
import pandas as pd
import matplotlib.pyplot as plt

# 定义一个函数来安全地读取CSV文件
def safe_read_csv1(file_path, encoding='gbk'):
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
def process_csv_files1(file_path1, file_path2):
    # 读取两个CSV文件
    df1 = safe_read_csv1(file_path1)
    df2 = safe_read_csv1(file_path2)

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

# 确保目标目录存在
output_dir1 = 'C:\\Users\\ooo\\Desktop\\shixun111'
os.makedirs(output_dir1, exist_ok=True)

# 调用主处理函数
result_df = process_csv_files1(
    'C:\\Users\\ooo\\Desktop\\project-2024-a-master\\data\\ERP_KHXD.csv',
    'C:\\Users\\ooo\\Desktop\\project-2024-a-master\\data\\ERP_KHXX.csv'
)

# 如果DataFrame存在且非空，则将其写入.txt文件
if isinstance(result_df, pd.DataFrame) and not result_df.empty:
    output_path = os.path.join(output_dir1, 'output1.txt')
    result_df.to_string(output_path, index=False)
    print(f"结果已保存至 {output_path}")
else:
    print("处理过程中出现错误或结果为空。")

def safe_read_csv2(file_path, encoding='gbk'):
    try:
        df = pd.read_csv(file_path, encoding=encoding, dtype=object, low_memory=False)
        # 检查并转换'sjfhze'列为数值类型
        if 'sjfhze' in df.columns:
            df['sjfhze'] = pd.to_numeric(df['sjfhze'], errors='coerce')
        return df
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return None

# 主处理函数
def process_csv_files2(file_path1, file_path2):
    # 读取两个CSV文件
    df1 = safe_read_csv2(file_path1)
    df2 = safe_read_csv2(file_path2)

    # 检查文件是否读取成功
    if df1 is None or df2 is None:
        print("读取文件失败，请检查文件路径和格式。")
        return

    # 确保 'khxx_id' 和 'sjfhze' 列存在
    if 'khxx_id' not in df1.columns or 'sjfhze' not in df1.columns:
        print("必要的列在文件中不存在。")
        return

    # 按 'khxx_id' 分组求和 'sjfhze'
    summed_df1 = df1.groupby('khxx_id')['sjfhze'].sum().reset_index(name='sjfhze_sum')

    # 选择 'sjfhze_sum' 前五的 'khxx_id'
    top5_index = summed_df1.nlargest(5, 'sjfhze_sum')['khxx_id']

    # 从第一个CSV中筛选出前五的 'khxx_id' 对应的 'sjfhze_sum'
    top5_sjfhze = summed_df1.loc[summed_df1['khxx_id'].isin(top5_index)]

    # 在第二个CSV中筛选 'id' 与 'khxx_id' 相同的行，并获取 'khqc'
    matched_df2 = df2[df2['id'].isin(top5_index)][['id', 'khqc']]

    # 合并 'khqc' 和 'sjfhze_sum'
    result_df = pd.merge(matched_df2, top5_sjfhze, left_on='id', right_on='khxx_id', how='inner')

    # 重置索引，从1开始
    result_df = result_df.reset_index(drop=True)

    # 删除 'id' 和 'khxx_id' 列
    result_df = result_df.drop(columns=['id', 'khxx_id'])

    # 按 'sjfhze_sum' 降序排列
    result_df = result_df.sort_values('sjfhze_sum', ascending=False)

    # 在生成最终结果后，添加新的一列 'Rank'
    result_df['Rank'] = range(1, len(result_df) + 1)

    # 重新排序列，将 'Rank' 放在第一位
    cols = ['Rank'] + [col for col in result_df.columns if col != 'Rank']
    result_df = result_df[cols]

    return result_df

# 调用主处理函数
result_df = process_csv_files2(
    'C:\\Users\\ooo\\Desktop\\project-2024-a-master\\data\\ERP_KHXD.csv',
    'C:\\Users\\ooo\\Desktop\\project-2024-a-master\\data\\ERP_KHXX.csv'
)

# 确保目标目录存在
output_dir2 = 'C:\\Users\\ooo\\Desktop\\shixun111'
os.makedirs(output_dir2, exist_ok=True)

# 将结果保存到 'output2.txt'
output_file_path = os.path.join(output_dir2, 'output2.txt')
if isinstance(result_df, pd.DataFrame) and not result_df.empty:
    result_df.to_string(output_file_path, index=False)
    print(f"结果已保存至 {output_file_path}")
else:
    print("处理过程中出现错误或结果为空。")


plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为SimHei
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 定义文件路径
file_path3 = 'C:\\Users\\ooo\\Desktop\\project-2024-a-master\\data\\ERP_KHXD.csv'

# 尝试读取CSV文件，使用GBK编码，设置low_memory=False以处理混合类型数据
try:
    data = pd.read_csv(file_path3, encoding='GBK', low_memory=False)
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

# 准备饼状图的数据
labels = ['陆运', '海运']
sizes = [land_transport_sum, sea_transport_sum]

# 绘制饼状图
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('运输方式分布')

# 确保饼状图是圆形的
plt.axis('equal')

# 指定保存路径
save_path3 = 'C:\\Users\\ooo\\Desktop\\shixun111\\output3.png'

# 确保保存目录存在
directory3 = os.path.dirname(save_path3)
if not os.path.exists(directory3):
    os.makedirs(directory3)

# 将图表保存为图片
plt.savefig(save_path3)


# 定义CSV文件的路径
file_path_erp_khxd = r'C:\Users\ooo\Desktop\project-2024-a-master\data\ERP_KHXD.csv'
file_path_erp_fhddx = r'C:\Users\ooo\Desktop\project-2024-a-master\data\ERP_FHDXX.csv'

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

# 检查保存图片的目录是否存在，若不存在则创建
save_dir4 = r"C:\Users\ooo\Desktop\shixun111"
if not os.path.exists(save_dir4):
    os.makedirs(save_dir4)

# 保存图片
save_path4 = os.path.join(save_dir4, 'output4.png')
plt.savefig(save_path4)


# 定义文件路径
txt_file1 = r'C:\Users\ooo\Desktop\shixun111\output1.txt'
txt_file2 = r'C:\Users\ooo\Desktop\shixun111\output2.txt'
png_file3 = r'C:\Users\ooo\Desktop\shixun111\output3.png'
png_file4 = r'C:\Users\ooo\Desktop\shixun111\output4.png'

output_dir = r'C:\Users\ooo\Desktop\shixun111'
index_html_path = os.path.join(output_dir, 'index.html')
output_html1_path = os.path.join(output_dir, 'output1.html')
output_html2_path = os.path.join(output_dir, 'output2.html')
output_html3_path = os.path.join(output_dir, 'output3.html')
output_html4_path = os.path.join(output_dir, 'output4.html')

# 确保输出目录存在
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 读取文件内容
def read_file_content(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"读取文件 {filepath} 时出错: {e}")
        return None

# 创建文本内容页面
def create_text_content_page(content, filename):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <title>文本内容展示</title>
        <style>
            body {{ font-family: Arial, sans-serif; }}
            pre {{ font-size: 20px; padding: 20px; border: 1px solid #ddd; white-space: pre-wrap; }}
            #close-btn {{ position: fixed; top: 10px; left: 20px; }}
        </style>
    </head>
    <body>
        <button id="close-btn" onclick="closeWindow()">返回主页</button>
        <pre>
            {content}
        </pre>
        <script>
            function closeWindow() {{
                window.close();
            }}
        </script>
    </body>
    </html>
    """
    with open(filename, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

# 创建图片内容页面
def create_image_content_page(image_path, filename):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <title>图片内容展示</title>
        <style>
            body {{ font-family: Arial, sans-serif; }}
            img {{ max-width: 100%; height: auto; margin: 20px; display: block; }}
            #close-btn {{ position: fixed; top: 10px; left: 20px; }}
        </style>
    </head>
    <body>
        <button id="close-btn" onclick="closeWindow()">返回主页</button>
        <img src="{image_path}" alt="Image Content">
        <script>
            function closeWindow() {{
                window.close();
            }}
        </script>
    </body>
    </html>
    """
    with open(filename, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

# 创建主页
def create_index_page():
    index_content = f"""
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <title>主页</title>
        <style>
            body {{ font-family: Arial, sans-serif; }}
            h1 {{ font-size: 24px; }}
            ul {{ list-style-type: none; padding: 0; }}
            ul li {{ margin-bottom: 10px; }}
            a {{ font-size: 18px; }} /* 放大链接字体大小 */
        </style>
    </head>
    <body>
        <h1>请选择要查看的内容：</h1>
        <ul>
            <li><a href="{os.path.basename(output_html1_path)}" target="_blank">实际发货吨位前五的公司</a></li>
            <li><a href="{os.path.basename(output_html2_path)}" target="_blank">实际发货总额前五的公司</a></li>
            <li><a href="{os.path.basename(output_html3_path)}" target="_blank">海运陆运吨位占比</a></li>
            <li><a href="{os.path.basename(output_html4_path)}" target="_blank">各码头仓库发货总吨位</a></li>
        </ul>
    </body>
    </html>
    """
    with open(index_html_path, 'w', encoding='utf-8') as index_file:
        index_file.write(index_content)
# 主函数
def main():
    # 读取文件内容
    txt_content1 = read_file_content(txt_file1)
    txt_content2 = read_file_content(txt_file2)

    # 检查文件内容是否已读取
    if txt_content1 is None or txt_content2 is None:
        print("读取文件内容失败，请检查文件路径和编码。")
        return

    # 创建文本和图片内容页面
    create_text_content_page(txt_content1, output_html1_path)
    create_text_content_page(txt_content2, output_html2_path)
    create_image_content_page(png_file3, output_html3_path)
    create_image_content_page(png_file4, output_html4_path)

    # 创建主页
    create_index_page()

    print("所有HTML页面已生成。")

# 程序入口
if __name__ == "__main__":
    main()