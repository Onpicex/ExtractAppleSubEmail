# import re
# import pandas as pd

# # 使用 'r' 参数和 'utf-8' 编码打开文件以便读取
# with open('input.txt', 'r', encoding='utf-8') as f:
#     text = f.read()

# pattern = r'[a-zA-Z0-9_.+-]+@icloud\.com'
# matches = re.findall(pattern, text)

# # 去除重复匹配项
# unique_matches = list(set(matches))

# # 将匹配结果转换为 DataFrame
# df = pd.DataFrame(unique_matches, columns=['Email'])

# # 将 DataFrame 写入 Excel 文件
# df.to_excel("output.xlsx", index=False)


import re

# 从对话框输入数据
text = input("Please enter the text: ")

pattern = r'[a-zA-Z0-9_.+-]+@icloud\.com'
matches = re.findall(pattern, text)

# 去除重复匹配项
unique_matches = list(set(matches))

# 在对话框中输出每个匹配的电子邮件地址
for email in unique_matches:
    print(email)
