# utils_llm.py
# 同济子豪兄 2024-5-22
# 调用大语言模型API

print('导入大模型API模块')


import openai
from openai import OpenAI
from API_KEY import *
def llm_yi(PROMPT='你好，你是谁？'):
    '''
    零一万物大模型API
    '''
    
    API_BASE = "https://api.lingyiwanwu.com/v1"
    API_KEY = YI_KEY

    MODEL = 'yi-large'
    # MODEL = 'yi-medium'
    # MODEL = 'yi-spark'
    
    # 访问大模型API
    client = OpenAI(api_key=API_KEY, base_url=API_BASE)
    completion = client.chat.completions.create(model=MODEL, messages=[{"role": "user", "content": PROMPT}])
    result = completion.choices[0].message.content.strip()
    return result
    
