from selenium.webdriver.chrome.options import *
from selenium import webdriver
from discord.ext import commands
import discord
import requests
from bs4 import BeautifulSoup
import time
import os

token = os.environ['BOT_TOKEN']



bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(bot.user.name)
    print('connection was succesful')
    await bot.change_presence(status=discord.Status.online, activity=None)

@bot.command()
async def 유저(ctx, *, nickname):
    # Selenium 웹 드라이버 설정
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
  # 웹드라이버 경로에는 실제 웹드라이버 파일의 경로를 입력해야 합니다.
 
    # 검색 페이지 URL
    search_url = 'https://barracks.sa.nexon.com/search'
    
    # 검색 페이지로 이동
    driver.get(search_url)
  
    # 검색 결과 URL 추출
    result_url = driver.current_url
    # 디스코드에 정보 전송
    await ctx.send(result_url)
    driver.quit()


bot.run(token)

