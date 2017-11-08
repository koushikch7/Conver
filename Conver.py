#!/usr/bin/env python3
import speech_recognition as sr;
import wikipedia, os, requests, re, pyglet.media, sys, webbrowser, datetime, threading, time, urllib.parse, urllib.request;
from google import search;
from bs4 import BeautifulSoup;
from pushbullet import Pushbullet;
from nltk.corpus import wordnet;
from pyglet.gl import *;
from gtts import gTTS;

data_txt_file = "ConverData.txt";
commands_file = "Commands.txt";
notes_file = "Notes.csv";
contacts_file = "Contacts.csv";

today = datetime.datetime.now().strftime("%m/%d/%y %I:%M%p");

def text(reciever, message):
    device = pb.devices[0];
    push = pb.push_sms(device, reciever, message);

def getStocks(stockSymbol):
    url = "https://finance.yahoo.com/quote/" + stockSymbol;
    searchSite = requests.get(url).text;
    searchSoup = BeautifulSoup(searchSite, 'html.parser');
    price = searchSoup.find("span", attrs={"data-reactid": "35"});
    print(price)
    price = price.contents[1];

    change = searchSoup.find("span", attrs={"data-reactid": "37"});
    print("|" + change + "|")
    change = change.contents[1];
    change = change[:change.find(" (")];
    
    items = [];
    items.append(price);
    items.append(change);
    return items;

def searchWikipedia(searchText):
    searchResults = wikipedia.search(searchText);

    if(len(searchResults) > 0):
        try:
            summary = wikipedia.summary(searchResults[0], sentences=1);
        except Exception as e:
            return "Sorry, but you might have to be a bit more specific.";

        return "Alright " + getData("master") + ", " + summary;
    else:
        return "Sorry, but I can't find anything on Wikipedia fer that.";

def searchGoogle(searchText, links):
    iterationTimes = 0;
    websites = [];
    for url in search(searchText, tld='com.pk', lang='es', stop=1):
        if(iterationTimes <= links - 1):
            response = requests.get(url);
            soup = BeautifulSoup(response.text, 'html.parser')
            websites.append(translate(str(soup.title.string), "auto", "english"));
        iterationTimes += 1;
    return(websites);

def define(word):
    synsets = wordnet.synsets(word);

    if(len(synsets) > 0):
        synset = synsets[0];
        partOfSpeech = synset.lexname()
        partOfSpeech = partOfSpeech[:partOfSpeech.find(".")];

        return word, partOfSpeech, synset.definition();
    else:
        return "Sorry, I can't find a definition for that.";

def timer(secLength, minLength, hourLength):
    # Loop until we reach 20 minutes running

    endSecVal = int(datetime.datetime.now().strftime("%S")) + secLength;
    endMinVal = int(datetime.datetime.now().strftime("%M")) + minLength;
    endHourVal = int(datetime.datetime.now().strftime("%H")) + hourLength;

    val = 0;

    while int(datetime.datetime.now().strftime("%S")) != endSecVal:
        #Action
        val = 1;

    while int(datetime.datetime.now().strftime("%M")) != endMinVal:
        #Action
        val = 2;

    while int(datetime.datetime.now().strftime("%H")) != endHourVal:
        #Action
        val = 3;

    os.system("py playSound.py message.mp3");

def play(search):
    query_string = urllib.parse.urlencode({"search_query" : search});
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string);
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode());
    webbrowser.open("http://www.youtube.com/watch?v=" + search_results[0] + "#t=0s");

def downloadVid(search):
    query_string = urllib.parse.urlencode({"search_query" : search});
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string);
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode());
    os.system('py -m youtube_dl "https://www.youtube.com/watch?v=' + search_results[0] + '"');

def translate(text, lang1="auto", lang2="auto"):
    lang = "auto";

    langTwo = "auto";
    if(lang1.lower() == "english"):
        lang = "en";
    elif(lang1.lower() == "spanish"):
        lang = "es";
    elif(lang1.lower() == "french"):
        lang = "fr";

    if(lang2.lower() == "english"):
        langTwo = "en";
    elif(lang2.lower() == "spanish"):
        langTwo = "es";
    elif(lang2.lower() == "french"):
        langTwo = "fr";

    urllib.parse.clear_cache()
    hex_sentence = urllib.parse.quote(text)
    url = "https://translate.google.com/m?hl={1}&sl={0}&q={2}".format(lang, langTwo, hex_sentence)

    agents = {"User-Agent":"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko/20090327 Galeon/2.0.7"}
    request = urllib.request.Request(url, headers=agents)
    response = urllib.request.urlopen(request)
    data = response.read().decode("utf-8")

    translation = re.findall(r'<div dir="ltr" class="t0">(.*?)</div>', data)

    if not translation:
        translation = text
        
    return translation[0]

