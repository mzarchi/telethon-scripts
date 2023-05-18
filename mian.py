from codes.login import UserManager
from config import api_id, api_hash


userManage = UserManager(api_id=api_id, api_hash=api_hash)
userManage.login()