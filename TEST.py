def introspection_info(obj):
    info_obj = {}
    info_obj['Тип объекта'] = type(obj).__name__
    info_obj['Атрибуты и методы объекта'] = dir(obj)
    try:
        info_obj['Объект из модуля'] = obj.__module__
    except:
        info_obj['Объект из модуля'] = 'У объекта такого нет...'

    return info_obj


class OK:
    
    def __init__(self):
        self.ff = 42
        self.gg = "asd"
    def met(self):
        return 'FF'

num1 = 1
num2 = 1.1
str1 = 'dozor'
lst1 = [0]
dict1 = {'key1': 'value1'}


lst = [num1, num2, str1, lst1, OK, dict1, introspection_info]

for i in lst:
    print(introspection_info(i))