import csv

def read_csv_file(filename):
    data = []
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            data.append(row)
    return data

# Example usage:
filename = '/export/xgen-hs/home/jasonlee/sales-call-data/summarized/summarized_call_data.csv'  # Provide the path to your CSV file
csv_data = read_csv_file(filename)
print (len(csv_data))
csv_data = [row for row in csv_data if not "Transcript" in row[2]]
print (len(csv_data))
#print(csv_data)

def create_dicts(data):
    dicts_list = []
    for row in data:
        input_dict = {
            "inputs": [
                {
                    "label": "text",
                    "type": "text",
                    "content": row[0]
                }
            ],
            "metadata": {
                "task_name": "highlighted_text_example_task",
                "desc": "task 1 for file upload taks configuration test",
                "queue_name": "highlighted text example collection"
            },
            "outputs": [
                {
                    "label": "xGen",
                    "type": "text",
                    "content": "",
                }
            ]
        }
        dicts_list.append(input_dict)
    return dicts_list

results = create_dicts(csv_data)
