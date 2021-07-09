import datetime

alphabets = [str(x) for x in range(10000000)]
print(alphabets)

a = datetime.datetime.now()  # store initial time
for item in alphabets:
    len(item)
b = datetime.datetime.now()  # store final time
print(b - a)  # results

a = datetime.datetime.now()
fn = len  # function stored locally
for item in alphabets:
    fn(item)
b = datetime.datetime.now()
print(b - a)
