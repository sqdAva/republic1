from pypresence import Presence
from time import time

RPC = Presence("839139415774986270")
btns = [
	{
		"label": "Что?",
		"url": "https://google.com"
	},
	{
		"label": "А?",
		"url": "https://yandex.su"
	}
]

RPC.connect()
RPC.update(
	state="Why?",
	details="What?",
	buttons=btns,
	large_image="1",
	small_image="2",
	large_text="┐(‘～ )┌",
	small_text="╮( ˘ ､ ˘ )╭"
)

input()