from asyncio import sleep
from discord.utils import oauth_url
from discord.errors import Forbidden
from discord import Embed, Permissions

async def invite(message, client, color):
  """Return the bot's invite url."""
  async with message.channel.typing():
    await sleep(1)
    await message.channel.send(
      embed=Embed(title="**C O N V I T E**!",
                  url=oauth_url(client.user.id, Permissions(10860)),
                  color=color)
      .set_thumbnail(url=client.user.avatar_url)
      .add_field(name=f"👤 **DE**: *{client.user.name}*",
                 value="🗓️ **Dia**: *HOJE*\n"
                       "🕛 **Horário**: *Ja ja*\n"
                       f"🏠 **Local**: *No seu servidor*")
      .set_footer(text="Conto com você!")
    )