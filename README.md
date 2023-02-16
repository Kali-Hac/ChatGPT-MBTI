# Can ChatGPT Judge Human Personalities? A General Evaluation Framework

## Introduction
This is the implementation of automated testing codes for “Can ChatGPT Judge Human Personalities? A General Evaluation Framework”. The codes are used to reproduce experimental results in the paper.

## Environment
```bash
pip install openai, ChatGPT_lite, asyncio, requests, brotli, numpy, csv, json
```

## Usage
- (1) Run ``Query_ChatGPT.py`` and ``Query_InstructGPT.py`` to query personalities of different subjects (**"People", "Men", "Women", "the Asian", "the American", "the African"**). The program will automatically save the answers of ChatGPT and InstructGPT into ``.csv`` files.

- (2) Run ``Crawler_16personalities.py`` to automatically submit the saved answers to the MBTI testing website [16personalities](https://www.16personalities.com/), and return the results of personality scores, types, and roles.

Note: ``Query_ChatGPT.py`` (Line 160) requires the session token from the ChatGPT interface, and it is free and connected using [ChatGPT_lite](https://github.com/acheong08/ChatGPT-lite) library. ``Query_InstructGPT.py`` (Line 8) requires the API key generated from your OpenAI account. 


## Configuration
- In ``Query_InstructGPT.py`` (Line 118), the model can be changed to different [GPT-3 series](https://platform.openai.com/docs/models/overview) such as "text-davinci-003", "text-davinci-002", "text-davinci-001", "text-curie-001", etc. This enables our program to test more LLMs.
```bash
response = openai.Completion.create(
model="text-davinci-003",  # choose your testing LLM
prompt=first_statement+question,
temperature=t,
max_tokens=2000,
top_p=1,
frequency_penalty=0,
presence_penalty=0)
```

## License

ChatGPT-MBTI is released under the MIT License. 
