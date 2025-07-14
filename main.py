import discord
from discord.ext import commands
import config
import asyncio
import random
from datetime import datetime

# Function to create and run a bot for a single account
async def run_account(account):
    account_id = account.get('token', 'Unknown')[:10] + "..."
    print(f'[{datetime.now().strftime("%H:%M:%S")}] Starting account: {account_id}')
    
    bot = commands.Bot(command_prefix="!", self_bot=True)
    sleeping = account['sleep']

    async def spam():
        message_count = 0
        while not sleeping:
            try:
                channel = bot.get_channel(int(account['SpamId']))
                if channel is None:
                    print(f'[{datetime.now().strftime("%H:%M:%S")}] Account {account_id}: Channel not found')
                    await asyncio.sleep(5)
                    continue
                
                result = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=13))
                await channel.send(result)
                message_count += 1
                
                random_interval = random.uniform(1, 4)
                await asyncio.sleep(random_interval)
                
            except discord.Forbidden:
                print(f'[{datetime.now().strftime("%H:%M:%S")}] Account {account_id}: Permission denied')
                await asyncio.sleep(10)
            except discord.HTTPException as e:
                print(f'[{datetime.now().strftime("%H:%M:%S")}] Account {account_id}: HTTP error - {e}')
                await asyncio.sleep(5)
            except Exception as e:
                print(f'[{datetime.now().strftime("%H:%M:%S")}] Account {account_id}: Error - {e}')
                await asyncio.sleep(5)

    @bot.event
    async def on_ready():
        print(f'\033[91mLOGGED IN AS {bot.user.name} ({bot.user.id})\033[0m')
        print(f'\033[91mSERVER STATUS: ONLINE\033[0m')
        print(f'\033[91mMade by amansingh903\033[0m')
        print(f'\033[91m------------------------------------------------------------------------------------------\033[0m')
        
        if account['SpamId']:
            await spam()

    @bot.event
    async def on_disconnect():
        print(f'[{datetime.now().strftime("%H:%M:%S")}] Account {account_id}: DISCONNECTED')

    try:
        await bot.start(account['token'])
    except discord.LoginFailure:
        print(f'[{datetime.now().strftime("%H:%M:%S")}] Account {account_id}: INVALID TOKEN')
    except Exception as e:
        print(f'[{datetime.now().strftime("%H:%M:%S")}] Account {account_id}: STARTUP ERROR - {e}')

# Main entry point to run all accounts
async def main():
    print(f'[{datetime.now().strftime("%H:%M:%S")}] Starting {len(config.accounts)} accounts')
    tasks = [run_account(account) for account in config.accounts]
    await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f'[{datetime.now().strftime("%H:%M:%S")}] Bot stopped by user')
    except Exception as e:
        print(f'[{datetime.now().strftime("%H:%M:%S")}] FATAL ERROR: {e}')
