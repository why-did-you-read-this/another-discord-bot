# 1.0

import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()  # не удалять
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(), case_insensitive=True)
bot.remove_command('help')
gdz_dict1 = {  # Решак
    'алг': 'https://reshak.ru/otvet/reshebniki.php?otvet=~~~&predmet=nikol11',
    'гео': 'https://reshak.ru/otvet/otvet6.php?otvet1=~~~',
    'рус': 'https://reshak.ru/otvet/reshebniki.php?otvet=part2/~~~&predmet=golcova10-11',
    'физ': 'https://reshak.ru/otvet/otvet10.php?otvet1=~~~',  # --------------------------------------------------------
    'alg': 'https://reshak.ru/otvet/reshebniki.php?otvet=~~~&predmet=nikol11',
    'geo': 'https://reshak.ru/otvet/otvet6.php?otvet1=~~~',
    'rus': 'https://reshak.ru/otvet/reshebniki.php?otvet=part2/~~~&predmet=golcova10-11',
    'fis': 'https://reshak.ru/otvet/otvet10.php?otvet1=~~~',
    'fiz': 'https://reshak.ru/otvet/otvet10.php?otvet1=~~~'
}
gdz_dict2 = {  # ГДЗ
    'алг': 'https://reshak.ru/otvet/reshebniki.php?otvet=~~~&predmet=nikol11',
    'гео': 'https://reshak.ru/otvet/otvet6.php?otvet1=~~~',
    'рус': 'https://reshak.ru/otvet/reshebniki.php?otvet=part2/~~~&predmet=golcova10-11',
    'физ': 'https://reshak.ru/otvet/otvet10.php?otvet1=~~~',
    'анг': 'https://gdz.ru/class-7/english/new-afanasjeva/~~~-s/',  # --------------------------------------------------
    'alg': 'https://gdz.ru/class-11/algebra/nikolskij-potapov/~~~/',
    'geo': 'https://gdz.ru/class-10/geometria/atanasyan-10-11/11-class-~~~/',
    'rus': 'https://gdz.ru/class-10/russkii_yazik/reshebnik-golcova-n-g-shamshin-i-v/~~~-nom/',
    'fis': 'https://gdz.ru/class-11/fizika/rymkevich/~~~-nom/',
    'fiz': 'https://gdz.ru/class-11/fizika/rymkevich/~~~-nom/',
    'ang': 'https://gdz.ru/class-7/english/new-afanasjeva/~~~-s/'
}


@bot.event
async def on_ready():
    print('Bot on')
    await bot.change_presence(status=discord.Status.dnd,
                              activity=discord.Activity(type=discord.ActivityType.listening, name='рабочий народ'))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        await ctx.send(f'{ctx.author.mention} такой команды не существует.')


@bot.command(aliases=['гдз'])  # gdz
async def gdz(ctx, subject='абв', number="0"):
    l1, l2 = '', ''
    if (subject in gdz_dict1) or (subject in gdz_dict2):
        if subject in gdz_dict1:  # Решак
            l1 = gdz_dict1[subject]
            l1 = str(l1)
            l1 = ((l1.replace('~~~', number)).replace('.', '-')).replace('-', '.', 2)
        if subject in gdz_dict2:  # ГДЗ
            l2 = gdz_dict2[subject]
            l2 = str(l2)
            l2 = ((l2.replace('~~~', number)).replace('.', '-nom-')).replace('-nom-', '.', 1)
        await ctx.send(f'{l1}\n{l2}')
    else:
        await ctx.send(f'{ctx.author.mention} предмет указан не верно.')


@bot.command()  # clear
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=0):
    await ctx.message.delete()
    if amount > 0:
        await ctx.channel.purge(limit=amount)
        await ctx.send('Сообщения успешно удалены.')
    else:
        await ctx.send(f'{ctx.author.mention} указано не натуральное число.')


# ----------------------------------------------------------ERRORS------------------------------------------------------
@clear.error
async def clear_error(ctx, error):
    await ctx.channel.purge(limit=1)
    if isinstance(error, commands.errors.CommandError):
        await ctx.send(f'{ctx.author.mention} указано не натуральное число.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.mention} у вас не достаточно прав.')


bot.run(os.getenv("DISCORD_TOKEN"))
