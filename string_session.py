from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print("")
print("""Welcome To LuciferUserBot String Session\nGenerator By @Murat_30_God\n\n""")
print("""Enter Your Valid Details To Continue!\n\n """)

API_KEY = input("API_ID:  ")
API_HASH = input("API_HASH:  ")

while True:
    try:
        with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
            print(
                "String Session Sucessfully Sent To Your Saved Message, Store It To A Safe Place!!\n\n "
            )
            print("")
            session = client.session.save()
            client.send_message(
                "me",
                f"Here is your TELEGRAM STRING SESSION\n(Tap to copy it)ðŸ‘‡ \n\n `{session}` \n\n And Visit @LUCIFER_SUPPORT_GROUP For Any Help!\n\n",
            )

            print(
                "Thanks for Choosing Lucifer UserBotHave A Good Time....Note That When You Terminate the Old Session ComeBack And Genrate A New String Session Old One Wont Work"
            )
    except:
        print("")
        print(
            "Wrong phone number \n make sure its with correct country code. Example : +918925534834! Kindly Retry"
        )
        print("")
        continue
    break
