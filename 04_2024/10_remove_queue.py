import sys

import requests
url = "https://xgenide.salesforceresearch.ai/api/upload"
print (sys.argv[1])
requests.post(url, json={"queue_name": f"{sys.argv[1]}"})
