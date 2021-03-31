# Group 4 Project (GUI Test)

- The purpose of this is to pull player information from the Hypixel API, which stores Minecraft (an online game) Player Data.
- The User will filter the data using input from the terminal filtering on name data and game mode type.
- This application will return kills, deaths, wins and kill/death ratio for the selected player and game mode.
- Kill/Death ratio will be calculated by a function which utilises the data from API called 'kills' and 'deaths'.

## How the program works

- Run the program [functions/main](functions/main.py)
- Enter the username/player you are looking for
- Program will get, filter and display the required stats

## Useful information

- [Project Trello board](https://trello.com/b/N6nXzian/tsi-team-4)
- [Hypixel API link](https://api.hypixel.net/player?key=c1e412b1-5131-49f9-b7a2-bdfda4371684&name=Jif)

## Well refactored code

- [getData](functions/getData.py)
- [getGameMode](functions/getGameMode.py)
- [getRatio](functions/getRatio.py)

## Tests

- [testGetData](tests/test_get_data.py)
- [testGetGameMode](tests/test_get_game_mode.py)
- [testRatio](test/test_ratio.py)
