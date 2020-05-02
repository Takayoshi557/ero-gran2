import discord
from discord.ext import commands
import asyncio
import os


# 自分のBotのアクセストークンに置き換えてください
#TOKEN = 'Njg5NzM2OTc5MDc1ODI1NzA2.XnLKlQ.VwxXI3msQeqyHc7cpQ9Q3igL8AQ'
token = os.environ[DISCORD_BOT_TOKEN]


client = commands.Bot(command_prefix='.')
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command()
async def get(ctx, about = "drop", pcs= "1"):
    cnt, settime = int(100), float(86400)
    reaction_member = [">>>"]
    test = discord.Embed(title=f"boss: {about} == {pcs}pcs", colour=0x1e90ff)
    test.add_field(name=f"投降後24時間で締め切り/The deadline is 24hrs after the surrender.\n", value=None, inline=True)
    msg = await ctx.send(embed=test)
    #投票の欄
    await msg.add_reaction('⏫')
    await msg.add_reaction('✖')

    def check(reaction, user):
        emoji = str(reaction.emoji)
        if user.bot == True:    # botは無視
            pass
        else:
            return emoji == '⏫' or emoji == '✖'

    while len(reaction_member)-1 <= cnt:
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=settime, check=check)
        except asyncio.TimeoutError:
            await ctx.send('締め切り！/CLOSED!')
            break
        else:
            print(str(reaction.emoji))
            if str(reaction.emoji) == '⏫':
                reaction_member.append(user.name)
                cnt -= 1
                test = discord.Embed(title=f"boss: {about} == {pcs}pcs",colour=0x1e90ff)
                test.add_field(name=f"投降後24時間で締め切り/The deadline is 24hrs after the surrender.\n", value='\n'.join(reaction_member), inline=True)
                await msg.edit(embed=test)

                if cnt == 0:
                    test = discord.Embed(title=about,colour=0x1e90ff)
                    test.add_field(name=f"投降後24時間で締め切り/The deadline is 24hrs after the surrender.\n", value='\n'.join(reaction_member), inline=True)
                    await msg.edit(embed=test)
                    finish = discord.Embed(title=f"boss: {about} == {pcs}pcs",colour=0x1e90ff)
                    finish.add_field(name=f"投降後24時間で締め切り/The deadline is 24hrs after the surrender.",value='\n'.join(reaction_member), inline=True)
                    await ctx.send(embed=finish)

            elif str(reaction.emoji) == '✖':
                if user.name in reaction_member:
                    reaction_member.remove(user.name)
                    cnt += 1
                    test = discord.Embed(title=f"boss: {about} == {pcs}pcs",colour=0x1e90ff)
                    test.add_field(name=f"投降後24時間で締め切り/The deadline is 24hrs after the surrender.\n", value='\n'.join(reaction_member), inline=True)
                    await msg.edit(embed=test)
                else:
                    pass
        # リアクション消す。メッセージ管理権限がないとForbidden:エラーが出ます。
        await msg.remove_reaction(str(reaction.emoji), user)



client.run(token)
