# インストールした discord.py を読み込む
import asyncio
import time
import discord
from discord.ext import commands
from datetime import datetime as dt
from datetime import timedelta
import csv
import os
import math
import random
import gspread
#import json


# 自分のBotのアクセストークンに置き換えてください
TOKEN = os.environ['DISCORD_BOT_TOKEN']
#SPREADSHEET_KEY =os.environ['GSS_CAMA']

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
    
    
#ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountCredentials

#2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

#認証情報設定
#ダウンロードしたjsonファイル名をクレデンシャル変数に設定（秘密鍵、Pythonファイルから読み込みしやすい位置に置く）
credentials = ServiceAccountCredentials.from_json_keyfile_name('camarade-secret_key.json', scope)

#OAuth2の資格情報を使用してGoogle APIにログインします。
gc = gspread.authorize(credentials)

#共有設定したスプレッドシートキーを変数[SPREADSHEET_KEY]に格納する。
#SPREADSHEET_KEY = '1HsQ_p2Hsg2g4tb8bXClOqseIhCYoI-4-FaWNrlktdnE'



@client.event
async def on_raw_reaction_add(payload):
#async def on_raw_reaction_add(reaction, user):
#    with open('gran_log.txt', 'a', newline='') as f:
    if not payload.channel_id == 732658643740262553:
        return
    else:    
        channel = client.get_channel(722253361159864479)
        now = dt.now()
        now1 = str(now)
#        writer = csv.writer(f)
#        reac_m = str(reaction.message)
#        f.write("Date&Time:\r\n"+now1+"\r\n")
#        f.write("reaction has been added"+"\r\n")
#        reac_reac = reaction
#       f.write(str(reac_reac))
#        f.write("message channel & id\r\n")
#    print(reaction.message)
#        f.write(str(payload.channel_id)+"\r\n")
#        f.write(str(reaction.message.channel.id)+"\r\n")
#        f.write(reac_m+"\r\n")
#    print("message-author")
#    print(reaction.message.author.id)
#        f.write("reaction-user-id\r\n")
#        f.write(str(payload.user_id)+"\r\n\r\n")
#    await message.channel.send('reac_m')
    #    await reaction.channel.send(reaction.message)
        await channel.send('Date&Time:\n'+now1+'\nmessage channel\n'+str(payload.channel_id)+'\nmessage-id\n'+str(payload.message_id)+'\nreaction-user-id\r\n'+str(payload.user_id)+'\n_')

 #       lot_result_channel = [channel for channel in client.get_all_channels() if channel.id == lot_result_channel_id][0]
#        await client.send_message(lot_result_channel, 'good!')


@client.event
async def on_raw_reaction_remove(payload):
#async def on_raw_reaction_add(reaction, user):
#    with open('gran_log.txt', 'a', newline='') as f:
        if not payload.channel_id == 732658643740262553:
            return
        else:
            channel = client.get_channel(722253361159864479)
            now2 = dt.now()
            now3 = str(now2)
#        writer = csv.writer(f)
#        reac_m = str(reaction.message)
#        f.write("Date&Time:\r\n"+now3+"\r\n")
#        f.write("reaction has been added"+"\r\n")
#        reac_reac = reaction
#       f.write(str(reac_reac))
#        f.write("message channel & id\r\n")
#    print(reaction.message)
#        f.write(str(reaction.message.channel)+"\r\n")
#        f.write(str(payload.channel_id)+"\r\n")
#        f.write(reac_m+"\r\n")
#    print("message-author")
#    print(reaction.message.author.id)
#        f.write("delete-reaction-user-id\r\n")
#        f.write(str(payload.user_id) + "del\r\n\r\n")
        await channel.send('Date&Time:\n' + now3 + '\nmessage channel\n' + str(payload.channel_id) + '\nmessage-id\n'+str(payload.message_id) + '\nreaction-user-id\r\n' + str(payload.user_id) + 'del\n_')
        
@client.event
async def on_message(message):
    culc_channel = client.get_channel(679730751360466963)  #本番用
#    culc_channel = client.get_channel(722253530576060497)   #debag用
    wai_channel = client.get_channel(658468918243098626)  #本番用
