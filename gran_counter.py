# インストールした discord.py を読み込む
import asyncio
import time
import discord
from discord.ext import commands
from datetime import datetime as dt
from datetime import timedelta
import csv
import os

# 自分のBotのアクセストークンに置き換えてください
TOKEN = os.environ['DISCORD_BOT_TOKEN']

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
        
@client.event
async def on_message(message):
    culc_channel = client.get_channel(679730751360466963)  #本番用
#    culc_channel = client.get_channel(722253530576060497)   #debag用

    if message.content.startswith('!bun '):
        m_num = message.content.strip('!bun ')
        m_list = m_num.split()
        # 人数ppとdiaに分ける。
        pp = int(m_list[0])
        dia = int(m_list[1])

        if pp < 10 and dia < 5000:
            bunpa = dia / pp
            await culc_channel.send('10人未満,5000dia未満なので以下となります。\n分配：' + str(round(bunpa)) + 'dia\n血盟資金、分配者手数料はありません。')

        elif pp < 10 and dia >= 5000:
            ketsu = dia * 0.03
            bunpb = (dia - ketsu * 3) / pp
            await culc_channel.send('10人未満, 5000dia以上なので以下となります。\n血盟資金:' +str(round(ketsu)) +'diaを各盟主へ渡してください。\n分配：' +str(round(bunpb)) + 'diaになります。\n分配者手数料は１０人未満なのでありません。')

        else:
            if 10 <= pp < 25 and dia >= 5000:
                ketsu = dia * 0.03
                tema = dia * 0.05
                bunpb = (dia - ketsu * 3 - tema) / pp
                await culc_channel.send('10人以上, 5000dia以上なので以下となります。\n血盟資金:' +str(round(ketsu)) +'diaを各盟主へ渡してください。\n分配：' +str(round(bunpb)) + 'diaになります。\nちなみに手間賃は'+ str(round(tema))+ 'diaです。')
            elif 10 <= pp < 25 and dia < 5000:
                tema = dia * 0.05
                bunpb = (dia - tema) / pp
                await culc_channel.send('10人以上, 5000dia未満なので以下となります。\n分配：' + str(round(bunpb)) + 'diaになります。\n分配者手数料は'+ str(round(tema))+ 'diaです。\n血盟資金はありません。')
            else:
                if pp >= 25 and dia >= 5000:
                    meishutema = dia * 0.05
                    ketsushi = dia * 0.03
                    bunpc = (dia - meishutema * 3) / pp
                    if bunpc < 100:
                        meishubun1 = dia/3
                        await culc_channel.send('25人以上 / 分配 100dia未満なので全額血盟資金となります。\n３等分した' + str(round(meishubun1)) + 'diaを各盟主に渡してください。\n分配者手数料、血盟資金はありません。')
                    else:
                        await culc_channel.send('25人以上 / 分配 100dia以上なので盟主が分配します。以下に従って盟主と取引して下さい。\n'+str(round(bunpc))+' × 各血盟の対象人数 + ' + str(round(ketsushi)) + 'dia(血盟資金）の合計を各盟主に渡してください。\n分配者手数料はありません。')
                elif pp >= 25 and dia < 5000:
                    bunpd = dia / pp
                    if bunpd < 100:
                        meishubun2 = dia / 3
                        await culc_channel.send('25人以上で分配が100dia/人 未満なので全額血盟資金となります。\n' + str(round(meishubun2))+ 'diaを各盟主に渡してください。\n分配者手数料、血盟資金はありません。')
                    else:
                        await culc_channel.send('25人以上で分配が100dia/人 以上なので以下に従って盟主と取引して下さい。\n今回は盟主が分配するため、血盟資金 + 各血盟の対象人数 × ' + str(round(bunpd)) + 'diaを各盟主に渡してください。\n分配者手数料はありません。')
                else:
                    await culc_channel.send('えろてろまで問い合わせを。')

client.run(TOKEN)
