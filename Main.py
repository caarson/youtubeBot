"""
author : Carson Rhodes

modifier:--- #your name here 

Description:
This program will comment on a youtube video
"""

# imports
import random
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class VideoLoader:
    # search results
    def __init__(self):
        self.error = "[!] There was a critical error that broke the program!"
        self.url = "https://www.youtube.com/results?search_query=rapchat&sp=CAISBAgFEAE%253D" #insert a different search url for a query
        #self.url = input("input a video search: ")
        self.browser = webdriver.Chrome(executable_path = '/Users/carsonrhodes/Desktop/Chrome Driver/chromedriver')  # comment out to remove browser if isolating a method
    def video_url_getter(self):
        self.browser.get(self.url)
        for number in videos():
            xpath = "//ytd-video-renderer[" + number + "]//div[1]//div[1]//div[1]//div[1]//h3[1]//a[1]'"
            self.browser.find_element_by_xpath(xpath)





class Commenter:
# declares variables for commentor script
    def __init__(self):
        self.error = "[!] There was a critical error that broke the program!"
        self.browser = webdriver.Chrome(executable_path = '/Users/carsonrhodes/Desktop/Chrome Driver/chromedriver') #comment out to remove browser if isolating a method
        self.comment_box = " "
        self.comment = " "

# logs user into browser so that they may comment on a video.
    def login(self):

        # URL for google login



        url = "https://accounts.google.com/servicelogin"

        try:
            print("Passing URL to Browser...")
            self.browser.get(url)
            print(" ")
            time.sleep(4)
            print("What is your Google email?")
            email = "imitremc@gmail.com"
            #email = raw_input("") #uncomment to ask for user input
            print("What is your Google password?")
            password = "K!E87LM$"
            #password = raw_input("") #uncomment to ask for user input
            print("Passing infomation to Browser...")
            time.sleep(.5)
            email_input_box = self.browser.find_element_by_id("identifierId")
            time.sleep(.5)
            email_input_box.send_keys(email, Keys.ENTER)
            time.sleep(7.5)
            password_input_box = self.browser.find_element_by_class_name("whsOnd")
            time.sleep(.5)
            password_input_box.send_keys(password, Keys.ENTER)
            time.sleep(3)

        except Exception as exception:
            print(self.error)
            print("there was an exception when passing information to browser: ")
            print(exception)

# fetches input URL from user
    def fetch_input(self):
        print("- ")
        print("What video do you want to comment on?")
        print("- ")
        #self.url = raw_input("Enter URL: ") #sample url : https://www.youtube.com/watch?v=uRVusUSNd2E
        self.url = "https://www.youtube.com/watch?v=uRVusUSNd2E"

# finds comment box so that the script can comment.
    def find_comment_box(self):
        print("Passing URL to Browser...")
        self.browser.get(self.url)
        bg = self.browser.find_element_by_css_selector('body')
        for _ in range(2):
            bg.send_keys(Keys.PAGE_DOWN)
            time.sleep(.5)
        print("Fetching comment box...")
        time.sleep(5)
        try:
            #self.comment_box = self.browser.find_element_by_id('contenteditable-root')
            self.comment_box = self.browser.find_element_by_xpath('//*[@id="placeholder-area"]')
            self.comment_box.click()
            time.sleep(1.5)
            self.comment_box = self.browser.find_element_by_xpath('//*[@id="contenteditable-root"]')

        except Exception as internalerror:
            print("failed to find comment box: ")
            print(internalerror)
            print(self.error)

# generates a comment from CSV file.
    def generate_comment(self):
         comments = []
         print("Generating a comment...")
         try:
            with open('Comments for Bot .csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter='\n')
                for row in csv_reader:
                    comments.append(row)
            self.comment = random.choice(comments)
            self.comment = str(self.comment)
            print("selected comment: " + self.comment)
         except Exception as internalerror:
            print("failed to successfully generate a comment:")
            print(internalerror)
            print(self.error)

# enters comment into comment box on YouTube
    def enter_comment(self):
        try:
            self.comment_box.send_keys(self.comment)
        except Exception as internalerror:
            print("failed to successfully enter a comment:")
            print(internalerror)
            print(self.error)

#Commenter = Commenter() #creates class (cannot call methods without calling class)
VideoLoader = VideoLoader()
VideoLoader.video_url_getter()

# code starts here:
#Commenter.login()
#Commenter.fetch_input()
#Commenter.find_comment_box()
#Commenter.generate_comment()
#Commenter.enter_comment()

