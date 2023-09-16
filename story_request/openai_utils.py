import os

import openai

def get_message_from_complete_gpt_output(gpt_response):
    """Hint: gpt_response is the full output of ChatCompletion"""
    try:
        content = gpt_response["choices"][0]["message"]["content"]
        return content
    except Exception as e:
        print("ERROR EXTRACTING THE CONTENT FROM THE GPT OUTPUT")
        print(e)


def get_story_from_openai(prompt):
    try:
        chat_gpt_output = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a kind and gentle storyteller for kids."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        message_output = get_message_from_complete_gpt_output(chat_gpt_output)
    except Exception as e:
        print(e)
        print("ERROR USING ChatCompletion.create. Generating a backup story!")
        file_path = os.path.join(os.path.dirname(__file__), "stories", '0_bird_story_backup.txt')
        with open(file_path) as f:
            message_output = f.read()

    return message_output


