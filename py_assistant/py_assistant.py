import speech_recognition as sr     # For recognition the voice input of user
import sys                          # Getting system support
import pyttsx3                      # Text to speech
import datetime                     # Greeting user according to time
import wikipedia, wikipediaapi      # Getting Wikipedia support
import os   
# import smtplib
import webbrowser                   # For web searching
import pyhibp                       # To knowing that password is pawned or not           
from pyhibp import pwnedpasswords as pw
import pyjokes                      # Programming jokes
from translate import Translator    # Translating the English language into another language
import getpass                      # Hiding user password to checking pawned status
import bs4                          # For web support
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen  # URL support
import GoogleNews                   # Getting news from Google News 
import time                         # Greeting the user 


print("This project is made by \"Laxmi Narayan Vaishnav\". \nYou can use this project to understand how it works and how to implement such things. \nViolation of code might a tremendous way to express yourself (Be Careful with it). Thanks")
print("Hey! Welcome to the LN's World!")
user_restrictions = "NOTE:- You are restrict with these features only: Email/Password Pawned \n\t\t\t\t\t\t  Fun Facts \n\t\t\t\t\t\t  English to other Language Translation \n\t\t\t\t\t\t  Google News \n\t\t\t\t\t\t  Web Data Access \n\t\t\t\t\t\t  Wikipedia"
print(user_restrictions)
input("\nPress ENTER to continue....")

# User Voice Command Input

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

rate = engine.getProperty('rate')
engine.setProperty('rate', 160)


           
volume = engine.getProperty('volume')
engine.setProperty('volume',1.0)

           
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.say("This is male voice. If you like, hit '1'")
engine.runAndWait()
engine.setProperty('voice', voices[1].id)
engine.say("This is female voice. If you like, hit '2'")
engine.runAndWait()

user_in = int(input("So, which voice you want to be continue? \n 1:Male, 2:Female "))
engine.setProperty('voice', voices[user_in - 1].id)                 # It'll let you use the voice which you like.
engine.say("Finally. I appreciate your choice. Let's dig in")
engine.runAndWait()

# Voice Recognizing

r = sr.Recognizer()
user_name_ask = "Hey there! What's your name: "
print(user_name_ask)
engine.say(user_name_ask)
engine.runAndWait()
with sr.Microphone() as source:
    getting_user_name = r.listen(source, timeout = 5)

getting_user_name_storing = r.recognize_google(getting_user_name)
print("Welcome ", end="")
engine.say(getting_user_name_storing)
engine.runAndWait()
print(f"{getting_user_name_storing.upper()}. Let me know, what you're looking for?")

# User name input issue
# If pronunciation of your name is wrong then you can manually input your name
getting_user_name_error = "Sorry, if I got your name wrong! \nYou can manually input your name  \nPlease say, \"Change\" to change your name...\nIf I pronounced right then simply say, \"No\" and wait..."
print(getting_user_name_error)
engine.say(getting_user_name_error)
engine.runAndWait()
getting_user_name_re = sr.Recognizer()
with sr.Microphone() as source:
    getting_user_name_re_2 = r.listen(source, timeout = 5)
    
getting_user_name_re_3 = r.recognize_google(getting_user_name_re_2)
if getting_user_name_re_3 == "Change" or getting_user_name_re_3 ==  "change":
    getting_user_name_storing = str(input("Enter Your Name: "))
elif getting_user_name_re_3 == "no" or "No":
    engine.say("Be continued...")
    engine.runAndWait()
else:
    engine.say("Be continued...")
    engine.runAndWait()

# Wishing user

def user_wishing():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        engine.say(f"Good Morning {getting_user_name_storing}!")
        engine.runAndWait()

    elif hour>=12 and hour<18:
        engine.say(f"Good Afternoon {getting_user_name_storing}!")
        engine.runAndWait()

    else:
        engine.say(f"Good Evening {getting_user_name_storing}!")
        engine.runAndWait()

# Taking user actions (voice)

print(f"Please check again: \n{user_restrictions}")
print("Say your query according to above actions...")
print("NOTE: After completion of one content, you'll redirect to give another voice input")
input("Hit ENTER...")
def user_action():
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        user_action_X = r.listen(source, timeout = 5)   # It will terminate the session in 5 seconds. If you failed to give your voice input then you've to give voice input again.

    try:
        user_action_on = f"I'm on action {getting_user_name_storing} "
        print(user_action_on)
        engine.say(user_action_on)
        engine.runAndWait()
        user_action_on_fire = r.recognize_google(user_action_X, language='en-US')
        user_action_on_fire_said = f"{getting_user_name_storing} said: {user_action_on_fire}"
        engine.say(user_action_on_fire_said)
        engine.runAndWait()
    
    except Exception as oops:
        print("Sorry, say that again...")
        return "None"
    return user_action_on_fire


