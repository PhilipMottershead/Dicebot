[![Build Status](https://travis-ci.com/PhilipMottershead/Dicebot.svg?branch=main)](https://travis-ci.com/PhilipMottershead/Dicebot)
<a href="https://scan.coverity.com/projects/philipmottershead-dicebot">
  <img alt="Coverity Scan Build Status"
       src="https://scan.coverity.com/projects/22096/badge.svg"/>
</a>
# Dice Bot

Creating a open source alternative to existing dicebots on discord.

## Testing install instructions

Run `pipenv install` into the terminal

Run `pipenv shell` to enter pip environment

Create .env file like bellow:

```conf
# .env
DISCORD_TOKEN=YOUR_TOKEN_HERE
```

Replacing YOUR_TOKEN_HERE with the token for your bot, see <https://discordpy.readthedocs.io/en/latest/discord.html> for how to get that.

Run in console via running `python dicebot.py`

If is correct it should output :

`<Your bot name> has connected to Discord!`

To test see <https://discordpy.readthedocs.io/en/latest/discord.html> on how to add bot to a server.

## Running Unit tests

To run the unit test run `python test_dicebot.py` in Pipenv shell
