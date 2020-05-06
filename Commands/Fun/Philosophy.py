from textwrap import wrap
from random import choice
from os import path, listdir
from PIL.ImageDraw import Draw
from discord import File, Embed
from PIL.ImageFont import truetype
from discord.errors import Forbidden
from PIL.Image import open as op_img

async def philosophy(message, *args):
  """Show your message as some philosopher's mention."""
  msg = str(message.content).split(" ")[1:]
  if len(msg) != 0:

    def is_mixed(text):
      return any(_.islower() for _ in text) and any(_.isupper() for _ in text)

    user_text = " ".join(str(_) for _ in msg)

    async def define_message_length_limit():
      line_limit, wrap_limit = 250, 0
      if is_mixed(user_text):
        wrap_limit, line_limit = 28, 208
      elif user_text.isupper():
        wrap_limit, line_limit = 24, 185
      else:
        wrap_limit = 35

      async def write_text():
        if not len("".join(str(_) for _ in msg)) > line_limit:
          try:
            file_dir = "Assets\\PhilosophyImages"
            file = choice(
              [_ for _ in listdir(file_dir)
               if path.isfile(path.join(file_dir, _))])

            def center_text(image, text, color, font):
              draw = Draw(image)
              width, height = image.size
              text_width, text_height = draw.textsize(text, font)
              position = (
                (width - text_width) / 2 + 100,
                ((height - (text_height * 1.5)) / 2)
              )
              draw.text(position, text, color, font)
              image.save("Assets\\PhilosophyImages\\temporary.png")

            center_text(image=op_img(f"{file_dir}/{file}"),
                        text="\n".join(wrap(text=user_text, width=wrap_limit)),
                        color=(255, 255, 255),
                        font=truetype("times", 16))
            await message.channel.send(
              file=File(
                fp=open("Assets\\PhilosophyImages\\temporary.png", "rb")
              )
            )
          # No "attach_files" permission.
          except Forbidden:
            await message.channel.send(
              embed=Embed(
                title="Permissões insuficientes:",
                description="*Não tenho `attach_files` ativada no canal ou no "
                            "meu cargo*.",
                color=0xFFFF00
              )
            )
        else:
          await message.channel.send(
            embed=Embed(
              title="**Limite máximo atingido**",
              description="Você ultrapassou o limite de caracteres permitido.",
              color=0xFFFF00
            )
          )
      await write_text()
    await define_message_length_limit()
  else:
    await message.channel.send(
      embed=Embed(
        title="**Mesagem inválida**",
        description="Nenhuma mensagem foi inserida.",
        color=0xFFFF00
      )
    )