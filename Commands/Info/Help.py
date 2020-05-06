from discord import Embed

async def help_cmd(message, client, color):
  """Show all the commands available for use."""
  await message.channel.send(
    embed=Embed(
      description="**Prefixos**: `j! ou J!`",
      color=color)
    .set_author(
      name="Comandos disponíveis:",
      icon_url=client.user.avatar_url
    )
    .add_field(
      name="🛹 - **Diversão**",
      value="> [`J!Diga + mensagem`](https://github.com/jlmsc) - Reenvia "
            "sua mensagem como fala do bot.\n"
            "> [`J!Fbi`](https://github.com/jlmsc) - FBI! Open Up!\n"
            "> [`J!Filosofar + mensagem`](https://github.com/jlmsc) - "
            "Mostra sua mensagem como fala de algum filósofo.\n"
            "> [`J!Paint`](https://github.com/jlmsc) - Um lindo quadro "
            "para você desenhar.",
      inline=False
    )
    .add_field(
      name="🎲 - **Jogos**",
      value="> [`J!Anagrama`](https://github.com/jlmsc) - É um anagrama, "
            "só isso.\n"
            "> [`J!Balloon`](https://github.com/jlmsc) - É tipo um "
            "TypeRacer.\n"
            "> [`J!Cpmin + comprimento + largura + qntd. de bombas`]("
            "https://github.com/jlmsc) - Campo minado customizável.\n"
            "> [`J!Jdv + @user`](https://github.com/jlmsc) - Jogo da "
            "velha, PvE ou PvP.\n"
            "> [`J!Wally`](https://github.com/jlmsc) - *Where's Wally?*",
      inline=False
    )
    .add_field(
      name="❔ - **Informação**",
      value="> [`J!Ajuda`](https://github.com/jlmsc) - É esse comando "
            "~~psiiiiiu~~!\n"
            "> [`J!Sinfo`](https://github.com/jlmsc) - Mostra as "
            "informações do servidor.\n"
            "> [`J!Update`](https://github.com/jlmsc) - Mostra o registro de "
            "alterações da nova versão.",
      inline=False
    )
    .add_field(
      name="🕵️ - **Utilidade**",
      value="> [`J!Avatar + @user`](https://github.com/jlmsc) - Mostra a "
            "sua imagem ou a de alguém.\n"
            "> [`J!Convite`](https://github.com/jlmsc) - Cria um convite "
            "do bot.\n"
            "> [`J!Emote + emote`](https://github.com/jlmsc) - Mostra a "
            "imagem de algum emote em grande escala.",
      inline=False
    )
  )