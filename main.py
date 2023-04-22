
import requests
import json
OPENAI_API_KEY ="TOKEN HERE"



def get_res2(prompt, max_tokens):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "max_tokens": max_tokens,
        "temperature": 0.3,
        "messages": [{"role": "user", "content": prompt}]
       
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, data=json.dumps(data))

    if response.status_code != 200:
        raise ValueError("Request to OpenAI API failed with error code:", response.status_code)

    response_json = response.json()

    if "choices" not in response_json:
        raise ValueError("Response from OpenAI API does not contain 'choices' key:", response_json)
    print(response_json)

    return response_json["choices"][0]["message"]["content"]



def sendtoopenai(mode,mtext):
    if mode == "1":
        print("\n \nAPI request wird gemacht bitte warte...")
        res = get_res2(mtext,250)
        print("\n \n\n\n\n"+f"{res}")


x = input("Dein text => ")

words = len(x.split())
tokens = words * 0.8
price = tokens * 0.000004
formatted_price = "{:.7f}".format(price)
print("Words => "+str(words)+" | Tokens => "+str(tokens) + " | Price => " +str(formatted_price)+"$")
sendtoopenai("1","Correct the gramma : "+x)

