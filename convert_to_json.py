import json
import os

# 读取原始的 JSON 数据并格式化
def format_json(input_file):
    # 获取输入文件的绝对路径并添加 "output_" 前缀到输出文件名
    absolute_input_path = os.path.abspath(input_file)
    output_file = "output_" + os.path.basename(absolute_input_path)
    
    # 检查文件是否存在
    if not os.path.isfile(absolute_input_path):
        print(f"错误: 输入的文件 '{input_file}' 不存在，请检查路径。")
        return
    
    with open(absolute_input_path, 'r', encoding='utf-8') as infile:
        data = json.load(infile)  # 读取 JSON 数据
        
    # 使用 json.dumps 格式化 JSON 数据，确保缩进为 4 个空格
    formatted_json = json.dumps(data, indent=4, ensure_ascii=False)
    
    # 获取输出文件的路径，并保存格式化后的 JSON 数据
    output_path = os.path.join(os.path.dirname(absolute_input_path), output_file)
    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.write(formatted_json)

    print(f"JSON 文件已经格式化并保存为: {output_path}")

# 用户输入文件路径（相对路径或绝对路径）
input_file = input("请输入输入文件名（可以是相对路径或绝对路径）: ")

# 调用函数格式化 JSON
format_json(input_file)
