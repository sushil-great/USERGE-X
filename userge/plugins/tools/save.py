#New Update Soon😅
from userge import Config, Message, userge

@userge.on_cmd(
    "save", about={"header": "Save message"}, allow_channels=True
)
async def savemsg(message: Message):
    await userge.forward_messages("me",message.chat.id,message.reply_to_message.message_id)
