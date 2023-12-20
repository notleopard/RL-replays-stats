
# Rocket League Replay Stats Extractor

## Overview
This mini Python script is designed to extract and update player statistics from Rocket League replay files. It uses the `carball` library to decompile replay files, extracts player statistics, and updates them in a CSV file. This tool is useful if you are trying to track your team stats in rocket league!

## Features
- Decompile Rocket League replay files.
- Extract specific player statistics: Goals, Assists, Saves, and Shots.
- Update an existing CSV file or create a new one with the extracted data.
- Filter statistics for specific players.

## Installation
To run this script, you will need Python installed on your system. Additionally, the script depends on a couple external libraries.

1. Clone the repository:
   ```bash
   git clone https://github.com/notleopard/RL-replays-stats.git
   ```
2. Navigate to the cloned directory:
   ```bash
   cd RL-replays-stats
   ```
3. Install required packages and versions:
   ```bash
   pip install pandas==1.0.3
   pip install numpy==1.18.2
   pip install protobuf==3.6.1
   pip install xlrd==1.1.0
   pip install boxcars-py==0.1.*
   pip install carball
   ```

## Usage
1. Place your Rocket League replay files in a designated folder.
2. Update the script with the path to your replay file, your replay file name, and the desired output CSV file path.
3. Run the script:
   ```bash
   python replay_analysis.py
   ```

## Configuration
- `replay_path`: Path to the Rocket League replay file.
- `output_file_path`: Path where the output CSV file will be saved.
- `target_players`: List of player names whose stats you want to extract. Make sure to change it to extract your own name.
- `target_stats`: List of stats to extract (Goals, Assists, Saves, Shots).

