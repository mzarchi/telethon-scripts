import telethon
import config as cf

from telethon.sync import TelegramClient

phone = input("Insert Your Phone: ")
name = phone
client = TelegramClient(
    f'{name.replace("+", "")}', cf.api_id, cf.api_hash)
client.connect()
client.send_code_request(phone, force_sms=False)
value = input("Insert Login Code: ")
try:
    client.sign_in(phone, code=value)
except telethon.errors.SessionPasswordNeededError:
    password = input("Insert Your 2-Step Code: ")
    client.sign_in(password=password)
print("Successfully Connect!\nSession created at sessions dir")
