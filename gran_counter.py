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
import json


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
SPREADSHEET_KEY = '1HsQ_p2Hsg2g4tb8bXClOqseIhCYoI-4-FaWNrlktdnE'

@client.event
async def on_raw_reaction_add(payload):
    if not payload.channel_id == 7732658643740262553:
        return

    if payload.user_id == 695680339497975828 and payload.user_id == 689736979075825706:
        return
    else:
        channel = client.get_channel(722253361159864479)
        now = dt.now()
        now1 = str(now)
        await channel.send('Date&Time:\n'+now1+'\nmessage channel & id\n'+str(payload.channel_id)+'\nmessage-id\n'+str(payload.message_id)+'\nreaction-user-id\r\n'+str(payload.user_id)+'\n_')
    
@client.event
async def on_raw_reaction_remove(payload):
    if not payload.channel_id == 732658643740262553:
        return
    else:
        channel = client.get_channel(722253361159864479)
        now2 = dt.now()
        now3 = str(now2)
    await channel.send('Date&Time:\n' + now3 + '\nmessage channel\n' + str(payload.channel_id) + '\nmessage-id\n'+str(payload.message_id) + '\nreaction-user-id\r\n' + str(payload.user_id) + 'del\n_')
        
#    if not payload.channel_id == 732658643740262553:
#        if not payload.channel_id == 744727455293767711:
#            channel = client.get_channel(722253361159864479)
#            worksheet_find = gc.open_by_key(SPREADSHEET_KEY).worksheet('rare(red,purple)')
#            search_mid = payload.message_id
#            mid_cell = worksheet_find.find(str(search_mid))
#            entry_num = worksheet_find.cell(mid_cell.row, 165).value
#            entry_col = int(entry_num) + int(11)
#            worksheet_find.update_cell(mid_cell.row, int(entry_col), str(payload.user_id))
#                await channel.send('なぜに？')
#            return
#        else:    
#            channel = client.get_channel(722253361159864479)
#            now = dt.now()
#            now1 = str(now)
#            await channel.send('Date&Time:\n'+now1+'\nmessage channel\n'+str(payload.channel_id)+'\nmessage-id\n'+str(payload.message_id)+'\nreaction-user-id\r\n'+str(payload.user_id)+'\n_')
#        
#    if not payload.channel_id == 744727455293767711:
#        return
#    else:
#        channel = client.get_channel(722253361159864479)
#        worksheet_find = gc.open_by_key(SPREADSHEET_KEY).worksheet('rare(red,purple)')
#        search_mid = payload.message_id
#        mid_cell = worksheet_find.find(str(search_mid))
#        entry_num = worksheet_find.cell(mid_cell.row, 165).value
#        entry_col = int(entry_num) + int(11)
#        worksheet_find.update_cell(mid_cell.row, int(entry_col), str(payload.user_id))
#        await channel.send('なぜに？')
   
@client.event
async def on_message(message):
    culc_channel = client.get_channel(740355050182017135)  #本番用
    wai_channel = client.get_channel(658468918243098626)  #本番用
    ami_channel = client.get_channel(675359824803790850)
    list_channel = client.get_channel(743314066713477251)
    regi_channel = client.get_channel(744727455293767711)
    
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
#            await wai_channel.send(message.author.name + 'や。さるじやあらへん。\nあいつは今びっくり焼きを調べるのに夢中やで！')
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
            
