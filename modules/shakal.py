# Coded by Stunni & D4n1l3k300
# t.me/D4n13l3k00
# t.me/askorblnka
from .. import loader, utils
import os, string, random
@loader.tds
class VSHAKALMod(loader.Module):
  strings = {"name": "Shakal"}
  @loader.owner
  async def shakalcmd(self, m):
	  ".shakal <реплай на видео>\
	  \nСшакалить видео Спасибо @D4n13l3k00 за ориг соурс"
	  reply = await m.get_reply_message()
	  if not reply: return await m.edit("дай видео на реплай...")
	  if reply.file.mime_type.split("/")[0]=="video":
	    args = utils.get_args_raw(m)
	    if args:
	      if args in lvls:
	        lvl = lvls[args]
	      else:
	        await message.edit("не знаю такого")
	        return
	    else:
	      lvl = lvls["3"]
	    vid = await reply.download_media("".join([random.choice(string.ascii_letters) for i in range(25)])+".mp4")
	    out = "".join([random.choice(string.ascii_letters) for i in range(25)])+".3gp"
	    await m.edit("[Шакал] Шакалю...")
	    os.system(f"ffmpeg -y -i \"{vid}\" -b 300k -s 320x240 -vcodec mpeg4 -ac 2 -ab 16k -acodec aac \"{out}\"")
	    await reply.reply(file=out)
	    await m.delete()
	    os.remove(vid)
	    os.remove(out)
	  else:
	    await m.edit("shit...")
	    return
