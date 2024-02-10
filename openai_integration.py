# import openai

# def generate_openai_recommendations(financial_context):
#     openai.api_key = "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"
#     response = openai.ChatCompletion.create(
#       model="gpt-3.5-turbo",
#       messages=[{"role": "system", "content": financial_context}, {"role": "user", "content": "What are some personalized investment recommendations?"}]
#     )
#     return response.choices[0].message["content"]


import openai

def generate_openai_recommendations(api_key, financial_context):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": financial_context}, {"role": "user", "content": "What are some personalized investment recommendations?"}]
    )
    return response.choices[0].message["content"]
