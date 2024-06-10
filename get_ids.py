import sys

import requests
url = "https://xgenide.salesforceresearch.ai/api/annotations/getUniqueIds"
for queue_name in sys.argv[1:]:
    res = requests.post(url, json={"queue_name": f"{queue_name}"})
    print (f"Deleting {queue_name}: {res}")
