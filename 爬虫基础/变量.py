_name = 'zhangsan'
def a():
    global _name
    _name='lisi'

a()
print(_name)
