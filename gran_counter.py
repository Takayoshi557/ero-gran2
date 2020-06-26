# インストールした discord.py を読み込む
import asyncio
import time
import discord
from discord.ext import commands
from datetime import datetime as dt
from datetime import timedelta
import csv

# 自分のBotのアクセストークンに置き換えてください
TOKEN = DISCORD_BOT_TOKEN

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='!', description=description)



# 接続に必要なオブジェクトを生成
client = discord.Client()


# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')


# お試しリマインダ
# def isdecimal():
#    pass


@client.event
async def on_raw_reaction_add(payload):
#async def on_raw_reaction_add(reaction, user):
    with open('gran_log.txt', 'a', newline='') as f:
        channel = client.get_channel(722253361159864479)
        now = dt.now()
        now1 = str(now)
#        writer = csv.writer(f)
#        reac_m = str(reaction.message)
        f.write("Date&Time:\r\n"+now1+"\r\n")
#        f.write("reaction has been added"+"\r\n")
#        reac_reac = reaction
#       f.write(str(reac_reac))
        f.write("message channel & id\r\n")
#    print(reaction.message)
        f.write(str(payload.channel_id)+"\r\n")
#        f.write(str(reaction.message.channel.id)+"\r\n")
#        f.write(reac_m+"\r\n")
#    print("message-author")
#    print(reaction.message.author.id)
        f.write("reaction-user-id\r\n")
        f.write(str(payload.user_id)+"\r\n\r\n")
#    await message.channel.send('reac_m')
    #    await reaction.channel.send(reaction.message)
        await channel.send('Date&Time:\n'+now1+'\nmessage channel & id\n'+str(payload.channel_id)+'\nreaction-user-id\r\n'+str(payload.user_id)+'\n_')

 #       lot_result_channel = [channel for channel in client.get_all_channels() if channel.id == lot_result_channel_id][0]
#        await client.send_message(lot_result_channel, 'good!')


@client.event
async def on_raw_reaction_remove(payload):
#async def on_raw_reaction_add(reaction, user):
    with open('gran_log.txt', 'a', newline='') as f:
        channel = client.get_channel(722253361159864479)
        now2 = dt.now()
        now3 = str(now2)
#        writer = csv.writer(f)
#        reac_m = str(reaction.message)
        f.write("Date&Time:\r\n"+now3+"\r\n")
#        f.write("reaction has been added"+"\r\n")
#        reac_reac = reaction
#       f.write(str(reac_reac))
        f.write("message channel & id\r\n")
#    print(reaction.message)
#        f.write(str(reaction.message.channel)+"\r\n")
        f.write(str(payload.channel_id)+"\r\n")
#        f.write(reac_m+"\r\n")
#    print("message-author")
#    print(reaction.message.author.id)
        f.write("delete-reaction-user-id\r\n")
        f.write(str(payload.user_id) + "del\r\n\r\n")


        await channel.send('Date&Time:\n' + now3 + '\nmessage channel & id\n' + str(payload.channel_id) + '\nreaction-user-id\r\n' + str(payload.user_id) + 'del\n_')
        
client.run(TOKEN)