#**********************************#
# アイテム管理用リアクション追加
#**********************************#

    #boss drop management bot. (!get(n or r) BossName DropItem)### n = normal, r = rare
    if message.content.startswith('!getr '):
        if message.channel.id == 744727455293767711:
            drop_high_list = message.content.split()
            drop_high_boss = drop_high_list[1]
            drop_high_item = drop_high_list[2]
            today = dt.now()
            worksheet_list = gc.open_by_key(SPREADSHEET_KEY).worksheet('rare(red,purple)')
            worksheet_id = gc.open_by_key(SPREADSHEET_KEY).worksheet('ID_LIST')
            id_num = worksheet_id.cell(4, 8).value
            input_id = int(id_num) + 2
            id_no = int(id_num) + 1
            worksheet_list.update_cell(input_id, 1, 'r' + str(id_no))
            worksheet_list.update_cell(input_id, 2, str(drop_high_boss))
            worksheet_list.update_cell(input_id, 3, str(drop_high_item))
            worksheet_list.update_cell(input_id, 4, str(message.author.name))
            worksheet_list.update_cell(input_id, 5, str(today.year) + '/' + str(today.month) + '/' + str(today.day))
            worksheet_list.update_cell(input_id, 6, str('none'))
            worksheet_list.update_cell(input_id, 7, str(message.id))
            worksheet_list.update_cell(input_id, 9, str('-'))
            worksheet_list.update_cell(input_id, 10, str('-'))

            drp = discord.Embed(title= '" ' + str(drop_high_boss) + ' " dropped " ' + str(drop_high_item) + ' "\nOwner(所有者):  ' + str(message.author.name) + '\nAllocated ID: r' + str(id_no),
                                description='Please reaction!',
                                color=discord.Colour.red())
            #               await wai_channel.send(embed=grn)
            msg = await regi_channel.send(embed=drp)  # debag
            #               msg = await grn_channel.send(embed=grn)#本番
            emoji1 = '\U0001F947'
            await msg.add_reaction(emoji1)
            worksheet_list.update_cell(input_id, 7, str(msg.id))
            await message.delete()
            return
        
    if message.content.startswith('!r_del '):
        if message.channel.id == 743314066713477251:
            worksheet_find = gc.open_by_key(SPREADSHEET_KEY).worksheet('rare(red,purple)')
            del_list = message.content.split()
            del_cell = worksheet_find.findall(str(del_list[1]))
            worksheet_find.update_cell(del_cell[0].row, 1, '')
            worksheet_find.update_cell(del_cell[0].row, 2, '')
            worksheet_find.update_cell(del_cell[0].row, 3, '')
            worksheet_find.update_cell(del_cell[0].row, 4, '')
            worksheet_find.update_cell(del_cell[0].row, 5, '')
            worksheet_find.update_cell(del_cell[0].row, 6, '')
            worksheet_find.update_cell(del_cell[0].row, 7, '')
            worksheet_find.update_cell(del_cell[0].row, 9, '')
            worksheet_find.update_cell(del_cell[0].row, 10, '')
            del_p = int(worksheet_find.cell(del_cell[0].row, 165).value)
            for num in range(del_p):
                num = num + int(11)
                worksheet_find.update_cell(del_cell[0].row, num, '')
                
    if message.content.startswith('!own_change '):
        if message.channel.id == 743314066713477251:
            worksheet_find = gc.open_by_key(SPREADSHEET_KEY).worksheet('rare(red,purple)')
            che_list = message.content.split()
            che_cell = worksheet_find.findall(str(che_list[1]))
            worksheet_find.update_cell(che_cell[0].row, 4, str(che_list[2]))
                
    if message.content.startswith('!rlist'):
        if message.channel.id == 743314066713477251:
            worksheet_find = gc.open_by_key(SPREADSHEET_KEY).worksheet('rare(red,purple)')
            worksheet_id = gc.open_by_key(SPREADSHEET_KEY).worksheet('ID_LIST')
            cell_list = worksheet_find.findall('none')
            deal_count = worksheet_id.cell(5, 8).value
            r_list = list()
            for num in range(int(deal_count)):
                get_id = worksheet_find.cell(cell_list[num].row, 1).value
                get_boss = worksheet_find.cell(cell_list[num].row, 2).value
                get_item = worksheet_find.cell(cell_list[num].row, 3).value
                get_name = worksheet_find.cell(cell_list[num].row, 4).value
                get_date = worksheet_find.cell(cell_list[num].row, 5).value
                r_list.append(get_id+'\t: '+ get_boss+'\t/ '+ get_item+'\t/ '+get_name+'\t/ '+get_date)
            r_list = '\n'.join(r_list)
            get_r = discord.Embed(title='DROP ITEM LIST (GRADE: RARE)', description='ID \t:\t  boss \t/  item \t/  holder \t/  date', color=discord.Colour.red())
            get_r.add_field(name='---------------------------------------------', value=str(r_list), inline=True)
            await list_channel.send(embed=get_r)
            return

    if message.content.startswith('!repor '):
        if message.channel.id == 743314066713477251:
            worksheet_find = gc.open_by_key(SPREADSHEET_KEY).worksheet('rare(red,purple)')
            id_cell_list = message.content.split()
            id_cell = worksheet_find.findall(str(id_cell_list[1]))
            pp = worksheet_find.cell(id_cell[0].row, 165).value
            get_id = worksheet_find.cell(id_cell[0].row, 1).value
            get_boss = worksheet_find.cell(id_cell[0].row, 2).value
            get_item = worksheet_find.cell(id_cell[0].row, 3).value
            get_name = worksheet_find.cell(id_cell[0].row, 4).value
            get_date = worksheet_find.cell(id_cell[0].row, 5).value
            add_col = int(11)
            id_check = list()
            for num in range(int(pp)):
                id_col = int(num) + int(add_col)
                id_check.append('<@' + worksheet_find.cell(id_cell[0].row, id_col).value + '>')
            drp = discord.Embed(
                title='ID: '+str(get_id)+' detail',
                description='BOSS: '+str(get_boss)+' / ITEM: '+str(get_item)+'\nOWNER: '+str(get_name)+' / DATA: '+str(get_date)+'\nENTRY\n'+str(id_check),
                color=discord.Colour.red())
            msg = await list_channel.send(embed=drp)  # debag

        if str(worksheet_list.cell(id_cell.row, 6).value) == str('finish'):
            await culc_channel.send('このID案件は分配案内が完了しています。\n変更したい方は えろてろ までご連絡おねがいします。')
            return
        else:
            worksheet_list.update_cell(id_cell.row, 6, str('finish'))   # 分配実行フラグ変更
            worksheet_list.update_cell(id_cell.row, 9, str(rbun_dia))   # 分配ダイア入力
            worksheet_list.update_cell(id_cell.row, 10, str(rbun_buyer))   # 購入者入力

            pp = int(worksheet_list.cell(id_cell.row, 8).value)
            dia = int(rbun_dia)

            if pp < 10 and dia < 5000:
                bunpa = dia / pp
                if bunpa < 50:
                    dice = random.randint(1, pp)  # サイコロを振る。出る目を指定。
                    dice_a = int(dice) + int(11) - int(1)
                    ran_men = worksheet_list.cell(id_cell.row, int(dice_a)).value
                    await culc_channel.send(str(rbun_id) + 'の' + str(worksheet_list.cell(id_cell.row, 2).value) + '/' + str(worksheet_list.cell(id_cell.row, 3).value) +' が' + str(dia) + ' diaで売れたので分配を行います。\n分配が50dia未満(' + str(math.floor(bunpa)) + 'dia/人)なので、抽選になります。\n抽選の結果、<@' + str(ran_men) + '> が当選！\n' + str(dia) + ' diaの取引をお願いします。')
                    return
                else:
                    await culc_channel.send(str(rbun_id) + 'の' + str(worksheet_list.cell(id_cell.row, 2).value) + '/' + str(worksheet_list.cell(id_cell.row, 3).value) +' が' + str(dia) + ' diaで売れました。\nメンションされている方々は以下に従い' + str(worksheet_list.cell(id_cell.row, 4).value) +'と取引を行って下さい。\n分配：' + str(math.floor(bunpa)) + 'dia')
                    for num in range(pp):
                        id_col = int(num) + int(11)
                        ment_id = '<@' + str(worksheet_list.cell(id_cell.row, id_col).value) + '>'
                        await culc_channel.send(' %s ' % ment_id)
                    return

            elif pp < 10 and dia >= 5000:
                ketsu = dia * 0.03
                bunpb = (dia - ketsu * 3) / pp
                await culc_channel.send(str(rbun_id) + 'の' + str(worksheet_list.cell(id_cell.row, 2).value) + '/' + str(worksheet_list.cell(id_cell.row, 3).value) +' が' + str(dia) + ' diaで売れました。\nメンションされている方々は以下に従い' + str(worksheet_list.cell(id_cell.row, 4).value) +'と取引を行って下さい。\n各盟主は血盟資金として ' + str(math.floor(ketsu)) + 'diaを出品してください。\nメンションされている方々は ' + str(
                        math.floor(bunpb)) + 'diaで出品して下さい。')
                await culc_channel.send('血盟資金\n<@462190506655612929>, <@477504935727071232>, <@290377448711782400>\n\n分配\n')
                for num in range(pp):
                    id_col = int(num) + int(11)
                    ment_id = '<@' + str(worksheet_list.cell(id_cell.row, id_col).value) + '>'
                    await culc_channel.send(' %s ' % ment_id)
                return
            else:
                if 10 <= pp < 25 and dia >= 5000:
                    ketsu = dia * 0.03
                    tema = dia * 0.05
                    if tema < 500:
                        bunpb = (dia - ketsu * 3 - tema) / pp
                        await culc_channel.send(str(rbun_id) + 'の' + str(worksheet_list.cell(id_cell.row, 2).value) + '/' + str(worksheet_list.cell(id_cell.row, 3).value) +' が' + str(dia) + ' diaで売れました。\nメンションされている方々は以下に従い' + str(worksheet_list.cell(id_cell.row, 4).value) +'と取引を行って下さい。\n血盟資金:' + str(math.floor(ketsu)) + 'diaを各盟主へ渡してください。\n分配：' + str(math.floor(bunpb)) + 'diaになります。')
                        await culc_channel.send(
                            '血盟資金\n<@462190506655612929>, <@477504935727071232>, <@290377448711782400>\n\n分配\n')
                        for num in range(pp):
                            id_col = int(num) + int(11)
                            ment_id = '<@' + str(worksheet_list.cell(id_cell.row, id_col).value) + '>'
                            await culc_channel.send(' %s ' % ment_id)
                    elif tema >= 500:
                        tema = 500
                        bunpb = (dia - ketsu * 3 - tema) / pp
                        await culc_channel.send(str(rbun_id) + 'の' + str(worksheet_list.cell(id_cell.row, 2).value) + '/' + str(worksheet_list.cell(id_cell.row, 3).value) +' が' + str(dia) + ' diaで売れました。\nメンションされている方々は以下に従い' + str(worksheet_list.cell(id_cell.row, 4).value) +'と取引を行って下さい。\n血盟資金:' + str(
                            math.floor(ketsu)) + 'diaを各盟主へ渡してください。\n分配：' + str(
                            math.floor(bunpb)) + 'diaになります。\nちなみに手間賃は上限の' + str(math.floor(tema)) + 'diaです。')
                        await culc_channel.send(
                            '血盟資金\n<@462190506655612929>, <@477504935727071232>, <@290377448711782400>\n\n分配\n')
                        for num in range(pp):
                            id_col = int(num) + int(11)
                            ment_id = '<@' + str(worksheet_list.cell(id_cell.row, id_col).value) + '>'
                            await culc_channel.send(' %s ' % ment_id)
                    else:
                        await culc_channel.send('えろてろまで問い合わせを。')

                    return
                elif 10 <= pp < 25 and dia < 5000:
                    tema = dia * 0.05
                    bunpb = (dia - tema) / pp
                    if bunpb < 50:
                        dice = random.randint(1, pp)  # サイコロを振る。出る目を指定。
                        dice_a = int(dice) + int(11) - int(1)
                        ran_men = worksheet_list.cell(id_cell.row, int(dice_a)).value
                        await culc_channel.send(str(rbun_id) + 'の' + str(worksheet_list.cell(id_cell.row, 2).value) + '/' + str(worksheet_list.cell(id_cell.row, 3).value) +' が' + str(dia) + ' diaで売れました。\n分配が50dia未満(' + str(math.floor(bunpb)) + 'dia/人)なので、抽選を行います。\n抽選の結果、<@' + str(ran_men) + '> が当選！\n' + str(dia) + ' diaの取引をお願いします。')
                        return
                    else:
                        await culc_channel.send(str(rbun_id) + 'の' + str(worksheet_list.cell(id_cell.row, 2).value) + '/' + str(worksheet_list.cell(id_cell.row, 3).value) +' が' + str(dia) + ' diaで売れました。\n10人以上, 5000dia未満なので以下となります。\n分配：' + str(math.floor(bunpb)) + 'diaになります。\n分配者手数料は' + str(
                                math.floor(tema)) + 'diaです。\n血盟資金はありません。')

                        for num in range(pp):
                            id_col = int(num) + int(11)
                            ment_id = '<@' + str(worksheet_list.cell(id_cell.row, id_col).value) + '>'
                            await culc_channel.send(' %s ' % ment_id)
                        return
                else:
                    if pp >= 25 and dia >= 5000:
                        ketsushi = dia * 0.03
                        bunpc = (dia - ketsushi * 3) / pp
                        if bunpc < 100:
                            meishubun1 = dia / 3
                            await culc_channel.send('25人以上 / 分配 100dia未満なので全額血盟資金となります。\n３等分した' + str(
                                math.floor(meishubun1)) + 'diaを各盟主に渡してください。\n分配者手数料、血盟資金はありません。')
                            return
                        else:
                            await culc_channel.send('25人以上 / 分配 100dia以上なので盟主が分配します。以下に従って盟主と取引して下さい。\n' + str(
                                math.floor(bunpc)) + ' × 各血盟の対象人数 + ' + str(
                                math.floor(ketsushi)) + 'dia(血盟資金）の合計を各盟主に渡してください。\n分配者手数料はありません。')
                            return
                    elif pp >= 25 and dia < 5000:
                        bunpd = dia / pp
                        if bunpd < 100:
                            meishubun2 = dia / 3
                            await culc_channel.send('25人以上で分配が100dia/人 未満なので全額血盟資金となります。\n' + str(
                                math.floor(meishubun2)) + 'diaを各盟主に渡してください。\n分配者手数料、血盟資金はありません。')
                        else:
                            await culc_channel.send(
                                '25人以上で分配が100dia/人 以上なので以下に従って盟主と取引して下さい。\n今回は盟主が分配するため、血盟資金 + 各血盟の対象人数 × ' + str(
                                    math.floor(bunpd)) + 'diaを各盟主に渡してください。\n分配者手数料はありません。')
                    else:
                        await culc_channel.send('えろてろまで問い合わせを。')

#*****************以下はじゃんけんBOT*******************

            
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
