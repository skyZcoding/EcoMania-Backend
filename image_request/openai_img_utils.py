import openai


def get_image_url_from_complete_gpt_output(gpt_response):
    """Hint: gpt_response is the full output of ChatCompletion"""
    try:
        content = gpt_response["data"][0]["url"]
        return content
    except Exception as e:
        print("ERROR EXTRACTING THE CONTENT FROM THE GPT OUTPUT")
        print(e)


def get_image_url_from_openai(prompt):
    try:
        chat_gpt_output = openai.Image.create(
            prompt=prompt,
            n=1,
            size=f"256x256"
        )
    except Exception as e:
        print("ERROR USING Image.create")
        print(e)
        return
    img_output = get_image_url_from_complete_gpt_output(chat_gpt_output)
    return img_output
