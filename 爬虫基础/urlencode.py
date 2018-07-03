from urllib import parse
a = {'wd':'French法国人'}
print('转换前：',a)
a = parse.urlencode(a)
print('转换后:',a)
#通过urllib.parse.unquote()方法，把URL编码字符串，转换回原先的字符串
a = parse.unquote(a)
print('转换回：',a)