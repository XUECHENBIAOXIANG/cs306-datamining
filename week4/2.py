import chardet


def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        return result


file_path = "ks-projects-201801.csv"
encoding = detect_encoding(file_path)
print("Detected Encoding:", encoding)
file_path = "PoliceKillingsUS.csv"
encoding = detect_encoding(file_path)
print("Detected Encoding:", encoding)
with open('PoliceKillingsUS.csv', 'r', encoding='cp1252') as file:
    content = file.read()

# 处理特殊字符
content = content.replace('€', 'euro_symbol')
content = content.replace('’', "'")
