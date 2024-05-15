# try:
#     file = open('try-except/a_file.txt')
#     a_dict = {'key':'value'}
#     print(a_dict['key'])
# except FileNotFoundError:
#     file = open('try-except/a_file.txt','w')
#     file.write('Something')
# except KeyError as error_message:
#     print(f'that key {error_message} does not exist')
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError ('yang betul dong')
#     file.close()
#     print('file was closed.')


height =float(input('Height: '))
weight = int(input('Weight: '))
bmi = weight/height**2
print(bmi)