##########
# Imports
##########
from moviepy.editor import *
import mutagen
from mutagen.mp3 import MP3


#####
# Classes:
#####
class VideoGenerator: # generate videos
    def __init__(self):
        pass

    def import_audio_clip(self, audio_file_path): # function built for the purpose of importing an audio clip into movie.py

        ###
        # Import audio clip:
        ###
        print("now importing audio clip...")

        # import audio clip and return it for later use.
        try:
            audio_clip = AudioFileClip(str(audio_file_path))

            # get audio duration:
            try:
                audio = MP3(audio_clip)
                audio_info = audio.info
                duration = int(audio_info.length)
                print(duration)
            except Exception as exception:
                print("failed to import audio clip!\n" + str(exception))

        except Exception as exception:
            print("failed to import audio clip!\n" + str(exception))

        # return for later use.
        return audio_clip, duration

    def import_image_clip(self, image_file_path): # function built for the purpose of importing an audio clip into movie.py

        ###
        # Import image clip:
        ###
        print("now importing audio clip...")

        # add video clip
        try:
            video_clip = ImageClip(image_file_path)
        except Exception as exception:
            print("failed to grab image clip!\n" + str(exception))

        # return for later use.
        return video_clip

    def import_logo_image_clip(self, logo_image_file_path): # function built for the purpose of importing an audio clip into movie.py

        ###
        # Import logo image clip:
        ###
        print("now importing audio clip...")

        # import logo image
        try:
            video_clip = ImageClip(logo_image_file_path)
        except Exception as exception:
            print("failed to grab image clip!\n" + str(exception))

        # return for later use.
        return video_clip

    def import_intro_clip(self, intro_file_path): # function built for the purpose of importing an audio clip into movie.py

        ###
        # Import logo image clip:
        ###
        print("now importing intro clip...")

        # import logo image
        try:
            video_clip = VideoFileClip(str(intro_file_path))
        except Exception as exception:
            print("failed to grab intro clip!\n" + str(exception))

        # return for later use.
        return video_clip


    def attach_photo_to_audio_clip(self, audio_clip, central_image_clip, logo_image_clip, intro_clip):

        ###
        # Attach photo to audio clip:
        ###
        print("now attaching photo to audio clip...")

        # grab audio file duration.
        print(type(audio_clip))
        try:
            audio_duration = audio_clip.duration()
            print(audio_duration)
        except Exception as exception:
            print("failed to grab duration of audio clip!\n" + str(exception))


        # edit video - add logo, add image, add audio
        try:
            # set duration of video to audio clip length.
            central_image_clip.set_duration(video_duration)
            central_image_clip.set_audio(audioclip=audio_clip)

            # set logo equal to logo_image_clip on the bottom left of the video file.
            logo = (logo_image_clip
                    .set_duration(video_duration)
                    .resize(height=50)  # if you need to resize...
                    .margin(right=8, top=8, opacity=0)  # (optional) logo-border padding
                    .set_pos(("left", "bottom")))

            composite_video = CompositeVideoClip([central_image_clip, logo, intro_clip]).set_audio(audio_clip)  # combine video

            return composite_video

        except Exception as exception:
            print("failed to edit video - add logo, add image, add audio!\n" + str(exception))

    def render_video(self, composite_video, video_name): # function built for the purpose of importing an audio clip into movie.py

        ###
        # Render composite file.
        ###
        print("now exporting composite file...")

        # import logo image
        try:
            composite_video.write_videofile(video_name)
        except Exception as exception:
            print("failed to export composite clip!\n" + str(exception))

