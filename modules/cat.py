from .. import loader, utils  # pylint: disable=relative-beyond-top-level
import logging
import requests
import io
import os
import time

logger = logging.getLogger(__name__)

@loader.tds
class ertertertMod(loader.Module):
	"""rand cat"""
	strings = {
		"name": "randomcat"
	}

	async def client_ready(self, client, db):
		self.client = client
	
	
	@loader.sudo
	async def catcmd(self, message):
		url = "http://sergatvsite.000webhostapp.com/api/cat/"
		r = requests.get(url, allow_redirects=True)
		catName = 'cat.png'
		open(catName, 'wb').write(r.content)
		await message.reply(file=catName)
		os.remove(catName)
	
