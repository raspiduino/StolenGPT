# StolenGPT
Free ChatGPT API from a random app (but it doesn't set quota on your message), wrapped in Python

## Summary
- There is a free ChatGPT web interface at [`https://chat.mindtastik.com/test3/`](https://chat.mindtastik.com/test3/), which (at least for now) offer free ChatGPT chat without any quota or ads
- This module wraps its API

## Dependencies
- [`requests`](https://pypi.org/project/requests/)
- `time` (build-in Python)

## Usage
```python
>>> from StolenGPT import StolenGPT
>>> a = StolenGPT()
>>> a.chat("hi")
'Hello! How can I assist you today?'
>>> a.chat("who are you?")
'I am ChatGPT, a large language model developed by OpenAI. I am designed to understand and respond to natural language queries and conversations. I can assist you with a wide range of tasks, from answering questions to providing information on various topics.'
>>> a.chat("list number from 1 to 20")
'Sure, here are the numbers from 1 to 20:\\n\\n1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20.'
>>> a.chat("now do the same for 20 to 30")
'Certainly! Here are the numbers from 20 to 30:\\n\\n20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30.'
```
There are also some useful methods in the class. You can open the source code, there will be comments about its usage. I'm just to lazy to put them here :)

Enjoy!
