from codes.user import UserManager
from config import api_id, api_hash


userManage = UserManager(
    api_id=api_id,
    api_hash=api_hash,
    session="989361445010"
)

# userManage.login()
# userManage.sendMessage(username="@mhzarchi", message="Hello")
userManage.getNewMessages()
