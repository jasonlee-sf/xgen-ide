import requests
import json
import csv

guidelines = """
INSTRUCTIONS

You will be presented with a transcript of a sales call between a seller/sales representative and a customer. The transcript can be noisy and contain several mistakes, e.g. when both speakers are speaking simultaneously. Only the raw transcript will be provided and not the Speaker IDs, so you will have to identify the seller and the customer in the conversation in order to perform your task.

Your job is to read the transcript carefully and answer a few questions regarding the prospect of the deal being discussed, e.g. customer sentiment, concrete next steps, mentions of competitors, or any blockers from closing the deal. Construct your response using only the information contained in the call transcript. If you are unable to find sufficient evidence to answer a given question, say so in the response rather than conjecturing beyond what’s evident from the call transcript.

Make sure your response is direct, concise and professional. Refrain from using redacted PIIs (e.g. [ORG-1], [PERSON-2]) in your response and use generic terms such as “seller”, “customer”, “seller’s product” and “customer’s boss” as much as possible. Only use the specific naming convention ([PERSON-1]) when there are other individuals mentioned apart from seller/customer that are worth noting.

Avoid using pronouns in your response when possible. If you have to, use they/their/them.
"""
url = "https://xgenide.salesforceresearch.ai/api/upload"

def upload(input_data, queue_name, task_name):
    examples = []
    for transcript, questions in input_data:
        inputs = [{
            "label": "",
            "type": "text",
            "content": f"{transcript}"
        }]
        outputs = []
        for question in questions:
            outputs.append({
                "label": f"{question}",
                "type": "text",
                "content": ""
            })

        example = {
            "inputs": inputs,
            "outputs": outputs,
            "metadata": {
                "task_name": f"{task_name}",
                "desc": f"{guidelines}",
                "queue_name": f"{queue_name}"
            },
        }
        examples.append(example)
    data = {'data': json.dumps(examples, separators=(',', ':'))}
    res = requests.post(url, json=data)
    return res

if __name__ == '__main__':
    input_data = []
    with open("/Users/jason.lee2/scr/xgen-ide/04_2024/donna_gen_insights_eval.csv") as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            questions = row[0]
            questions = questions.split("Questions:")[1]
            questions = questions.split("Transcript:")[0]
            questions = questions.strip().split("\n")
            transcript = row[1]
            input_data.append(
                (transcript, questions)
            )
    #import ipdb; ipdb.set_trace()
    queue_name = "gen_insights_queue_0409_02"
    task_name = "gen_insights_task_0409_02"
    upload(input_data, queue_name, task_name)
    print (1)

