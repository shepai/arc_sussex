import json
from   arc_utils import *
from   openai    import OpenAI

openai_api_key = json.load(open('openai_api_key.json'))

client = OpenAI(**openai_api_key)

prompt = \
"""I would like you to look at the following three pairs of number matrices.

In each pair, the first matrix represents the input to some program, and the second matrix represents the output.

A single rule relates all the input-output pairs. Your task is to help me deduce this rule by pointing out ways in which parts of the output may be deduced from the input. You do not have to propose a "final solution", only relationships which may exist between all the outputs and their corresponding inputs.

""" + evaluation_puzzles['27a77e38'].worked_examples() + """

What patterns do you see?"""

response = client.chat.completions.create(
    messages=[{
        "role": "user",
        "content": prompt,
    }],
    model="gpt-4o-mini",
)

print(response.to_dict()['choices'][0]['message']['content'])