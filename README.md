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

## FAQ
Q: What is the GPT version? 3.5 or 4 or something?
A: It's ChatGPT 3.5. I haven't found any free GPT4 app online to hack :)

Q: When will it collapse / run out of money for token?
A: I don't know. Maybe someday, so use it with responsibility and don't abuse it

Q: Do you own the site that host the free ChatGPT web interface?
A: __NO__. This module and I have nothing associated with the original web interface/app in the link I provided above.

Q: How do you find this?
A: Long story. I tried every single app on Google Play that claim to offer free ChatGPT, and found this one have the most stable interface. Before this, I use Fiddler to get token from Evolly free ChatGPT, but that app stucks now (It has has SSL certificate pin using Firebase.). If you can hack it, you will get a Firebase database contain real OpenAI key(s). So might worth trying for you, but I'm just too lazy since I already got this :)
