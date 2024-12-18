# 假设输入的代码是一个字符串，每行一个代码
input_data = """
SJ-B-23-1-Efp-0001_AE01_F
SJ-B-23-1-Efp-0002_AE01_F
SJ-B-23-1-Efp-0003_AE01_F
SJ-B-23-1-Efp-0004_AE01_F
SJ-B-23-1-Efp-0005_AE01_F
SJ-B-23-1-Efp-0006_AE01_F
SJ-B-23-1-Efp-0007_AE01_F
SJ-B-23-1-Efp-0008_AE01_F
SJ-B-23-1-Efp-0009_AE01_F
SJ-B-23-1-Efp-0010_AE01_F
SJ-B-23-1-Efp-0011_AE01_F
SJ-B-23-1-Efp-0012_AE01_F
SJ-B-23-1-Efp-0013_AE01_F
SJ-B-23-1-Efp-0014_AE01_F
SJ-A-23-1-Efp-0001_AE01_F
SJ-A-23-1-Efp-0002_AE01_F
SJ-A-23-1-Efp-0003_AE01_F
SJ-T-23-1-Efp-0001_AE01_F
SJ-T-23-1-Efp-0002_AE01_F
SJ-T-23-1-Efp-0003_AE01_F
SJ-T-23-1-Efp-0004_AE01_F
SJ-T-23-1-Efp-0005_AE01_F
SJ-T-23-1-Efp-0006_AE01_F
SJ-T-23-1-Efp-0007_AE01_F
"""

# 将输入数据按行分割
input_codes = input_data.strip().split('\n')

# 打印输出的格式
print("tagCodes = [")
for code in input_codes:
    print(f'    "{code}",')
print("]")
