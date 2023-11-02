from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr
import subprocess
import re
import os
import sys

replacement_dict = {
    'e': 'E'
}

def tex_to_wolfram(s):
    pattern = r'(?<!\\)(' + '|'.join(re.escape(key) for key in replacement_dict.keys()) + ')'
    replaced_string = re.sub(pattern, lambda match: replacement_dict[match.group()], s)
    replaced_string = replaced_string.replace("\\", "\\\\")
    return replaced_string

if len(sys.argv) > 1:
    current_dir = sys.argv[1]
    if len(sys.argv) > 2:
        input_file = sys.argv[2]
    else:
        input_file = "curr"
    os.chdir(current_dir)


tex_file_path = f"./data/{input_file}.tex"

# command = ["mpx", "convert", f"./data/{input_file}.png", tex_file_path]

try:
    with open(f"{tex_file_path}.zip", 'r') as file:
        expr = file.read()
except Exception as e:
    print(f"An error occurred: {str(e)}")

session = WolframLanguageSession()

print(f"Parsed expression: {expr}")
wolf_expr = wlexpr(f'ToExpression["{tex_to_wolfram(expr)}", TeXForm]//N')
# print(f"Evaluating : {wolf_expr}")

print(session.evaluate(wolf_expr))

session.terminate()
