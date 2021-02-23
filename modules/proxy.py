from .. import loader, utils  # pylint: disable=relative-beyond-top-level
import logging
import requests
import io
import os
import time

logger = logging.getLogger(__name__)

@loader.tds
class ertertertMod(loader.Module):
	"""Uploader"""
	strings = {
		"name": "ertertertr"
	}

	async def client_ready(self, client, db):
		self.client = client
	
	
	@loader.sudo
	async def proxycmd(self, message):
		url = "https://sergatvsite.000webhostapp.com/api/proxy"
		r = requests.post(url, allow_redirects=True)
		proxyName = 'proxies.txt'
		open(proxyName, 'wb').write(r.content)
		await message.reply(file=proxyName)
		os.remove(proxyName)
	