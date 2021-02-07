# matrix-personal-bot
A Matrix messenger bot designed to run as daemon with logging and signal handling

* Auto-join of rooms and auto-leave when room is empty.
* Receive and parse commands.
* Can send images and files to rooms.
* Can execute scheduled actions using cronjob syntax.
* Signal handling.
* Can run in background or foreground.
* Logging to stdout (if running in foreground) or file (if running in background).
* Wants to be robust in exception handling.
* Reading configuration file from a JSON file.

## croniter

To schedule **cronjob like tasks**, matrix-personal-bot uses 
**croniter**, which is a python module to provide iteration for 
datetime object. Get it from 
[github.com/taichino/croniter](https://github.com/taichino/croniter).

## Session handling

The matrix-personal-bot **does not handle encryption** at the 
moment. Due this semplifcation we can skip entirely the use of 
**storage classes** which are used to store encryption devices, 
encryption keys and the trust state of devices.

To keep the code as simple as possible, the bot does not save 
the **access\_token** granted by the homeserver after the 
`client.login()`. So the bot does a full login using **user**, 
**device\_id** and **password** on each run. The program also 
assumes to be the only running instance of the bot; on program 
exit it does a `client.logout(all_devices=True)`. If you intend 
to run different instances of this bot, it is advised to use 
different **BOT\_DEVICEID** in configuration file for each 
instance, and you must set `client.logout(all\_devices=False)`.