def calculate(equation):
    value = equation.replace("what's ", "");
    value = value.replace(" times", "*");
    value = value.replace(" x", "*");
    result = value.replace(" million", "000000");
    result = result.replace(" billion", "000000000");
    result = result.replace(" trillion", "000000000000");

    finalValue = eval(result);

    finalValue = str(finalValue).replace("000000", " million", 1);
    finalValue = finalValue.replace("000000000", " billion", 1);
    finalValue = finalValue.replace("000000000000", " trillion", 1);

    return finalValue;

def weather(city, country, request):
    r = requests.get("http://api.wunderground.com/api/d2767b3664f4110f/forecast/q/" + country + "/" + city + ".json");
    data = r.json();

    if(request == "HF_Temp"):
        return data['forecast']['simpleforecast']['forecastday'][0]['high']['fahrenheit'];
    elif(request == "LF_Temp"):
        return data['forecast']['simpleforecast']['forecastday'][0]['low']['fahrenheit'];
    if(request == "HC_Temp"):
        return data['forecast']['simpleforecast']['forecastday'][0]['high']['celcius'];
    elif(request == "LC_Temp"):
        return data['forecast']['simpleforecast']['forecastday'][0]['low']['celcius'];
    elif(request == "Conditions"):
        return data['forecast']['simpleforecast']['forecastday'][0]['conditions'];
    elif(request == "AF_Temp"):
        return str((int(data['forecast']['simpleforecast']['forecastday'][0]['high']['fahrenheit']) + int(data['forecast']['simpleforecast']['forecastday'][0]['low']['fahrenheit'])) / 2)

def getCommand(userMSG):
    openFile = open(commands_file, 'r');
    fileCommands = openFile.readlines();
    
    for line in fileCommands:
        result = line;

        if(line.find(userMSG + "=") != -1):
            result = result.replace("\n", "");

            inVal = result[:result.find("=")];
            outVal = result[result.find("=") + 1:];

            if(outVal.find("(master)") != -1):
                outVal = outVal.replace("(master)", getData("master"));
            elif(outVal.find("(exit)") != -1):
                openFile.close();
                exit();
            elif(outVal.find("(play favorite song)") != -1):
                play(getData('song'));
                outVal = " ";

            openFile.close();
            return outVal;

    return "";
            
def getData(container):
    file = open(data_txt_file, 'r');

    for line in file:
        data = line;
        if(data.find("|" + container + "|") != -1):
            data = data.replace("|" + container + "|=", "");
            data = data.replace("\n", "");
            return data;

    return ""
    file.close();

def sendData(container, data):
    file = open(data_txt_file, 'r');
    fileData = file.read();
    
    # If the item is not there:
    if(fileData.find(container) == -1):
        file.close();
        
        file = open(data_txt_file, 'a');
        file.write("|" + container + "|=" + data + "\n");
        file.close();

    # If the item is there:
    else:
        file.close()
        
        file = open(data_txt_file, 'r');
        for line in file:
            if(line.find("|" + container + "|") != -1):

                filew = open(data_txt_file, 'w');
                info = fileData;
                info = info.replace(line, "|" + container + "|=" + data);
                filew.write(info);
                filew.close();

        file.close();
        
def exit_callback(dt):
    pyglet.app.exit();

def say(message):
    tts = gTTS(text=message, lang="en", slow=False)
    tts.save("message.mp3")

    pyglet.options['audio'] = ('openal', 'directsound', 'silent')

    sound = pyglet.resource.media('message.mp3')
    sound.play()
    pyglet.clock.schedule_once(exit_callback, sound.duration)

    pyglet.app.run()

def note(action, title, info):
    if(action == "take"):
        notes = open(notes_file, "a");
        if(info != ""):
            notes.write(today + "," + title + "," + info + "\n");
            notes.close();
            return "Note Saved!";

    elif(action[:4] == "read"):
        dates = [];
        titles = [];
        noteFiles = [];

        notes = open(notes_file, "r");
        lines = notes.readlines();
        notes.close();

        for line in range(0, len(lines)):
            splitData = fileLines[line].split(",");

            dates.append(splitData[0].strip());
            titles.append(splitData[1].strip());
            noteFiles.append(splitData[2].strip());

        return dates, titles, noteFiles;

def findall(string, sub, listindex=[], offset=0):
    i = string.find(sub, offset)
    while i >= 0:
        listindex.append(i)
        i = string.find(sub, i + 1)
    return listindex

def listen(message):
    # Play Ding
    pyglet.options['audio'] = ('openal', 'directsound', 'silent')

    player = pyglet.media.Player();
    sound = pyglet.media.load('ding.wav')
    player.queue(sound);
    player.volume = 0.5;
    player.play()

    pyglet.clock.schedule_once(exit_callback, sound.duration)

    pyglet.app.run()

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(message)
        audio = r.listen(source)

    # try:
    recAudio = r.recognize_google(audio).lower().replace("convert ", "");
    # except sr.request:
    #     print("Sorry " + getData("master") + ", I'm not connected to the internet.");
    #     exit();

    print(recAudio);
    return recAudio;

