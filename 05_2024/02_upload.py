from pprint import pprint as pp
import requests
import json
import csv
import argparse

guidelines = ""
url = "https://xgenide.salesforceresearch.ai/api/upload"

def upload(input_data, queue_name, task_name):
    examples = []
    for id, transcript, questions, answers in input_data:
        inputs = [{
            "label": "",
            "type": "text",
            "content": f"{transcript}"
        }]
        outputs = []
        q_idx = 1
        for question, answer in zip(questions, answers):
            outputs.append({
                "label": f"{q_idx}. {question}",
                "type": "text",
                "content": f"{answer}"
            })
            q_idx += 1

        id = id.split("_")
        id = "_".join(id[1:])
        # "#task_name": f"{id}",
        example = {
            "inputs": inputs,
            "outputs": outputs,
            "metadata": {
                "input_header": "Transcript",
                "output_headder": "Questions",
                "task_name": f"{task_name}",
                "desc": f"{guidelines}",
                "queue_name": f"{queue_name}",
                "id": f"{id}",
            },
        }
        examples.append(example)
    data = {'data': json.dumps(examples, separators=(',', ':'))}
    res = requests.post(url, json=data)
    #print (f"requests.post result: {res}")
    return res

def main(args):
    queue_name = f"gi_0513_main_queue"
    task_name = "gi_task"
    with open(args.csv_path) as f:
        reader = csv.reader(f)
        input_data = []
        for idx, row in enumerate(reader):
            # if idx < 2000:
            #     continue
            if idx == 2000:
                break
            if idx % args.upload_every == 0:
                print (idx)
                upload(input_data, queue_name, task_name)
                input_data = []
            id = row[0]
            transcript = row[1]
            questions = row[2::2]
            answers = row[3::2]
            assert len(questions) == len(answers)
            input_data.append(
                (id, transcript, questions, answers)
            )
    if len(input_data) > 0:
        upload(input_data, queue_name, task_name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv_path", type=str, default="/Users/jason.lee2/scr/xgen-ide/05_2024/13_data/gi_result.csv")
    parser.add_argument("--upload_every", type=int, default=20)
    args = parser.parse_args()
    main(args)
