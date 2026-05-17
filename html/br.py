file_path = "c:\\Users\\A\\Desktop\\html源码\\pagedemo-master\\html\\hlm.txt"  # 原始文件路径
output_path = "c:\\Users\\A\\Desktop\\html源码\\pagedemo-master\\html\\hlm_processed.html"  # 处理后保存的文件路径

try:
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()  # 逐行读取内容

    # 处理内容，在每一行的前后加上 <br><br>
    processed_content = ""
    for line in content:
        line = line.strip()  # 去掉行首尾的空白
        if line:  # 如果不是空行
            processed_content += f"{line}<br><br>\n"

    # 将处理后的内容写入到一个新文件
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(processed_content)

    print(f"内容已处理并保存到：{output_path}")

except UnicodeDecodeError as e:
    print(f"文件解码错误: {e}")
except Exception as e:
    print(f"出现错误: {e}")
