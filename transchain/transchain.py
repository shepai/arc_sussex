import json
from   arc_utils import *
from   openai    import OpenAI

openai_api_key = json.load(open('openai_api_key.json'))

client = OpenAI(**openai_api_key)











prompt1 = \
"""I would like you to look at the following pairs of number matrices.

In each pair, the first matrix represents the input to some program, and the second matrix represents the output.

A single rule relates all the input-output pairs. Your task is to help me deduce this rule by pointing out ways in which parts of the output may be deduced from the input. You do not have to propose a "final solution", only relationships which may exist between all the outputs and their corresponding inputs.

""" + evaluation_puzzles['27a77e38'].worked_examples() + """

What patterns do you see?

At the end of your response, give a summary of the pattern you're surest of, delimited with <summary></summary> tags."""


response = client.chat.completions.create(
    messages=[{
        "role": "user",
        "content": prompt1,
    }],
    model="gpt-4o",
)

summary = response.to_dict()['choices'][0]['message']['content'].split('<summary>')[1].split('</summary>')[0]

orange_escape_code = '\033[38;5;208m'
reset_code = '\033[0m'

print(f'\n\nPattern:\n\n{orange_escape_code}{summary}{reset_code}')



















prompt2 = \
"""I have a puzzle which I would like you to help me simplify. The puzzle consists of pairs of matrices (one input matrix and one output matrix) each containing numbers from 0 to 9 in each of their cells. My task is to find the relationship between the input and the output matrix in each pair.

Because the matrices contain a lot of data and it's hard to know what to pay attention to, I am trying to simplify them by making them smaller or having them contain fewer redundant elements.

Below are the pairs of matrices making up this puzzle. Take a look:

""" + evaluation_puzzles['27a77e38'].worked_examples() + """

With the help of an LLM, I was able to spot the following pattern which relates the input and output in each pair:

<pattern>""" + summary + """</pattern>

Using this pattern as an inspiration, I would like you to first decide on a *simple* reversible transformation you can perform on an input-output pair that would give another (simpler) input-output pair.

I would then like you to write a pair of functions `f()` and `g()` in Python that perform and reverse that transformation, i.e.

`f(I, O)` takes the two matrices making up a pair and returns two new matrices where a redundancy outlined in the pattern above has been eliminated.

`g(IPrime, OPrime)` is the inverse of `f()`. That is, it takes `f()`'s outputs as its input and reconstructs I and O from them.

As you can see, `f()` must be an invertible function.

Your response must start with you laying out your reasoning about how to construct the two functions, and checking that the functions `f` and `g` that you propose are in fact inverses.

Your response must contain Python code giving the two functions `f()` and `g()`. Each function must be self-contained and not rely on global variables. Each function must take exactly two arguments (a pair of matrices) and return exactly two arguments (another pair of matrices). All of the arguments of the functions must be `numpy.ndarray` objects, and they must each return a tuple of two `numpy.ndarray` objects.

Your Python code MUST be preceded with a <python> tag and followed by a </python> tag and must not contain anything apart from the functions `f` and `g`.

Good luck!
"""

response = client.chat.completions.create(
    messages=[{
        "role": "user",
        "content": prompt2,
    }],
    model="gpt-4o",
)

python = response.to_dict()['choices'][0]['message']['content'].split('<python>')[1].split('</python>')[0]

print(f'\n\nPython code for performing the transformation and reversing it:\n\n{orange_escape_code}{python}{reset_code}')