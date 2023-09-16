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
        img_url_output = get_image_url_from_complete_gpt_output(chat_gpt_output)
    except Exception as e:
        print(e)
        print("ERROR USING Image.create, returning a backup url")
        img_url_output = "https://oli.show/scrapsters/tetrabreeze.jpeg"

    return img_url_output
