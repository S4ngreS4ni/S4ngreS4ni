from asyncio.tasks import sleep
import discord
import credentials
import calendars
import help_msg
import globals

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    """ if message.content.startswith('!kalendarz'):
        await message.channel.send() """

# KOMENDA !KALENDARZ
    if message.content == '!kalendarz':
        await message.channel.send('*Jaki kalendarz? Majów?\nSkopałeś to. Wpisz \
!skokobot help by zobaczyć dostępne komendy.*')

    if message.content == '!kalendarz lgp':
        calendars.Message.barColour = 15158332  # RED
        cal = calendars.Message('lgp').create_message()
        for i in range(len(cal)):
            embed = cal[i]
            await message.author.send(embed=embed)
            await sleep(0.5)
    elif message.content == '!kalendarz ps':
        calendars.Message.barColour = 3447003  # BLUE
        cal = calendars.Message('ps').create_message()
        for i in range(len(cal)):
            embed = cal[i]
            await message.author.send(embed=embed)
            await sleep(0.5)
    elif message.content == '!kalendarz coc':
        calendars.Message.barColour = 3426654  # NAVY
        cal = calendars.Message('coc').create_message()
        for i in range(len(cal)):
            embed = cal[i]
            await message.author.send(embed=embed)
            await sleep(0.5)
    elif message.content == '!kalendarz lcoc':
        calendars.Message.barColour = 10038562  # DARK RED
        cal = calendars.Message('letni_coc').create_message()
        for i in range(len(cal)):
            embed = cal[i]
            await message.author.send(embed=embed)
            await sleep(0.5)
    elif message.content == '!kalendarz fc':
        calendars.Message.barColour = 15105570  # ORANGE
        cal = calendars.Message('fis_cup').create_message()
        for i in range(len(cal)):
            embed = cal[i]
            await message.author.send(embed=embed)
            await sleep(0.5)

# KOMENDA !KIEDYSKOKI
    globals.initialize_comptype()
    if message.content == '!kiedyskoki':
        await message.channel.send('*A konkretnie? Jaki event?\nSprawdź \
dostępne komendy wpisując !skokobot help*')
    elif message.content == '!kiedyskoki lgp':
        globals.compType = 'lgp'
        import kiedyskoki
        await message.author.send(embed=kiedyskoki.create_message())
    elif message.content == '!kiedyskoki ps':
        globals.compType = 'ps'
        import kiedyskoki
        await message.author.send(embed=kiedyskoki.create_message())
    elif message.content == '!kiedyskoki coc':
        globals.compType = 'coc'
        import kiedyskoki
        await message.author.send(embed=kiedyskoki.create_message())
    elif message.content == '!kiedyskoki lcoc':
        globals.compType = 'letni_coc'
        import kiedyskoki
        await message.author.send(embed=kiedyskoki.create_message())
    elif message.content == '!kiedyskoki fc':
        globals.compType = 'fis_cup'
        import kiedyskoki
        await message.author.send(embed=kiedyskoki.create_message())

# KOMENDA !SKOKOBOT HELP
    if message.content == '!skokobot help':
        await message.author.send(embed=help_msg.helpKalendarz)

client.run(credentials.token)
