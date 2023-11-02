from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr
import subprocess
import re

replacement_dict = {
    'e': 'E'
}

def tex_to_wolfram(s):
    pattern = r'(?<!\\)(' + '|'.join(re.escape(key) for key in replacement_dict.keys()) + ')'
    replaced_string = re.sub(pattern, lambda match: replacement_dict[match.group()], s)
    replaced_string = replaced_string.replace("\\", "\\\\")
    return replaced_string
    # return s.replace("\\", "\\\\").replace("e", "E")


input_file = "sum"
tex_file_path = f"data/{input_file}.tex"

command = ["mpx", "convert", f"data/{input_file}.png", tex_file_path]

try:
    subprocess.run(command, check=True)
    try:
        with open(f"{tex_file_path}.zip", 'r') as file:
            expr = file.read()
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    session = WolframLanguageSession()

    print(f"Parsed expression: {expr}")
    wolf_expr = wlexpr(f'ToExpression["{tex_to_wolfram(expr)}", TeXForm]//N')
    print(f"Evaluating : {wolf_expr}")

    print(session.evaluate(wolf_expr))

    session.terminate()

except subprocess.CalledProcessError as e:
    print(f"Command '{' '.join(command)}' failed with error code {e.returncode}.")
except FileNotFoundError:
    print("The 'mpx' command is not found. Make sure it's installed and in your system's PATH.")




