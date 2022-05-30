import discord, asyncio, pytz, datetime
import os

client = discord.Client()


@client.event 
async def on_message(message):
  if message.content.startswith ("!공지"):
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[4:]
            channel = client.get_channel(970683398337208442)
            embed = discord.Embed(title="**후레초등학교 공지사항**", description="공지사항은 꼭 따라주십시오!\n――――――――――――――――――――――――――――\n\n{}\n\n――――――――――――――――――――――――――――".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. 그린애플 #8471 | 담당 관리자 : {}".format(message.author), icon_url="https://media.discordapp.net/attachments/974672463596228678/980718934930116628/unknown.png")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/974672463596228678/980718934930116628/unknown.png")
            await channel.send ("@everyone", embed=embed)
            await message.author.send("*[ BOT 자동 알림 ]* | 정상적으로 공지가 채널에 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}".format(channel, message.author, notice))
 
        if i is False:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))

@client.event 
async def on_message(message):
  if message.content.startswith ("!청소"):
        i = (message.author.guild_permissions.administrator)

        if i is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n관리자 {}님의 요청으로 인해 정상 삭제 조치 되었습니다".format(amount, message.author), color=0x000000)
            embed.set_footer(text="Bot Made by. 바코드 #1741", icon_url="https://media.discordapp.net/attachments/974672463596228678/980718934930116628/unknown.png")
            await message.channel.send(embed=embed)
        
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))

@client.event

async def on_message(message):

    if message.content.startswith ("!인증 "):
        if message.author.guild_permissions.change_nickname:
            await message.delete()
            user = message.mentions[0]

            embed = discord.Embed(title="인증 시스템", description="인증이 정상적으로 완료 되었습니다 !",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.add_field(name="인증 대상자", value=f"{user.name} ( {user.mention} )", inline=False)
            embed.add_field(name="담당 관리자", value=f"{message.author} ( {message.author.mention} )", inline=False)
            embed.set_footer(text="Bot Made by. 그린애플 #8471")
            await message.author.send (embed=embed)
            role = discord.utils.get(message.guild.roles, name = '1학년')
            await user.add_roles(role)

        else:
            await message.delete()
            await message.channel.send(embed=discord.Embed(title="권한 부족", description = message.author.mention + "님은 권한이 없습니다", color = 0x00ff13))

@client.event
async def on_message(message):
    if message.content == "!서버정보": # 메세지 감지
        embed = discord.Embed(title="제목", description="부제목",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x01ff00)

        embed.add_field(name="개설 : 2022년 5월 2일", value="따끈따끈한 서버", inline=False)
        embed.add_field(name="채널 개수 : 45", value="관리자 채널 제외, 음성채널 제외", inline=False)

        embed.add_field(name="봇의 수 : 8", value="미인증 봇의 수 : 2", inline=True)
        embed.add_field(name="개교기념일 : ~~~~년 5월 2일", value="~~~~년 5월 2일은 수업 없습니다.", inline=True)

        embed.set_footer(text="Bot Made by. 그린애플 #8471", icon_url="https://media.discordapp.net/attachments/974672463596228678/980718934930116628/unknown.png")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/974672463596228678/980718934930116628/unknown.png")
        await message.channel.send (embed=embed)



@client.event
async def on_message(message):
  if message.content == "!온라인":
    await message.channel.send (f"저는 온라인입니다!")

@client.event
async def on_message(message):
  if message.content == "!청사과야":
    await message.channel.send (f"넵! 다기능(까진 아닌가?)봇 청사과 봇 입니다!")

@client.event
async def on_message(message):
  if message.content == "!명령어":
    await message.channel.send (f"현재는 !온라인, !청사과야, !명령어 밖에 없어요 ㅠㅠ")

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("봇이 켜졌습니다!")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("봇 테스트 중입니다."))

access_token = os.environ['BOT_TOKEN']                                    
client.run(access_token)
