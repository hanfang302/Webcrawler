import re
#import ssl

html = """
    <img alt="" src="https://img.meituan.net/msmerchant/e637f5b1064ff5dff2005e1f361db659529831.jpg%40300w_225h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20">
"""

#context = ssl._create_unverified_context

a = re.compile('<img.*?src="(.*?)">',re.S)
b = re.findall(a,html)
print(b)
