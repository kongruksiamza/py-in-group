from fbchat import Client
from fbchat.models import *

client=Client('email','password') # ลงชื่อเข้าใช้งาน facebook

friend_id=""
group_id=""
client.send(Message(text="สวัสดีเพื่อนๆเราคือบอทนะ"),thread_id=group_id,thread_type=ThreadType.GROUP)
client.send(Message(emoji_size=EmojiSize.LARGE),thread_id=group_id,thread_type=ThreadType.GROUP)
client.logout()