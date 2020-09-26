import uuid 
data = [uuid.uuid4() for x in range(0,10000)]

print(len(data))
print(len(list(set(data))))