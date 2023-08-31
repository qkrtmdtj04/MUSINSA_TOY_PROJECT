import nest_asyncio # 무조건 실행해야 오류 안생김
nest_asyncio.apply() # 무조건 실행해야 오류 안생김
import discord
from discord.ext import commands
from discord.ui import Button, View
from discord.utils import get


from crawling_def import musinsa


client = commands.Bot(command_prefix='!',intents=discord.Intents.all())
 
@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)


clothes_all = []   #이놈 초기화 명령어

@client.command()
async def mu(ctx,*,text):
    global clothes_all
    clothes_all = [] 
    await ctx.send("환경 설정 시작하겠습니다 :)") 
    print(text)
    for i in range(1,6):
        clothes_all.append(musinsa(text,i)) #후드티 5개[0~4] -> 셔츠 5
        await ctx.send(f"{i}번째 설정 완료!")

    #환경설정 명령어에서 txt 파일에다가 명령어 저장



# 환경설정 => chat GPT => 옷이 좋다 => 디코봇 작동하는거죠 => 오류날거 같긴한데 세팅값이 없으면 na 

@client.command()
async def 버튼(ctx):
    text = '셔츠' #테스트 chat GPT
    global clothes_all
    button1 = Button(label="1번 버튼", style = discord.ButtonStyle.green)
    button2 = Button(label="2번 버튼", style = discord.ButtonStyle.green)
    button3 = Button(label="3번 버튼", style = discord.ButtonStyle.green)
    button4 = Button(label="4번 버튼", style = discord.ButtonStyle.green)
    button5 = Button(label="5번 버튼", style = discord.ButtonStyle.green)

    # clothes_all[0][0] 첫번째 괄호 옷 종류 // 두번째 괄호 해당 옷 0:이름 ,1: url, 2:가격  



    async def button_callback1(interaction:discord.Interaction):
        await interaction.response.send_message('1번 버튼 클릭!')
        embed=discord.Embed(title="URL", url=clothes_all[0][1], description="1번 버튼에 해당하는 정보입니다.", color=0x1100ff)
        embed.set_author(name=clothes_all[0][0])
        embed.set_thumbnail(url=clothes_all[0][4])
        embed.add_field(name="가격", value=clothes_all[0][2], inline=True)
        embed.add_field(name="누적판매(1년)", value=clothes_all[0][3], inline=True)
        embed.add_field(name="평점", value=clothes_all[0][5], inline=True)
        await ctx.send(embed=embed)

    async def button_callback2(interaction:discord.Interaction):
        await interaction.response.send_message("2번 버튼 클릭!")
        embed=discord.Embed(title="URL", url=clothes_all[1][1], description="2번 버튼에 해당하는 정보입니다.", color=0x1100ff)
        embed.set_author(name=clothes_all[1][0])
        embed.set_thumbnail(url=clothes_all[1][4])
        embed.add_field(name="가격", value=clothes_all[1][2], inline=True)
        embed.add_field(name="누적판매(1년)", value=clothes_all[1][3], inline=True)
        embed.add_field(name="평점", value=clothes_all[1][5], inline=True)
        await ctx.send(embed=embed)


    async def button_callback3(interaction:discord.Interaction):
        await interaction.response.send_message("3번 버튼 클릭!")
        embed=discord.Embed(title="URL", url=clothes_all[2][1], description="3번 버튼에 해당하는 정보입니다.", color=0x1100ff)
        embed.set_author(name=clothes_all[2][0])
        embed.set_thumbnail(url=clothes_all[2][4])
        embed.add_field(name="가격", value=clothes_all[2][2], inline=True)
        embed.add_field(name="누적판매(1년)", value=clothes_all[2][3], inline=True)
        embed.add_field(name="평점", value=clothes_all[2][5], inline=True)
        await ctx.send(embed=embed)

    async def button_callback4(interaction:discord.Interaction):
        await interaction.response.send_message("4번 버튼 클릭!")
        embed=discord.Embed(title="URL", url=clothes_all[3][1], description="4번 버튼에 해당하는 정보입니다.", color=0x1100ff)
        embed.set_author(name=clothes_all[3][0])
        embed.set_thumbnail(url=clothes_all[3][4])
        embed.add_field(name="가격", value=clothes_all[3][2], inline=True)
        embed.add_field(name="누적판매(1년)", value=clothes_all[3][3], inline=True)
        embed.add_field(name="평점", value=clothes_all[3][5], inline=True)
        await ctx.send(embed=embed)

    async def button_callback5(interaction:discord.Interaction):
        await interaction.response.send_message("5번 버튼 클릭!")
        embed=discord.Embed(title="URL", url=clothes_all[4][1], description="5번 버튼에 해당하는 정보입니다.", color=0x1100ff)
        embed.set_author(name=clothes_all[4][0])
        embed.set_thumbnail(url=clothes_all[4][4])
        embed.add_field(name="가격", value=clothes_all[4][2], inline=True)
        embed.add_field(name="누적판매(1년)", value=clothes_all[4][3], inline=True)
        embed.add_field(name="평점", value=clothes_all[4][5], inline=True)
        await ctx.send(embed=embed)

    button1.callback = button_callback1
    button2.callback = button_callback2
    button3.callback = button_callback3
    button4.callback = button_callback4
    button5.callback = button_callback5

    view = View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)
    view.add_item(button5)
    embed=discord.Embed(title="메뉴 선택하기", description="원하시는 옷을 선택하세요", color=0xffffff)
    embed.add_field(name=1, value= clothes_all[0][0], inline=False)
    embed.add_field(name=2, value= clothes_all[1][0], inline=False)
    embed.add_field(name=3, value= clothes_all[2][0], inline=False)
    embed.add_field(name=4, value= clothes_all[3][0], inline=False)
    embed.add_field(name=5, value= clothes_all[4][0], inline=False)
    await ctx.send(embed=embed,view=view) 

 

client.run('YOUR TOKEN') #토큰



