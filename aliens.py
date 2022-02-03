alien0 = {'color': 'zielony', 'points': 5}
alien1 = {'color': 'żółty', 'points': 10}
alien2 = {'color': 'czerwony', 'points': 15}

aliens = [alien0, alien1, alien2]

for alien in aliens:
    print(alien)

aliens =[]

for alien in range(30):
    new_alien = {'color': 'zielony', 'points': 5, 'speed': 'wolno'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'zielony':
        alien['color'] = 'żółty'
        alien['points'] = 10
        alien['speed'] = 'średnio'

for alien in aliens[:5]:
    print(alien)
print('-----------------------------------')
print(f"Całkowita liczba obcych : {len(aliens)}")