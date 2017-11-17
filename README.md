# Introducing Conver
Conver is an open source personal/home assistant project built entirely in [Python](https://github.com/python/cpython). It uses [Google Speech To Text](https://pypi.python.org/pypi/SpeechRecognition) along with [Google's Text To Speech](https://pypi.python.org/pypi/gTTS) functionality to put together this work in progress productivity tool. Conver is extremly useful and has a variety of cool things it can do which you can find here, in the [Features](https://github.com/Codiscite/Conver/blob/master/README.md#features) section.

## Features
Built by [Spike Corronell](https://github.com/SpikeTheKing), Conver is a great tool for productivity or just taking a second to let things sink in. Here are some of the functionality this project witholds:
- Giving Weather Information - [Weather Underground](https://www.wunderground.com/)
- Reading Stock Prices and Change - [Yahoo Finance](https://finance.yahoo.com/)
- Remembering User Favorites
- Playing Songs and YouTube Videos - [Pyglet Media Player](https://bitbucket.org/pyglet/pyglet/wiki/Home)
- Search Google
- Define Words and their Part of Speech - [NLTK Language Processing](http://www.nltk.org/)
- Set a Timer
- Download YouTube Videos - [YouTube DL](http://rg3.github.io/youtube-dl/)
- Translating Between Almost any Language - [Google Translate](https://translate.google.com/)
- Calculating
- Simple Interface for Users to Create their own Commands - [Tkinter](https://wiki.python.org/moin/TkInter)
- Note Taking
- Setting Name Conver Calls You
- Searching and Summarizing Wikipedia - [Wikipedia Python Module](https://pypi.python.org/pypi/wikipedia)

And their is much more to come! Here are just a few of the features, we plan to add:
- [ ] Backing Up Files
- [ ] (Work In Progress) Hand-free Recipe Reading - [AllRecipes](http://allrecipes.com/)
- [ ] Hand-free Calling
- [ ] (Work In Progress) Voice Emailing- [SMTP Servers](http://computer.howstuffworks.com/e-mail-messaging/email3.htm)

## Setup
To setup Conver:
  1. Install the Latest Version of [Python](https://www.python.org/)
  2. Download the [Files for Conver](https://github.com/Codiscite/Conver)
  3. Run [setup.py](https://github.com/Codiscite/Conver/blob/master/setup.py)

Steps may be a bit different depending on your operating system but hopefully everything should work the same way. If their are any issues, be sure to contact me via my [email](mailto:spiketheking2@gmail.com).

## Voice Texting
Voice Texting is the newest feature of Conver. It adds the ability to message a contact hands-free and even when your phone isn't close by! It uses the awesome functionality of [Pushbullet](https://www.pushbullet.com/), a service built by a team of superheroes in San Francisco that allows SMS messaging and text management from a computer!

Setting up Voice Texting:
  1. Create a [Pushbullet](https://www.pushbullet.com/) Account.
  2. [Download and Setup Pushbullet](https://play.google.com/store/apps/details?id=com.pushbullet.android) on Your Phone!
  3. Change the Text After "|pushbullet_API_Key|=" in [ConverData.txt](https://github.com/Codiscite/Conver/blob/master/ConverData.txt) to be your [Pushbullet API Key](https://www.pushbullet.com/#settings/account) (Scroll down to 'Access Tokens').

And there you are. Voice Texting is super simple to setup and works like a charm! Try it out by saying something like: "text (contact) Hey Bro!" or "conver, text (contact) I'm on my way home."

Currently Voice Texting is only compatible with contacts in the [Contacts.csv](https://github.com/Codiscite/Conver/blob/master/Contacts.csv) file but can be easily added in the format of: "{contact name}, {conact number}".

## About
We hope Conver will be liked and be sure to fork us if you want to help support the development of Conver!

Cheers! :smiley:

[Discord Server](https://discord.gg/9Cp3s9X) -
[Code of Conduct](https://github.com/Codiscite/Conver/blob/master/CODE_OF_CONDUCT.md) - 
[Licence](https://github.com/Codiscite/Conver/blob/master/LICENSE)

Copyright © 2017 Spike Corronell
