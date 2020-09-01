
# All in one code.

"""Available Commands:
.tlol
.lol
.heart
.candy
.nothappy"""

from telethon import events
import asyncio
from collections import deque
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern=r"candy"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("馃崷馃崸馃崺馃崻馃巶馃嵃馃馃崼馃崿馃嵀"))
	for _ in range(999):
		await asyncio.sleep(1)
		await event.edit("".join(deq))
		deq.rotate(1)

@borg.on(admin_cmd(pattern=r"nothappy"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("馃榿鈽癸笍馃榿鈽癸笍馃榿鈽癸笍馃榿"))
	for _ in range(999):
		await asyncio.sleep(1)
		await event.edit("".join(deq))
		deq.rotate(1)

@borg.on(admin_cmd(pattern=r"heart"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("鉂わ笍馃А馃挍馃挌馃挋馃挏馃枻"))
	for _ in range(999):
		await asyncio.sleep(1)
		await event.edit("".join(deq))
		deq.rotate(1)

@borg.on(admin_cmd(pattern=r"tlol"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("馃馃馃え馃馃馃え"))
	for _ in range(999):
		await asyncio.sleep(1)
		await event.edit("".join(deq))
		deq.rotate(1)

@borg.on(admin_cmd(pattern=r"lol"))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("馃槀馃ぃ馃槀馃ぃ馃槀馃ぃ"))
	for _ in range(999):
		await asyncio.sleep(1)
		await event.edit("".join(deq))
		deq.rotate(1)
