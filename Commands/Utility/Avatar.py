from discord import Embed

async def avatar(message, client, color):
  """Shows your picture os someone's profile picture."""
  message_in = str(message.content).split(" ")
  if len(message_in) > 1:
    target = client.get_user(
      int("".join(c for c in message_in[1] if c.isdigit()))
    )
    await message.channel.send(
      embed=Embed(title=f"`Avatar de {target.name}`", color=color)
      .set_image(url=target.avatar_url))
  else:
    await message.channel.send(
      embed=Embed(title=f"`Avatar de {message.author.name}`", color=color)
      .set_image(url=message.author.avatar_url))