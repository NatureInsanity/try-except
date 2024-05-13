try:
    file = open('try-except/a_file.txt')
    a_dict = {'key':'value'}
    print(a_dict['key'])
except FileNotFoundError:
    file = open('try-except/a_file.txt','w')
    file.write('Something')
except KeyError as error_message:
    print(f'that key {error_message} does not exist')
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print('file was closed.')