from .. import loader, utils  # pylint: disable=relative-beyond-top-level
import logging
import requests
import io
import os
import time

logger = logging.getLogger(__name__)

@loader.tds
class ertertertMod(loader.Module):
	"""rand dog"""
	strings = {
		"name": "randomdog"
	}

	async def client_ready(self, client, db):
		self.client = client
	
	
	@loader.sudo
	async def dogcmd(self, message):
		url = "http://sergatvsite.000webhostapp.com/api/dog/"
		r = requests.get(requests.get(url).json()['message']).content
		catName = 'dog.png'
		open(catName, 'wb').write(r)
		await message.reply(file=catName)
		os.remove(catName)
	
