from discord.errors import HTTPException

async def change_icon(month, client):
  events = {1: "Assets\\Icons\\new_year.png",
            2: "Assets\\Icons\\carnival.png",
            4: "Assets\\Icons\\easter.png",
            6: "Assets\\Icons\\valentines_day.png",
            10: "Assets\\Icons\\halloween.png",
            12: "Assets\\Icons\\christmas.png"}
  try:
    if month in list(events.keys()):
      with open(events[month], "rb") as file:
        icon = file.read()
      await client.user.edit(avatar=icon)
    # No events.
    else:
      with open("Assets\\Icons\\no_events.jpg", "rb") as file:
        icon = file.read()
      await client.user.edit(avatar=icon)
  # Changing avatar too fast.
  except HTTPException: pass