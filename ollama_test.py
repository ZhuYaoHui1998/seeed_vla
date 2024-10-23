import ollama
SYSTEM_PROMPT = '''
I am about to give a command to the robotic arm, and I need you to extract the starting object and the ending object from this command. Then, find the top-left and bottom-right pixel coordinates of these two objects in the image and output them in JSON format. For example, if my command is: "Please help me place the red block on the house drawing," you should output the following format: {"start":"red block","start_xyxy":[[102,505],[324,860]],"end":"house drawing","end_xyxy":[[300,150],[476,310]]}. Only respond with the JSON itself, do not reply with anything else. My current command is:
'''


res = ollama.chat(
	model="llava:13b",
	messages=[
		{
			'role': 'user',
            'prompt':SYSTEM_PROMPT,
			'content': 'Please help me place the red block on the pen.',
			'images': ['./temp/vl_now.jpg']
		}
	]
)

print(res['message']['content'])