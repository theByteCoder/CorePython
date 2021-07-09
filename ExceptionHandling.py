def exception_handling(n):
    result = 0
    try:
        result = 1 / n
        print('try -run when no exception : ', result)
    except ZeroDivisionError:
        print('except - run when exception : ', 'zero division error')
    else:
        print('else - run when no exception : ', result)
    finally:
        print('finally - always run : ', result)


exception_handling(0)

exception_handling(1)
