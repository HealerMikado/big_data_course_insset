import random
import time
import json
import math
toggle = False
for _ in range(100):

    account_id = random.randint(1,10)
    data = {
    "account_id" : account_id,
    "value" : round(random.uniform(0,500), 2),
    "timestamp" : time.time()+random.uniform(-5,5)
}
    if account_id==9:
        if toggle :
            toggle = False
            data["value"] = round(random.uniform(500,100), 2)
        else :
            toggle = True
            data["value"] = round(random.random(), 2)
    print(json.dumps(data))