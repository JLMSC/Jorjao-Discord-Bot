from discord import Embed

async def fbi(message, *args):
  """Send a FBI's gif in the channel."""
  await message.channel.send(
    embed=Embed(
      title="🚔 **PERDEU! PERDEU! PERDEU!** 🚔",
      description="A GENTE DESCOBRIU TEU ESQUEMA! TEJE PRESO VAGABUNDO!",
      color=0xFF0000,
    ).set_image(
      url="https://media1.tenor.com/images/334edcb20a41a037c18963e6e63cabba/tenor.gif?itemid=11411207"
    )
  )
