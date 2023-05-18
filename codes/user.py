import sys
import telethon

from telethon.sync import TelegramClient
from .utils import ValidatePhone, LOGIN_MESSAGE


class UserManager:
    """
    """

    __api_hash = None
    __api_id = None
    __session = None

    def __init__(self, api_id, api_hash, session):
        self.__api_hash = api_hash
        self.__api_id = api_id
        self.__session = session

    def login(self):
        """
        this method login user to telegram
        """
        print(LOGIN_MESSAGE)
        PhoneNumber = input("\nEnter a Phone number: ")
        if not ValidatePhone(PhoneNumber):
            sys.exit(
                "[x] Phone number is not valid, please enter a valid phone number ...")

        client = TelegramClient(self.__session, self.__api_id, self.__api_hash)
        client.connect()
        client.send_code_request(PhoneNumber, force_sms=False)
        value = input("Enter Login Code: ")
        try:
            client.sign_in(PhoneNumber, code=value)
        except telethon.errors.SessionPasswordNeededError:
            password = input("Enter Your 2-Step Code: ")
            client.sign_in(password=password)
        print("Successfully Connect!\nSession created at sessions dir")

    def sendMessage(self, username: str, message: str):

        client = TelegramClient(self.__session, self.__api_id, self.__api_hash)
        client.start()

        client.send_message(
            entity=client.get_entity(username),
            message=message
        )