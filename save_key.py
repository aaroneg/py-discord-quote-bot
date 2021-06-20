#!/usr/bin/env python3
import keyring
import getpass

service_id='QUOTE_BOT'
token=getpass.getpass(prompt='Token: ', stream=None)
keyring.set_password(service_id, service_id, token)
