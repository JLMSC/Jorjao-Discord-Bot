from random import choice
from datetime import datetime
from discord.errors import Forbidden
from Commands.Execute import commands
from Configurations import prefix, token
from Assets.Icons.ChangeIcon import change_icon
from discord import Client, ChannelType, Embed, Status, Game

client = Client()

@client.event
async def on_ready():
  print(f"[+] {client.user.name} is now on-line")
  await change_icon(datetime.now().strftime("%m").replace("0", ""), client)
  await client.change_presence(
    status=choice([Status.online, Status.idle, Status.dnd]),
    activity=Game(f"J!ajuda em {len(client.guilds)} servidor(es).")
  )

@client.event
async def on_message(message):
  if not message.author.bot and message.channel.type is ChannelType.text:
    has_prefix = str(message.content).lower().startswith(prefix, 0, 2)
    command_used = str(message.content).split(" ")[0][2::].lower()
    if has_prefix and command_used in commands:
      try:
        await message.delete()
        await commands[command_used](message, client, client.get_guild(
          message.guild.id).get_member(message.author.id).top_role.color)
      # No "manage_messages" or "send_messages" permission.
      except Forbidden:
        await message.channel.send(
          embed=Embed(
            title="Não tenho `Gerenciar Mensagens` ativado em meu cargo.",
            color=0xFFFF00
          ).set_author(
            name="Permissões necessárias",
            icon_url=client.user.avatar_url
          )
        )

client.run(token)