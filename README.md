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
To schedule **cronjob like tasks**, matrix-personal-bot uses **croniter**, which
is a python module to provide iteration for datetime object.
Get it from https://github.com/taichino/croniter
