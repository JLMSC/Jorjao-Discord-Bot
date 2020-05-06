from discord import Embed
from unicodedata import name
from emoji import UNICODE_EMOJI

async def emote(message, client, color):
  """Show a emote's image in a large scale."""
  emote = str(message.content).split(" ")[1]
  # If it's not a custom emote.
  try:
    if emote in UNICODE_EMOJI:
      emote_name = str(name(emote)).lower().replace(" ", "-")
      emote_unicode = u"{}".format(emote).encode("unicode-escape")
      emote_unicode_str = ("%s" % emote_unicode
                           ).replace("b'\\\\U000", ""
                                     ).replace("b'\\\\u", "")
      final_url = f"https://emojipedia-us.s3.dualstack.us-west-1.amazonaws" \
                    f".com/thumbs/120/twitter/236/{emote_name}" \
                    f"_{emote_unicode_str[:-1]}.png"
      await message.channel.send(
        embed=Embed(color=color)
        .set_author(name=emote_name.replace("-", " ").capitalize(),
                    icon_url=message.author.avatar_url)
        .set_image(url=final_url)
      )
    # Custom emote only
    else:
      custom_emote = client.get_emoji(int(emote.split(":")[-1][:-1]))
      await message.channel.send(
        embed=Embed(color=color)
        .set_author(name=str(custom_emote.name).capitalize(),
                    icon_url=message.author.avatar_url)
        .set_image(url=custom_emote.url)
      )
  # Invalid entry.
  except (TypeError, AttributeError, ValueError):
    await message.channel.send(
      embed=Embed(title="O Emote inserido não é válido.", color=0xFFFF00))