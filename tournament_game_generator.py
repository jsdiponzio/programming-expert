def get_number_of_teams():
    num_teams = 0
    while num_teams < 2:
        num_teams = int(input("Enter the number of teams in the tournament: "))
        if num_teams < 2:
            print("The minimum number of teams is 2, try again.")

    return num_teams

def get_team_names(num_teams):
    team_names = []
    for i in range(num_teams):
        i += 1
        team_name = ""
        while len(team_name) < 2 or team_name.count(" ") > 2:
            team_name = input(f"Enter the name for team #{i}: ")
            if len(team_name) < 2:
                print("Team names must have at least 2 characters, try again.")
            elif team_name.count(" ") >= 2:
                print("Team names may have at most 2 words, try again.")
        team_names.append(team_name)
        
    return team_names

def get_number_of_games_played(num_teams):
    games_played = 0
    while games_played < num_teams - 1:
        games_played = int(input("Enter the number of games played by each team: "))
        if games_played < num_teams - 1:
            print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")

    return games_played

def get_team_wins(team_names, games_played):
    team_wins = {}
    for team in team_names:
        team_total = None
        while team_total is None or team_total < 0 or team_total > games_played:
            team_total = int(input(f"Enter the number of wins {team} had: "))
            if team_total < 0:
                print("The minimum number of wins is 0, try again.")
            elif team_total > games_played:
                print(f"The maximum number of wins is {games_played}, try again.")

        team_wins[team] = team_total
    
    return team_wins

def calc_games(num_teams, team_wins):
    print("Generating the games to be played in the first round of the tournament...")
    tournament_games = int(num_teams / 2)
    for i in range(tournament_games):
        most_wins = max(team_wins, key=team_wins.get)
        least_wins = min(team_wins, key=team_wins.get)
        print(f"Home: {least_wins} VS Away: {most_wins}")
        del team_wins[most_wins]
        del team_wins[least_wins]

def main():
    num_teams = get_number_of_teams()
    team_names = get_team_names(num_teams)
    games_played = get_number_of_games_played(num_teams)
    team_wins = get_team_wins(team_names, games_played)
    calc_games(num_teams, team_wins)

if __name__ == "__main__":
    main()