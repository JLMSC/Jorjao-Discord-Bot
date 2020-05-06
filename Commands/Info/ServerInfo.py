from discord import Embed

async def sinfo(message, client, color):
  """Return some information about the guild."""
  actual_guild = client.get_guild(message.guild.id)
  await message.channel.send(
    embed=Embed(
      title=f"📂 **{actual_guild.name}**",
      description="📄 **Descrição**: %s" % actual_guild.description
      if actual_guild.description is not None
      else "📄 **Descrição**: Nenhuma",
      color=color)
    .set_thumbnail(url=actual_guild.icon_url)
    .add_field(
      name=f"🌎 **Região** {str(actual_guild.region).upper()[0:2]}",
      value=f"👥 **Quantidade de usuários**: {actual_guild.member_count}",
      inline=False)
    .add_field(
      name=f"📡 **Criado em**: %s" %
           str(actual_guild.created_at).split(" ")[0].replace("-", "/"),
      value="👑 **Dono do servidor**: %s" %
            client.get_user(actual_guild.owner_id),
      inline=False)
    .add_field(
      name="🎙️ **Quantidade de canais de voz**: %i" %
           len(actual_guild.voice_channels),
      value="💬 **Quantidade de canais de texto**: %i" %
            len(actual_guild.text_channels),
      inline=False)
    .add_field(
      name=f"🗃️ **Limite de emotes**: {actual_guild.emoji_limit}",
      value="📨 **Limite de Bit rate**: {:.2f} kbps".format(
        float(actual_guild.bitrate_limit / 1000)
      ), inline=False)
    .add_field(
      name="📥 **Tamanho máximo de arquivos**: {:.2f} MB".format(
        float((actual_guild.filesize_limit / 1024) / 1024)),
      value="🔒 **Nível da autenticação de dois fatores**: %i" %
            actual_guild.mfa_level,
      inline=False
    )
  )