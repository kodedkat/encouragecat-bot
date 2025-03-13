# EncourageCat Bot ≽^•⩊•^≼

### **YouTube Demo:** https://youtu.be/SrZENxFQlQE

## **Introduction**
EncourageCat Bot is a Discord bot created to message encouraging quotes and cat-themed holiday wishes in the servers it is invited to. The commands to prompt it are /encat and $encat. This project is for Codédex’s Python course final project. One of the options is to build a Discord bot with Python, which in the Codédex guide is a MemeBot. I followed the guide to familiarize myself with the process, then decided to create one of my own. The idea sparked from TikTok hopecore videos and my cat motif.

## **What Went Wrong + What I Learned**
I encountered quite a bit of error trying to code this bot to function how I wanted it to. These are the more important issues I ran into and learned how to fix.
1. Problem: couldn’t run the program, error said “No such file or directory”
   <be>
   Solution: The program needs to be run in the script files (not the Python install files I had it in). The path can be set by clicking the search icon, which is two icons below the VSCode icon in the top left, or it can also be set by typing ‘cd C:\Users\kathina\code\discord_encouragecat_bot\’. The command to run the program is ‘python ./encouragecat_bot.py’.
3. Problem: trying to add a Discord bot slash syntax
   Solution: I searched how to, and I followed this Stack Overflow answer (https://stackoverflow.com/questions/71165431/how-do-i-make-a-working-slash-command-in-discord-py). I attempted the discord.py version at first. However, I saw the py-cord version is simpler and more understandable, so I ran ‘pip uninstall discord.py’ and then ‘pip install py-cord’ and adjusted my code.
4. Problem: $encat printed three encouraging messages instead of just one
   Solution: I hadn’t realized that I had multiple processes running my bot code until I saw that in the right area of the terminal window, there were several ‘python’ listed, which I deleted.

## **Future Improvements + Plans**
I would like to learn to manipulate the percent chance a particular message appears. I would also like to adapt and scale this bot to create other bots that use quotes strictly from a particular piece of media. For example, I have subsequently created EncourageMon Bot, which responds with inspiring quotes from the Pokémon series. The GitHub link to EncourageMon Bot is https://github.com/kodedkat/encouragemon-bot.

## **Conclusion**
This project was a valuable lesson in both Python and VSCode. It was my first time running a program that functions elsewhere (e.g., Discord). Writing encouraging messages of my creation was cathartic. I also enjoyed cat-ifying the holiday messages and assigning corresponding emojis. Raising EncourageCat Bot was a good experience, and it is the first in my beginning collection of coding projects.

*Credits: EncourageCat Bot's icon courtesy of Cheerleader Cat from The Battle Cats*

ᓚ₍⑅^..^₎♡
