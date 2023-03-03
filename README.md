# Can ChatGPT Assess Human Personalities? <br> A General Evaluation Framework

## Introduction
This is a simplified implementation of automated testing codes for “Can ChatGPT Assess Human Personalities? A General Evaluation Framework”. The codes are used to produce **one independent testing** result of personality assessment. User may customize the codes to execute multiple testings to reproduce the complete result in the paper.

## Environment
```bash
pip install openai, ChatGPT_lite, asyncio, requests, brotli, numpy, csv, json
```

## Usage
- (1) Run ``Query_ChatGPT.py`` and ``Query_InstructGPT.py`` to query personalities of different subjects (**"People", "Men", "Women", "barbers", "accountants", "doctors"**). The program will automatically save the answers of ChatGPT and InstructGPT into ``.csv`` files. We provide two example saved files in ``/ChatGPT`` and ``/InstructGPT``.

- (2) Run ``Crawler_16personalities.py`` to automatically submit the saved answers to the MBTI testing website [16personalities](https://www.16personalities.com/), and return the results of personality scores, types, and roles.

An example result returned from ``Crawler_16personalities.py`` is shown as:
```bash
Subject: Men
Trait: Extraverted (E) 59 | Introverted (I) 41
Trait: Intuitive (N) 62 | Observant (S) 38
Trait: Thinking (T) 48 | Feeling (F) 52
Trait: Judging (J) 63 | Prospecting (P) 37
Trait: Assertive (A) 40 | Turbulent (T) 60
Character: enfj-protagonist
Dic. Judge: ENFJ-T Protagonist
```

Note: ``Query_ChatGPT.py`` (Line 160) requires the session token from the ChatGPT interface, and it is free and connected using [ChatGPT_lite](https://github.com/acheong08/ChatGPT-lite) library. ``Query_InstructGPT.py`` (Line 8) requires the API key generated from your OpenAI account. 


## Configuration
- In ``Query_InstructGPT.py`` (Line 119), the model can be changed to different [GPT-3 series](https://platform.openai.com/docs/models/overview) such as "text-davinci-003", "text-davinci-002", "text-davinci-001", "text-curie-001", etc. This enables our program to test more LLMs.

Update on 2 March: Currently ChatGPT API is available, and users can load its official model “gpt-3.5-turbo” or “gpt-3.5-turbo-0301” in ``Query_InstructGPT.py`` to perform a more stable testing with ChatGPT.

```bash
response = openai.Completion.create(
model="text-davinci-003",  # choose your testing LLM
prompt=[statement + instruction],
temperature=1.0,
max_tokens=2000,
top_p=1,
frequency_penalty=0,
presence_penalty=0)
```

## License

ChatGPT-MBTI is released under the MIT License. 
