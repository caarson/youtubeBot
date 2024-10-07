# *confidential*confidential*confidential*confidential*confidential*confidential*confidential* #
# # - Coded by Carson Rhodes for ItsLit Records - Confidential ~ !!!NOT TO BE SOLD OR REDISTRIBUTED!!!
# # - API with the purpose of promoting a youtube channel through a complicated chain of social interactions using Python automation.
# # - Intellectual Property - Confidential - NOT TO BE SOLD OR REDISTRIBUTED
# *confidential*confidential*confidential*confidential*confidential*confidential*confidential* #
user_database = {}
import os, sys, time, random
import zipfile

# import gspread & associated methods
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# import selenium & associated methods
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import user_agent as UserAgent
from user_agents import parse


###################################################
# declare browser
###################################################
browser = ""

###################################################
# proxies
###################################################
''' class abandoned
class ProxyUtility:
    def __init__(self):
        self.proxy_ip = ""
    def return_proxy_ip(self):
        return self.proxy_ip

ProxyUtility = ProxyUtility()
def zip_proxy_extension():

    # Get project directory
    project_directory = os.path.abspath(os.curdir)
    extension_directory = project_directory + "/proxy/"

    # Create zipped extension
    ## Read in your extension files
    file_names = os.listdir(extension_directory)
    file_dict = {}
    for fn in file_names:
        with open(os.path.join(extension_directory, fn), 'r') as infile:
            file_dict[fn] = infile.read()

    ## Save files to zipped archive
    with zipfile.ZipFile("proxy.zip", 'w') as zippedfile:
        for fn, content in file_dict.items():
            zippedfile.writestr(fn, content)
'''
def get_ip(browser):
    browser.get("http://www.whatsmyip.org/")
    ip = browser.find_element_by_xpath("//span[@id='ip']")
    WebDriverWait(browser, 10).until(EC.visibility_of(ip))
    print("the current ip: " + ip.text)

###################################################
# mobile emulation
###################################################
mobile_emulation = {

    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},

    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}

