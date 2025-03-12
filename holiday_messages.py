holiday_messages_dict = {
  # standard public holidays in the united states
  (1, 1): "Happy Mew Year 🎉",
  (1, 29): "Happy Lunar Mew Year 🧨",
  (2, 14): "Happy Purr-lentine's Day 💕",
  (3, 17): "Happy St. Catrick's Day ☘️",
  (4, 20): "Happy Meow-aster 🐇",
  (5, 11): "Happy Meow-ther's Day 👩‍🍼",
  (6, 15): "Happy Paw-ther's Day 👨‍🍼",
  (7, 4): "Happy Fur-th of July 🎆",
  (10, 31): "Happy Cat-oween 🎃",
  (11, 28): "Happy Thanks-kitten 🦃",
  (12, 24): "Meowy Christmas Eve ⛪",
  (12, 25): "Meowy Cristmas 🎄",
  (12, 31): "Happy Mew Year's Eve 🥂"
}

# utilizing dictionary avoids unnecessarily long
#   if datetime.date.today() == datetime.day(1, 1):
#     print(holiday_messages_list[0])
#   elif datetime.date.today() == datetime.day(1, 29):
#     print(holiday_messages_list[1])
#   elif etc.