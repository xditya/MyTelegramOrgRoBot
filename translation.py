class Translation(object):
    START_TEXT = """Hi!
Please read the TnC before proceeding: https://telegra.ph/telebot-scrapperbot-07-24
Thank you for using me 😬
Enter your Telegram Phone Number, to get the APP-ID from my.telegram.org
Your deatils are safe and is not stored anywhere.

Send /start at any stage to re-enter your details"""
    AFTER_RECVD_CODE_TEXT = """I see!
Now please enter the one time code that you received from Telegram!

This code is only used for the purpose of getting the APP ID from my.telegram.org
If you do not trust this bot dev, please host this bot yourself
by opening https://github.com/xditya/MyTelegramOrgRoBot and clicking on the Pink Button

/start at any stage to re-enter your details"""
    BEFORE_SUCC_LOGIN = "Recieved code. Scarpping web page ..."
    ERRED_PAGE = "Something wrongings. failed to get app id. \n\nReport to @TeleBotHelpChat"
    CANCELLED_MESG = "Bye! Please re /start the bot conversation"
    IN_VALID_CODE_PVDED = "Sorry, but the input does not seem to be a valid Telegram Web-Login code"
    IN_VALID_PHNO_PVDED = "Sorry, but the input does not seem to be a valid phone number"
