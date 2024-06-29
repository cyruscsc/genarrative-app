from dotenv import load_dotenv
from llm.models import MessageRole, TextMessage
from openai import AsyncOpenAI
from openai.types.chat import ChatCompletion

load_dotenv()

client = AsyncOpenAI()


def create_messages(system_msg: TextMessage, user_msg: TextMessage):
    return [
        {"role": MessageRole.system, "content": [system_msg.model_dump()]},
        {"role": MessageRole.user, "content": [user_msg.model_dump()]},
    ]


async def get_completion(messages: list[dict]) -> str:
    response: ChatCompletion = await client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response.choices[0].message.content
