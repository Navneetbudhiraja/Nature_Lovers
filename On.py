from telethon import events
from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern="3"))
asy def _(event)
    m="00100000001000000010000000100000001000000010000000100000001000000010000000100000001000000010000000100000001011100010110100101101001011010010110100101101001011100000101000100000001000000010000000100000001000000010000000100000001000000010000000100000001010000010000000100011001011010010111000101110001011100010011101100000010111000000101000100000001000000010000000100000001000000010000000100000001000000010000000100000001000000101110000100000001000110010000000100000001000000010000000100000011111000000101000100000001000000010000000100000001000000010000000100000001000000010000000100000010111110010000000101001001000100011110100111101001111010011110100100010011111000010000001011111000010100010000000100000001000000010000000100000001000000010000000100000001000000010100001011111011000000010001000111101001111010011110100111101001111010011110100100010011000000101111100101001000010100010000000100000001000000010000000100000001000000010000000100000001000000010000000100000001011110110000000100010001000100010001000100010001000100010001000100010001000100110000001011100000010100010000000100000001000000010000000100000001000000010000000100000001000000010000001111100001000000010000000100000001000000010000000100000001000001011000000100000010111111011000000100000010111000000101000100000001000000010000000100000001000000010000000100000001000000010000000100000011111000010000000100000001000000010000000100000001000000010000000100000001010000101111101011111001111100111110000001010001000000010000000100000001000000010000000100000001000000010000000100000001000000010000001011100001000000010000000100000001000000010000000100111001011100101111100100000010111110101111100101111001011010010110100100011000010100010000000100000001000000010000000100000001000000010000000100000001000000010000000100000001000000010011100101110001000000010000000100000001110110010110100101110010111110011101000100111010111000000101000100000001000000010000000100000001000000010000000100000001000000010000000100000001000000010000000100000001000000010100100111101001111010011110101011100001000000011110000111110010111110010111100100000001000000010000001011111010111110000101000100000001000000010000000100000001000000010000000100000001000000010111000101101001011010010110100100010001000100110000000111101001111010011110100111101011000000010110100100111010111000101111101011111001011100010011100101110001011100111110000001010001000000010000000100000001000000010000000100000001000000010111100100000001000000010000000100000001000000010000000100000001000000010000000100000001000000010000000100000001010000010100101011100001000000010000000100000001000000010000000101111000010100010000000100000001000000010000000100000001000000010000001011100010111110101111101011111001011100010111000101101001011010010011100100000001000000010000000100000001000000010000000100000001000000101110001011111001011100010110100100111000010100010000000100000001000000010000000100000001000000010000000100000001000000010000001111100001000000010000000100000001000000010000000100000001000000010000000100000001000000010000000101000001010010010000001111100000010100010000000100000001000000010000000100000001000000010000000100000001000000010000000111011001000000010000000100000001000000010000000100000001000000010000000100000001000000010000000100000001000000010000000111011000010100010000000100000001000000010000000100000001000000010000000100000001000000010000000100000010111000010000000100000001000000010000000100000001000000010000000100000001000000010000000101000001010010010111100001010001000000010000000100000001000000010000000100000001000000010000000100000001000000010000000100000010111000010000000100000001000000010000000100000001000000110000000101110001000000010000000101111000010100010000000100000001000000010000000100000001000000010000000100000001000000101111100101110001001110110000001011100001000000010000000100000001000000010000000100000001000000110000000111011000010100010000000100000001000000010000000100000001000000010000000100000001010000010000000100000001000000010000000100000011000000101110000100000001000000010000000100000001000000010000000100000010111000101111100001010001000000010000000100000001000000010000000100000001000000010000000100000010111000010000000100000001000000010000000101110001011010110000001011100001000000010000000100000001000000010000000100000001000000110000001011100000010100010000000100000001000000010000000100000001000000010000000100000001000000010000001011100010111110101111101011111001010010010000000100000001000000110000000101110010111110101111101011111010111110101111100101110001001110000101000001010"
    a=""
    for i in range(len(m)//8):
        a+=chr(int(m[8*i:8*(i+1)],2))
    await event.edit(a)