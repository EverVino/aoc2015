import hashlib

#x= 'abcdef'
x = input()
n = len(x)
init = int("1" + "0"*5)
end = int("9"*(n+1))
print(init, end)
for number in range(init, end+1):
    s = x + str(number)
    has_obj = hashlib.md5(s.encode('utf-8'))
    if has_obj.hexdigest()[:6]== "00000":
        print(number)
        break



