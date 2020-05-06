from random import choice
from discord import Embed
from asyncio import TimeoutError
from Assets.AllWords import words
from discord.errors import NotFound, Forbidden

async def anagram(message, client, color):
  """Allow the user to play a anagram's game."""
  try:
    def get_anagram(main_word):
      normal_words.append(main_word)
      main_word_scramble = sorted(list(main_word))
      anagram_words.append(main_word_scramble)
      for word in words:
        if not len(normal_words) >= 10:
          new_word = word
          if new_word != main_word:
            new_word_scramble = sorted(list(new_word))
            if all(letter in main_word_scramble
                   for letter in set(new_word_scramble)):
              normal_words.append(new_word)
        else:
          break
    anagram_words, normal_words = [], []
    get_anagram(choice(words))

    normal_words = list(set(normal_words))

    async def show_game_message():
      discovered_words = []
      game_message = await message.channel.send(
        embed=Embed(title=" ".join(str(letter).capitalize()
                                   for letter in anagram_words[0]),
                    description=f"Restam {len(normal_words)} palavras",
                    color=color)
        .set_footer(text="Você tem 60 segundos para enviar uma palavra, "
                         "digite \"cancelar jogo\" para sair.")
      )

      async def start_game():
        if len(normal_words) == 0:
          await game_message.edit(
            embed=Embed(title="Todas as palavras foram desembaralhadas!",
                        color=0x00FF00)
            .add_field(name="Palavras encontradas:",
                       value="\n".join(str(item) for item in discovered_words))
          )
        else:
          if len(discovered_words) > 0:
            await game_message.edit(
              embed=Embed(title=" ".join(str(letter).capitalize()
                                         for letter in anagram_words[0]),
                          description="Você tem 60 segundos para enviar uma "
                                      "palavra.",
                          color=color)
              .add_field(name=f"Restam {len(normal_words)} palavras.",
                         value="\n".join(str(item) for item in discovered_words
                                         if len(discovered_words) > 0))
              .set_footer(text="Digite \"cancelar jogo\" para sair.")
            )
          else:
            await game_message.edit(
              embed=Embed(title=" ".join(str(letter).capitalize()
                                         for letter in anagram_words[0]),
                          description="Você tem 60 segundos para enviar uma "
                                      "palavra.",
                          color=color)
              .add_field(name=f"Restam {len(normal_words)} palavras.",
                         value="Não achou nenhuma palavra ainda.")
              .set_footer(text="Digite \"cancelar jogo\" para sair.")
            )

          def verify_message(msg):
            if msg.author.id == message.author.id: return msg
          user_msg = await client.wait_for("message",
                                           check=verify_message,
                                           timeout=60.0)
          await user_msg.delete()
          user_msg = str(user_msg.content).lower()

          if user_msg in normal_words:
            del normal_words[normal_words.index(user_msg)]
            discovered_words.append(user_msg.upper())
            await start_game()
          elif user_msg == "cancelar jogo":
            await game_message.edit(
              embed=Embed(description=f"Faltou {len(normal_words)} palavras.",
                          color=0xFFFF00)
              .set_author(name="O jogo foi cancelado",
                          icon_url=message.author.avatar_url)
            )
          else: await start_game()
      await start_game()
    await show_game_message()
  except TimeoutError:
    await message.channel.send(
      embed=Embed(title="Tempo esgotado.", color=0xFFFF00))
  # Deleted message or missing permissions.
  except (NotFound, Forbidden): pass