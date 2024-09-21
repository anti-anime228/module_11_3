def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = []
    methods = []
    for atr in dir(obj):
        if not atr.startswith('__') or not atr.endswith('__'):
            attribute = getattr(obj, atr)
            if callable(attribute):
                methods.append(atr)
            else:
                attributes.append(atr)

    module = getattr(obj, "__module__", "__main__")

    return {
        "type": obj_type,
        "attributes": sorted(attributes),
        "methods": sorted(methods),
        "module": module
    }

num1 = 1
num2 = 1.1
str1 = 'dozor'
lst1 = [0]
dict1 = {'key1': 'value1'}

lst = [num1, num2, str1, lst1, dict1]

for i in lst:
    print(introspection_info(i))