if __name__ == "__main__":
    user_wishing()
    while True:

        user_action_on_fire = user_action().lower()     # It will take data in lower case
        print(f"{getting_user_name_storing} said, '{user_action_on_fire}'")
            # Checking user's Password/E-mail pawned or not

        if user_action_on_fire == 'email' or user_action_on_fire == 'password' or user_action_on_fire == 'pawned':
            pyhibp.set_user_agent(ua="None")
            def pswd_email_pwned_check():
                pswd_email_pwned_check_str1 = "You won't be able to see your password because of security reasons, but in background, it will be written"
                print(pswd_email_pwned_check_str1)
                engine.say(pswd_email_pwned_check_str1)
                engine.runAndWait()
                pswd_email_pwned_check_str2 = "Enter your password: "
                print(pswd_email_pwned_check_str2, end="")
                engine.say(pswd_email_pwned_check_str2)
                engine.runAndWait()
                user_pswd = getpass.getpass(stream = sys.stderr)
                resp = pw.is_password_breached(password=f"{user_pswd}")
                if resp:
                    user_pswd_breached = "Password breached!"
                    user_pswd_breached_time = f"This password was used {resp} times before."
                    print(f"{user_pswd_breached} \n{user_pswd_breached_time}")
                    engine.say(user_pswd_breached)
                    engine.say(user_pswd_breached_time)
                    engine.runAndWait()
                else:
                    user_pswd_breached_x = "Your password is not breached yet!!! \nBut keep your password strong"
                    print(user_pswd_breached_x)
                    engine.say(user_pswd_breached_x)
                    engine.runAndWait()
                user_email_pwned = "Check if your email is pwned or not? \nIf you wanna check, say, 'Check it'..."
                print(user_email_pwned)
                engine.say(user_email_pwned)
                engine.runAndWait()
                user_email_res_wait = "I'm waiting for your response..."
                engine.say(user_email_res_wait)
                engine.runAndWait()
                with sr.Microphone() as source:
                    user_email_rec = r.listen(source)
                user_email_query = r.recognize_google(user_email_rec, language='en-US')
                if 'check' or 'email' or 'mail' or 'it' in user_email_query:
                    engine.say("Here you go")
                    engine.runAndWait()
                    webbrowser.open('https://haveibeenpwned.com/')      # It will proceed you to the official website of email pawned checking
            pswd_email_pwned_check()
            time.sleep(5)

            # This function will help you to recheck your password pawned status
            user_email_query_cont = "If you wanna check more password breach data, say, 'More' or 'Again'"
            engine.say(user_email_query_cont)
            engine.runAndWait()
            with sr.Microphone() as source:
                user_email_rec = r.listen(source)
            user_email_query = r.recognize_google(user_email_rec, language='en-US')
            user_email_query = user_email_query.lower()
            if 'more' or 'again' in user_email_query:
                while True:
                    pswd_email_pwned_check()
                    engine.say(user_email_query_cont)
                    engine.runAndWait()
                    with sr.Microphone() as source:
                        user_email_rec = r.listen(source)
                    user_email_query = r.recognize_google(user_email_rec, language='en-US')
                    user_email_query = user_email_query.lower()
                    if  'more' or 'again' not in user_email_query:
                        break

            #return user_action_on_fire

            # Giving funny jokes to user

        elif user_action_on_fire == 'joke' or user_action_on_fire == 'jokes' or user_action_on_fire == 'fun' or user_action_on_fire == 'funny':
            user_jokes = "Don't you love jokes? Then for whom you're waiting! Set a range in number..."     # You have to give a range for jokes
            print(user_jokes)
            engine.say(user_jokes)
            engine.runAndWait()
            with sr.Microphone() as source:
                user_jokes_rec = r.listen(source)
            user_jokes_X = r.recognize_google(user_jokes_rec, language='en-US')
            user_jokes_X = int(user_jokes_X)
            for x in range(user_jokes_X):
                user_jo = pyjokes.get_joke()
                print(user_jo)
                engine.say(user_jo)
                engine.runAndWait()
        
          ##  return user_action_on_fire

            # Language Translation

        elif user_action_on_fire == 'translation' or user_action_on_fire == 'translator' or user_action_on_fire == 'translate':

            user_translation_lang_code = "Please check the language code here if you ain't aware about it: "
            user_translation_lang_code_url = "https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes"
            print(user_translation_lang_code,end="")
            print(user_translation_lang_code_url)
            engine.say(user_translation_lang_code)
            engine.runAndWait()
            user_translation_lang_code_url_X = f"To open this URL, say 'Take me to the Link or URL or Address or Open it'"
            print(user_translation_lang_code_url_X)
            engine.say(user_translation_lang_code_url_X)
            engine.say("I'm waiting for your response...")
            engine.runAndWait()
            with sr.Microphone() as source:
                user_translation_rec = r.listen(source)
            user_translation_query = r.recognize_google(user_translation_rec, language='en-US')
            user_translation_query = user_translation_query.lower()
            if 'take' or 'link' or 'url' or 'address'  or 'open' or 'it' in user_translation_query:
                engine.say("Here you go")
                engine.runAndWait()
                webbrowser.open(user_translation_lang_code_url)
            else:
                engine.say("Be continued...")
                engine.runAndWait()
            
            user_translation_text = "Enter the text you want to translate: " 
            print(user_translation_text, end="")
            engine.say(user_translation_text)
            engine.runAndWait()
            user_translation_text_X = str(input(""))
            engine.say(user_translation_text_X)
            engine.runAndWait()
            user_language_code = f"Sorry {getting_user_name_storing} but you have to manually input the language code: "
            print(f"{user_language_code} ", end="")
            engine.say(user_language_code)
            engine.runAndWait()
            user_language_code_in = str(input())
            user_language_code_dec = "NOTE: If language code is appropriate then you'll get the result!"
            print(user_language_code_dec)
            engine.say(user_language_code_dec)
            engine.runAndWait()
            translator = Translator(to_lang=user_language_code_in)
            user_translated_data = translator.translate(user_translation_text_X)
            engine.say("Here you go...")
            engine.runAndWait()
            print(f"The translated data in language code '{user_language_code_in}': ", end="")
            print(user_translated_data)
        
            # return user_action_on_fire

            # Google News

        elif user_action_on_fire == 'news' or user_action_on_fire == 'google' or user_action_on_fire == 'breaking':
            user_wish_news = "Say, 'RSS' to check Top News or say, 'Search a News' to search your choice"
            print(user_wish_news)
            engine.say(user_wish_news)
            engine.runAndWait()
            with sr.Microphone() as source:
                user_news_rec = r.listen(source)
            user_news_query = r.recognize_google(user_news_rec, language='en-US')
            user_news_query = user_news_query.lower()
            if 'search' or 'me' in user_news_query:
                user_wish_news_enter = "What you wanna search? "
                print(user_wish_news_enter)
                engine.say(user_wish_news_enter)
                engine.runAndWait()
                with sr.Microphone() as source:
                    user_wish_news_enter_rec = r.listen(source)
                user_wish_news_enter_query = r.recognize_google(user_wish_news_enter_rec, language='en-US')
                webbrowser.open(f'https://news.google.com/search?q={user_wish_news_enter_query}')

            elif 'rss' or 'top' in user_news_query:
                engine.say("Here you go...")
                engine.runAndWait()
                news_url= "https://news.google.com/news/rss"
                Client=urlopen(news_url)
                xml_page=Client.read()
                Client.close()

                soup_page=soup(xml_page,"xml")
                news_list=soup_page.findAll("item")
                # Print news title, url and publish date
                for news in news_list:
                    print(news.title.text)
                    print(news.link.text)
                    print(news.pubDate.text)
                    print("-"*60)
        
            #return user_action_on_fire

            # Web Access

        elif user_action_on_fire == 'web' or user_action_on_fire == 'website':
            user_web_input = "What you wanna search? "
            print(user_web_input)
            engine.say(user_web_input)
            engine.runAndWait()
            with sr.Microphone() as source:
                user_web_rec = r.listen(source)
            user_web_query = r.recognize_google(user_web_rec, language='en-US')
            engine.say(f"I'm searching {user_web_query}")
            engine.runAndWait()
            webbrowser.open(f"https://www.google.com/search?q={user_web_query}")
        
            #return user_action_on_fire

            # Wikipedia

        elif user_action_on_fire == 'wiki' or user_action_on_fire == 'wikipedia':
            # # 1. ****** Getting User Input ******

            user_wikipedia_query = "What you wanna search: "
            print(user_wikipedia_query)
            engine.say(user_wikipedia_query)
            engine.runAndWait()

            with sr.Microphone() as source:
                user_wikipedia_rec = r.listen(source)
            user_input_wikipedia = r.recognize_google(user_wikipedia_rec, language='en-US')
            wiki = wikipediaapi.Wikipedia(language="en")
            engine.say(f"I'm on your mark for {user_input_wikipedia}...")
            engine.runAndWait()

            # # 2. ****** Checking page's existence *******
            page_py = wiki.page(f"{user_input_wikipedia}")
            user_input_wikipedia_exist = page_py.exists()

            #  # 3. ****** Detailed data *******

            user_input_wikipedia_exist_res = "Let's check if your query exist on Wikipedia database or not"
            print(user_input_wikipedia_exist_res)
            engine.say(user_input_wikipedia_exist_res)
            engine.runAndWait()
            if user_input_wikipedia_exist is True:
                user_input_wikipedia_exist_T = f"Congratulations, your query {user_input_wikipedia} exists on Wikipedia database"
                print(user_input_wikipedia_exist_T)
                engine.say(user_input_wikipedia_exist_T)
                engine.runAndWait()
                engine.say("Let's explore the Wikipedia world more... \nWait for a few seconds...")
                engine.runAndWait()
                time.sleep(3)
                engine.say("Hey! I'm, sorry but you manually checkout your choice here...")
                engine.runAndWait()
                user_selection_wikipage = int(input(f"Choose, what you want to know about {user_input_wikipedia} \n1. Category 2. Contents 3. Coordinates 4. Link 5. Original Title 6. Parent ID \n7. References 8. Revision ID 9. Sections 10. Summary 11. Title 12. URL \nEnter your response: "))
                if user_selection_wikipage == 1:
                    user_selection_wikipage_list = wikipedia.page(user_input_wikipedia).categories
                    print(user_selection_wikipage_list)
                    engine.say("Now manually input '1' to know more about categories of current state...")
                    engine.runAndWait()
                    user_input_wikipedia_categories = int(input("Enter '1' if you wanna know more... "))
                    if user_input_wikipedia_categories == 1:
                        user_input_wikipedia_categories_summary = int(input("Enter the no from the list to know more. \nNote:- starts from '0' : "))
                        print("\n")
                        print(user_selection_wikipage_list[user_input_wikipedia_categories_summary])
                        print(wikipedia.summary(user_selection_wikipage_list[user_input_wikipedia_categories_summary]))
                elif user_selection_wikipage == 2:
                    print(wikipedia.page(user_input_wikipedia).content)
                elif user_selection_wikipage == 3:
                    print(wikipedia.page(user_input_wikipedia).coordinates)
                elif user_selection_wikipage == 4:
                    print(wikipedia.page(user_input_wikipedia).links)
                elif user_selection_wikipage == 5:
                    print(wikipedia.page(user_input_wikipedia).original_title)
                elif user_selection_wikipage == 6:
                    print(wikipedia.page(user_input_wikipedia).parent_id)
                elif user_selection_wikipage == 7:
                    print(wikipedia.page(user_input_wikipedia).references)
                elif user_selection_wikipage == 8:
                    print(wikipedia.page(user_input_wikipedia).revision_id)
                elif user_selection_wikipage == 9:
                    print(wikipedia.page(user_input_wikipedia).sections)
                elif user_selection_wikipage == 10:
                    user_input_wikipedia_sum_X = wikipedia.page(user_input_wikipedia).summary
                    print(user_input_wikipedia_sum_X)
                    engine.say(f"Here you go for the summary of {user_input_wikipedia}...\n {user_input_wikipedia_sum_X}")
                    engine.runAndWait()
                elif user_selection_wikipage == 11:
                    user_input_wikipedia_sum_X = wikipedia.page(user_input_wikipedia).title
                    print(f"The official title of {user_input_wikipedia} according to Wikipedia database is {user_input_wikipedia_sum_X}")
                    engine.say(user_input_wikipedia_sum_X)
                    engine.runAndWait()
                elif user_selection_wikipage == 12:
                    print(wikipedia.page(user_input_wikipedia).url)
            else:
                user_input_wikipedia_exist_F = f"Sorry!!! The request page {user_input_wikipedia} doesn't exist on Wikipedia.org"
                print(user_input_wikipedia_exist_F)
                engine.say(user_input_wikipedia_exist_F)
                engine.say("You can retry it... \nI'm waiting for your response...")
                engine.runAndWait()
                #exit(0)
            # # 4. ******* To know Category of the page *********

            user_input_wikipedia_continuity = f"Enter '1' if you wanna continue to know much about the category of {user_input_wikipedia}, else '0' to exit from the process..."
            print(user_input_wikipedia_continuity)
            engine.say(user_input_wikipedia_continuity)
            engine.runAndWait()
            if user_input_wikipedia_continuity == 1:
                input("Press 'ENTER' for step 4th...")
                user_input_wikipedia_link = wikipedia.page(user_input_wikipedia).url
                page_py_wiki = wiki.page(user_input_wikipedia_link)
                def print_categories(page):
                        categories = page.categories
                        for title in sorted(categories.keys()):
                            print("%s: %s" % (title, categories[title]))

                print("Categories")
                print_categories(page_py)
            else:
                user_input_wikipedia_link_X = "Thanks for using Wikipedia service..."
                print(user_input_wikipedia_link_X)
                engine.say(user_input_wikipedia_link_X)
                engine.runAndWait()
                #exit(0)

            # # 5. ******* To know Category members *********

            engine.say("Again, you've to manually input. Sorry for inconvenience")
            engine.runAndWait()
            user_input_wikipedia_categories_search = int(input("Enter '1' if you wanna search other categories data, else '0' to exit "))
            if user_input_wikipedia_categories_search == 1:
                input("Press 'ENTER' for step 5th...")
                user_input_wikipedia_categories_search_X = "You can search a category data from here. \nPronounce a category"
                print(user_input_wikipedia_categories_search_X)
                engine.say(user_input_wikipedia_categories_search_X)
                engine.runAndWait()
                with sr.Microphone() as source:
                    user_wikipedia_rec = r.listen(source)
                user_wikipedia_category = r.recognize_google(user_wikipedia_rec, language='en-US')
                engine.say(f"I'm searching {user_wikipedia_category}")
                engine.runAndWait()
                def print_categorymembers(categorymembers, level=0, max_level=1):
                        for c in categorymembers.values():
                            print("%s: %s (ns: %d)" % ("*" * (level + 1), c.title, c.ns))
                            if c.ns == wikipediaapi.Namespace.CATEGORY and level < max_level:
                                print_categorymembers(c.categorymembers, level=level + 1, max_level=max_level)

                cat = wiki.page(f"Category:{user_wikipedia_category}")
                print(f"Category members: Category:{user_wikipedia_category}")
                print_categorymembers(cat.categorymembers)

            else:
                user_input_wikipedia_link_X = "Thanks for using Wikipedia service..."
                print(user_input_wikipedia_link_X)
                engine.say(user_input_wikipedia_link_X)
                engine.runAndWait()
                #exit(0)

            # # 6. ******* To print other same type links *******

            engine.say("Again, you've to manually input. Sorry for inconvenience")
            engine.runAndWait()
            user_input_wikipedia_link_generate = int(input(f"Enter '1' to fetch similar links related to {user_input_wikipedia} : {user_input_wikipedia_link}, else '0' to exit..."))
            if user_input_wikipedia_link_generate == 1:
                def print_links(page):
                        links = page.links
                        for title in sorted(links.keys()):
                            print("%s: %s" % (title, links[title]))

                print_links(page_py)

            else:
                user_input_wikipedia_link_X = "Thanks for using Wikipedia service..."
                print(user_input_wikipedia_link_X)
                engine.say(user_input_wikipedia_link_X)
                engine.runAndWait()
                #exit(0)

            #  # 7. ******** Getting page in different languages *******

            engine.say("Again, you've to manually input. Sorry for inconvenience")
            engine.runAndWait()
            user_input_wikipedia_diff_lang_links = int(input(f"Enter '1' to fetch links of {user_input_wikipedia} in different languages, else '0' to exit..."))
            if user_input_wikipedia_diff_lang_links == 1:
                def print_langlinks(page):
                        langlinks = page.langlinks
                        for k in sorted(langlinks.keys()):
                            v = langlinks[k]
                            print("%s: %s - %s: %s" % (k, v.language, v.title, v.fullurl))

                print_langlinks(page_py)

                page_py_cs = page_py.langlinks['cs']
                print("Page - Summary: %s" % page_py_cs.summary[0:60])
            else:
                user_input_wikipedia_link_X = "Thanks for using Wikipedia service..."
                print(user_input_wikipedia_link_X)
                engine.say(user_input_wikipedia_link_X)
                engine.runAndWait()
                #exit(0)
                
            #return user_action_on_fire

