# requires: pycoingecko
from .. import loader, utils  # pylint: disable=relative-beyond-top-level
import logging
from pycoingecko import CoinGeckoAPI
import io

logger = logging.getLogger(__name__)
cg = CoinGeckoAPI()
@loader.tds
class bitcoincheckMod(loader.Module):
	"""Uploader"""
	strings = {
		"name": "bitcoin checker"
	}

	async def client_ready(self, client, db):
		self.client = client
	
	
	@loader.sudo
	async def btccmd(self, message):
		
		await message.edit(str(cg.get_price(ids='bitcoin', vs_currencies='usd')['bitcoin']['usd']) + "$")
	
