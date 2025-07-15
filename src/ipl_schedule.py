import itertools

def create_ipl_schedule(teams):
    matches = list(itertools.combinations(teams, 2))
    schedule = []
    seen = set()
    match_no = 1
    for team1, team2 in matches:
        # Use frozenset to treat (A, B) and (B, A) as the same match
        fixture = frozenset([team1, team2])
        if fixture not in seen:
            schedule.append(f"Match {match_no}: {team1} vs {team2}")
            seen.add(fixture)
            match_no += 1
    return schedule

if __name__ == "__main__":
    teams_input = input("Enter team names separated by commas (e.g. CSK,MI,SRH,RCB): ")
    teams = [team.strip() for team in teams_input.split(",") if team.strip()]
    if len(teams) < 2:
        print("Please enter at least two teams.")
    else:
        schedule = create_ipl_schedule(teams)
        for match in schedule:
            print(match)