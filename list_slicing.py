#modules in pyhton-pyhton files: lovercase, underscore
 #firstname(snake case)
#sql,java~>listsSliicing, Firstname(camel case :combination of upper case lower case
players = ['charles','martha', 'micheal', 'florence', 'eli']
print(players[0:3]) #3 players
print(players[1:3]) #2 players
print(players[:3]) # it will starts begining by default

print(players[2:4])
print(players[2:5])
print(players[:]) #it will run whole elements by default
new_players = players[:] # copied to new list, independent from player list
players.append('martin')
new_players.append('mark')
print(players)
print(new_players)
players1 = players #it is not a copy but duplicate reference
