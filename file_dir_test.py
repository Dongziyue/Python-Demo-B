import os

# print(os.name)  # posix

# print(os.uname())

# print(os.environ)

# print(os.environ.get('PATH'))

# if os.path.exists('logo.png'):
#     os.remove('logo.png')
# else:
#     print('file not exists.')

# os.rename('google.png', 'logo-google.png')

# import shutil
#
# shutil.copyfile('logo-google.png', 'google.png')

print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[-1] == '.md'])

# print(os.path.splitext('test.txt')[-1])

# print(os.path.abspath('README.md'))


# print(os.path.join('C:\\', 'test1', 'test2', 'test.txt'))

# os.mkdir(os.path.join('D:\\', 'test1', 'test2'))

# os.rmdir(os.path.join('D:\\', 'test1', 'test2'))

# os.rmdir(os.path.join('D:\\', 'test1'))

# print(os.path.split('C:\\test1\\test2\\test.txt'))

# print(os.path.splitext('test1.test2.md')[-1])  # extension

print([x for x in os.listdir('.') if os.path.isdir(x)])