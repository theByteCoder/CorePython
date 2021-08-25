file = open('requirements.txt', 'r')
try:
    for x in file:
        print(x)
    # raise EOFError('End of file')
except EOFError as e:
    print(e)
else:
    print(file.name)
finally:
    file.close()