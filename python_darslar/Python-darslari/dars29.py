#dir() funksiyasi yordamida istalgan obyekt yoki klassning xususiyatlari va metodlarini ko'rib olishimiz mumkin:
>>> dir(Talaba)
['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 'get_age',
 'get_fullname',
 'get_info',
 'get_lastname',
 'get_name',
 'set_bosqich',
 'update_bosqich']
def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]

print(see_methods(Talaba))