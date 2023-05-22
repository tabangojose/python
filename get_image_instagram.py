
import instaloader

instance = instaloader.Instaloader()

user_name = 'tabangojose_dev'
instance.download_profile(user_name, profile_pic_only=True)
instance.download_profile()


