import json
f = open(r"C:\Users\Saeem\Desktop\GitHub\Machine Learning Check\deploy\Model-Deploy\Backend\Model_Deploy\Model\non_iid.json")

data = json.load(f)
print(data["Sheet1"])
f.close()