#    wai_channel = client.get_channel(722253530576060497)   #debag用
    ami_channel = client.get_channel(675359824803790850)

                    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!bun '):
        m_num = message.content.strip('!bun ')
        m_list = m_num.split()
        # 人数ppとdiaに分ける。
        pp = int(m_list[0])
        dia = int(m_list[1])

        if pp < 10 and dia < 5000:
            bunpa = dia / pp
            if bunpa < 50:
                dice = random.randint(1, pp)  #サイコロを振る。出る目を指定。
                await culc_channel.send('分配が50dia未満(' + str(math.floor(bunpa)) + 'dia/人)なので、抽選を行います。\nリアクション表示の上から ' + str(dice) + ' 番目の方に ' + str(dia) + ' diaを渡してください。\nリアクション表示と人数が異なる場合は別途抽選を行ってください。')
            else:
                await culc_channel.send('10人未満,5000dia未満なので以下となります。\n分配：' + str(math.floor(bunpa)) + 'dia\n血盟資金、分配者手数料はありません。')
                
        elif pp < 10 and dia >= 5000:
            ketsu = dia * 0.03
            bunpb = (dia - ketsu * 3) / pp
            await culc_channel.send('10人未満, 5000dia以上なので以下となります。\n血盟資金:' + str(math.floor(ketsu)) +'diaを各盟主へ渡してください。\n分配：' +str (math.floor(bunpb)) + 'diaになります。\n分配者手数料は１０人未満なのでありません。')

        else:
            if 10 <= pp < 25 and dia >= 5000:
                ketsu = dia * 0.03
                tema = dia * 0.05
                if tema < 500:
                    bunpb = (dia - ketsu * 3 - tema) / pp
                    await culc_channel.send('10人以上, 5000dia以上なので以下となります。\n血盟資金:' + str(math.floor(ketsu)) +'diaを各盟主へ渡してください。\n分配：' +str(math.floor(bunpb)) + 'diaになります。\nちなみに手間賃は'+ str(math.floor(tema))+ 'diaです。')
                elif tema >= 500:
                    tema = 500
                    bunpb = (dia - ketsu * 3 - tema) / pp
                    await culc_channel.send('10人以上, 5000dia以上なので以下となります。\n血盟資金:' + str(math.floor(ketsu)) + 'diaを各盟主へ渡してください。\n分配：' + str(math.floor(bunpb)) + 'diaになります。\nちなみに手間賃は上限の' + str(math.floor(tema)) + 'diaです。')
                else:
                    await culc_channel.send('えろてろまで問い合わせを。')
               
            elif 10 <= pp < 25 and dia < 5000:
                tema = dia * 0.05
                bunpb = (dia - tema) / pp
                if bunpb < 50:
                    dice = random.randint(1, pp)  # サイコロを振る。出る目を指定。
                    await culc_channel.send('分配が50dia未満(' + str(math.floor(bunpb)) + 'dia/人)なので、抽選を行います。\nリアクション表示の上から ' + str(dice) + ' 番目の方に' + str(dia) + 'diaを渡してください。\nリアクション表示と人数が異なる場合は別途抽選を行ってください。')
                else:
                    await culc_channel.send('10人以上, 5000dia未満なので以下となります。\n分配：' + str(math.floor(bunpb)) + 'diaになります。\n分配者手数料は'+ str(math.floor(tema))+ 'diaです。\n血盟資金はありません。')
                
            else:
                if pp >= 25 and dia >= 5000:
                    ketsushi = dia * 0.03
                    bunpc = (dia - ketsushi * 3) / pp
                    if bunpc < 100:
                        meishubun1 = dia/3
                        await culc_channel.send('25人以上 / 分配 100dia未満なので全額血盟資金となります。\n３等分した' + str(math.floor(meishubun1)) + 'diaを各盟主に渡してください。\n分配者手数料、血盟資金はありません。')
                    else:
                        await culc_channel.send('25人以上 / 分配 100dia以上なので盟主が分配します。以下に従って盟主と取引して下さい。\n'+str(math.floor(bunpc))+' × 各血盟の対象人数 + ' + str(math.floor(ketsushi)) + 'dia(血盟資金）の合計を各盟主に渡してください。\n分配者手数料はありません。')
                elif pp >= 25 and dia < 5000:
                    bunpd = dia / pp
                    if bunpd < 100:
                        meishubun2 = dia / 3
                        await culc_channel.send('25人以上で分配が100dia/人 未満なので全額血盟資金となります。\n' + str(math.floor(meishubun2))+ 'diaを各盟主に渡してください。\n分配者手数料、血盟資金はありません。')
                    else:
                        await culc_channel.send('25人以上で分配が100dia/人 以上なので以下に従って盟主と取引して下さい。\n今回は盟主が分配するため、血盟資金 + 各血盟の対象人数 × ' + str(math.floor(bunpd)) + 'diaを各盟主に渡してください。\n分配者手数料はありません。')
                else:
                    await culc_channel.send('えろてろまで問い合わせを。')
                             
    if message.content.startswith('!dice '):
        if message.channel.id == 675359824803790850:
        #if message.channel.id == 722253530576060497:
            rami_num = message.content.strip('!dice ')
            rami_list = rami_num.split()
            # 人数ppとdiaに分ける。
            rami_rand = int(rami_list[0])
            rami_dice = random.randint(1, rami_rand)  # サイコロを振る。出る目を指定。
            await ami_channel.send('抽選した結果、' + str(rami_dice) + ' 番が当選！オーメデトーゴーザイマース！')
            return
        return

    if message.content.startswith('!nami '):
        if message.channel.id == 675359824803790850:
            nami_num = message.content.strip('!nami')
            nami_list = nami_num.split()
            nami_rand = random.choice(nami_list)
            await ami_channel.send('抽選した結果、' + str(nami_rand) + ' が当選！オーメデトーゴーザイマース！')
            return
        return

    

    if message.content.startswith('ワイが'):
        if message.author.id == 591281241798737938:
            await wai_channel.send('アンタ誰や？下の板言うてないで狩りしーや？')
        else:
            await wai_channel.send(message.author.name + 'や。さるじやあらへん。\nあいつは今びっくり焼きを調べるのに夢中やで！')
