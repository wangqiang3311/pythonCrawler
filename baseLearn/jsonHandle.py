import json
str=[{"username":"七夜","age":24},(2,3),1]
json_str=json.dumps(str,ensure_ascii=False)

print(json_str)

with open('qiye.txt','w') as fp:
    json.dump(str,fp=fp,ensure_ascii=False)