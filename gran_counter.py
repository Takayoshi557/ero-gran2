# インストールした discord.py を読み込む
import asyncio
import time
import discord
from discord.ext import commands
from datetime import datetime
from datetime import timedelta
import csv
import os
import math
import random
import gspread
import json
import sys
import pytz


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


# ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountCredentials

# 2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# 認証情報設定
# ダウンロードしたjsonファイル名をクレデンシャル変数に設定（秘密鍵、Pythonファイルから読み込みしやすい位置に置く）
credentials = ServiceAccountCredentials.from_json_keyfile_name('camarade-secret_key.json', scope)

# OAuth2の資格情報を使用してGoogle APIにログインします。
gc = gspread.authorize(credentials)

# 共有設定したスプレッドシートキーを変数[SPREADSHEET_KEY]に格納する。
SPREADSHEET_KEY = '1HsQ_p2Hsg2g4tb8bXClOqseIhCYoI-4-FaWNrlktdnE'

@client.event
async def on_message(message):
    a_channel = client.get_channel(762669239588487208)  # 本番用
    b_channel = client.get_channel(762669299248398366)  # 本番用
    c_channel = client.get_channel(762669351064305724)
    d_channel = client.get_channel(762669465891504169)
    e_channel = client.get_channel(762669524771274802)
    #worksheet_event = gc.open_by_key(SPREADSHEET_KEY).worksheet('event')
    entry_channel = client.get_channel(737598436693770282)
    pt_channel = client.get_channel(816666355004735518)
    # pt_channel = client.get_channel(722253470023024640)