def main():
    recAudio = listen("\nSay Something!");
    audioCom = getCommand(recAudio);
    print(audioCom);
    
    # Commands
    if(audioCom != ""):
        say(audioCom);
        main();

    elif(recAudio[:5] == "text "):
        recAudio = recAudio[5:];
        spaces = findall(recAudio, " ");
        contact = recAudio[:spaces[0]];
        message = recAudio[len(contact) + 1:];

        contacts = open(contacts_file, "r");
        contacts = contacts.readlines();

        number = "nothing";

        for line in range(0, len(contacts)):
            splitData = contacts[line].split(",");

            if(splitData[0].strip() == contact):
                number = splitData[1].strip();
                text(number, message);
                break

        if(number != "nothing"):
            say("Message Sent!");
        else:
            say("Sorry, but there was an error sending that message.")

        main();

    elif(recAudio[:11] == "take a note"):
        say("What would you like the title to be? ");
        title = listen("");

        say("Alright, you may now read aloud you note!");
        info = listen("");

        say(note("take", title, info));
        main();

    elif(recAudio[:11] == "stocks for "):
        results = getStocks(recAudio[11:]);
        results[1] = results[1].replace("-", "negative ")
        say("The current price is " + results[0]);
        say("and it changed by " + results[1] + " today.")
        main();

    elif(recAudio.find("call me ") != -1):
        master = recAudio.split("call me ");
        master = master[len(master) - 1];
        sendData("master", master);
        say("Alright " + str(master));
        main();
    
    elif(recAudio[:8] == "weather "):
        result = recAudio.replace("what's the ","");
        result = result.replace("in ", "");
        result = result.split("weather ");
        result = result[len(result) - 1];

        city = result[:result.find(" place")]
        country = result[(result.find("place") + 6):]
        country.replace(" ", "_");
        city.replace(" ", "_");

        say("The average temperature today in " + city + " is: " + weather(city, country, "AF_Temp") + " degrees Fahrenheit and the weather was " + weather(city, country, "Conditions"))
        main();

    elif(recAudio[:5] == "play "):
        play(recAudio.replace(recAudio[:5], ""));
        # rTwo = sr.Recognizer()

        # with sr.Microphone() as source:
        #     print("\nSay something!")
        #     audio = r.listen(source)

        # recAudioTwo = rTwo.recognize_google(audioTwo).lower().replace("convert ", "");
        # print(recAudioTwo);
        # audioComTwo = getCommand(recAudioTwo);
        # print(audioComTwo);

    elif(recAudio[:14] == "tell me about "):
        say(searchWikipedia(recAudio[14:]));
        main();

    elif(recAudio[:10] == "translate " and recAudio[:10] != "translate file "):
        newAudio = recAudio[10:];
        places = list(re.finditer(" to ", newAudio));

        if(len(places) != 0):
            language = newAudio[places[len(places) - 1].end():];

        finalAudioStr = newAudio[:len(newAudio) - (4 + len(language))];
        print(translate(finalAudioStr, "auto", language));
        say(translate(finalAudioStr, "auto", language));

        main();

    elif(recAudio[:7] == "define "):
        theWord = recAudio[7:];

        if(define(theWord) != "Sorry, I can't find a definition for that."):
            say(define(theWord)[0]);
            time.sleep(0.2);
            say(define(theWord)[1]);
            time.sleep(0.2);
            say(define(theWord)[2]);
        else:
            say(define(theWord));

        main();

    elif(recAudio[:9] == "download "):
        downloadVid(recAudio[9:]);
        say(recAudio[9:] + " finished downloading.");
        main();

    elif(recAudio[:10] == "calculate "):
        say(recAudio.replace(recAudio[:10], "") + " equals " + calculate(recAudio[10:]));
        main();

    elif(recAudio[:12] == "my favorite "):
        result = recAudio[12:];

        isPos = result.find("is") - 1;
        container = result[:isPos];
        data = result[isPos + 4:];

        sendData(container, data);
        main();

    elif(recAudio[:16] == "set a timer for "):
        newAudio = recAudio[16:];
        newAudio = newAudio.replace(" seconds", "");

        thread = threading.Thread(target=timer, args=(int(newAudio), 0, 0))
        say("Timer set for " + recAudio.replace(recAudio[:16], ""));
        main();

    else:
        say("Sorry, I don't understand.");
        main(); 

# Setup Pushbullet API Integration for Voice Texting:
pb = Pushbullet(getData("pushbullet_API_Key"));

# Make the 'master' object default to 'creator':
if(getData("master") == ""):
    sendData("master", "creator");

#Start
main();
