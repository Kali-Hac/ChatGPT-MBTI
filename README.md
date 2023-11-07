# Can ChatGPT Assess Human Personalities? <br> A General Evaluation Framework
![](https://img.shields.io/badge/LLMsPA-v1.O-darkcyan)
![](https://black.readthedocs.io/en/stable/_static/license.svg)


By Haocong Rao, Cyril Leung, and Chunyan Miao. In EMNLP 2023 (Findings).
 

## Introduction
This is a simplified implementation of automated testing codes for “[**Can ChatGPT Assess Human Personalities? A General Evaluation Framework**](https://arxiv.org/abs/2303.01248)”. The codes are used to produce **one independent testing** result of personality assessment. Users may customize the codes to execute multiple testings to reproduce the complete result in the [**paper**](https://arxiv.org/pdf/2303.01248v3.pdf).

## Environment
```bash
pip install openai, ChatGPT_lite, asyncio, requests, brotli, numpy, csv, json
```

## Usage
- The first way (Using ChatGPT_lite Library): Simply run ``Query_ChatGPT.py`` and ``Query_InstructGPT.py`` to query personalities of different subjects (**"People", "Men", "Women", "barbers", "accountants", "doctors"**) with ChatGPT or InstructGPT. The program will automatically save the answers of ChatGPT and InstructGPT into ``.csv`` files. We provide two example saved files in ``/ChatGPT`` and ``/InstructGPT``.

- The second way (Using OpenAI API): Run ``Query_GPT.py`` as below to query personalities of different subjects with **GPT4 ("gpt-4")**, **ChatGPT ("gpt-3.5-turbo")** or **InstructGPT ("text-davinci-003")**. The program will automatically save the answers of GPT4, ChatGPT or InstructGPT into ``.csv`` files. We provide two example saved files in ``/GPT4``, ``/ChatGPT``and ``/InstructGPT``. Note that GPT-4 is currently only accessible to those who have been granted access. Users can apply for the GPT-4 API [**here**](https://openai.com/waitlist/gpt-4). The API key can be viewed [**here**](https://platform.openai.com/account/api-keys).

```bash
python Query_GPT.py --model ChatGPT --api_key [input your api key]

# Default options: --model GPT4 
# --model [GPT4, ChatGPT, InstructGPT]
```


- After assessing/saving the MBTI answers of different subjects, simply run ``Crawler_16personalities.py`` to automatically submit the saved answers to the MBTI testing website [16personalities](https://www.16personalities.com/), and return the results of personality scores, types, and roles.

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
- In ``Query_InstructGPT.py`` (Line 119) and ``Query_GPT.py`` (Line 139), the model can be changed to different [GPT-3/3.5 series](https://platform.openai.com/docs/models/overview) such as "text-davinci-003", "text-davinci-002", "text-davinci-001", "text-curie-001", etc. Different versions of ChatGPT and GPT-4 can also be loaded in ``Query_GPT.py`` (Line 130 and Line 122).


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

## Update
- **Update on [2 March 2023]**: Currently ChatGPT API is available, and users can load its official model "gpt-3.5-turbo" or "gpt-3.5-turbo-0301" in ``Query_InstructGPT.py`` to perform a more stable testing with ChatGPT.

- **Update on [16 April 2023]**: Currently [ChatGPT_lite](https://github.com/acheong08/ChatGPT-lite) library may not work, so we add the file ``Query_GPT.py`` to use the official OpenAI API for testing **GPT4 ("gpt-4")**, **ChatGPT ("gpt-3.5-turbo")**, and **InstructGPT ("text-davinci-003")**. Note that GPT-4 is currently only accessible to those who have been granted access. Users can apply for the GPT-4 API [**here**](https://openai.com/waitlist/gpt-4). The API key can be viewed [**here**](https://platform.openai.com/account/api-keys).

- **Update on [9 July 2023]**: We develop a desktop application ([**LLMs-PA-V1.0.exe**](https://drive.google.com/file/d/1gqa11B70pX4d2rATizy9s-O0VKrRRcfp/view?usp=sharing)) with a friendly UI to visualize the human personality assessment via LLMs. Users can easily utilize this UI to test GPT models (**InstructGPT, ChatGPT, GPT-4**) on different subjects (**60 professions and 5 general people groups**) with different questions. The source codes will be released soon. The overview of the current repository can be presented as follows:

![image](https://github.com/Kali-Hac/ChatGPT-MBTI/blob/main/img/overview.png)

## [LLMs-PA](https://drive.google.com/file/d/1gqa11B70pX4d2rATizy9s-O0VKrRRcfp/view?usp=sharing) UI Usage
### 1. Menu overview (API Key Required)
![image](https://github.com/Kali-Hac/ChatGPT-MBTI/blob/main/img/demo_menu.png)

### 2. Query different subjects (65 Subjects)
![image](https://github.com/Kali-Hac/ChatGPT-MBTI/blob/main/img/demo_subject.png)

### 3. Make a single-question query
![image](https://github.com/Kali-Hac/ChatGPT-MBTI/blob/main/img/demo_single_ques.png)

### 4. Query all questions
![image](https://github.com/Kali-Hac/ChatGPT-MBTI/blob/main/img/demo_query.png)

### 5. Obtain personality results
![image](https://github.com/Kali-Hac/ChatGPT-MBTI/blob/main/img/demo_result.png)

For more details on these functions, please refer to the framework in our paper.

## Citation
If you found this repository useful, please consider citing:
```bash
@article{rao2023can,
  title={Can {ChatGPT} Assess Human Personalities? A General Evaluation Framework},
  author={Rao, Haocong and Leung, Cyril and Miao, Chunyan},
  journal={arXiv preprint arXiv:2303.01248},
  year={2023}
}
```

## License

ChatGPT-MBTI is released under the MIT License. 
