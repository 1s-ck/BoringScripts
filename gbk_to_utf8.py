import argparse
import os

def convert_gbk_to_utf8(input_path, output_path=None):
    """
    将GBK编码文件转换为UTF-8编码文件
    :param input_path: 输入文件路径
    :param output_path: 输出文件路径（默认添加_utf8后缀）
    :return: 转换成功返回True，否则返回False
    """
    try:
        # 设置默认输出路径
        if output_path is None:
            base, ext = os.path.splitext(input_path)
            output_path = f"{base}_utf8{ext}"

        # 检测文件是否存在
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"输入文件不存在：{input_path}")

        # 执行转换
        with open(input_path, 'r', encoding='gbk') as f_in:
            content = f_in.read()

        with open(output_path, 'w', encoding='utf-8') as f_out:
            f_out.write(content)

        print(f"转换成功！输出文件已保存至：{output_path}")
        return True

    except UnicodeDecodeError as e:
        print(f"解码失败：{e}\n提示：文件可能不是GBK编码格式")
        return False
    except Exception as e:
        print(f"发生未知错误：{str(e)}")
        return False

if __name__ == "__main__":
    # 设置命令行参数
    parser = argparse.ArgumentParser(
        description="GBK到UTF-8文件编码转换工具",
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('input', help='输入文件路径')
    parser.add_argument('-o', '--output', help='输出文件路径（可选）')
    
    # 示例说明
    example_usage = '''示例：
    python gbk2utf8.py input.txt -o output.txt
    python gbk2utf8.py example.csv
    （默认会在同目录生成 example_utf8.csv）'''
    parser.epilog = example_usage

    # 解析参数
    args = parser.parse_args()

    # 执行转换
    result = convert_gbk_to_utf8(args.input, args.output)
    
    # 设置退出码（0成功，1失败）
    exit(0 if result else 1)