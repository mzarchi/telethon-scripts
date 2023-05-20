<p>
<img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/mzarchi/telethon-scripts">
<img alt="GitHub contributors" src="https://img.shields.io/github/contributors/mzarchi/telethon-scripts">
</p>

# Telethon Scripts

* Clone repo by ```git clone https://github.com/mzarchi/telethon-scripts.git```
* Install require libs by ```pip install -r requirements.txt```

* Copy .env.example to .env (`` `cp .env.example .env` ``) and put your <b>api_id</b> and <b>api_hash</b>

    > <sub>At this step, you must get **api_id** and **api_hash** from [Telegram Apps](https://my.telegram.org/auth?to=apps)</sub>

## Contributors tasks:

* [x] Login to telegram with 2FA ([login](https://github.com/mzarchi/telethon-scripts/blob/main/codes/user.py#L21))
* [x] Send Message to another user ([sendMessage](https://github.com/mzarchi/telethon-scripts/blob/main/codes/user.py#L42))
* [x] Get new messages ([getNewMessages](https://github.com/mzarchi/telethon-scripts/blob/main/codes/user.py#L61))
* [x] Get user data by username ([getUserData](https://github.com/mzarchi/telethon-scripts/blob/main/codes/user.py#L84))
* [x] Get all user contacts ([getContactsList](https://github.com/mzarchi/telethon-scripts/blob/main/codes/user.py#L97))
* [ ] Get all user channels
* [ ] Get channel all posts
* [ ] Get all user groups
