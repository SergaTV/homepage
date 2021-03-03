
from .. import loader
from random import choice as allahbabah


def register(cb):
	cb(btcbankerMod())

class btcbankerMod(loader.Module):
	"""Использует @btcprices."""
	strings = {'name': 'Btc Price'}

	async def btccmd(self, event):
		'''Выводит стоимость биткоина'''
		while True:
			a=allahbabah(await event.client.get_messages('btcprices',1))
			if not a.entities:
				await event.edit(f'<b>{a.text}</b>')
				break 
			else:
				pass


		