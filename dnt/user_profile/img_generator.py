import openai
openai.api_key = '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'
response = openai.Image.create(
  prompt="лес закат",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(response)
