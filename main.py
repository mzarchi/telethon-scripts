from codes.user import UserManager
from config import api_id, api_hash


userManage = UserManager(
    api_id=api_id,
    api_hash=api_hash,
    session="989361445010"
)

"""
    For run this program you should login
    to your telegram account first and this 
    code create session file in main dir
"""
# userManage.login()
userManage.getContactsList()
