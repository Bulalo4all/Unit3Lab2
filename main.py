with open('weather.csv', 'r') as weather:
    data = weather.read()

items = data.split(",")
#print(items)

#Second portion of code to write to a file
num_of_players = input("Please enter the number of players: ")
num_of_players = int(num_of_players)

player_list = []
player_score_list = []

#taking user input and adding to list
for i in range(num_of_players):
    player_name = input(f"Please enter Player number {i +1}'s name: ")
    player_name = f"{player_name}"
    player_list.append(player_name)

    player_score = input(f"Please enter Player number {i+1}'s score: ")
    player_score_list.append(player_score)

    del player_name
    del player_score

#Writing out the players input to a file
with open('golf.txt', 'w') as golf:
    golf.write(f"Number of Players: {num_of_players}\n")
    for i in range(num_of_players):
        golf.write(f"{player_list[i]}, {player_score_list[i]}\n")