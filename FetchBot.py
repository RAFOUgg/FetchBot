import discord
from discord.ext import commands


#[SETTINGS]
token = ('TOKEN HERE')
client = discord.Client()

client = commands.Bot(command_prefix="r!")
client.remove_command("help")


@client.event
async def on_ready():
    activity = discord.Game(name="RAFOUgg\FetchBot | r!", type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print("Client ready to use !")



#[COMMANDS]


#[FETCH STATS]
@client.command()
async def fetch(ctx):

    if len(ctx.message.channel_mentions) == 1:
        target_channel = ctx.message.channel_mentions[0]
    else:
        target_channel = ctx.channel

    try:
        fetch_target = ctx.message.mentions[0]
    except:
        return await ctx.reply(f"**Error in the command, please use __{client.command_prefix}fetch @user #channel__**")

    target_messages_counter = 0
    total_messages_counter = 0

    async for msg in target_channel.history(limit=10000):
        if msg.author == fetch_target:
            target_messages_counter += 1
        total_messages_counter += 1

    percent_messages_target = (target_messages_counter / total_messages_counter) * 100
    percent_messages_target_cutted = round(percent_messages_target,2)

    dp_name = str(ctx.message.author)[:-5]
    embed = discord.Embed(title=f"Fetch de {fetch_target}", color=0x9975b9)
    embed.set_author(name=dp_name, icon_url=ctx.message.author.avatar_url)
    embed.add_field(name="Number of messages :", value=f"{fetch_target.mention} has sent : {target_messages_counter} messages in {target_channel.mention}",inline=False)
    embed.add_field(name="Percent of messages :", value=f"{fetch_target.mention} has sent : {percent_messages_target_cutted}% of messages in {target_channel.mention}",inline=False)
    embed.set_footer(text="Made by RAFOU , KodeSade and OverTube !")
    await ctx.reply(embed=embed)



#[SECRETSTORY]
@client.command()
async def secretstory(ctx):
    dp_name = str(ctx.message.author)[:-5]
    embed = discord.Embed()
    embed.set_author(name=dp_name, icon_url=ctx.message.author.avatar_url)
    embed.add_field(name="Conway...", value="This game will forever remain in our hearts...")
    embed.add_field(name="Delta Place", value="A community of very respectable junkies :)")
    embed.add_field(name="Ocram...", value="Deserter... nothings more.")
    embed.set_footer(text="Made by RAFOU , KodeSade and OverTube !")
    await ctx.send(embed=embed)


#[CREDENTIALS]
@client.command()
async def creds(ctx): 
    dp_name = str(ctx.message.author)[:-5]
    embed = discord.Embed()
    embed.set_author(name=dp_name, icon_url=ctx.message.author.avatar_url)
    embed.add_field(name="RAFOU", value="**Github :** https://github.com/RAFOUgg \n __Owner of the bot.__")
    embed.add_field(name="OverTube", value="**Github :** https://github.com/0verTube \n __A developper of the bot.__")
    embed.add_field(name="Kodesade", value="**Github :** https://github.com/Kodesade \n __A developper of the bot.__")
    embed.set_footer(text="Made by RAFOU , KodeSade and OverTube !")
    await ctx.send(embed=embed)

#[SALVIA CALC MESSAGES]
@client.command()
async def scalc(ctx, filtrage=None):
    if not filtrage:
        return await ctx.reply(f"**Error in the command, please use __{client.command_prefix}scalc [filtering].__**")
    filtrage = float(filtrage)
    dp_name = str(ctx.message.author)[:-5]
    embed = discord.Embed(title="Saliva Dosages Calculator :")
    embed.set_author(name=dp_name, icon_url=ctx.message.author.avatar_url)
    #SET DOSAGES
    Light = 0.25 / filtrage
    Common = 0.5 / filtrage
    Strong = 0.75 / filtrage
    Heavy = 1 / filtrage
    PLight = round(Light,3)
    PCommon = round(Common,3)
    PStrong = round(Strong,3)
    PHeavy = round(Heavy,3)

    embed.add_field(name=f"__Dosages for x{filtrage}__", value=f"(*Smocked & Sublingual*) \n **Light**:{PLight}g \n **Common**:{PCommon}g \n **Strong**:{PStrong}g \n **Heavy**:{PHeavy}g")
    embed.set_footer(text="Made by RAFOU , KodeSade and OverTube !")
    await ctx.send(embed=embed)

#[BIODISPINIBILITE KETAMINE]
@client.command()
async def bioketa(ctx):
    dp_name = str(ctx.message.author)[:-5]
    embed = discord.Embed(title="Bioavailability of K??tamine :")
    embed.set_author(name=dp_name, icon_url=ctx.message.author.avatar_url)
    embed.add_field(name="Bioavailability", value=f"**Intravenous**: 100% \n **Intramuscular**: 93% \n **Nasal**: 25%-50% \n **Rectal**: 20% \n **Sublingual**: 30% \n **Oral** 16%-24% \n")
    embed.set_footer(text="Made by RAFOU , KodeSade and OverTube !")
    await ctx.send(embed=embed)

#[COMBOCHART]
@client.command()
async def combochart(ctx):
    await ctx.reply("https://raw.githubusercontent.com/RAFOUgg/FetchBot/main/bin/ComboChart-v4.jpg")

#[BREATH HELPING]
@client.command()
async def breathe(ctx):
    await ctx.reply("https://raw.githubusercontent.com/RAFOUgg/FetchBot/main/bin/breathe2.gif")

#[CLEAR MESSAGES]
@client.command()
async def purge(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"The messages are deleted !")


#[RICKROLLED]
@client.command()
async def rick(ctx):
    await ctx.send('||**RickRolled**||')
    await ctx.send('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


#[ADMIN HELP]
@client.command()
async def admin(ctx):
    embed = discord.Embed(title=f"[ Prefix is {client.command_prefix} ]", color=0x9975b9)
    embed.set_author(name=f"Help:")
    embed.add_field(name='clear',value='`Clear all messages in the channel.`',inline=False)
    embed.set_footer(text="Made by RAFOU , KodeSade and OverTube !")
    await ctx.send(embed=embed)
            

#[IMPORTANTS LINKS]
@client.command()
async def links(ctx):
    dp_name = str(ctx.message.author)[:-5]
    embed = discord.Embed(title=f"Link:", color=0x9975b9)
    embed.set_author(name=dp_name, icon_url=ctx.message.author.avatar_url)
    embed.add_field(name="Psychonaut:", value="[Psychonaut](https://www.psychonaut.fr/portal.php)", inline=True)
    embed.add_field(name="Psychoactif:", value="[PsychoActif](https://www.psychoactif.org/forum/index.php)", inline=True)
    embed.add_field(name="TripSit:", value="[TripSit](https://tripsit.me/)", inline=True)
    embed.add_field(name="Mixtures:", value="[Mixtures](https://mixtures.info/fr/)", inline=True)
    embed.add_field(name="Delta Plane:", value="[Delta Plane](https://www.youtube.com/channel/UCBrT-3mepRSPOfO9aDdvJ2A)", inline=True)
    embed.add_field(name="Calcoolateur:", value="[Calcoolateur](https://www.educalcool.qc.ca/vos-outils/calcoolateur/)", inline=True)
    embed.set_footer(text="Made by RAFOU , KodeSade and OverTube !")
    await ctx.send(embed=embed)


#[HELP]
@client.command()
async def help(ctx):
    embed = discord.Embed(title=f"[ Prefix is {client.command_prefix} ]", color=0x9975b9)
    embed.set_author(name=f"Help:")
    embed.add_field(name='fetch',value='`Fetch the statistic of sent messages by a member.`',inline=False)
    embed.add_field(name='links',value='`Show the importance links for risks reduction.`',inline=False)
    embed.add_field(name='breath',value='`Show a breath helping gif.`',inline=False)
    embed.add_field(name='combochart',value='`Show the combochart-v.4 image.`',inline=False)
    embed.add_field(name='bioketa',value='`Show the bioavailability of k??tamine.`',inline=False)
    embed.add_field(name='scalc',value='`Calcul the dosages for salvia.`',inline=False)
    embed.add_field(name='creds',value='`Show credentials of the bot.`',inline=False)
    embed.add_field(name='rick',value='`Send a RickRoll links.`',inline=False)
    embed.set_footer(text="Made by RAFOU , KodeSade and OverTube !")
    await ctx.send(embed=embed)


#[START BOT]
client.run(token)
