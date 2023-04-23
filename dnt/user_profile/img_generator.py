import openai
from secret import OPEN_AI
openai.api_key = OPEN_AI
response = openai.Image.create(
  prompt="I am Groot",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(response)
