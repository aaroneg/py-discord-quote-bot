# py-discord-quote-bot

## Discord pre-reqs

1. Create an application - https://discord.com/developers/applications
1. On your new application's **General Information** tab, assign an icon, name, etc
1. On the **OAuth2** tab, select the `bot` scope, then scroll down and select at minimum read message history & send messages permissions.
1. Scroll up and copy the URL generated by the developer portal.
1. Open a new tab and paste the URL, which will allow you to add the bot to any server where you have appropriate permissions.
1. On the **Bot** tab, copy the token.

## Hosting system setup

Install Pipenv on your system, then:

```bash
pipenv install
pipenv shell
# Have the bot token copied so you can paste it for save_key.py
python ./save_key.py
python ./init.py
```
You'll want to create quotes.txt, with one quote per line.

You can run it in a `screen` session, or go to the effort of making a systemd unit for it.

## Bot Commands

There's only one command - `!quote`. If you put that anywhere the bot can read the command and send the message, you should be good to go.
