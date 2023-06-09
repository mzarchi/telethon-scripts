import sys
import telethon

from telethon import functions
from telethon.sync import TelegramClient, events
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

    def sendMessage(self, username: str = "@mhzarchi", message: str = "Hello from GitHub :)"):
        """Send message to another user
        ~~~~~~~~~~~~~~~~~~~~~
        Args:
            :param `username`: (str) telegram username like @mhzarchi
            :param `message`: (str) message text like Hello

        Returns:
            :return: (class) telethon.tl.patched.Message
        """

        client = TelegramClient(self.__session, self.__api_id, self.__api_hash)
        client.start()

        return client.send_message(
            entity=client.get_entity(username),
            message=message
        )

    def getNewMessages(self):
        """Get new message
        ~~~~~~~~~~~~~~~~~~~~~
        If you want to get all new
        message like channel or group
        remove try/except block and print event
        """

        with TelegramClient(self.__session, self.__api_id, self.__api_hash) as client:
            print("Start ..")

            @client.on(events.NewMessage(pattern="(?i).*"))
            async def handler(event):
                try:
                    msg = "New Message! \n"
                    msg += f"ChatId: {event.peer_id.user_id} \n"
                    msg += f"Text: {event.message.message} \n"
                    print(msg)
                except:
                    print("Chat is not contact!")

            client.run_until_disconnected()

    def getUserData(self, username: str):
        """Send message to another user
        ~~~~~~~~~~~~~~~~~~~~~
        Args:
            :param `username`: (str) telegram username like @mhzarchi
        """
        with TelegramClient(self.__session, self.__api_id, self.__api_hash) as client:
            username = str(input("Insert @username or exit: "))
            entity = client.get_entity(username)
            msg = f"ChatId: {entity.id}"
            print(msg)

    def getContactsList(self):
        with TelegramClient(self.__session, self.__api_id, self.__api_hash) as client:
            contacts = client(functions.contacts.GetContactsRequest(hash=0))
            for contact in contacts.users:
                txt = f"Id: {contact.id}, Mutual: {contact.mutual_contact}, Number: {contact.phone}, Name: {contact.first_name} {contact.last_name}"
                print(txt)
