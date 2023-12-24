# Scrapsters API
This is the API that powers the Scrapsters app, winner of the Migros challenge at [Hackzurich](https://hackzurich.com/) 2023!

### What it does
SCRAPSTERS is an app that makes shopping sustainable and engaging. Our app boosts customers' sustainable shopping habits by evaluating their shopping lists for sustainability and rewarding them with our unique superheroes - Scrapsters. These Scrapsters are sustainable toys made out of recycled materials, serving both an entertaining and educational function. Each Scrapster comes with a customized story generated through AI, making every toy truly unique and personalized.

### Pitch video
[<img src="https://img.youtube.com/vi/4AcOAane8W0/maxresdefault.jpg" width="350">](https://youtu.be/4AcOAane8W0?si=IfXOGqy1Yh5XtENi)

### Links
- Full project on [DevPost](https://devpost.com/software/scrapsters)
- Front-end source code available at this [repo](https://github.com/skyZcoding/EcoMania-Frontend).

## Setup and run

Get a valid OpenAi key.

Create a `.env` file on the root of the repo with the following content:

```
OPENAI_KEY=<valid-key-of-openai>
```

Then, you can install the requirements and run the web app:
```
pip install -r requirement.txt
flask run
```
