import youtubebot
from youtubebot import start_api
import time
from random import randint

# load in libraries:
GoogleHandler = youtubebot.GoogleHandler()
YouTubeToolKit = youtubebot.YouTubeToolKit()
GetSpreadsheetInformation = youtubebot.GetSpreadsheetInformation()

# import spreadsheet for use, (at least 4 worksheets made in spreadsheet) ## ABANDONED
#SpreadsheetHandler.spreadsheet_url = "link here"
#SpreadsheetHandler.import_sheet() # by default uses spreadsheet for ItsLitRecords

# start api call
youtubebot.browser = start_api(firefox=True, chrome=False, proxy=False, user_agent=True, recache=False)


# login information & variables
google_email = "imitremc@gmail.com"
google_password = "H8$$66recar1"
keyword = "type beat"

''' I was trying todo a multi instantation of "browser" -- the browser now needs to be passed to >GoogleHandler<
youtubebot.browser2 = start_api(firefox=False, chrome=True, proxy=False, user_agent=True, recache=False)
youtubebot.browser3 = start_api(firefox=False, chrome=True, proxy=False, user_agent=True, recache=False)

# add views to counter:
YouTubeToolKit.open_youtube()

# search youtube
YouTubeToolKit.open_video_url(google_email, video_url="https://www.youtube.com/watch?v=e4JpJ6OnKYg&ab_channel=CarsonRhodes")
YouTubeToolKit.add_view(google_email, 30)

'''


# script to go and comment:
variable = False
intial_sleep_value = randint(86400, 89400)

while variable == False:
    # login
    GoogleHandler.login(google_email, google_password)

    time.sleep(100)

    #tags = YouTubeToolKit.steal_tag_data(email="imitremc@gmail.com", video_url="https://www.youtube.com/watch?v=yY7iGa4t9-I")
    #print(tags)

    # switch youtube account to CloutMusic
    YouTubeToolKit.open_youtube()
    GoogleHandler.youtube_account_switcher(google_email, accountname="Dyl")

    # search youtube and post comments for type beats.
    YouTubeToolKit.open_youtube()
    YouTubeToolKit.search_youtube(google_email, keyword, filter_by_date_today=True)


    # open a youtube page and comment on videos.
    tries = 0
    skipComment = False
    for number in range(10):
        tries = tries + 1
        print(tries)
        YouTubeToolKit.open_youtube_video_from_search_page(google_email, number + 1)
        YouTubeToolKit.wait(2)

        subscribed = YouTubeToolKit.check_if_subscribed(google_email)
        comment = YouTubeToolKit.find_and_select_comment(google_email, comment_text="None", commenter_name="Ryan Samani Beats")
        time.sleep(5)
        print("check this comment: " + str(comment))

        if subscribed != True:
            YouTubeToolKit.subscribe_on_video_page(google_email)

        if str(comment) == "None":
            print("Adding comment to this video...")
            YouTubeToolKit.like_video(google_email)
            YouTubeToolKit.comment_on_video(google_email, comment=GetSpreadsheetInformation.fetch_random_comment(13))

            YouTubeToolKit.wait(1)
            print("Navigating back...")
            YouTubeToolKit.navigate_back()
            YouTubeToolKit.wait(3)

        try:
            if True in comment:
                print("found comment!")
                skipComment = True
                YouTubeToolKit.navigate_back()
                YouTubeToolKit.wait(1)
        except:
            continue

        if skipComment != True:
            print("unable to find comment now proceeding to add on.")
            YouTubeToolKit.comment_on_video(google_email, GetSpreadsheetInformation.fetch_random_comment(13))
            YouTubeToolKit.like_video(google_email)

            YouTubeToolKit.wait(1)
            print("Navigating back...")
            YouTubeToolKit.navigate_back()
            YouTubeToolKit.wait(3)

    # Sleep for one day
    print("completed action @: " + str(time.localtime()))
    sleep_time = 86400 + abs(intial_sleep_value - randint(86400, 89400))
    print("waiting : " + str(sleep_time))
    time.sleep(sleep_time)

#video_details = GetSpreadsheetInformation.fetch_posting_information(email="imitremc@gmail.com", information_type="all", video_number=1)
#YouTubeToolKit.upload_video(email="imitremc@gmail.com", video_file_directory="/videos/video1cloutmusic.m4v", video_details=video_details, use_classic_uploader=False)
#GoogleHandler.youtube_account_create("imitremc@gmail.com","gang")
#YouTubeToolKit.open_video_url(email="imitremc@gmail.com", video_url="https://www.youtube.com/watch?v=Jz7Zk_04Ok0")
#GoogleHandler.youtube_account_switcher(email="imitremc@gmail.com", accountname="CloutMusic")
#video_details = GetSpreadsheetInformation.fetch_posting_information(email="imitremc@gmail.com", information_type="all", video_number=2)
#YouTubeToolKit.upload_video(email="imitremc@gmail.com", video_file_directory="/videos/lil uzi vert x lil tecca type beat.m4v", video_details=video_details, use_classic_uploader=False)

'''
# please login on all accounts before using YouTubeToolKit. 
GoogleHandler.login(email="imitremc@gmail.com", password="H8$$66recar")
GoogleHandler.login(email="derejcar@gmail.com", password="H8$$66recar")

print("opening video tab") 
YouTubeToolKit.open_video_url(email= "imitremc@gmail.com", video_url = "https://www.youtube.com/watch?v=aKKDBxGUY44")
print("switching youtube accounts")
GoogleHandler.youtube_account_switcher(email="imitremc@gmail.com", accountname="CloutMusic")
# YouTubeToolKit functionality.
print("commenting on video")
YouTubeToolKit.comment_on_video(email="imitremc@gmail.com", comment=GetSpreadsheetInformation.fetch_random_comment(10))
print("liking video")
YouTubeToolKit.like_video(email="imitremc@gmail.com")

# "selection" of comments, making it easy to perform actions on them
print("selecting comment")
selected_comment = YouTubeToolKit.find_and_select_comment(email="imitremc@gmail.com", comment_text="Let’s GO Dyl!! This video is fly my guy!! Mr.IndependentMan from RC comin through again!! Stay up!!", commenter_name="Tristen Waters")
print("liking comment")
YouTubeToolKit.like_comment(email="imitremc@gmail.com", selected_comment=selected_comment)
print("replying to comment")
YouTubeToolKit.reply_to_comment(email="imitremc@gmail.com", selected_comment=selected_comment, comment_text="hello")
'''
