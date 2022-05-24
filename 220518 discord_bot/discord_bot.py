# -*- coding: cp949 -*-
import asyncio
import discord
import crawler
import util
from collections import deque


token = "�������� ������ �����ϴ�."
client = discord.Client()
queue = deque()

# ���� ���������� ��Ÿ���°�
@client.event
async def on_ready():
    print('bot  ������ �����մϴ�.')


# �޼����� ������ ���̰ų� ��ɾ� ������ �ƴ� ��쿡�� None�� ������.
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
        prefix = cmd[0] # '#'�̳�, '!'�̳Ŀ� ���� �ٸ�.

        #��ȯ�� �˻� -> '!'�� �˻���.
        #���� ��� : op.gg�� ��ȯ�簡 �˻��� ��ũ�� �������ݴϴ�. + Ƽ�� + �·� + ��Ʈ è�Ǿ�
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
