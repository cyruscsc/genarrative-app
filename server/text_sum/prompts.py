system_message = """
Your task is to generate a summary of the given text. \
Your response should be precise and concise.
"""

prompt_template = """
Generate a comprehensive summary of the given text below, \
delimited in triple backticks, in bulleted lists. \
The summary should cover all the key points and main ideas \
presented in the original text, \
while also condensing the information into \
a concise and easy-to-understand format, \
with clear title, headings and subheadings.
"""


def create_prompt(text: str) -> str:
    return f"{prompt_template}\n{f'```{text}```'}"
