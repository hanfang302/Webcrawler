from lxml import etree

text = '''
<div>
    <ul>
        <li class="item-0"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-inactive"><a href="link3.html">third item</a></li>
        <li class="item-1"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a> # 注意，此处缺少一个 </li> 闭合标签
    </ul>
</div>
'''
#利用etree.HTML，将字符串解析为HTML文档类型，这里会自动帮我们补全不完整的字符串
html = etree.HTML(text)
# 按字符串序列化HTML文档,如果要读取本地的HTML可以使用以下方法
#etree.parse('html文件名')

result = etree.tostring(html)
#print(result)
#/从根节点开始
#result = html.xpath('//div/ul/li')
#result = html.xpath('//div/ul/li[position()>3]')
#result = html.xpath('//div/ul/li[position()<4]/a/text()')
#result = html.xpath('//li[@class="item-1"]//a/@href')
result = html.xpath('//li[@class="item-1"]/a/@href')
#容错
if result:
    a = result[0]
print(result)
#//从HTML文本中查找目标节点