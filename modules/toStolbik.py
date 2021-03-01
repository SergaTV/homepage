from PIL import Image, ImageDraw
import io
import asyncio
import logging

from .. import loader, utils

logger = logging.getLogger(__name__)

class DotifyMod(loader.Module):
	"""lol"""
	strings = {"name": "[PRIVATE]stolbik"}

	@loader.unrestricted
	async def stolbcmd(self, message):
		"""text to stolb"""
		arrgs = utils.get_args_raw(message)
		x = 1
		temp=''
		slov = arrgs
		for letter in slov:
		  if x == 1:
		    temp = temp+letter.lower()
		    x=0
		  else:
		    temp = temp+letter.upper()
		    x=1
		await message.edit(temp)