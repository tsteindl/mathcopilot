from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr
import subprocess
import re
import os
import sys
import requests
import config

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


def get_latex_mpx():
    tex_file_path = f"./data/{input_file}.tex"
    command = ["mpx", "convert", f"./data/{input_file}.png", tex_file_path]

    command = ["mpx", "convert", f"./data/{input_file}.png", tex_file_path]
    subprocess.run(command, check=True)
    try:
        with open(f"{tex_file_path}.zip", 'r') as file:
            expr = file.read()
            return expr
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    return None

def get_latex_simpletex():
    api_url="https://server.simpletex.cn/api/latex_ocr" # interface address
    data = {  } # request data
    header={ "token": config.TOKEN } # Authentication information, use UAT method here
    file=[("file",("./img/int.png",open("./img/int.png", 'rb')))] # request file, field name is usually file
    res = requests.post(api_url, files=file, data=data, headers=header) # Use the requests library to upload files
    print(res.status_code)
    print(res.text)
    j = res["text"].json()
    return j["res"]["latex"]

def get_tex_from_file():
    with open("img/sum.tex", "r") as file:
        return file.read()
    return None

try:
    expr = get_tex_from_file()
    session = WolframLanguageSession()

    print(f"Parsed expression: {expr}")
    wolf_expr = wlexpr(f'ToExpression["{tex_to_wolfram(expr)}", TeXForm]//N')
    print(f"Evaluating : {wolf_expr}")

    print(session.evaluate(wolf_expr))

    session.terminate()
except:
    print("error")
