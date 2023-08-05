import os
import os
def read_cpp_files(folder_path):
    cpp_files = []
    for root, directories, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".cpp") or file.endswith(".hpp"):
                file_path = os.path.join(root, file)
                cpp_files.append(file_path)
    
    cpp_code_texts = []
    for file_path in cpp_files:
        with open(file_path, "r", encoding="utf-8") as file:  # 指定编码为 utf-8
            code_text = file.read()
            cpp_code_texts.append((file_path, code_text))  # 存储代码文本和文件路径的元组
    
    return cpp_code_texts

def save_code_text_to_file(cpp_code_texts, output_file):
    with open(output_file, "w", encoding="utf-8") as file:  # 指定编码为 utf-8
        for file_path, code_text in cpp_code_texts:
            file.write(f"File Path: {file_path}\n\n")
            file.write(code_text + "\n\n")
            file.write("=" * 80 + "\n\n")  # 使用分隔符分隔每个代码文本
import os
import os

def find_keyword_in_files(folder_path, keyword):
    matching_lines = []
    for root, directories, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".cpp") or file.endswith(".hpp"):  # 只搜索 C++ 文件
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    lines = f.readlines()
                    for line_number, line_text in enumerate(lines, 1):
                        if keyword in line_text:
                            matching_lines.append((file_path, line_number, line_text.strip()))
    return matching_lines




# 要搜索的文件夹路径
folder_path = "C://pytorch"

# 要搜索的关键代码名字
keyword = "sub"

# 在指定文件夹中查找包含关键代码名字的文件
matching_files = find_keyword_in_files(folder_path, keyword)

# 打印匹配的文件路径
for file_path in matching_files:
    print("",keyword,"代码名字出现在文件路径:", file_path)


# 要搜索的文件夹路径
#folder_path = "C://pytorch"

# 获取所有C++文件的代码文本和文件路径
#cpp_code_texts = read_cpp_files(folder_path)

# 将代码文本保存到一个文件中
#output_file = "cpp_code_texts.txt"
#save_code_text_to_file(cpp_code_texts, output_file)

# 显示代码所在的文件夹路径
#for file_path, _ in cpp_code_texts:
 #   print("代码所在文件夹路径:", file_path)

#print("所有C++文件的代码保存到文件:", output_file)

