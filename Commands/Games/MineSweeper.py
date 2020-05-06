from discord import Embed
from random import randint
from discord.errors import Forbidden

class InvalidBombQuantity(Exception): pass
class InvalidBoardSize(Exception): pass

async def mine_sweeper(message, *args):
  """Allow the user to play mine sweeper."""
  try:
    async def generate_board(row=10, col=10, bomb_count=10):
      if bomb_count >= (row * col):
        raise InvalidBombQuantity(
          await message.channel.send(
            embed=Embed(title="A quantidade de bombas não pode ser maior que o "
                              "campo.",
                        color=0xFFFF00)
          )
        )
      if row > 10 or col > 10:
        raise InvalidBoardSize(
          await message.channel.send(
            embed=Embed(title="O comprimento e a largura não podem ser "
                              "maiores do que **10**.",
                        color=0xFFFF00)
          )
        )
      board = [[0 for _ in range(row)] for _ in range(col)]
      bomb_location = []

      def add_bombs_in_board():
        while len(bomb_location) < bomb_count:
          r = randint(0, len(board) - 1)
          c = randint(0, len(board[r]) - 1)
          if board[r][c] != -1:
            board[r][c] = -1
            bomb_location.append([r, c])
      add_bombs_in_board()

      def count_neighboor_bombs():
        for bomb_place in bomb_location:
          (bomb_row, bomb_col) = bomb_place
          for r in range(bomb_row - 1, bomb_row + 2):
            for c in range(bomb_col - 1, bomb_col + 2):
              if 0 <= r < row and 0 <= c < col and board[r][c] != -1:
                board[r][c] += 1
      count_neighboor_bombs()

      def send_formatted_message():
        number_to_emote = {-1: "💥",
                           0: "0️⃣", 1: "1️⃣", 2: "2️⃣",
                           3: "3️⃣", 4: "4️⃣", 5: "5️⃣",
                           6: "6️⃣", 7: "7️⃣", 8: "8️⃣"}
        plain_board = []

        def remove_nested_list(lst):
          for item in lst:
            if type(item) == list:
              remove_nested_list(item)
            else:
              plain_board.append(item)
        remove_nested_list(board)

        for _ in range(len(plain_board)):
          plain_board[_] = number_to_emote[plain_board[_]]

        for _ in range(row, len(plain_board) * 2, row + 1):
          plain_board.insert(_, "\n")
        return plain_board
      return send_formatted_message()

    game_message = await generate_board(
      *[int(item) for item in str(message.content).split(" ")[1:]]
    )

    await message.channel.send(
      embed=Embed(
        description="".join("|| {} ||".format(game_message[_])
                            if game_message[_] != "\n"
                            else "\n"
                            for _ in range(len(game_message))),
        color=args[-1]
      )
    )
  # Invalid entry, negative numbers, emotes or text.
  except ValueError: pass
  # Specific invalid size
  except IndexError: pass
  # No "send_messages" permission
  except Forbidden: pass
  # Too much bombs or board > 100
  except (InvalidBombQuantity, InvalidBoardSize): pass
  # More than three entries.
  except TypeError:
    await message.channel.send(embed=Embed(title="Uso incorreto do comando.",
                                           description="Ex:. `J!cpmin 4 1 3`",
                                           color=0xFFFF00))