#            worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1
#            import_value = str(message.author.name + 'や。さるじやあらへん')
#            worksheet.update_cell(1, 2, import_value)

    if message.content.startswith('$ワイが')
            worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1
            import_value = str(message.author.name + 'や。さるじやあらへん')
            worksheet.update_cell(1, 2, import_value)

        

    if message.content.endswith('さるじや'):
        if message.content.startswith('ワイが'):
            if message.author.id == 591281241798737938:
                await wai_channel.send('パカラッパカラッ！\nヒヒーン(*´ω｀*)')
            else:
                await wai_channel.send('さるじのケツでも蹴っとき！')
        else:
            await wai_channel.send('さるじなら100dia罰金な')
    
    if message.content.startswith('残高照会'):
        if message.author.id == 591281241798737938:
            await wai_channel.send('どうせまた借金するんやろ？')
        else:
            await wai_channel.send('さるじさん６万')
            
    global result, judge
    if message.content == '！じゃんけん':
        if message.author.id == 591281241798737938:
            saruji = random.choice(('？', '遊んどらんで金返せや', '最初はパー！私の勝ち！100dia払って＾＾'))
            await wai_channel.send(str(saruji))
            return

        else:
            await message.channel.send("最初はぐー、じゃんけん")

            jkbot = random.choice(("ぐー", "ちょき", "ぱー"))
            draw = str(jkbot) + "！引き分けだよ～"
            wn = str(jkbot) + "･･･君の勝ち！"
            lst = random.choice((str(jkbot) + 'だよ！私の勝ち！弱ｗｗｗｗｗｗｗｗｗｗｗｗやめたら？じゃんけん',
                              str(jkbot) + 'だから私の勝ちだね(∩´∀｀)∩、また挑戦してね！'))

        def jankencheck(m):
            return (m.author == message.author) and (m.content in ['ぐー', 'ちょき', 'ぱー'])

        reply = await client.wait_for("message", check=jankencheck)
        if reply.content == jkbot:
            judge = draw
        else:
            if reply.content == "ぐー":
                if jkbot == "ちょき":
                    judge = wn
                else:
                    judge = lst

            elif reply.content == "ちょき":
                if jkbot == "ぱー":
                    judge = wn
                else:
                    judge = lst

            else:
                if jkbot == "ぐー":
                    judge = wn
                else:
                    judge = lst

        await message.channel.send(judge)
            
            
client.run(TOKEN)
