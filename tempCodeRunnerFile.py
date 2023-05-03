
import openai
import os


openai.api_key = "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"
""" response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"{str}",
    max_tokens=25,
    temperature=0.8,

) """
while (True):
    str = input("You: ")
    if str.lower == "stop":
        break
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"{str}"}
        ]
    )
    """ print(response.choices[0].message.role + ": " +
          response.choices[0].message.content) """
