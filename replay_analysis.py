import os
import sys
import csv
from carball.decompile_replays import decompile_replay


def update_csv(csv_file_path, new_player_stats):
    existing_player_stats = {}

    # Check if the CSV file exists
    if os.path.exists(csv_file_path):
        # Read the existing data from the CSV file
        with open(csv_file_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                player_name = row["Player"]
                existing_player_stats[player_name] = {
                    stat: int(row[stat]) for stat in target_stats
                }
    else:
        # Create the CSV file with the header row
        with open(csv_file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Player", "Goals", "Assists", "Saves", "Shots"])

    # Update the existing data with the new data
    for player_name, stats in new_player_stats.items():
        if player_name in existing_player_stats:
            for stat in target_stats:
                existing_player_stats[player_name][stat] += stats[stat]
        else:
            existing_player_stats[player_name] = stats

    # Write the updated data back to the CSV file
    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Player", "Goals", "Assists", "Saves", "Shots"])

        for player_name, stats in existing_player_stats.items():
            writer.writerow([player_name, stats["Goals"],
                            stats["Assists"], stats["Saves"], stats["Shots"]])

    print(f"Data updated in {csv_file_path}")


sys.path.append("C:/Users/USER/carball")
replay_path = "C:/Users/USER/Desktop/RLReplay/Replays/a491bb8b-2d17-486a-9441-5e0cd9e63433.replay"
output_file_path = "C:/Users/USER/Desktop/RLReplay/output.csv"

# Parse the replay file
json_data = decompile_replay(replay_path)
print()
properties = json_data["properties"]
player_stats = properties["PlayerStats"]

# create a list of dictionaries for the desired players
target_players = ["Not Leopard", "Wiseyslides", "OfficialPaper1"]
target_stats = ["Goals", "Assists", "Saves", "Shots"]
target_player_stats = {}
for player in player_stats:
    if player["Name"] in target_players:
        # Create a new dictionary with only the desired stats
        stats = {stat: player[stat] for stat in target_stats}
        target_player_stats[player["Name"]] = stats

# Print the stats for each player
for player_name, stats in target_player_stats.items():
    print(player_name, stats)

# Call the update_csv function to update the CSV file with the new data
update_csv(output_file_path, target_player_stats)
