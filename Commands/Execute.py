from Commands.Fun.Say import say
from Commands.Fun.Fbi import fbi
from Commands.Fun.Paint import paint
from Commands.Fun.Philosophy import philosophy
from Commands.Games.Anagram import anagram
from Commands.Games.Balloon import balloon
from Commands.Games.MineSweeper import mine_sweeper
from Commands.Info.Help import help_cmd
from Commands.Info.ServerInfo import sinfo
from Commands.Info.Update import update
from Commands.Utility.Emote import emote
from Commands.Utility.Avatar import avatar
from Commands.Utility.Invite import invite

commands = {
  "fbi": fbi,
  "diga": say,
  "paint": paint,
  "filosofar": philosophy,
  "ajuda": help_cmd,
  "sinfo": sinfo,
  "emote": emote,
  "avatar": avatar,
  "convite": invite,
  "anagrama": anagram,
  "balloon": balloon,
  "cpmin": mine_sweeper,
  "update": update
}