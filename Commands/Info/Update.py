from discord import Embed

async def update(message, client, color):
  """Show the version and the patch notes."""
  await message.channel.send(
    embed=Embed(color=color)
    .set_author(name="Novidades da versão 1.20",
                icon_url=client.user.avatar_url)
    .add_field(name="⚙ - **Futuros**",
               value="[`J!Jdv`](https://github.com/jlmsc) - Jogo da velha, "
                     "PvE ou PvP.\n"
                     "[`J!Wally`](https://github.com/jlmsc) - *Where's Wally?*",
               inline=False)
    .add_field(name="📥 - **Adicionados**",
               value="[`J!Anagrama`](https://github.com/jlmsc) - Anagramas!\n"
                     "[`J!Cpmin`](https://github.com/jlmsc) - Campo minado "
                     "totalmente customizável.\n"
                     "[`J!Balloon`](https://github.com/jlmsc) - Um jogo "
                     "baseado no TypeRacer.\n"
                     "[`J!Convite`](https://github.com/jlmsc) - Convite "
                     "instantâneo de bot.",
               inline=False)
    .add_field(name="🛠️ - **Modificados**",
               value="[`J!Update`](https://github.com/jlmsc) - Visual "
                     "alterado.\n"
                     "[`J!Ajuda`](https://github.com/jlmsc) - Nome e visual "
                     "alterados.\n"
                     "[`J!Emote`](https://github.com/jlmsc) - Nome e visual "
                     "alterados e compatibilidade com qualquer emote.\n"
                     "[`J!Avatar`](https://github.com/jlmsc) - Visual "
                     "alterado.\n"
                     "[`J!Paint`](https://github.com/jlmsc) - Agora o usuário "
                     "pode escolher qualquer emote não customizado como cor, "
                     "a forma como o fundo é preenchido foi aterado e "
                     "alteração no visual.\n"
                     "[`J!Sinfo`](https://github.com/jlmsc) - Visual "
                     "alterado.\n"
                     "[`J!Diga`](https://github.com/jlmsc) - Nome e visual "
                     "alterados, adicionado uma pequena animação antes do "
                     "envio da mensagem.\n"
                     "[`J!Filosofar`](https://github.com/jlmsc) - Melhorias no "
                     "alinhamento e alteração na fonte.",
               inline=False)
    .add_field(name="📤 - **Removidos**",
               value="[`J!Bricks`](https://github.com/jlmsc) - Um jogo "
                     "baseado em Breakout.\n"
                     "[`J!Math`](https://github.com/jlmsc) - Jogo que envolve "
                     "solução de equações.\n"
                     "[`J!Feedback`](https://github.com/jlmsc) - Permitia a "
                     "reportagem de bugs ou o envio de mensagens aleatórias.",
               inline=False)
    .set_thumbnail(url=client.user.avatar_url)
    .set_footer(text="Os prefixos continuam a ser j! e J!")
  )