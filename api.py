import config

print(config.TOKEN)

import requests
api_url="https://server.simpletex.cn/api/latex_ocr" # interface address
data = {  } # request data
header={ "token": config.TOKEN } # Authentication information, use UAT method here
file=[("file",("./img/int.png",open("./img/sum.png", 'rb')))] # request file, field name is usually file
res = requests.post(api_url, files=file, data=data, headers=header) # Use the requests library to upload files
print(res.status_code)
print(res.text)
