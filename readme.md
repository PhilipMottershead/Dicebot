# Dice Bot

[![Build Status](https://travis-ci.com/PhilipMottershead/Dicebot.svg?branch=main)](https://travis-ci.com/PhilipMottershead/Dicebot)

DiceBot is a dice rolling bot for discord

## Installation

Run `pipenv install -r requirements.txt` into the terminal

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

## Usage

Run in console via running `python dicebot.py`

If is correct it should output :

`<Your bot name> has connected to Discord!`

To test see <https://discordpy.readthedocs.io/en/latest/discord.html> on how to add bot to a server.

## Run tests

To run the unit test run `python test_dicebot.py` in Pipenv shell

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)