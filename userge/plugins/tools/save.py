#New Update Soon😅
from userge import Config,userge

@userge.on_message(filters.command("save",[Config.CMD_TRIGGER,Config.SUDO_TRIGGER]))
async def savemsg(userge, message):
    await userge.forward_messages("me",message.chat.id,message.reply_to_message.message_id)
