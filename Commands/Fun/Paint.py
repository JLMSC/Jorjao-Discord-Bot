from discord import Embed
from emoji import UNICODE_EMOJI
from asyncio import TimeoutError
from discord.errors import NotFound, Forbidden

async def paint(message, client, color):
  """Allow the user to draw something."""
  try:
    game_settings = ["⬜", "⬛"]

    def create_canvas():
      return [[0 for _ in range(9)] for _ in range(9)]
    canvas = create_canvas()

    def human_readable_canvas():
      new_canvas = canvas.copy()
      for _ in range(1, 16, 2): new_canvas.insert(_, "\n")

      letters = ["🇦", "🇧", "🇨", "🇩", "🇪", "🇫", "🇬", "🇭", "🇮"]
      for _ in range(0, 25, 3): new_canvas.insert(_, letters[int(_ / 3)])

      nums = ["⏹️", ":one:", ":two:", ":three:",
              ":four:", ":five:", ":six:",
              ":seven:", ":eight:", ":nine:", "\n"]
      for _ in range(0, len(nums)): new_canvas.insert(_, nums[_])

      def remove_nested_list(lst):
        for item in lst:
          if type(item) == list: remove_nested_list(item)
          else: plain_canvas.append(item)
      plain_canvas = []
      remove_nested_list(new_canvas)

      for _ in range(len(plain_canvas)):
        if plain_canvas[_] == 0: plain_canvas[_] = game_settings[0]
      return plain_canvas

    game_message = await message.channel.send(
      embed=Embed(
        description="".join(str(_) for _ in human_readable_canvas()),
        color=color
      ).add_field(
        name="_ _ " * 9 + "**Comandos**:",
        value="**`cor`** - Muda a cor do pincel.\n"
              "**`fundo`** - Muda a cor de fundo.\n"
              "**`reiniciar`** - Limpa o quadro.\n"
              "**`salvar`** - Salva o desenho.\n"
              "**`sair`** - Cancela o desenho.\n"
              f"cor do pincel: {game_settings[1]}"
      )
    )

    async def new_round():
      """Start a new round in the game."""
      await game_message.edit(
        embed=Embed(
          description="".join(str(_) for _ in human_readable_canvas()),
          color=color
        ).add_field(
          name="_ _ " * 9 + "**Comandos**:",
          value="**`cor`** - Muda a cor do pincel.\n"
                "**`fundo`** - Muda a cor de fundo.\n"
                "**`reiniciar`** - Limpa o quadro.\n"
                "**`salvar`** - Salva o desenho.\n"
                "**`sair`** - Cancela o desenho.\n"
                f"cor do pincel: {game_settings[1]}"
        )
      )

      def check_message(msg):
        if msg.author.id == message.author.id: return msg
      try:
        async def change_brush_color():
          await game_message.edit(
            embed=Embed(
              title="Selecione um emote e envie no chat.",
              description="Ele sera a nova cor do pincel.",
              color=color
            ).set_footer(
              text="Você tem 25 segundos, emotes customizados não serão "
                   "aceitos."
            )
          )
          new_color = await client.wait_for("message",
                                            check=check_message,
                                            timeout=25.0)
          await new_color.delete()
          new_color = str(new_color.content).lower()

          if new_color in UNICODE_EMOJI:
            game_settings[1] = new_color
          await new_round()

        async def change_background_color():
          for row in range(len(canvas)):
            for col in range(len(canvas[row])):
              canvas[row][col] = game_settings[1]
          await new_round()

        async def restart_canvas():
          for row in range(len(canvas)):
            for col in range(len(canvas[row])):
              canvas[row][col] = 0
          await new_round()

        async def save_canvas():
          await game_message.edit(
            embed=Embed(
              description="".join(str(_) for _ in human_readable_canvas()),
              color=0x00FF00
            ).set_author(
              name=f"Desenho de {message.author.name}",
              icon_url=message.author.avatar_url
            )
          )

        commands = {
          "cor": change_brush_color,
          "fundo": change_background_color,
          "reiniciar": restart_canvas,
          "salvar": save_canvas
        }

        user_message = await client.wait_for("message",
                                             check=check_message,
                                             timeout=60.0)
        await user_message.delete()
        places = {"a1": [0, 0], "a2": [0, 1], "a3": [0, 2], "a4": [0, 3],
                  "a5": [0, 4], "a6": [0, 5], "a7": [0, 6], "a8": [0, 7],
                  "a9": [0, 8], "b1": [1, 0], "b2": [1, 1], "b3": [1, 2],
                  "b4": [1, 3], "b5": [1, 4], "b6": [1, 5], "b7": [1, 6],
                  "b8": [1, 7], "b9": [1, 8], "c1": [2, 0], "c2": [2, 1],
                  "c3": [2, 2], "c4": [2, 3], "c5": [2, 4], "c6": [2, 5],
                  "c7": [2, 6], "c8": [2, 7], "c9": [2, 8], "d1": [3, 0],
                  "d2": [3, 1], "d3": [3, 2], "d4": [3, 3], "d5": [3, 4],
                  "d6": [3, 5], "d7": [3, 6], "d8": [3, 7], "d9": [3, 8],
                  "e1": [4, 0], "e2": [4, 1], "e3": [4, 2], "e4": [4, 3],
                  "e5": [4, 4], "e6": [4, 5], "e7": [4, 6], "e8": [4, 7],
                  "e9": [4, 8], "f1": [5, 0], "f2": [5, 1], "f3": [5, 2],
                  "f4": [5, 3], "f5": [5, 4], "f6": [5, 5], "f7": [5, 6],
                  "f8": [5, 7], "f9": [5, 8], "g1": [6, 0], "g2": [6, 1],
                  "g3": [6, 2], "g4": [6, 3], "g5": [6, 4], "g6": [6, 5],
                  "g7": [6, 6], "g8": [6, 7], "g9": [6, 8], "h1": [7, 0],
                  "h2": [7, 1], "h3": [7, 2], "h4": [7, 3], "h5": [7, 4],
                  "h6": [7, 5], "h7": [7, 6], "h8": [7, 7], "h9": [7, 8],
                  "i1": [8, 0], "i2": [8, 1], "i3": [8, 2], "i4": [8, 3],
                  "i5": [8, 4], "i6": [8, 5], "i7": [8, 6], "i8": [8, 7],
                  "i9": [8, 8]}
        user_message = str(user_message.content).lower()
        if user_message in list(places.keys()):
          place_to_paint = places[user_message]
          canvas[place_to_paint[0]][place_to_paint[1]] = game_settings[1]
          await new_round()
        elif user_message == "sair":
          await game_message.edit(
            embed=Embed(
              description="".join(str(_) for _ in human_readable_canvas()),
              color=0xFF0000
            ).set_author(
              name="O desenho foi cancelado.",
              icon_url=message.author.avatar_url
            )
          )
        elif user_message in commands: await commands[user_message]()
        else: await new_round()
      except TimeoutError: await new_round()
    await new_round()
  # If someone deletes the message or missing permissions.
  except (NotFound, Forbidden): pass