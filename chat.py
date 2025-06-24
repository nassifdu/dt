
import openai
from os import getenv

MODEL = 'gpt-4.1-mini'

client = openai.OpenAI(api_key=getenv("OPENAI_API_KEY"))

def gen(
        user: list[str] | str,
        system: list[str] | str = [],
        assistant: list[str] | str = [],
        model=MODEL
    ) -> str:

    """Generate a response from the OpenAI model."""
    if isinstance(user, str):
        user = [user]
    if isinstance(system, str):
        system = [system]
    if isinstance(assistant, str):
        assistant = [assistant]

    messages = [{'role': 'system', 'content': sys} for sys in system] + \
               [{'role': 'user', 'content': use} for use in user] + \
                [{'role': 'assistant', 'content': ass} for ass in assistant]

    response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    
    return response.choices[0].message.content