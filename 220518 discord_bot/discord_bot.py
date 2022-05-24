# -*- coding: cp949 -*-
import asyncio
import discord
import crawler
import util
from collections import deque


token = "보안적인 이유로 가립니다."
client = discord.Client()
queue = deque()

# 가동 시작했을때 나타내는거
@client.event
async def on_ready():
    print('bot  가동을 시작합니다.')


# 메세지를 보낸게 봇이거나 명령어 형식이 아닌 경우에는 None을 리턴함.
@client.event
async def on_message(message):
    #print(message)
    if message.author.bot and (message.content[0]!="!" or message.content[0]!="#"):
        return None

    queue.append(message.content)
    
    #help
    if message.content == "#help":
        _help = util.print_help()
        msg1 = message.channel
        await msg1.send(_help)

    while queue:
        cmd = queue.popleft()
        prefix = cmd[0] # '#'이냐, '!'이냐에 따라서 다름.

        #소환사 검색 -> '!'로 검색함.
        #제공 기능 : op.gg의 소환사가 검색된 링크를 제공해줍니다. + 티어 + 승률 + 모스트 챔피언
        if prefix == "!":
            user_name = cmd[1:]
            info = crawler.search_user(user_name)
            info = util.print_user_info(info)
            user_info = message.channel
            await user_info.send(info)

        if prefix == "#":
            if cmd[1:] != "help":    
                info = crawler.search_champ(cmd)
                info = util.print_champ_info(info)
                champ_info = message.channel
                await champ_info.send(info)

if __name__ == "__main__":
    client.run(token)