###################################################
# browser
###################################################
def start_api(firefox, chrome, proxy, user_agent, recache):  # start call for the api

    # startup script
    print("@ ItsLit Records LLC -- This API is built for ItsLit Records LLC")
    print("Redistribution of this API is not allowed unless explicit permission from ItsLit Records LLC.")
    print("yvngbull crhodee - All Rights Reserved")
    print("Supports: Chrome, more coming soon...\n\n")

    #############
    # user options
    #############

    # load configuration
    config_file = open("config.txt", "r")
    contents = config_file.read()
    contents = contents.split('"')

    mobile_emulation = contents[1]
    proxy_ip = contents[3]
    fire_fox = contents[5]
    driver_path = contents[7]
    random_user_agent = contents[9]

    ##############################
    # Functions:
    ############
    def get_spreadsheet(): # Get spreadsheet function, set spreadsheet URL for future use
        spreadsheet_url = contents[9]
        # If spreadsheet URL contains a string variable execute the following code.
        if isinstance(spreadsheet_url, str):
            print("executing get function URL")
            SpreadsheetHandler.spreadsheet_url = spreadsheet_url
    ###############
    ###############
    def get_random_user_agent():
        print("\nfetching a random user agent...")
        def fetch_user_agents():
            try:
                time.sleep(1)
                useragent = UserAgent.generate_user_agent(os=None, navigator=None, platform=None, device_type=None)
                print("printing user cache: " + str(useragent))

                return useragent  # return the user_agent

            except Exception as exception:
                print("unable to load user cache!\n" + str(exception))

        # parse user agent information
        def user_agent_parser(useragent):
            #### print "user_agent" type:
            print("\nparsing the user_agent info...")

            print("user_agent being passed to parser: " + str(useragent))
            # parse user agent information.
            try:
                print("parsing user agent...")
                parsed_user_agent = parse(useragent)
            except Exception as exception:
                print("failed to parse user_agent!" + str(exception))

            user_agent_version = parsed_user_agent.browser.version_string

            return user_agent_version, parsed_user_agent, useragent

        ##########
        # find the correct user agent with right version.
        # check the fetched user agents

        count_of_user_agents_tested = 0
        user_agent_found = False
        #count_of_tries = 0

        print("checking user agents...")
        while not user_agent_found:  # while false
            count_of_user_agents_tested = count_of_user_agents_tested + 1

            # fetch the user_agents
            print("fetching the user_agents...")
            time.sleep(1)  # wait 1 s
            try:
                user_agent = fetch_user_agents()  # retrieves UA list
                print("\nuseragents retrieved: \n" + str(user_agent) + "\nprinting type: " + str(type(user_agent)))

            except Exception as exception:
                print("there was an issue fetching the user_agents!\n" + str(exception))

            print(user_agent)

            useragent_info = user_agent_parser(useragent=user_agent) # returns user_agent_version, parsed_user_agent, user_agent

            print("user agent info: \n" + str(useragent_info) + "\n")
            print("version: " + useragent_info[0])

            #count_of_tries = count_of_tries + 1

            #if count_of_tries == 20:
            #    exit()

            # check if user_agent is equal to a version defined below.
            if int(useragent_info[1].browser.version_string.split(".")[0]) > 60:
                user_agent_found = True

        try: # if unable to find user_agent
            print("\nuseragent: " + str(useragent_info[0]) + "\nNew Version: " + str(useragent_info[2]))

            return useragent_info
        except Exception as exception:
            print("unable to fetch user agent, try again.\n" + str(exception))

    ##############################
    # Run needed startup code:
    ##############################

    # Declare options for browsers as objects:
    chrome_options = Options()

    # Add options depending on configuration
    if chrome:  # adds chrome protections
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--profile-directory=Default')
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-plugins-discovery")
        chrome_options.add_argument("--start-maximized")


    if mobile_emulation != "False":
        print("launching with mobile emulation enabled...")
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    if proxy_ip == "":
        print("no proxy_ip! \ncheck config.")
        exit()

    # User agent initialization:
    random_useragent = get_random_user_agent() # recache is a bool
    print("\n" + "random useragent identified!:\n" + str(random_useragent) + str(type(random_useragent)) + "\n")

    print("now seperating the variables inside of random_useragent")
    fetched_user_agent = random_useragent[2]

    # run defined functions:
    get_spreadsheet()

    ####
    # launch browser:
    ####

    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(r'https://accounts.google.com/signin/v2/identifier?continue=' + \
                   'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1' + \
                   '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
        driver.implicitly_wait(15)

        loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
        loginBox.send_keys(gmailId)

        nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
        nextButton[0].click()

        passWordBox = driver.find_element_by_xpath(
            '//*[@id ="password"]/div[1]/div / div[1]/input')
        passWordBox.send_keys(passWord)

        nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
        nextButton[0].click()

        print('Login Successful...!!')
    except:
        print('Login Failed')

###################################################
# classes
###################################################
''' class unsupported.
class GoogleTrendsToolKit: # a master class containing methods relating to google trends interaction/automation
    def __init__(self):
        self.trends_information = {}

    def search_term(self, email, search_term):
        BrowserHandler.switch_to_tab_with_account(email)
        SpreadsheetHandler.tasking(account_name=email, current_task="searching term: " + str(search_term), next_task=0, last_successful_task=0)

        browser.get(url="https://trends.google.com/trends/?geo=US") # Get Google trends URL

        # get trends url :
        try:
            browser.find_element_by_xpath("//input[@placeholder='Enter a search term or a topic']").send_keys(search_term, Keys.RETURN)
        except:
            print("failed to enter keys in search (google trends)!")

    def get_related_search_queries(self, email):
        BrowserHandler.switch_to_tab_with_account(email)
        SpreadsheetHandler.tasking(account_name=email, current_task=0, next_task=0, last_successful_task=0)

        def scroll_down():
            SCROLL_PAUSE_TIME = 0.5

            while True:
                print("scrolling...")
                # Get scroll height
                ### This is the difference. Moving this *inside* the loop
                ### means that it checks if scrollTo is still scrolling
                last_height = browser.execute_script("return document.documentElement.scrollHeight")

                # Scroll down to bottom
                browser.execute_script("window.scrollBy(0, 500);")

                # Wait to load page
                time.sleep(SCROLL_PAUSE_TIME)

                # Calculate new scroll height and compare with last scroll height
                new_height = browser.execute_script("return document.documentElement.scrollHeight")
                if new_height == last_height:

                    # try again (can be removed)
                    browser.execute_script("window.scrollBy(0, 1500);")

                    # Wait to load page
                    time.sleep(SCROLL_PAUSE_TIME)

                    # Calculate new scroll height and compare with last scroll height
                    new_height = browser.execute_script("return document.documentElement.scrollHeight")

                    # check if the page height has remained the same
                    if new_height == last_height:
                        # return no more scrolling
                        return False
                    # if not, move on to the next loop
                    else:
                        last_height = new_height
                        continue

        time.sleep(1) # wait

        scroll_down() # scroll down

        div_number = 0 # set div number to one

        print("getting trending tags...")
        # get trending tags
        while browser.find_element_by_xpath("//div[4]//trends-widget[1]//ng-include[1]//widget[1]//div[1]//div[1]//ng-include[1]//div[1]//div[6]//pagination[1]//div[1]//button[2]//md-icon[1]"): # While browser can detect right arrow perform following code
            div_number = div_number + 1 # Set DIV search number to equal 1+ itself
            data_container = "//div[@class='fe-related-queries fe-atoms-generic-container']/ng-include/div[@class='fe-atoms-generic-content-container']//div[" + str(div_number) + "]"  # Data container is equal to

            # locate data container.
            try:
                print("trying to search for data container")
                if browser.find_element_by_xpath(data_container):
                    print("successfully located: " + data_container)
            except Exception as exception:
                print("THERE WAS AN ERROR WHEN TRYING TO DETECT DATA CONTAINER.")
                SpreadsheetHandler.report_error(email=email, error_message=exception)

            # get trends line number.
            try:
                trends_line_number = browser.find_element_by_xpath(data_container + "//div[@class='label-line-number']").text # Trends line number is equal to
            except Exception as exception:
                print("There was an error when trying to detect trends line number.")
                SpreadsheetHandler.report_error(email=email, error_message=exception)

            # get keyword type
            try:
                keyword_type = browser.find_element_by_xpath(data_container + "//div[3]").text # find keyword type
            except Exception as exception:
                print("There was an error when trying to detect keyword_type.")
                SpreadsheetHandler.report_error(email=email, error_message=exception)

            # combine trends line and keyword type into tuple value
            try:
                tuple = (trends_line_number, keyword_type)
            except Exception as exception:
                print("failed to make a tuple value! \n Do trends_line_number, keyword_type exist?")
                SpreadsheetHandler.report_error(email=email, error_message=exception)

            # get keyword
            try:
                keyword = browser.find_element_by_xpath(data_container + "//span").text
            except Exception as exception:
                print("There was an error when trying to get keyword.")
                SpreadsheetHandler.report_error(email=email, error_message=exception)

            # add values to dictionary
            try:
                self.trends_information[tuple] = keyword
            except Exception as exception:
                print("Unable to make dictionary! \n does tuple and keyword exist?")
                SpreadsheetHandler.report_error(email=email, error_message=exception)

            # if div number equals div number with an increase of five.
            if div_number % 5:
                repeat_number = div_number // 5
                for i in range(repeat_number):
                    right_arrow = browser.find_element_by_xpath("//div[4]//trends-widget[1]//ng-include[1]//widget[1]//div[1]//div[1]//ng-include[1]//div[1]//div[6]//pagination[1]//div[1]//button[2]//md-icon[1]") # Find right arrow
                    right_arrow.click() # Click right arrow
                    print(self.trends_information)
                    time.sleep(5)
'''

class BrowserHandler:  # A master class that handles browser related tasks.
    def __init__(self):
        self.count_of_tabs = 0

    def close_current_window(self):
        print("closing current window...")
        browser.close()

    def open_new_tab(self):  # Opens a new tab and adds it to the count of tabs
        print("opening a new tab...")
        browser.execute_script("window.open('');")
        time.sleep(3)
        self.count_of_tabs = self.count_of_tabs + 1

    def switch_tab(self, tabnumber):  # avoids long lines of non-sense and switches based on tab number
        print("switching tab...")
        browser.switch_to.window(browser.window_handles[tabnumber])

    def open_url(self, url):
        print("loading webpage...")
        time.sleep(.5)  # wait
        browser.get(url)  # get video
        time.sleep(5)  # wait

    def switch_to_tab_with_account(self, email):
        print("switching tabs to " + email)
        print(user_database)
        try:

            tabnumber = user_database.get(email)
            BrowserHandler.switch_tab(tabnumber)

        except Exception as execept:
            print("unable to find specified email!")
            print(execept)
            browser.__exit__()

class YouTubeToolKit:  # a master class containing methods relating to youtube interaction/automation
    def __init__(self):
        self.comment_search_failure_count = 0  # used to assist scrolling in: find_comment()

    def subscribe_on_video_page(self, email):
        # switch to correct tab and open video url
        BrowserHandler.switch_to_tab_with_account(email)

        print("Now subscribing on current video...")
        try:
            browser.find_element_by_xpath("//div[@id='container']//div[@id='subscribe-button']").click() # click subscribe
        except Exception as exception:
            print("Could not subscribe! \n" + str(exception))

    def navigate_back(self):
        print("went back a page.")
        browser.back()
        time.sleep(0.5)

    def wait(self, duration_of_time):
        time.sleep(duration_of_time)

    def open_youtube(self):
        browser.get(url="https://www.youtube.com/")

    def search_youtube(self, email, search_term, filter_by_date_today):
        # switch to correct tab and open video url
        BrowserHandler.switch_to_tab_with_account(email)

        # find search box
        search_box = browser.find_element_by_xpath("//input[@id='search']")

        # send keys to search box and search
        search_box.send_keys(search_term, Keys.RETURN)

        # wait
        time.sleep(1.5)

        if filter_by_date_today == True:
            try:
                browser.find_element_by_xpath("//yt-formatted-string[contains(text(),'Filter')]").click()
            except:
                try:
                    browser.find_element_by_xpath("//yt-formatted-string[contains(text(),'Filter')]").click()
                except:
                    print("unable to filter by date.")

            # wait
            time.sleep(1)

            browser.find_element_by_xpath("//yt-formatted-string[contains(text(),'Today')]").click()

        # wait
        time.sleep(1)

    def open_youtube_video_from_search_page(self, email, number):

        # define scroll method for later use
        def scroll_down():
            SCROLL_PAUSE_TIME = 0.5

            while True:
                print("scrolling...")
                # Get scroll height
                ### This is the difference. Moving this *inside* the loop
                ### means that it checks if scrollTo is still scrolling
                last_height = browser.execute_script("return document.documentElement.scrollHeight")

                # Scroll down to bottom
                browser.execute_script("window.scrollBy(0, 500);")

                # Wait to load page
                time.sleep(SCROLL_PAUSE_TIME)

                # Calculate new scroll height and compare with last scroll height
                new_height = browser.execute_script("return document.documentElement.scrollHeight")
                if new_height == last_height:

                    # try again (can be removed)
                    browser.execute_script("window.scrollBy(0, 1500);")

                    # Wait to load page
                    time.sleep(SCROLL_PAUSE_TIME)

                    # Calculate new scroll height and compare with last scroll height
                    new_height = browser.execute_script("return document.documentElement.scrollHeight")

                    # check if the page height has remained the same
                    if new_height == last_height:
                        # return no more scrolling
                        return False
                    # if not, move on to the next loop
                    else:
                        last_height = new_height
                        continue

        print("now attempting to open youtube video from search page.")

        video_found = False
        scroll_down_error_number = 1

        while video_found == False:
            try:
                print("try method 1")
                # switch to correct tab and open video url
                BrowserHandler.switch_to_tab_with_account(email)

                # open video according to xpath and click
                browser.find_element_by_xpath("//ytd-video-renderer[" + str(
                    number) + "]//yt-formatted-string[1]").click()  # select video by ytd-video-renderer tag pos.

                video_found = True
            except:
                try:
                    print("try method 2")
                    browser.find_element_by_xpath("//ytd-video-renderer[" + str(
                        number) + "]/div[1]/div[1]/div[1]/div[1]/h3[1]/a[1]").click()  # select video by ytd-video-renderer tag pos.

                    video_found = True
                except:
                    print("method 2 failure\nscrolling and retrying search...")
                    scroll_down_error_number = scroll_down_error_number + 1

                    # scroll down
                    try:
                        scroll_down()
                        if scroll_down_error_number == 10:
                            # browser refresh
                            try:
                                print("ALERT scroll_down_error_number reached 10:")
                                print("now refreshing the page.")
                                browser.refresh()
                            except:
                                print("unable to refresh page.")
                    except:
                        print("unable to scroll down!")

        # open video and wait
        try:
            self.video_title = browser.find_element_by_xpath(
                "//yt-formatted-string[@class='style-scope ytd-video-primary-info-renderer']").text
        except:
            print("unable to open youtube video")
        time.sleep(0.5)

    def steal_tag_data(self, email, video_url):
        # switch to correct tab and open video url
        BrowserHandler.switch_to_tab_with_account(email)
        BrowserHandler.open_url(video_url)

        tags_data = browser.find_element_by_xpath("//meta[@name='keywords']").get_attribute("content")
        return tags_data

    def upload_video(self, email, video_file_directory, video_details, use_classic_uploader):
        SpreadsheetHandler.tasking(account_name=email, current_task="uploading video on account: " + str(email),
                                   next_task=0, last_successful_task=0)  # update sheet

        def scroll_down(number_of_times):  # scroll down method
            SCROLL_PAUSE_TIME = 0.5

            for i in range(number_of_times):
                print("scrolling...")
                # Get scroll height
                ### This is the difference. Moving this *inside* the loop
                ### means that it checks if scrollTo is still scrolling
                # Scroll down to bottom
                browser.execute_script("scroll(0, 50)")

                # Wait to load page
                time.sleep(SCROLL_PAUSE_TIME)

        def classic_check_video_progress():
            try:
                upload_status = browser.find_element_by_xpath(
                    "//div[@class='upload-state-bar']//span[@class='progress-bar-percentage']").text
                if upload_status == "":
                    progress_status = browser.find_element_by_xpath(
                        "///div[@class='upload-state-bar']//span[@class='progress-bar-percentage']").text
                    return progress_status
                return upload_status
            except Exception as exception:
                print("failed to identify any values while preforming check_video_progress!")
                SpreadsheetHandler.report_error(email=email, error_message=exception)

        def check_video_progress():
            # check upload status
            try:
                upload_status = browser.find_element_by_xpath(
                    "//span[@class='progress-label style-scope ytcp-video-upload-progress']").text
                return upload_status
            except:
                print("failed to identify upload_status...")
                print("identify progress status...")
                try:
                    progress_status = browser.find_element_by_xpath(
                        "//span[@class='progress-label style-scope ytcp-video-upload-progress']").text
                    return progress_status
                except Exception as exception:
                    print("failed to identify any values while preforming check_video_progress!")
                    SpreadsheetHandler.report_error(email=email, error_message=exception)

        # click add content button
        print("clicking add content button...")
        try:
            browser.find_element_by_xpath(
                "//ytd-topbar-menu-button-renderer[1]//div[1]//a[1]//yt-icon-button[1]//button[1]//yt-icon[1]").click()
        except Exception as exception:
            print("failed to locate add content icon!")
            SpreadsheetHandler.report_error(email=email, error_message=exception)

        # click upload video button
        print("clicking upload video button...")
        try:
            browser.find_element_by_xpath("//yt-formatted-string[contains(text(),'Upload video')]").click()
        except Exception as exception:
            print("failed to locate upload video button!")
            SpreadsheetHandler.report_error(email=email, error_message=exception)

        # determine if using classic uploader
        if use_classic_uploader:
            print("using using classic uploader...")

            # click classic uploader.
            try:
                browser.find_element_by_xpath("//div[contains(text(),'Upload with Classic')]").click()
            except:
                print("failed to locate Upload with Classic button!")

            # check for YouTube uploader survey.
            try:
                if browser.find_element_by_xpath("//div[contains(text(),'Skip')]"):
                    browser.find_element_by_xpath("//div[contains(text(),'Skip')]").click()
            except:
                print("no skip button so proceeding")

            # place file into uploader.
            print("placing file into the upload tab...")
            try:
                upload_element = browser.find_element_by_xpath("//input[@type='file']")
                video_file_directory = os.path.dirname(
                    sys.argv[0]) + video_file_directory  # add project directory path.
                upload_element.send_keys(video_file_directory)  # send directory to uploader
            except Exception as exception:
                print("failed to place file into upload tab!")
                SpreadsheetHandler.report_error(email=email, error_message=exception)

            # enter in a title:
            title = str(video_details[2])
            print("entering in a title...")
            try:
                title_input_box = browser.find_element_by_xpath(
                    "//span[@class='yt-uix-form-input-container yt-uix-form-input-text-container yt-uix-form-input-non-empty']//input[@placeholder='Title']")
                for i in range(20):  # delete characters
                    title_input_box.send_keys(Keys.BACKSPACE)
                title_input_box.send_keys(title)
            except Exception as exception:
                print(exception)
                print("failed to input title!")
                SpreadsheetHandler.report_error(email=email, error_message=exception)

            # add description
            print("adding description...")
            description = str(video_details[4])
            try:
                description_input_box = browser.find_element_by_xpath(
                    "//div[@class='upload-item-main']//div//div[@class='sub-item-exp-zippy']//div[@class='sub-item-exp']//div[@class='metadata-editor-container']//div[@class='metadata-container']//form[@name='mdeform']//div[contains(@class,'metadata-tab basic-info-tab')]//fieldset[@class='metadata-two-column']//div//textarea[@placeholder='Description']")
                description_input_box.send_keys(description)
            except Exception as exception:
                print(exception)
                print("failed to input description!")
                SpreadsheetHandler.report_error(email=email, error_message=exception)

            # add tags
            tags = video_details[3].strip('"').replace('""', ",").split(",")  # split every '"'
            print("adding tags...")
            try:
                tags_input_box = browser.find_element_by_xpath(
                    "//div[@class='upload-item-main']//div//div[@class='sub-item-exp-zippy']//div[@class='sub-item-exp']//div[@class='metadata-editor-container']//div[@class='metadata-container']//form[@name='mdeform']//div[contains(@class,'metadata-tab basic-info-tab')]//fieldset[@class='metadata-two-column']//div//input[@placeholder='Tags (e.g., albert einstein, flying pig, mashup)']")
                for tag in tags:
                    tags_input_box.send_keys(tag + Keys.RETURN)
            except Exception as exception:
                print(exception)
                print("failed to add tags!")
                SpreadsheetHandler.report_error(email=email, error_message=exception)

            # check progress before proceeding
            progress = classic_check_video_progress()
            while progress != "Finished processing":
                time.sleep(2)
                progress = classic_check_video_progress()
                print(progress)
                if progress == "None":
                    progress = "Finished processing"
                    print('Uploader reported "None" -- Did you close the tab?')

            # click publish button
            try:
                browser.find_element_by_xpath(
                    "//button[@class='yt-uix-button yt-uix-button-size-default save-changes-button yt-uix-tooltip yt-uix-button-primary']").click()
            except Exception as exception:
                print(exception)
                print("failed to click done button!")
                SpreadsheetHandler.report_error(email=email, error_message=exception)

            print("complete uploading!")

        # if not using classic uploader
        if not use_classic_uploader:
            print("not using classic uploader...")
            # place file into uploader.
            print("placing file into the upload tab...")
            try:
                upload_element = browser.find_element_by_xpath("//input[@type='file']")
                video_file_directory = os.path.dirname(
                    sys.argv[0]) + video_file_directory  # add project directory path.
                upload_element.send_keys(video_file_directory)  # send directory to uploader
            except Exception as exception:
                print("failed to place file into upload tab!")
                SpreadsheetHandler.report_error(email=email, error_message=exception)

            time.sleep(3)  # wait

            # add title
            print("adding title...")
            title = str(video_details[2])
            try:
                title_input_box = browser.find_element_by_xpath(
                    "//ytcp-mention-textbox//div[@aria-label='Add a title that describes your video']")
                for i in range(100):  # delete characters
                    title_input_box.send_keys(Keys.BACKSPACE)
                title_input_box.send_keys(title)
            except Exception as exception:
                print(exception)
                print("failed to input title!")
                SpreadsheetHandler.report_error(email=email, error_message=exception)

            # add description
            print("adding description...")
            description = str(video_details[4])
            try:
                description_input_box = browser.find_element_by_xpath(
                    "//ytcp-mention-textbox//div[@aria-label='Tell viewers about your video']")
                for i in range(100):  # delete characters
                    description_input_box.send_keys(Keys.BACKSPACE)
                description_input_box.send_keys(description)
            except Exception as exception:
                print(exception)
                print("failed to input description!")
                SpreadsheetHandler.report_error(email=email, error_message=exception)

            scroll_down(2)  # scroll down

            # select if safe for kids
            print("selecting if safe for kids...")
            try:
                if video_details[5].lower() == "true":
                    browser.find_element_by_xpath("//paper-radio-button[@name='MADE_FOR_KIDS']").click()
                if video_details[5].lower() == "false":
                    browser.find_element_by_xpath("//paper-radio-button[@name='NOT_MADE_FOR_KIDS']").click()
            except Exception as exception:
                print(exception)
                print("failed to select if safe for kids!")
                SpreadsheetHandler.report_error(email=email, error_message=exception)

            # open more options
            print("opening more options...")
            try:
                browser.find_element_by_xpath(
                    "//ytcp-button[@class='advanced-button style-scope ytcp-uploads-details']").click()
            except Exception as exception:
                print(exception)
                print("failed to open more options!")
                SpreadsheetHandler.report_error(email=email, error_message=exception)

            scroll_down(2)  # scroll down

            # add tags
            tags = video_details[3].strip('"').replace('""', ",").split(",")  # split every '"'

            print("adding tags...")
            try:
                tags_input_box = browser.find_element_by_xpath(
                    "//ytcp-free-text-chip-bar//input[@placeholder='Add tag']")
                for tag in tags:
                    tags_input_box.send_keys(tag + Keys.RETURN)
            except Exception as exception:
                print(exception)
                print("failed to add tags!")
                SpreadsheetHandler.report_error(email=email, error_message=exception)

            # click next button
            try:
                browser.find_element_by_xpath("//div[contains(text(),'Next')]").click()
            except Exception as exception:
                print(exception)
                print("failed to click next button!")
                SpreadsheetHandler.report_error(email=email, error_message=exception)

            # click next again
            try:
                browser.find_element_by_xpath("//div[contains(text(),'Next')]").click()
            except Exception as exception:
                print(exception)
                print("failed to click next button again!")
                SpreadsheetHandler.report_error(email=email, error_message=exception)

            # click public option button
            try:
                browser.find_element_by_xpath("//paper-radio-button[@name='PUBLIC']").click()
            except Exception as exception:
                print(exception)
                print("failed to click public option button!")
                SpreadsheetHandler.report_error(email=email, error_message=exception)

            # check progress before proceeding
            progress = check_video_progress()
            while progress != "Finished processing":
                time.sleep(2)
                progress = check_video_progress()
                print(progress)
                if progress == "None":
                    progress = "Finished processing"
                    print('Uploader reported "None" -- Did you close the tab?')

            # click done button
            try:
                browser.find_element_by_xpath("//div[contains(text(),'Done')]").click()
            except Exception as exception:
                print(exception)
                print("failed to click done button!")
                SpreadsheetHandler.report_error(email=email, error_message=exception)

            print("complete uploading!")

    def open_video_url(self, email, video_url):
        if email == False:
            print("No email sign-in enabled, operating w/o.")
        else:
            try:
                BrowserHandler.switch_to_tab_with_account(email=email)
            except Exception as e:
                print("error opening video url!\n" + str(e))
        BrowserHandler.open_url(url=video_url)
        time.sleep(2)
        try:
            self.video_title = browser.find_element_by_xpath(
                "//yt-formatted-string[@class='style-scope ytd-video-primary-info-renderer']").text
        except:
            print("could not fetch video title.")

    # tasking methods:
    def add_view(self, email, video_duration):  # open a new tab for a video and watch it the whole way through
        print("adding view, please note that video_duration is in seconds...")
        if email == False:
            print("No email sign-in enabled, operating w/o.")
        else:
            # switch to proper account and tab
            BrowserHandler.switch_to_tab_with_account(email=email)

            SpreadsheetHandler.tasking(account_name=email, current_task="viewing video: " + self.video_title,
                                       next_task=0,
                                       last_successful_task=0)

        successfully_viewed_video = True

        # press play button:
        try:
            play_button = browser.find_element_by_xpath('//*[@id="movie_player"]/div[4]/button')
            play_button_class = browser.find_elements_by_class_name('ytp-large-play-button.ytp-button')
            play_button.click()
            # play_button_class.click()
            time.sleep(video_duration)  # Arbitrary time in seconds to watch the video.

        except Exception as exception:
            print("failed to add view to the video: " + self.video_title)
            successfully_viewed_video = False
            if email != False:
                SpreadsheetHandler.tasking(account_name=email, current_task="[ERROR] " + str(exception), next_task=0,
                                       last_successful_task="last task failed")  # update tasking tab

        if successfully_viewed_video:
            SpreadsheetHandler.tasking(account_name=email, current_task=" ", next_task=0,
                                       last_successful_task="viewing video: " + self.video_title)

    def comment_on_video(self, email,comment):  # finds comment box and inserts comment. GOAL: find comment box and enter comment
        SpreadsheetHandler.tasking(account_name=email, current_task="commenting on: " + self.video_title, next_task=0,
                                   last_successful_task=0)  # update spreadsheet
        successfully_commented = True

        def scroll_down():
            SCROLL_PAUSE_TIME = 0.5

            while True:
                print("scrolling...")
                # Get scroll height
                ### This is the difference. Moving this *inside* the loop
                ### means that it checks if scrollTo is still scrolling
                last_height = browser.execute_script("return document.documentElement.scrollHeight")

                # Scroll down to bottom
                browser.execute_script("window.scrollBy(0, 50);")

                # Wait to load page
                time.sleep(SCROLL_PAUSE_TIME)

                # Calculate new scroll height and compare with last scroll height
                new_height = browser.execute_script("return document.documentElement.scrollHeight")
                if new_height == last_height:

                    # try again (can be removed)
                    browser.execute_script("window.scrollBy(0, 50);")

                    # Wait to load page
                    time.sleep(SCROLL_PAUSE_TIME)

                    # Calculate new scroll height and compare with last scroll height
                    new_height = browser.execute_script("return document.documentElement.scrollHeight")

                    # check if the page height has remained the same
                    if new_height == last_height:
                        # return no more scrolling
                        return False
                    # if not, move on to the next loop
                    else:
                        last_height = new_height
                        continue

        print("commenting on video...")

        # scroll to the bottom of the page.
        scroll_down()

        # wait
        time.sleep(1)

        # find & click comment box
        try:
            comment_box = browser.find_element_by_xpath('//*[@id="placeholder-area"]')
            comment_box.click()
        except:
            print("click comment box")

        # wait
        time.sleep(1.5)

        # add comment
        print("adding comment...")
        try:
            print("trying method 1")
            comment_input_box = browser.find_element_by_xpath(
                "//yt-formatted-string[@id='contenteditable-textarea']//div[@id='contenteditable-root']")
            comment_input_box.send_keys(comment)
        except Exception as exception:
            print(exception)
            try:
                print("trying method 2")
                comment_input_box = browser.find_element_by_xpath(
                    "//div[@id='contenteditable-root']//aria-label[text()='Add a public comment...']")
                comment_input_box.send_keys(comment)
            except Exception as exception:
                print(exception)
                try:
                    print("trying method 3")
                    comment_input_box = browser.find_element_by_xpath(
                        '//yt-formatted-string//*[@id="contenteditable-root"]')
                    comment_input_box.send_keys()
                except Exception as exception:
                    print(exception)
                    try:
                        print("trying method 4")
                        comment_input_box = browser.find_element_by_xpath('//*[@id="placeholder-area"]')
                        comment_input_box.send_keys()
                    except Exception as exception:
                        SpreadsheetHandler.tasking(account_name=email, current_task="[ERROR] " + str(exception),
                                                   next_task=0,
                                                   last_successful_task="last task failed")  # update tasking tab
                        print(exception)
                        successfully_commented = False
                        print("there was an error when selecting the comment box!")
        try:
            # find comment submit box
            browser.find_element_by_xpath("//ytd-button-renderer[@id='submit-button']//yt-formatted-string[@id='text']").click()
        except:
            print("there was an issue trying to post comment")


        if successfully_commented:
            # update spreadsheet
            SpreadsheetHandler.tasking(account_name=email, current_task=" ", next_task=0,
                                       last_successful_task="commenting on: " + self.video_title)

    def check_if_subscribed(self, email):
        print("checking if subscribed on current video...")
        subscribed = False

        SpreadsheetHandler.tasking(account_name=email, current_task="checking subscribe status for: " + self.video_title, next_task=0,
                                   last_successful_task=0)  # update tasking tab

        # check subscribe button
        try:
            subscribed_button = browser.find_element_by_xpath(xpath="//ytd-subscribe-button-renderer[@class='style-scope ytd-video-secondary-info-renderer']//yt-formatted-string[@class='style-scope ytd-subscribe-button-renderer'][contains(text(),'Subscribed')]")
            subscribed = True
            print("subscribed status True")
            return subscribed
        except:
            subscribed = False
            print("subscribed status False")
            return subscribed

    def like_video(self, email):  # finds like button and clicks it.
        print("liking video...")
        successfully_liked_video = True

        SpreadsheetHandler.tasking(account_name=email, current_task="liking video: " + self.video_title, next_task=0,
                                   last_successful_task=0)  # update tasking tab

        # like video
        try:
            print("resolving method 1")
            like_button = browser.find_element_by_xpath(xpath="//div[@id='info']//ytd-toggle-button-renderer[1]")
            like_button[0].click()
        except:
            try:
                print("resolving method 2")
                like_button = browser.find_element_by_xpath(
                    xpath="//body/ytm-app[@id='app']/div[@class='page-container']/ytm-watch/ytm-single-column-watch-next-results-renderer[@class='watch-content']/ytm-item-section-renderer[@class='scwnr-content']/lazy-list/ytm-slim-video-metadata-renderer[@class='item']/div[@class='slim-video-metadata-actions']/c3-material-button[1]/button[1]/div[1]")
                like_button[0].click()
            except:
                try:
                    time.sleep(.5)
                    print("resolving method 3")
                    like_button = browser.find_element_by_xpath(
                        xpath="//div[@class='slim-video-metadata-actions']//c3-material-button[1]//button[1]")
                    like_button[0].click()
                except:
                    try:
                        time.sleep(.5)
                        print("resolving method 4")
                        like_button = browser.find_element_by_xpath(
                            xpath="//ytd-toggle-button-renderer[1]//a[1]//yt-icon-button[1]//button[1]//yt-icon[1]")
                        like_button.click()
                    except:
                        try:
                            print("resolving method 5")
                            like_button = browser.find_element_by_xpath(
                                xpath="//ytd-toggle-button-renderer[1]//a[1]//yt-icon-button[1]//button[1]")
                            like_button.click()
                        except:
                            try:
                                like_button = browser.find_element_by_css_selector(css_selector="#button")
                                like_button.click()
                            except:
                                try:
                                    print("resolving method 6")
                                    like_button = browser.find_element_by_xpath(
                                        xpath="//button[@class='style-scope yt-icon-button']")
                                    like_button.click()
                                except:
                                    try:
                                        print("resolving method 7")
                                        like_button = browser.find_element_by_xpath(
                                            xpath="//button[@class='c3-material-button-button']")
                                        like_button.click()
                                    except:
                                        try:
                                            print("resolving method 8")
                                            like_button = browser.find_element_by_xpath(
                                                xpath="//div[@id='info']//ytd-toggle-button-renderer[1]//a[1]//yt-icon-button[1]//button[1]//yt-icon[1]")
                                            like_button.click()
                                        except Exception as exception:
                                            SpreadsheetHandler.tasking(account_name=email,
                                                                       current_task="[ERROR] " + str(exception),
                                                                       next_task=0,
                                                                       last_successful_task="last task failed")  # update tasking tab
                                            print(exception)
                                            print('failed to click like!')
                                            successfully_liked_video = False

        if successfully_liked_video:
            print("successfully liked video!")
            SpreadsheetHandler.tasking(account_name=email, current_task=" ", next_task=0,
                                       last_successful_task="liking video: " + self.video_title)  # update tasking tab

    # comment actions:
    def find_and_select_comment(self, email, comment_text,
                                commenter_name):  # finds comment number to select a certain comment based on it's number on the comment list, scrolls down based on weather a corresponding true or false variable is true or false.
        print("selecting comment...")

        successfully_found_comment = True

        # update spreadsheet:
        SpreadsheetHandler.tasking(account_name=email, current_task="finding comment on: " + self.video_title,
                                   next_task=0, last_successful_task=0)

        # scroll down:
        def scroll_down():
            SCROLL_PAUSE_TIME = 0.5

            while True:
                print("scrolling...")
                # Get scroll height
                ### This is the difference. Moving this *inside* the loop
                ### means that it checks if scrollTo is still scrolling
                last_height = browser.execute_script("return document.documentElement.scrollHeight")

                # Scroll down to bottom
                browser.execute_script("window.scrollBy(0, 500);")

                # Wait to load page
                time.sleep(SCROLL_PAUSE_TIME)

                # Calculate new scroll height and compare with last scroll height
                new_height = browser.execute_script("return document.documentElement.scrollHeight")
                if new_height == last_height:

                    # try again (can be removed)
                    browser.execute_script("window.scrollBy(0, 1500);")

                    # Wait to load page
                    time.sleep(SCROLL_PAUSE_TIME)

                    # Calculate new scroll height and compare with last scroll height
                    new_height = browser.execute_script("return document.documentElement.scrollHeight")

                    # check if the page height has remained the same
                    if new_height == last_height:
                        # return no more scrolling
                        return False
                    # if not, move on to the next loop
                    else:
                        last_height = new_height
                        continue

        # find comment function:
        def find_comment(comment_row):  # finds comment based on the content of that comment and the row it's on.
            # challenge: make a loop that goes through every comment by it's xpath. "//body//ytd-comment-thread-renderer[" + str(comment_number) + "]" + "//span[contains(text(),'" + commenter_name + "')]"
            # find a comment by commenter and commenter's text

            # scroll down once
            scroll_down()

            # denotes current row to console.
            comment_container = "//body//ytd-comment-thread-renderer[" + str(comment_row) + "]" # set the comment_container
            print("scanning: " + comment_container)

            #####
            # try to find the comment box
            comment_box_found = False
            try:
                comment_box = browser.find_element_by_xpath(comment_container)
                print("!!! \n" + str(comment_box)) # check comment box
                comment_box_found = True

            except Exception as exception:
                print("!!! could not find comment box \n")
                print(str(exception))

                #if "Unable to locate element" in str(exception):


            #####
            # Check Comment Contents:
            #####

            # only preform comment name check if comment_name does not = "None"
            if commenter_name != "None":

                #####
                # Check Commenter's Name:
                try:
                    commenter_element = browser.find_element_by_xpath(
                        str(comment_container) + "//span[contains(text(),'" + str(commenter_name) + "')]")
                    print("comment element: " + str(commenter_element))

                except Exception as exception:
                    print("commenter name does not match!\n" + str(exception))

                #### check the comment name and compare it to the comment name
                # if commenter text == none
                if comment_text == "None":
                    if commenter_element.text == commenter_name:
                        print("comment found @ row " + str(comment_box))
                        matching_comment = True
                        return matching_comment, comment_box, comment_box_found


            # only preform comment text check if comment_text = "None"
            if comment_text != "None":

                #####
                # Check Commenter's Text:
                try:
                    content_element = browser.find_element_by_xpath(
                        comment_container + "//yt-formatted-string[contains(text(),'" + str(comment_text) + "')]")

                except:
                    try:
                        content_element = browser.find_element_by_xpath(
                            comment_container + "//ytd-expander[contains(text(),'" + str(comment_text) + "')]")
                    except:
                        print("content does not match!")

                #### check the comment content and compare it to the comment text
                # if commenter name == none
                if commenter_name == "None":
                    if content_element.text == comment_text:
                        print("comment found @ row " + str(comment_box))
                        matching_comment = True
                        return matching_comment, comment_box, comment_box_found

            if commenter_element.text == commenter_name and content_element.text == comment_text:  # if comment content is equal to search value, then matching comment is returned true.
                print("comment found @ row " + str(comment_box))
                matching_comment = True
                return matching_comment, comment_box, comment_box_found  # returns comment's number
        # denotes end of find comment function

        
        ######
        # code executes below :
        ######

        scroll_down()
        time.sleep(1) # wait and allow time for comment box to load.

        ###
        # while loop to find a matching comment - uses find_comment()

        # method code executes here:
        count_of_comments_scanned = 0
        scroll_down_attempts = 0
        comment_matching = False

        while not comment_matching:
            ###
            # begin to find comment:
            try:
                time.sleep(2)
                count_of_comments_scanned = count_of_comments_scanned + 1  # initialize the count_of_comments variable to keep track of number of tries.

                print("\nattempting search number: " + str(count_of_comments_scanned))


                comment_element = find_comment(
                    count_of_comments_scanned)  # comment element is equal to the output of find_comment method.

                print("comment element: " + str(comment_element))

            except Exception as exception: # THIS EXCEPT LOOP DOES NOT EXECUTE!
                print("was unable to find comment at the number : " + str(count_of_comments_scanned) + "\nerror at: " + str(exception))

            try:
                if not comment_element:  # if comment_element returns as false, repeat the method.
                    print("comment returned as false and did not match!")

                if comment_element[2] == False:
                    print("unable to find comment box! - stop searching.")
                    break



                if comment_element == 2:  # if the comment_element returns 2, then scroll_down.
                    print("attempting to scroll down...")

                    scroll_down()
                    time.sleep(3) # sleep for 3 seconds

                    if not scroll_down():  # if it cannot scroll down anymore the comment cannot be found.
                        print("cannot scroll down any longer on page - assuming max scroll depth has been reached.")
                        scroll_down_attempts = scroll_down_attempts + 1
                        if scroll_down_attempts == 2:
                            print("scroll down attempts is equal to 2")

            except Exception as exception:
                print(exception)


            try:
                if comment_element[0]:  # if the find_comment method returns true return the comment_element
                    comment_matching = True
                    return comment_element[0], comment_element[1]

            except Exception as exception:
                print("comment resolved as false.")



                # update spreadsheet
                SpreadsheetHandler.tasking(account_name=email, current_task="[ERROR] " + str(exception), next_task=0,
                                           last_successful_task="last task failed")  # update tasking tab

        if comment_matching:
            successfully_found_comment = True

        if successfully_found_comment:
            # update spreadsheet
            SpreadsheetHandler.tasking(account_name=email, current_task=0, next_task=0,
                                       last_successful_task="finding comment on: " + self.video_title)

    def like_comment(self, email,
                     selected_comment):  # likes a comment. GOAL: press like button on a comment based on it's number
        print("liking comment...")

        successfully_liked = True

        # update spreadsheet
        SpreadsheetHandler.tasking(account_name=email, current_task="liking comment on: " + self.video_title,
                                   next_task=0, last_successful_task=0)

        try:

            # find comment like button.
            comment_like_button = browser.find_element_by_xpath(
                selected_comment + "//ytd-comment-renderer[1]//div[2]//div[2]//ytd-comment-action-buttons-renderer[1]//div[1]//ytd-toggle-button-renderer[1]//a[1]//yt-icon-button[1]//button[1]//yt-icon[1]")
            comment_like_button.click()

        except Exception as exception:
            SpreadsheetHandler.tasking(account_name=email, current_task="[ERROR] " + str(exception), next_task=0,
                                       last_successful_task="last task failed")  # update tasking tab
            successfully_liked = False
            print("failed to like comment!")
            print(exception)

        if successfully_liked:
            # update spreadsheet
            SpreadsheetHandler.tasking(account_name=email, current_task=0, next_task=0,
                                       last_successful_task="liking comment on: " + self.video_title)  #

    def reply_to_comment(self, email, selected_comment, comment_text):
        print("replying to comment...")

        successfully_replied = True

        # update spreadsheet
        SpreadsheetHandler.tasking(account_name=email, current_task="reply to comment on: " + self.video_title,
                                   next_task=0, last_successful_task=0)

        try:

            # find comment reply button and click it.
            comment_reply_button = browser.find_element_by_xpath(str(
                selected_comment) + "//ytd-comment-renderer[1]//div[2]//div[2]//ytd-comment-action-buttons-renderer[1]//div[1]//div[4]//ytd-button-renderer[1]//a[1]//paper-button[1]//yt-formatted-string[1]")
            comment_reply_button.click()

            # find comment input box and send keys.
            comment_reply = browser.find_element_by_xpath(selected_comment + "//div[@id='contenteditable-root']")
            comment_reply.send_keys(comment_text)
            comment_reply.send_keys(Keys.RETURN)

            # find reply/submit button and click
            comment_reply_submit_button = browser.find_element_by_xpath(str(
                selected_comment) + "//ytd-comment-renderer[1]//div[2]//div[2]//ytd-comment-action-buttons-renderer[1]//div[2]//ytd-comment-reply-dialog-renderer[1]//ytd-commentbox[1]//div[1]//div[2]//div[4]//ytd-button-renderer[2]//a[1]//paper-button[1]//yt-formatted-string[1]")
            comment_reply_submit_button.click()

        except Exception as exception:
            SpreadsheetHandler.tasking(account_name=email, current_task="[ERROR] " + str(exception), next_task=0,
                                       last_successful_task="last task failed")  # update tasking tab
            successfully_replied = False
            print("failed to reply to comment!")
            print(exception)

        if successfully_replied:
            # update spreadsheet
            SpreadsheetHandler.tasking(account_name=email, current_task=0, next_task=0,
                                       last_successful_task="reply to comment on: " + self.video_title)

class GoogleHandler:  # class that handles google related tasks.
    def __init__(self):
        self.username = ""  # in login method
        self.password = ""  # in login method
        self.error = "[!] There was a critical error that broke the program! (googlehandler)"
        self.login_count = 0  # in login method
        self.critical_stop_during_signin_error = True  # in login method

    '''def login_method2(self, email, password): // stackoverflow - signing through the google sign in w/
        SpreadsheetHandler.information(account_name=email, is_running=False)
        SpreadsheetHandler.tasking(account_name=email, current_task="logging in...", next_task=0,
                                   last_successful_task=0)
        print("number of tabs currently open: " + str(BrowserHandler.count_of_tabs + 1))
        time.sleep(1)

        critical_stop_during_signin_error = self.critical_stop_during_signin_error
        successful_sign_in = True

        # URL for google login
        url = "https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f"

        if self.login_count > 0:  # opens a new tab if login_count is greater then zero.
            BrowserHandler.open_new_tab()
            time.sleep(.5)
            print("switching tab")
            BrowserHandler.switch_tab(self.login_count)
            url = "https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f"

        print("adding one to login count")
        self.login_count = self.login_count + 1
        browser.get(url)
        time.sleep(4)

        # sign-in
        print("attempting sign-in...")

        try:
            browser.'''

    def login(self, email, password):  # function that opens a new tab and logins into google.
        #browser.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        SpreadsheetHandler.information(account_name=email, is_running=False)
        SpreadsheetHandler.tasking(account_name=email, current_task="logging in...", next_task=0,
                                   last_successful_task=0)
        print("number of tabs currently open: " + str(BrowserHandler.count_of_tabs + 1))
        time.sleep(1)

        critical_stop_during_signin_error = self.critical_stop_during_signin_error
        successful_sign_in = True

        # URL for google login
        url = "https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier"

        if self.login_count > 0:  # opens a new tab if login_count is greater then zero.
            BrowserHandler.open_new_tab()
            time.sleep(.5)
            print("switching tab")
            BrowserHandler.switch_tab(self.login_count)
            url = "https://accounts.google.com/signin/v2/identifier?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Dsign_in_no_continue%26pli%3D1&csig=AF-SEnZ2VqnzHo8jZvx0%3A1571673893&flowName=GlifWebSignIn&flowEntry=AddSession"

        print("adding one to login count")
        self.login_count = self.login_count + 1
        browser.get(url)
        time.sleep(4)

        # sign-in
        print("attempting sign-in...")

        # select email
        print("selecting email box...")
        try:

            print("resolving method 1")
            email_input_box = browser.find_element_by_xpath(xpath="//input[@autocomplete='username']")
            email_input_box.send_keys(email, Keys.ENTER)

        except:
            try:

                print("resolving method 2")
                email_input_box = browser.find_element_by_css_selector(css_selector="#identifierId")
                email_input_box.send_keys(email, Keys.ENTER)

            except:
                try:

                    print("resolving method 3")
                    email_input_box = browser.find_element_by_id(id_="identifierId")
                    email_input_box.send_keys(email, Keys.ENTER)

                except:
                    try:

                        print("resolving method 4")
                        email_input_box = browser.find_element_by_xpath(xpath="//input[@aria-label='Email or phone']")
                        email_input_box.send_keys(email, Keys.ENTER)

                    except:
                        try:

                            print("resolving method 5")
                            email_input_box = browser.find_elements_by_class_name("whsOnd zHQkBf")
                            email_input_box.send_keys(email, Keys.ENTER)

                        except:
                            try:

                                print("resolving method 6")
                                email_input_box = browser.find_element_by_xpath(
                                    xpath="//input[@placeholder='Email or phone']")
                                email_input_box.send_keys(email, Keys.ENTER)

                            except Exception as exception:
                                successful_sign_in = False
                                print("there was an exception when trying to identify email box: ")
                                print(exception)

        # wait
        time.sleep(2)

        # select password
        print("selecting password box...")
        try:

            print("resolving method 1")
            password_input_box = browser.find_element_by_xpath(xpath="//input[@autocomplete='current-password']")
            password_input_box.send_keys(password, Keys.ENTER)

        except:
            try:

                print("resolving method 2")
                password_input_box = browser.find_element_by_xpath(xpath="//input[@placeholder='Password']")
                password_input_box.send_keys(password, Keys.ENTER)

            except:
                try:
                    password_input_box = browser.find_element_by_xpath(xpath="//input[@id='password']")
                    password_input_box.send_keys(password, Keys.ENTER)

                except Exception as exception:
                    successful_sign_in = False
                    print("there was an exception when trying to identify email box: ")
                    print(exception)

        # wait
        time.sleep(2)

        # check if login successful
        try:

            if browser.find_element_by_xpath(
                    "//span[contains(text(),'Wrong password. Try again or click Forgot password')]"):
                error = "[ERROR:] " + "Wrong password. Try again or click Forgot password"
                print(error)
                print(
                    "You can disable stop signal for signin by setting critical_stop_during_signin_error equal to False ")
                SpreadsheetHandler.update_information(account_name=email, is_running=False, username=error)
                successful_sign_in = False

                if critical_stop_during_signin_error:
                    browser.__exit__()

        except:
            pass

        # if successful login, add spreadsheet information.
        if successful_sign_in:
            tabnumber = BrowserHandler.count_of_tabs + 1
            print(email + " has successfully signed in and is tab number: " + str(tabnumber))
            SpreadsheetHandler.update_information(account_name=email, is_running=True, username=0)
            SpreadsheetHandler.tasking(account_name=email, current_task=" ", next_task=0,
                                       last_successful_task="logging in...")
            user_database[email] = tabnumber - 1
            print(" ")
            time.sleep(3)
            print("no sign in error detected")

    def youtube_account_switcher(self, email, accountname):
        url = "https://www.youtube.com/"
        BrowserHandler.switch_to_tab_with_account(email)
        BrowserHandler.open_url(url)
        successfully_switched_accounts = True

        SpreadsheetHandler.update_information(account_name=email, is_running=True, username=accountname)
        SpreadsheetHandler.tasking(account_name=email, current_task="switching to account: " + accountname, next_task=0,
                                   last_successful_task=0)

        # select account
        try:
            print("fetching a list of accounts...")

            # click the account icon
            try:

                print("clicking account_icon_button")
                account_icon_button = browser.find_element_by_xpath("//button[@id='avatar-btn']")
                account_icon_button.click()

            except:
                print("failed to click account_icon_button!")
                successfully_switched_accounts = False

            # wait
            time.sleep(1)

            # click the switch button
            try:

                print("clicking switch_accounts_button")
                switch_accounts_button = browser.find_element_by_xpath(
                    "//yt-formatted-string[contains(text(),'Switch account')]")
                switch_accounts_button.click()

            except:
                print("failed to click switch_accounts_button")
                try:

                    switch_accounts_button = browser.find_element_by_xpath(
                        "//yt-multi-page-menu-section-renderer[1]//div[2]//ytd-compact-link-renderer[4]//a[1]//paper-item[1]")
                    switch_accounts_button.click()

                except Exception as exception:
                    successfully_switched_accounts = False
                    print(exception)
                    print("failed to click switch_accounts_button")

            # wait
            time.sleep(1)

            # switch the account
            print("switching accounts...")
            try:

                print("trying method 1")
                youtube_account_list = "//ytd-multi-page-menu-renderer[@class='style-scope ytd-multi-page-menu-renderer']//div[@id='sections'].//*[@*='" + accountname + "']"  # all the youtube accounts

                email_name = browser.find_element_by_xpath(youtube_account_list)
                email_name.click()

            except:
                try:

                    print("trying method 2")
                    xpath = "//ytd-multi-page-menu-renderer[@class='style-scope ytd-multi-page-menu-renderer']//div[@id='sections']//yt-formatted-string[contains(text(),'" + accountname + "')]"
                    email_name = browser.find_element_by_xpath(xpath)
                    email_name.click()

                except:
                    print("unable to switch accounts!")
                    successfully_switched_accounts = False

        except Exception as exception:
            successfully_switched_accounts = False
            print("there was an error when trying to switch accounts")
            print(exception)

        if not successfully_switched_accounts:
            SpreadsheetHandler.update_information(account_name=email, is_running=False,
                                                  username="[ERROR] there was an error when trying to switch accounts!")

        if successfully_switched_accounts:
            SpreadsheetHandler.tasking(account_name=email, current_task=" ", next_task=0,
                                       last_successful_task="switching to account: " + accountname)

    def youtube_account_create(self, email, accountname):
        url = "https://www.youtube.com/channel_switcher"
        BrowserHandler.switch_to_tab_with_account(email)
        BrowserHandler.open_url(url)

        time.sleep(2)
        if browser.find_element_by_xpath("//div[@id='identity-prompt-dialog'"):
            browser.find_element_by_xpath("//input[@class='yt-uix-form-input-radio'")

        # click create channel
        try:
            create_channel_button = browser.find_element_by_xpath("//div[contains(@class,'create-channel-text')]")
            create_channel_button.click()
        except Exception as execption:
            print(execption)
            SpreadsheetHandler.report_error(email, execption)

        # enter keys to brand name account input_box
        try:
            brand_name_account_input = browser.find_element_by_xpath("//input[@class='brandaccount-signup-input']")
            brand_name_account_input.send_keys(accountname)
        except Exception as execption:
            print(execption)
            SpreadsheetHandler.report_error(email, execption)

        # click create channel button
        try:
            browser.find_element_by_xpath("//input[@value='Create']").click()
        except Exception as execption:
            print(execption)
            SpreadsheetHandler.report_error(email, execption)

class SpreadsheetHandler:  # handles spreadsheet information.
    def __init__(self):
        # use creds to create a client to interact with the Google Drive API
        self.scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        self.creds = ServiceAccountCredentials.from_json_keyfile_name('youtubeBot-bd59b0ee46a7.json', self.scope)
        self.gc = gspread.authorize(self.creds)
        self.account_database = {}  # stores accounts name and their row.
        self.start_row = 6  # puts data below this row.
        self.count_of_users = 0

    def check_cell_and_return_cell_as_string(self, email, column, sheet):
        # get cell value
        try:
            cell_value = column + str(self.account_database.get(email))  # combine column w/ cell row
            checked_cell = sheet.acell(cell_value).value  # retrieve cell content
            print("Fetched cell: " + cell_value + "\nRetrieved: " + checked_cell)
            return checked_cell

        except Exception as exception:
            print(str(exception) + "\nFailed to successfully retrieve posting data!")

    def switch_worksheet(self, sheet_number):
        print("switching to worksheet: " + str(sheet_number) + "...")
        sheet_number = sheet_number - 1
        sheet = self.sheet.get_worksheet(sheet_number)
        return sheet

    def clear_list_data(self, sheet, start, end):
        print("cleared data for sheet: " + str(sheet) + "\n" + "@rows: " + str(start) + " to " + str(end))
        # set all cells to blank cell
        sheet = SpreadsheetHandler.switch_worksheet(sheet)
        cell_list = sheet.range(str(start) + ':' + str(end))
        for cell in cell_list:
            cell.value = ' '
        sheet.update_cells(cell_list)

    def import_sheet(self):  # imports sheet and saves it to the init function.
        print("importing data...")
        try:

            # import sheet by url
            self.spreadsheet_url = "https://docs.google.com/spreadsheets/d/1MbsnksRWKyt9rmu3eOhL70Zes3eodqFTvj8fn-InP7U/edit?usp=sharing"  # change url for different spreadsheet output
            self.sheet = self.gc.open_by_url(str(self.spreadsheet_url))
            # SpreadsheetHandler.clear_list_data(sheet=1, start="A6", end="Q500")

        except Exception as exception:
            print("could not import sheet!")
            print(exception)

    def update_information(self, account_name, is_running, username):  # updates information tab based on account_name

        sheet = SpreadsheetHandler.switch_worksheet(1)  # switch worksheet

        print("updating information tab...")

        if isinstance(is_running, bool):  # status updater
            # make account row and cell
            row = self.account_database.get(account_name)
            account_cell = "C" + row
            if is_running == True:
                is_running = "(running)"
                # update sheet
                sheet.update_acell(account_cell, is_running)
            if is_running == False:
                is_running = "(not running)"
                # update sheet
                sheet.update_acell(account_cell, is_running)

        if isinstance(username, str):  # username updater
            # make account row and cell
            row = self.account_database.get(account_name)
            account_cell = "D" + row

            # update sheet with username
            sheet.update_acell(account_cell, username)

    def information(self, account_name, is_running):

        sheet = SpreadsheetHandler.switch_worksheet(1)  # switch worksheet

        def add_user(row, sheet):  # adds user count in spreadsheet as user(count)
            print("adding user...")
            self.count_of_users = self.count_of_users + 1
            user = "user" + str(self.count_of_users)
            account_cell = "A" + row
            sheet.update_acell(account_cell, user)  # update sheet

        if isinstance(account_name, str) and isinstance(is_running,
                                                        bool):  # if all variables contain strings execute code.
            print("updating information tab...")

            # if variables contain strings execute code.
            if isinstance(account_name, str):  # update username
                # make account row and cell
                row = str(self.start_row + self.count_of_users)
                account_cell = "B" + row

                # update sheet and update database
                sheet.update_acell(account_cell, account_name)  # update B column w/ accountname
                self.account_database[account_name] = row  # update database with new account_name and account_row

                # add user to row
                add_user(row=row, sheet=sheet)

            if isinstance(is_running, bool):  # update status
                # get account row and cell
                row = self.account_database.get(account_name)
                account_cell = "C" + str(row)
                if is_running == True:
                    is_running = "(running)"
                    # update sheet
                    sheet.update_acell(account_cell, is_running)
                if is_running == False:
                    is_running = "(not running)"
                    # update sheet
                    sheet.update_acell(account_cell, is_running)

        else:
            print("[!] failed to update information tab!")
            print(
                "criteria not met, make sure account_name = string , is_running = true/false ( bool ), username = string")

    def tasking(self, account_name, current_task, next_task, last_successful_task):
        sheet = SpreadsheetHandler.switch_worksheet(1)  # switch worksheet

        print("updating tasking tab...")

        # if variables contain strings execute code.
        if isinstance(current_task, str):  # current task

            row = self.account_database.get(account_name)
            account_cell = "F" + row

            # update sheet and update database
            sheet.update_acell(account_cell, current_task)  # update B column w/ accountname

        if isinstance(next_task, str):  # next task
            # make account row and cell
            row = self.account_database.get(account_name)
            account_cell = "G" + row

            # update sheet
            sheet.update_acell(account_cell, next_task)

        if isinstance(last_successful_task, str):  # last successful task
            # make account row and cell
            row = self.account_database.get(account_name)
            account_cell = "H" + row

            # update sheet with username
            sheet.update_acell(account_cell, last_successful_task)

    def report_error(self, email, error_message):
        SpreadsheetHandler.update_information(account_name=email, is_running=False,
                                              username="[ERROR] " + str(error_message))

class GetSpreadsheetInformation:
    def __init__(self):
        pass

    def fetch_login_list(self, number_of_users):
        sheet = SpreadsheetHandler.switch_worksheet(2)  # switch sheet

        login_list = {}

        # retrieve login list and save as dictionary value.
        username_cell_list = sheet.range('A2:A' + str(number_of_users))  # select range for username list
        password_cell_list = sheet.range('B2:B' + str(number_of_users))  # select range for password list

        # for username add the username and password to the database.
        for cell in range(len(username_cell_list)):
            login_list[username_cell_list[cell].value] = password_cell_list[cell].value

        # return login_list
        return login_list

    def fetch_random_comment(self, comment_range):
        sheet = SpreadsheetHandler.switch_worksheet(4)  # switch sheet

        comments = []

        comment_cell_list = sheet.range('A2:A' + str(comment_range))  # retrieve comments
        for cell in comment_cell_list:
            comments.append(cell.value)

        return random.choice(comments)  # return random comment

    def fetch_posting_information(self, information_type, email,
                                  video_number):  # fetchs posting information based on type and
        sheet = SpreadsheetHandler.switch_worksheet(1)  # get sheet
        SpreadsheetHandler.tasking(account_name=email, current_task="fetching posting information...", next_task=0,
                                   last_successful_task=0)  # update sheet
        cell = SpreadsheetHandler.check_cell_and_return_cell_as_string(sheet=sheet, column="J",
                                                                       email=email)  # find and return cell\

        def find_correct_video_details(cell,
                                       video_number):  # made with the purpose of locating the correct video by the passed through video_number variable.
            print("finding video to return...")
            new_data = cell.splitlines()  # split new lines
            for video in new_data:
                print("checking if " + video + " matches...")
                if video.split(",")[0] == "video (" + str(video_number) + ")":
                    print("found match! " + video)
                    new_data = video

            print(new_data)
            return new_data

        print("finding the correct video details...")
        cell = find_correct_video_details(cell=cell,
                                          video_number=video_number)  # set cell equal to correct video number.

        if information_type.lower() == "all":  # if information type = video_url then execute code.
            try:
                print("returning cell...")
                print(cell.split(","))
                return cell.split(",")
            except Exception as exception:
                print("could not retrieve cell!")
                SpreadsheetHandler.report_error(email=email, error_message=exception)

        if information_type.lower() == "video_directory_path":  # if information type = video_url then execute code.
            try:
                print("printing cell value...")
                video_url = cell.split(",")  # split every ","
                print("video url retrieved: \n" + video_url[1])  # print tags

                return video_url[1]  # return video URL

            except Exception as exception:
                error = str(exception) + "\nFailed to squccessfully retrieve posting data!"
                print(error)
                SpreadsheetHandler.report_error(email=email, error_message=error)  # report error

        if information_type.lower() == "video_number":  # if information type = video_number then execute code.
            try:
                print("printing cell value...")
                video_number = cell.split(",")  # split every ","
                print("video number retrieved: \n" + video_number[0])  # print tags

                return video_number[0]  # return video_number

            except Exception as exception:
                error = str(exception) + "\nFailed to squccessfully retrieve posting data!"
                print(error)
                SpreadsheetHandler.report_error(email=email, error_message=error)  # report error
        SpreadsheetHandler.tasking(account_name=email, current_task=0, next_task=0,
                                   last_successful_task="fetching posting information...")  # update sheet

        if information_type.lower() == "title":  # if information type = video_number then execute code.
            try:
                print("printing cell value...")
                title = cell.split(",")  # split every ","
                print("title retrieved: \n" + title[3])  # print titles

                return title[2]  # return title

            except Exception as exception:
                error = str(exception) + "\nFailed to squccessfully retrieve posting data!"
                print(error)
                SpreadsheetHandler.report_error(email=email, error_message=error)  # report error
        SpreadsheetHandler.tasking(account_name=email, current_task=0, next_task=0,
                                   last_successful_task="fetching posting information...")  # update sheet

        if information_type.lower() == "description":  # if information type = description then execute code.
            try:
                print("printing cell value...")
                description = cell.split(",")  # split every ","
                print("description retrieved: \n" + description[3])  # print descriptions

                return description[3]  # return description

            except Exception as exception:
                error = str(exception) + "\nFailed to squccessfully retrieve posting data!"
                print(error)
                SpreadsheetHandler.report_error(email=email, error_message=error)  # report error
        SpreadsheetHandler.tasking(account_name=email, current_task=0, next_task=0,
                                   last_successful_task="fetching posting information...")  # update sheet

        if information_type.lower() == "tags":  # if information type = tags then execute code.
            try:
                print("printing cell value...")
                tags = cell.split(",")  # split every ","
                tags = tags[3].strip('"').split('""')  # split every '"'

                print("tags retrieved: \n" + str(tags))  # print tags

                return tags  # return tags

            except Exception as exception:
                error = str(exception) + "\nFailed to squccessfully retrieve posting data!"
                print(error)
                SpreadsheetHandler.report_error(email=email, error_message=error)  # report error

        SpreadsheetHandler.tasking(account_name=email, current_task=0, next_task=0,
                                   last_successful_task="fetching posting information...")  # update sheet

    def fetch_last_successful_post(self, email):
        sheet = SpreadsheetHandler.switch_worksheet(1)  # get sheet
        SpreadsheetHandler.tasking(account_name=email, current_task="fetching last successful post...", next_task=0,
                                   last_successful_task=0)  # update sheet

        try:
            print("printing cell value...")
            cell = SpreadsheetHandler.check_cell_and_return_cell_as_string(sheet=sheet, column="K",
                                                                           email=email)  # find and return cell

            return cell  # return

        except Exception as exception:
            error = str(exception) + "\nFailed to squccessfully retrieve last post data!"
            print(error)
            SpreadsheetHandler.report_error(email=email, error_message=error)  # report error

    def fetch_scheduled_comments_on_video(self, email, information_type):
        sheet = SpreadsheetHandler.switch_worksheet(1)  # get sheet
        SpreadsheetHandler.tasking(account_name=email, current_task="fetching scheduled comments on video...",
                                   next_task=0, last_successful_task=0)  # update sheet

        if information_type.lower() == "video_url:":
            try:
                print("printing cell value...")
                cell = SpreadsheetHandler.check_cell_and_return_cell_as_string(sheet=sheet, email=email,
                                                                               column="L", )  # find and return cell
                posting_information = cell.split(",")  # split every ","

                return posting_information  # return

            except Exception as exception:
                error = str(exception) + "\nFailed to squccessfully retrieve scheduled comments on video data!"
                print(error)
                SpreadsheetHandler.report_error(email=email, error_message=error)  # report error


"""
 #methods abandoned. (adds accounts to google chrome account manager. new method now opens new tabs to handle accounts. this method is unsupported). 
 
    #def add_account(self, username, passkey):

        # load account page:
        #loaded_elem = WebDriverWait(browser, 10).until(lambda x: x.find_element_by_xpath("//div[@class='EyVCdb']"))
        #print("loaded account page!")

        #account_icon = browser.find_elements_by_xpath(xpath = "//a[@class='gb_B gb_Da gb_g']")[0]
        #account_icon.click()
        #add_account_button = browser.find_elemen_by_xpath(xpath = "//a[@class='gb_0 gb_5f gb_Se gb_pb']")[0]
        #add_account_button.click() 89

        # load login portal:
        #loaded_elem = WebDriverWait(browser, 10).until(lambda x: x.find_element_by_xpath("//div[@id='view_container']"))
        #print("loaded login portal!")
        #GoogleHandler.login(username="gang@gmail.com", passkey= "gang420")

"""

# start call
SpreadsheetHandler = SpreadsheetHandler()
BrowserHandler = BrowserHandler()
SpreadsheetHandler.import_sheet()