#    test_channel = client.get_channel()

    if message.author == client.user:
        return

    elif message.content.startswith('挨拶しなよえろぼっと'):
        await entry_channel.send('はじめまして。イベント採点に来ました。\n権限付与をお願いします。')

    elif message.content.startswith('タイム'):
        now = datetime.now(pytz.timezone('Asia/Tokyo'))
        print(now)
    elif message.content.startswith('res '):
        if message.channel.id == 816666355004735518:
        # if message.channel.id == 722253470023024640:
            worksheet_pt = gc.open_by_key(SPREADSHEET_KEY).worksheet('pt')
            today = datetime.now(pytz.timezone('Asia/Tokyo'))
            contents = message.content.split()
            day_from = contents[1]
            day_end = contents[2]
            cell_from = worksheet_pt.find(str(day_from))
            cell_end = worksheet_pt.find(str(day_end))
            print(str(cell_from.row))
            print(str(cell_end.col))
            worksheet_pt.update_cell(6, 13, '=SUM(B' + str(cell_from.row) + ':B' + str(cell_end.row) + ')')
            worksheet_pt.update_cell(6, 14, '=SUM(C' + str(cell_from.row) + ':C' + str(cell_end.row) + ')')
            worksheet_pt.update_cell(6, 15, '=SUM(D' + str(cell_from.row) + ':D' + str(cell_end.row) + ')')
            worksheet_pt.update_cell(6, 16, '=SUM(E' + str(cell_from.row) + ':E' + str(cell_end.row) + ')')
            worksheet_pt.update_cell(6, 17, '=SUM(F' + str(cell_from.row) + ':F' + str(cell_end.row) + ')')
            worksheet_pt.update_cell(6, 18, '=SUM(G' + str(cell_from.row) + ':G' + str(cell_end.row) + ')')
            worksheet_pt.update_cell(6, 19, '=SUM(H' + str(cell_from.row) + ':H' + str(cell_end.row) + ')')
            worksheet_pt.update_cell(6, 20, '=SUM(I' + str(cell_from.row) + ':I' + str(cell_end.row) + ')')
            worksheet_pt.update_cell(6, 21, '=SUM(J' + str(cell_from.row) + ':J' + str(cell_end.row) + ')')
            worksheet_pt.update_cell(6, 22, '=SUM(K' + str(cell_from.row) + ':K' + str(cell_end.row) + ')')

            cama_rank = worksheet_pt.cell(7, 13).value
            kimuchi_rank = worksheet_pt.cell(7, 14).value
            ten_rank = worksheet_pt.cell(7, 15).value
            lien_rank = worksheet_pt.cell(7, 16).value
            dl_rank = worksheet_pt.cell(7, 17).value
            pb_rank = worksheet_pt.cell(7, 18).value
            samurai_rank = worksheet_pt.cell(7, 19).value
            hiyoko_rank = worksheet_pt.cell(7, 20).value
            death_rank = worksheet_pt.cell(7, 21).value
            kgb_rank = worksheet_pt.cell(7, 22).value
            
            cama_total = worksheet_pt.cell(6, 13).value
            kimuchi_total = worksheet_pt.cell(6, 14).value
            ten_total = worksheet_pt.cell(6, 15).value
            lien_total = worksheet_pt.cell(6, 16).value
            dl_total = worksheet_pt.cell(6, 17).value
            pb_total = worksheet_pt.cell(6, 18).value
            samurai_total = worksheet_pt.cell(6, 19).value
            hiyoko_total = worksheet_pt.cell(6, 20).value
            death_total = worksheet_pt.cell(6, 21).value
            kgb_total = worksheet_pt.cell(6, 22).value
            
            await pt_channel.send(str(day_from) + 'から' + str(day_end) + '間のPT数と順位を報告するね！')
            
            #1位判定
            if int(cama_rank) == 1:
                await pt_channel.send(str(cama_rank) + '位 / CAMARADE / ' + str(cama_total) + ' PT')
            if int(kimuchi_rank) == 1:
                await pt_channel.send(str(kimuchi_rank) + '位 / kimchi / ' + str(kimuchi_total) + ' PT')
            if int(ten_rank) == 1:
                await pt_channel.send(str(ten_rank) + '位 / 天 / ' + str(ten_total) + ' PT')
            if int(lien_rank) == 1:
                await pt_channel.send(str(lien_rank) + '位 / Lien / ' + str(lien_total) + ' PT')
            if int(dl_rank) == 1:
                await pt_channel.send(str(dl_rank) + '位 / DL / ' + str(dl_total) + ' PT')
            if int(pb_rank) == 1:
                await pt_channel.send(str(pb_rank) + '位 / PB / ' + str(pb_total) + ' PT')
            if int(samurai_rank) == 1:
                await pt_channel.send(str(samurai_rank) + '位 / SAMURAI / ' + str(samurai_total) + ' PT')
            if int(hiyoko_rank) == 1:
                await pt_channel.send(str(hiyoko_rank) + '位 / ひよこの復讐 / ' + str(hiyoko_total) + ' PT')
            if int(death_rank) == 1:
                await pt_channel.send(str(death_rank) + '位 / DEATH / ' + str(death_total) + ' PT')
            if int(kgb_rank) == 1:
                await pt_channel.send(str(kgb_rank) + '位 / KGB / ' + str(kgb_total) + ' PT')

            # 2位判定
            if int(cama_rank) == 2:
                await pt_channel.send(str(cama_rank) + '位 / CAMARADE / ' + str(cama_total) + ' PT')
            if int(kimuchi_rank) == 2:
                await pt_channel.send(str(kimuchi_rank) + '位 / kimchi / ' + str(kimuchi_total) + ' PT')
            if int(ten_rank) == 2:
                await pt_channel.send(str(ten_rank) + '位 / 天 / ' + str(ten_total) + ' PT')
            if int(lien_rank) == 2:
                await pt_channel.send(str(lien_rank) + '位 / Lien / ' + str(lien_total) + ' PT')
            if int(dl_rank) == 2:
                await pt_channel.send(str(dl_rank) + '位 / DL / ' + str(dl_total) + ' PT')
            if int(pb_rank) == 2:
                await pt_channel.send(str(pb_rank) + '位 / PB / ' + str(pb_total) + ' PT')
            if int(samurai_rank) == 2:
                await pt_channel.send(str(samurai_rank) + '位 / SAMURAI / ' + str(samurai_total) + ' PT')
            if int(hiyoko_rank) == 2:
                await pt_channel.send(str(hiyoko_rank) + '位 / ひよこの復讐 / ' + str(hiyoko_total) + ' PT')
            if int(death_rank) == 2:
                await pt_channel.send(str(death_rank) + '位 / DEATH / ' + str(death_total) + ' PT')
            if int(kgb_rank) == 2:
                await pt_channel.send(str(kgb_rank) + '位 / KGB / ' + str(kgb_total) + ' PT')

            # 3位判定
            if int(cama_rank) == 3:
                await pt_channel.send(str(cama_rank) + '位 / CAMARADE / ' + str(cama_total) + ' PT')
            if int(kimuchi_rank) == 3:
                await pt_channel.send(str(kimuchi_rank) + '位 / kimchi / ' + str(kimuchi_total) + ' PT')
            if int(ten_rank) == 3:
                await pt_channel.send(str(ten_rank) + '位 / 天 / ' + str(ten_total) + ' PT')
            if int(lien_rank) == 3:
                await pt_channel.send(str(lien_rank) + '位 / Lien / ' + str(lien_total) + ' PT')
            if int(dl_rank) == 3:
                await pt_channel.send(str(dl_rank) + '位 / DL / ' + str(dl_total) + ' PT')
            if int(pb_rank) == 3:
                await pt_channel.send(str(pb_rank) + '位 / PB / ' + str(pb_total) + ' PT')
            if int(samurai_rank) == 3:
                await pt_channel.send(str(samurai_rank) + '位 / SAMURAI / ' + str(samurai_total) + ' PT')
            if int(hiyoko_rank) == 3:
                await pt_channel.send(str(hiyoko_rank) + '位 / ひよこの復讐 / ' + str(hiyoko_total) + ' PT')
            if int(death_rank) == 3:
                await pt_channel.send(str(death_rank) + '位 / DEATH / ' + str(death_total) + ' PT')
            if int(kgb_rank) == 3:
                await pt_channel.send(str(kgb_rank) + '位 / KGB / ' + str(kgb_total) + ' PT')

            # 4位判定
            if int(cama_rank) == 4:
                await pt_channel.send(str(cama_rank) + '位 / CAMARADE / ' + str(cama_total) + ' PT')
            if int(kimuchi_rank) == 4:
                await pt_channel.send(str(kimuchi_rank) + '位 / kimchi / ' + str(kimuchi_total) + ' PT')
            if int(ten_rank) == 4:
                await pt_channel.send(str(ten_rank) + '位 / 天 / ' + str(ten_total) + ' PT')
            if int(lien_rank) == 4:
                await pt_channel.send(str(lien_rank) + '位 / Lien / ' + str(lien_total) + ' PT')
            if int(dl_rank) == 4:
                await pt_channel.send(str(dl_rank) + '位 / DL / ' + str(dl_total) + ' PT')
            if int(pb_rank) == 4:
                await pt_channel.send(str(pb_rank) + '位 / PB / ' + str(pb_total) + ' PT')
            if int(samurai_rank) == 4:
                await pt_channel.send(str(samurai_rank) + '位 / SAMURAI / ' + str(samurai_total) + ' PT')
            if int(hiyoko_rank) == 4:
                await pt_channel.send(str(hiyoko_rank) + '位 / ひよこの復讐 / ' + str(hiyoko_total) + ' PT')
            if int(death_rank) == 4:
                await pt_channel.send(str(death_rank) + '位 / DEATH / ' + str(death_total) + ' PT')
            if int(kgb_rank) == 4:
                await pt_channel.send(str(kgb_rank) + '位 / KGB / ' + str(kgb_total) + ' PT')

            # 5位判定
            if int(cama_rank) == 5:
                await pt_channel.send(str(cama_rank) + '位 / CAMARADE / ' + str(cama_total) + ' PT')
            if int(kimuchi_rank) == 5:
                await pt_channel.send(str(kimuchi_rank) + '位 / kimchi / ' + str(kimuchi_total) + ' PT')
            if int(ten_rank) == 5:
                await pt_channel.send(str(ten_rank) + '位 / 天 / ' + str(ten_total) + ' PT')
            if int(lien_rank) == 5:
                await pt_channel.send(str(lien_rank) + '位 / Lien / ' + str(lien_total) + ' PT')
            if int(dl_rank) == 5:
                await pt_channel.send(str(dl_rank) + '位 / DL / ' + str(dl_total) + ' PT')
            if int(pb_rank) == 5:
                await pt_channel.send(str(pb_rank) + '位 / PB / ' + str(pb_total) + ' PT')
            if int(samurai_rank) == 5:
                await pt_channel.send(str(samurai_rank) + '位 / SAMURAI / ' + str(samurai_total) + ' PT')
            if int(hiyoko_rank) == 5:
                await pt_channel.send(str(hiyoko_rank) + '位 / ひよこの復讐 / ' + str(hiyoko_total) + ' PT')
            if int(death_rank) == 5:
                await pt_channel.send(str(death_rank) + '位 / DEATH / ' + str(death_total) + ' PT')
            if int(kgb_rank) == 5:
                await pt_channel.send(str(kgb_rank) + '位 / KGB / ' + str(kgb_total) + ' PT')

            # 6位判定
            if int(cama_rank) == 6:
                await pt_channel.send(str(cama_rank) + '位 / CAMARADE / ' + str(cama_total) + ' PT')
            if int(kimuchi_rank) == 6:
                await pt_channel.send(str(kimuchi_rank) + '位 / kimchi / ' + str(kimuchi_total) + ' PT')
            if int(ten_rank) == 6:
                await pt_channel.send(str(ten_rank) + '位 / 天 / ' + str(ten_total) + ' PT')
            if int(lien_rank) == 6:
                await pt_channel.send(str(lien_rank) + '位 / Lien / ' + str(lien_total) + ' PT')
            if int(dl_rank) == 6:
                await pt_channel.send(str(dl_rank) + '位 / DL / ' + str(dl_total) + ' PT')
            if int(pb_rank) == 6:
                await pt_channel.send(str(pb_rank) + '位 / PB / ' + str(pb_total) + ' PT')
            if int(samurai_rank) == 6:
                await pt_channel.send(str(samurai_rank) + '位 / SAMURAI / ' + str(samurai_total) + ' PT')
            if int(hiyoko_rank) == 6:
                await pt_channel.send(str(hiyoko_rank) + '位 / ひよこの復讐 / ' + str(hiyoko_total) + ' PT')
            if int(death_rank) == 6:
                await pt_channel.send(str(death_rank) + '位 / DEATH / ' + str(death_total) + ' PT')
            if int(kgb_rank) == 6:
                await pt_channel.send(str(kgb_rank) + '位 / KGB / ' + str(kgb_total) + ' PT')

            # 7位判定
            if int(cama_rank) == 7:
                await pt_channel.send(str(cama_rank) + '位 / CAMARADE / ' + str(cama_total) + ' PT')
            if int(kimuchi_rank) == 7:
                await pt_channel.send(str(kimuchi_rank) + '位 / kimchi / ' + str(kimuchi_total) + ' PT')
            if int(ten_rank) == 7:
                await pt_channel.send(str(ten_rank) + '位 / 天 / ' + str(ten_total) + ' PT')
            if int(lien_rank) == 7:
                await pt_channel.send(str(lien_rank) + '位 / Lien / ' + str(lien_total) + ' PT')
            if int(dl_rank) == 7:
                await pt_channel.send(str(dl_rank) + '位 / DL / ' + str(dl_total) + ' PT')
            if int(pb_rank) == 7:
                await pt_channel.send(str(pb_rank) + '位 / PB / ' + str(pb_total) + ' PT')
            if int(samurai_rank) == 7:
                await pt_channel.send(str(samurai_rank) + '位 / SAMURAI / ' + str(samurai_total) + ' PT')
            if int(hiyoko_rank) == 7:
                await pt_channel.send(str(hiyoko_rank) + '位 / ひよこの復讐 / ' + str(hiyoko_total) + ' PT')
            if int(death_rank) == 7:
                await pt_channel.send(str(death_rank) + '位 / DEATH / ' + str(death_total) + ' PT')
            if int(kgb_rank) == 7:
                await pt_channel.send(str(kgb_rank) + '位 / KGB / ' + str(kgb_total) + ' PT')

            # 8位判定
            if int(cama_rank) == 8:
                await pt_channel.send(str(cama_rank) + '位 / CAMARADE / ' + str(cama_total) + ' PT')
            if int(kimuchi_rank) == 8:
                await pt_channel.send(str(kimuchi_rank) + '位 / kimchi / ' + str(kimuchi_total) + ' PT')
            if int(ten_rank) == 8:
                await pt_channel.send(str(ten_rank) + '位 / 天 / ' + str(ten_total) + ' PT')
            if int(lien_rank) == 8:
                await pt_channel.send(str(lien_rank) + '位 / Lien / ' + str(lien_total) + ' PT')
            if int(dl_rank) == 8:
                await pt_channel.send(str(dl_rank) + '位 / DL / ' + str(dl_total) + ' PT')
            if int(pb_rank) == 8:
                await pt_channel.send(str(pb_rank) + '位 / PB / ' + str(pb_total) + ' PT')
            if int(samurai_rank) == 8:
                await pt_channel.send(str(samurai_rank) + '位 / SAMURAI / ' + str(samurai_total) + ' PT')
            if int(hiyoko_rank) == 8:
                await pt_channel.send(str(hiyoko_rank) + '位 / ひよこの復讐 / ' + str(hiyoko_total) + ' PT')
            if int(death_rank) == 8:
                await pt_channel.send(str(death_rank) + '位 / DEATH / ' + str(death_total) + ' PT')
            if int(kgb_rank) == 8:
                await pt_channel.send(str(kgb_rank) + '位 / KGB / ' + str(kgb_total) + ' PT')

            # 9位判定
            if int(cama_rank) == 9:
                await pt_channel.send(str(cama_rank) + '位 / CAMARADE / ' + str(cama_total) + ' PT')
            if int(kimuchi_rank) == 9:
                await pt_channel.send(str(kimuchi_rank) + '位 / kimchi / ' + str(kimuchi_total) + ' PT')
            if int(ten_rank) == 9:
                await pt_channel.send(str(ten_rank) + '位 / 天 / ' + str(ten_total) + ' PT')
            if int(lien_rank) == 9:
                await pt_channel.send(str(lien_rank) + '位 / Lien / ' + str(lien_total) + ' PT')
            if int(dl_rank) == 9:
                await pt_channel.send(str(dl_rank) + '位 / DL / ' + str(dl_total) + ' PT')
            if int(pb_rank) == 9:
                await pt_channel.send(str(pb_rank) + '位 / PB / ' + str(pb_total) + ' PT')
            if int(samurai_rank) == 9:
                await pt_channel.send(str(samurai_rank) + '位 / SAMURAI / ' + str(samurai_total) + ' PT')
            if int(hiyoko_rank) == 9:
                await pt_channel.send(str(hiyoko_rank) + '位 / ひよこの復讐 / ' + str(hiyoko_total) + ' PT')
            if int(death_rank) == 9:
                await pt_channel.send(str(death_rank) + '位 / DEATH / ' + str(death_total) + ' PT')
            if int(kgb_rank) == 9:
                await pt_channel.send(str(kgb_rank) + '位 / KGB / ' + str(kgb_total) + ' PT')

            # 10位判定
            if int(cama_rank) == 10:
                await pt_channel.send(str(cama_rank) + '位 / CAMARADE / ' + str(cama_total) + ' PT')
            if int(kimuchi_rank) == 10:
                await pt_channel.send(str(kimuchi_rank) + '位 / kimchi / ' + str(kimuchi_total) + ' PT')
            if int(ten_rank) == 10:
                await pt_channel.send(str(ten_rank) + '位 / 天 / ' + str(ten_total) + ' PT')
            if int(lien_rank) == 10:
                await pt_channel.send(str(lien_rank) + '位 / Lien / ' + str(lien_total) + ' PT')
            if int(dl_rank) == 10:
                await pt_channel.send(str(dl_rank) + '位 / DL / ' + str(dl_total) + ' PT')
            if int(pb_rank) == 10:
                await pt_channel.send(str(pb_rank) + '位 / PB / ' + str(pb_total) + ' PT')
            if int(samurai_rank) == 10:
                await pt_channel.send(str(samurai_rank) + '位 / SAMURAI / ' + str(samurai_total) + ' PT')
            if int(hiyoko_rank) == 10:
                await pt_channel.send(str(hiyoko_rank) + '位 / ひよこの復讐 / ' + str(hiyoko_total) + ' PT')
            if int(death_rank) == 10:
                await pt_channel.send(str(death_rank) + '位 / DEATH / ' + str(death_total) + ' PT')
            if int(kgb_rank) == 10:
                await pt_channel.send(str(kgb_rank) + '位 / KGB / ' + str(kgb_total) + ' PT')

            await pt_channel.send('これで結果発表を終わるよ！')
            return




    elif message.content.startswith('pt '):
        if message.channel.id == 816666355004735518:
        # if message.channel.id == 722253470023024640:
            worksheet_pt = gc.open_by_key(SPREADSHEET_KEY).worksheet('pt')
            today = datetime.now(pytz.timezone('Asia/Tokyo'))
            day_count = worksheet_pt.cell(1, 1).value
            day_cell = 5 + int(day_count)
            latest_day = worksheet_pt.cell(int(day_cell), 1).value
            print(latest_day)
            if not str(latest_day) == str(today.date()):
                day_cell = day_cell + 1
                worksheet_pt.update_cell(day_cell, 1, str(today.date()))
                # print('日付なかった')
            contents = message.content.split()
            pt_num = contents[1]
            name = str(message.author.display_name)
            # print(message.author.display_name)
            # print(message.author.name)

            if str('CAMARADE') in str(message.author.display_name):
                worksheet_pt.update_cell(day_cell, 2, str(pt_num))
                clan = str('CAMARADE')
            elif str('天-') in str(message.author.display_name):
                worksheet_pt.update_cell(day_cell, 4, str(pt_num))
                clan = str('天')
            elif str('Kimuchi') in str(message.author.display_name):
                worksheet_pt.update_cell(day_cell, 3, str(pt_num))
                clan = str('Kimuchi')
            elif str('Kimchi') in str(message.author.display_name):
                worksheet_pt.update_cell(day_cell, 3, str(pt_num))
                clan = str('Kimchi')
            elif str('kimuchi') in str(message.author.display_name):
                worksheet_pt.update_cell(day_cell, 3, str(pt_num))
                clan = str('kimuchi')
            elif message.author.id == 602177396053114881:
                worksheet_pt.update_cell(day_cell, 3, str(pt_num))
                clan = str('kimuchi')

            elif str('Lien-') in str(message.author.display_name):
                worksheet_pt.update_cell(day_cell, 5, str(pt_num))
                clan = str('Lien')
            elif str('Daylights') in str(message.author.display_name):
                worksheet_pt.update_cell(day_cell, 6, str(pt_num))
                clan = str('Daylights')
            elif str('PB-') in str(message.author.display_name):
                worksheet_pt.update_cell(day_cell, 7, str(pt_num))
                clan = str('PB')
            elif str('SAMURAI-') in str(message.author.display_name):
                worksheet_pt.update_cell(day_cell, 8, str(pt_num))
                clan = str('SAMURAI')
            elif str('ひよこの復讐') in str(message.author.display_name):
                worksheet_pt.update_cell(day_cell, 9, str(pt_num))
                clan = str('ひよこの復讐')
            elif str('】Death') in str(message.author.display_name):
                worksheet_pt.update_cell(day_cell, 10, str(pt_num))
                clan = str('DEATH')
            elif str('タコです') in str(message.author.display_name):
                worksheet_pt.update_cell(day_cell, 10, str(pt_num))
                clan = str('DEATH')

            elif str('】OL-') in str(message.author.display_name):
                worksheet_pt.update_cell(day_cell, 11, str(pt_num))
                clan = str('KGB')
            elif str('KGB-') in str(message.author.display_name):
                worksheet_pt.update_cell(day_cell, 11, str(pt_num))
                clan = str('KGB')
            elif str('来生瞳') in str(message.author.display_name):
                worksheet_pt.update_cell(day_cell, 11, str(pt_num))
                clan = str('KGB')

            else:
                await pt_channel.send('名前から該当するクランが判定出来ませんでした！')
                return

            await pt_channel.send(str(clan) + ' / ' + str(pt_num) + 'PT で登録しました。')

            return

client.run(TOKEN)

