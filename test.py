import discord, datetime, asyncio #모듈 불러오기
token = "NzkxNTU3MTI1MDQ5Njc5ODg1.X-Q5BQ.5iQ2T_0i4WIcF91twVHCJx00pHc" #봇 토큰 설정하기
client = discord.Client() #client 설정하기

@client.event
async def on_ready(): #봇이 준비 되었을 때
    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다')
    game = discord.Game('봇 상태메시지 ~하는중')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message): #메시지 답하기
    if message.content == "현우":
        await message.channel.send("현짱블라디미르푸틴대검버섯!")

@client.event
async def on_message(message): #임베드(프로필)
    if message.content.startswith("!정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(urI=message.author.urI)
        await client.send_message(message.channel, embed=embed)

client.run(token)