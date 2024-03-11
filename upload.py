import requests
import json

task_name="test_task"

def upload():
  url = 'https://xgenide.salesforceresearch.ai/api/upload'
  dataToBeUploaded = [
    {
      "inputs": [
        {
          "label": "input 1",
          "type": "text",
          "content": "Topic: New co-worker at the office\nMichael: Hi. Sam. \nSam: Michael. Good to meet you!\nMichael: Did you just arrive here?\nSam: Yeah, We arrived last week.\nMichael: How do you like it?\nSam: It's exciting! It's much busier than the last city we lived in. I was working in Seattle for the last 3 years.\nMichael: It really is very busy. I moved here from Tokyo 5 years ago and I still have trouble sometimes. Did you move here with your wife?\nSam: Actually, I'm not married. I moved here with my dog, Charles. We are very close.\nMichael: Oh. I see.\nSam: What about you?\nMichael: Yes, I am married and I have two children.\nSam: How old are they?\nMichael: 6 and 8 years old\nSam: Oh, great. That age is a lot of fun.\nMichael: But it is exhausting.\nSam: I understand. My brother has kids the same age. Every time we visit he falls asleep on the sofa.\nMichael: Must be nice. We don't have time to sleep, we have to drink a lot of coffee.\n"
        },
        {
          "label": "input 2",
          "type": "text",
          "content": "exhausting: something makes you very tired.\nEx: Working on a farm is exhausting, you have to exercise all day.\nEx: Speaking English all day can be exhausting.\nfall+ asleep: the beginning of sleep.\nEx: He was in bed and falling asleep when the phone rang.  \nvery close: to have a close relationship with a friend or family member.\nEx: You can be very close to your sister or your classmates.\nhave+ trouble: an informal way to speak about having problems.\nEx: I have trouble with my knee sometimes. She has trouble hearing because she is very old."
        }
      ],
      "metadata": {
        "task_name": task_name,
        "desc": "upload test",
        "queue_name": "upload test"
      },
      "outputs": [
        {
          "label": "output 1",
          "type": "text",
          "content": "Topic: Output for a conversation with highlighted text\nPERSON 1: This color for PERSON 1 should be different than for PERSON 2\nPERSON 2: Each selected highlighted word should have a different color (up to 10 words)\nPERSON 3: This persons name was not passed to the config\nPERSON 1: highlighted words are also case sensitive, PERSON 2 is highlighted but person 2 is not."
        }
      ]
    },
  ]
  data = {'data': json.dumps(dataToBeUploaded,separators=(',', ':'))}
  res = requests.post(url,json=data)
  return res

if __name__ == '__main__':
  upload()

