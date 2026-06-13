from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["API_KEY"],
)
#secondary code if you have one "API KEY"


def chat(history):
    

    stream = client.chat.completions.create(
        model="x-ai/grok-build-0.1",
        messages=history,
        stream=True,
    )

    for chunk in stream:
        content = chunk.choices[0].delta.content
        if content:
            yield content
