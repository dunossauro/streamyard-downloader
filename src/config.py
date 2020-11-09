from decouple import config
from datetime import datetime

TOKEN_URL = "https://streamyard.com/login"
CODE_URL = "https://streamyard.com/api/user/login"
LOGIN_URL = "https://streamyard.com/api/user/otp_token"
CREATE_DOWNLOADS_URL = "https://streamyard.com/api/broadcasts/{stream_id}/vod"
DOWNLOAD_URL = "https://streamyard.com/api/broadcasts/{stream_id}/vod_download_urls"
LIST_PAST_URL = "https://streamyard.com/api/broadcasts?limit=99&isComplete=true"

EMAIL = config("EMAIL")
LOCAL_DOWNLOAD_PATH = config("LOCAL_DOWNLOAD_PATH")
CHUNK_SIZE= int(config("CHUNK_SIZE"))
MAX_THREADS = config("MAX_THREADS")
FILTER_DATE = datetime.strptime(config("FILTER_DATE"), '%Y-%m-%d').date()