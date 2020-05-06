from asyncio import sleep
from discord.errors import HTTPException

async def say(message, *args):
  """Send a message with bot as author."""
  try:
    async with message.channel.typing():
      await sleep(1)
      await message.channel.send(
        content=" ".join(str(_) for _ in str(message.content).split(" ")[1:])
      )
  # Empty message.
  except HTTPException: pass