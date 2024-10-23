import ollama

def agent_ollama(AGENT_SYS_PROMPT,AGENT_PROMPT):
    response = ollama.chat(model="qwen2.5", messages=[
        {"role": "system", "content": AGENT_SYS_PROMPT},  # 系统提示设定人设
        {"role": "user", "content": AGENT_PROMPT}  # 用户的实际指令
    ])
    return response['message']['content']