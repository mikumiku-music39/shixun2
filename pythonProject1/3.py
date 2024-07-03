import pandas as pd
import matplotlib.pyplot as plt

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

# 准备饼状图的数据
labels = ['陆运', '海运']
sizes = [land_transport_sum, sea_transport_sum]

# 绘制饼状图
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('运输方式分布')

# 确保饼状图是圆形的
plt.axis('equal')

# 显示饼状图
plt.show()