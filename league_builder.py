import csv

# List of teams + additional list
Sharks = []
Dragons = []
Raptors = []

team_Sharks1 = []
team_Dragons1 = []
team_Raptors1 = []

team_Sharks2 = []
team_Dragons2 = []
team_Raptors2 = []

# The welcome message for each .txt file
coach = "Dear {},\n\n{}, Sharks,\nPractice at: 10:00  15/08/2017"

# Shortcuts for the dictionary keys:
g_name = 'Guardian Name(s)'
skill = 'Soccer Experience'

def write_text(row, rows, coach)
    with open('{}.txt'.format('_'.join(row['Name'].lower().split(' '))), 'w') as textfile:
        textfile.write(coach.format(row[g_name], row['Name']))
    return textfile

if __name__ == "__main__":

    # Read from CSV file and create a list of dictionaries
    with open('soccer_players.csv', newline='') as csvfile:
        player = csv.DictReader(csvfile, delimiter=',')
        rows = list(player)

        # Loop through dictionaries equally sorting the experienced players for each team
        for row in rows:
            if row[skill] == 'YES' and len(team_Sharks1) < 3:
                team_Sharks1.append(row['Name']+', '+row[skill]+', '+row[g_name])
                write_text(row, rows, coach)
                # Crate a txt file for each player guardians
#                 with open('{}.txt'.format('_'.join(row['Name'].lower().split(' '))), 'w') as textfile:
#                     textfile.write(coach.format(row[g_name], row['Name']))

            elif row[skill] == 'YES' and len(team_Dragons1) < 3:
                team_Dragons1.append(row['Name']+', '+row[skill]+', '+row[g_name])
                write_text(row, rows, coach)
#                 with open('{}.txt'.format('_'.join(row['Name'].lower().split(' '))), 'w') as textfile:
#                     textfile.write(coach.format(row[g_name], row['Name']))

            elif row[skill] == 'YES' and len(team_Raptors1) < 3:
                team_Raptors1.append(row['Name']+', '+row[skill]+', '+row[g_name])
                write_text(row, rows, coach)
#                 with open('{}.txt'.format('_'.join(row['Name'].lower().split(' '))), 'w') as textfile:
#                     textfile.write(coach.format(row[g_name], row['Name']))

        for row2 in rows:
            if row2[skill] == 'NO' and len(team_Sharks2) < 3:
                team_Sharks2.append(row2['Name']+', '+row2[skill]+', '+row2[g_name])
                write_text(row, rows, coach)
#                 with open('{}.txt'.format('_'.join(row2['Name'].lower().split(' '))), 'w') as textfile:
#                     textfile.write(coach.format(row2[g_name], row2['Name']))

            elif row2[skill] == 'NO' and len(team_Dragons2) < 3:
                team_Dragons2.append(row2['Name']+', '+row2[skill]+', '+row2[g_name])
                write_text(row, rows, coach)
#                 with open('{}.txt'.format('_'.join(row2['Name'].lower().split(' '))), 'w') as textfile:
#                     textfile.write(coach.format(row2[g_name], row2['Name']))

            elif row2[skill] == 'NO' and len(team_Raptors2) < 3:
                team_Raptors2.append(row2['Name']+', '+row2[skill]+', '+row2[g_name])
                write_text(row, rows, coach)
#                 with open('{}.txt'.format('_'.join(row2['Name'].lower().split(' '))), 'w') as textfile:
#                     textfile.write(coach.format(row2[g_name], row2['Name']))

        Sharks = team_Sharks1 + team_Sharks2
        Dragons = team_Dragons1 + team_Dragons2
        Raptors = team_Raptors1 + team_Raptors2

        # Create a file witch contains all the teams and players in it
        with open('teams.txt', 'w') as txtfile:
            txtfile.write('Sharks \n')
            txtfile.write('\n'.join(item for item in Sharks)+'\n')
            txtfile.write('\n')
            txtfile.write('Dragons \n')
            txtfile.write('\n'.join(item for item in Dragons)+'\n')
            txtfile.write('\n')
            txtfile.write('Raptors \n')
            txtfile.write('\n'.join(item for item in Raptors)+'\n')
            txtfile.write('\n')
