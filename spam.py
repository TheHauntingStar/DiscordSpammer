import requests
import time

payload = {
    'content': "MESSAGE HERE"
}

headers = {
    'authorization': 'PASTE TOKEN HERE'
}

channel_id = 'PASTE ID HERE'

for i in range(1000):
    response = requests.post('REQUEST URL HERE', data=payload, headers=headers)

    if response.status_code == 429:
        
        retry_after = response.json().get('retry_after', 5)  
        print(f"rate limited. waiting for {retry_after} seconds.")
        time.sleep(retry_after)
        i -= 1  #
    elif response.status_code != 200:
        print(f"couldn't send message. status code: {response.status_code}")
    else:
        print(f"msg {i + 1} sent successfully")

    time.sleep(1)  # adjust the time based on discord's rate limits retard
