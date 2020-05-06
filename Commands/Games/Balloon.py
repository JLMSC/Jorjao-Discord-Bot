from random import choice
from discord import Embed
from Assets.AllWords import words
from asyncio import sleep, TimeoutError
from discord.errors import NotFound, Forbidden

async def balloon(message, client, color):
  """Allow the user to play a TypeRacer based game."""
  starting_time = 5.0

  async def send_how_to_play_message():
    return await message.channel.send(
      embed=Embed(title="⏰ - **Iniciando**...",
                  color=color)
      .add_field(name="❓ - **Como joga**?",
                 value="> Um texto vai aparecer nesta mensagem, então, "
                       "você precisa enviá-la no chat o mais rápido possível.")
      .add_field(name="⏲ - **Só 5 segundos**?!",
                 value="> *Calma lá* ! O tempo aumenta em **0.5** para cada "
                       "acerto.")
      .add_field(name="⚠️- **ATENÇÃO, O JOGO NÃO TEM FIM**!",
                 value="> Você cancela o jogo enviando \"sair\" no chat, "
                       "durante o jogo.", inline=False)
      .set_footer(text=f"Você tem apenas {starting_time} segundos para "
                       "enviar a mensagem no canal.")
    )
  game_message = await send_how_to_play_message()
  await sleep(3)

  async def new_round(level, time, wrongs, corrects):
    game_text = " ".join(choice(words) for _ in range(level))
    try:
      await game_message.edit(
        embed=Embed(title=f"🎈 - Você está no level: **{level}**",
                    color=color)
        .add_field(name="**Frase**:",
                   value=f"> **{game_text}**")
        .set_footer(text="Corretas: {} | "
                         "Erradas: {} | "
                         "Tempo para esta rodada: {:.2f} | "
                         "Digite: \"sair\" para terminar o jogo."
                    .format(corrects, wrongs, time))
      )

      def check_message(msg):
        if msg.author.id == message.author.id: return msg
      user_message = await client.wait_for("message",
                                           check=check_message,
                                           timeout=time)
      await user_message.delete()
      if str(user_message.content).lower() == "sair":
        await game_message.edit(
          embed=Embed(title=f"Você chegou até o level **{level}**",
                      description=f"> ✅ Total de acertos: {corrects}\n"
                                  f"> ❌ Total de erros: {wrongs}",
                      color=0xFFFF00)
          .set_author(name=message.author.name,
                      icon_url=message.author.avatar_url)
        )
      elif user_message.content == game_text:
        time += 0.5
        level += 1
        corrects += 1
        await new_round(level, time, wrongs, corrects)
      else:
        wrongs += 1
        await new_round(level, time, wrongs, corrects)
    except TimeoutError:
      wrongs += 1
      await new_round(level, time, wrongs, corrects)
    # No permissions or deleted message.
    except (NotFound, Forbidden): pass
  await new_round(1, starting_time, 0, 0)