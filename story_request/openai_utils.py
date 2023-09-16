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
    except Exception as e:
        print("ERROR USING ChatCompletion.create")
        print(e)
        return
    message_output = get_message_from_complete_gpt_output(chat_gpt_output)
    return message_output


