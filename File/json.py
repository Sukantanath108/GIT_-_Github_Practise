import json
x =  '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)
#z = json.dumps(x)
#m = json.dumps(x, indent=4)
n = json.loads(z)

print(y)
print(z)
print(m)
print(n)