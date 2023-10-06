import discord
from discord.ext import commands # discord ext폴더에서 commands와 tasks를 불러온다고 지정

TOKEN = '' #디스코드 봇 토큰
YONYOO_ID = "929382649036959816" #연우 디스코드 사용자 ID
 
bot = commands.Bot(command_prefix='!',intents=discord.Intents.all()) #!로 명령어 시작
 
@bot.event # 준비되었을 때 콘솔에 Login bot: 꾸말라 #9082 출력
async def on_ready():
    print(f'Login bot: {bot.user}')
    await bot.change_presence(activity=discord.Game('함무드해비디'), status=discord.Status.idle) # idle: 자리비움, dnd: 방해금지, offline: 오프라인
 
@bot.command(aliases=['겐신', '탈모', '개탈모']) #!원신 입력했을 때 아래 메시지 출력
async def 원신(ctx): # 명령어를 입력한 사람을 ctx라고 변수를 지정
    embed=discord.Embed(title='안녕하세요!^^ 꾸말라입니다', description=f'<@{YONYOO_ID}>님! 원신 시작하신다고요?\n다운로드 링크 첨부해 드려요^^\n[PC 다운로드](https://sg-public-api.hoyoverse.com/event/download_porter/link/ys_global/genshinimpactpc/default) [iOS 다운로드](https://apps.apple.com/kr/app/id1517783697)')
    embed.set_thumbnail(url='https://pbs.twimg.com/media/Du7PpoQVsAEqmTG.jpg')
    await ctx.send(embed=embed)
    # await ctx.channel.send(f'안녕하세요!^^ 꾸말라입니다\n<@{YONYOO_ID}>님! 원신 시작하신다고요?\n다운로드 링크 첨부해 드려요^^\n[PC 다운로드](https://sg-public-api.hoyoverse.com/event/download_porter/link/ys_global/genshinimpactpc/default) [iOS 다운로드](https://apps.apple.com/kr/app/id1517783697)')

bot.run(TOKEN)