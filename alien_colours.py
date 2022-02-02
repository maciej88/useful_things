alien_color = 'red'
player_points = 0

if alien_color == 'green':
    player_points += 5
    print(f"you get {player_points} points!")
elif alien_color == 'yellow':
    player_points += 10
    print(f"you get {player_points} points!")
elif alien_color == 'red':
    player_points += 15
    print(f"you get {player_points} points!")
else:
    pass
