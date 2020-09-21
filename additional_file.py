import csv
import random

if __name__ == '__main__':

    # Creating Experienced and Unexperienced empty list
    exp = []
    nonexp = []

    # opening Soccer.csv file
    with open('soccer_players.csv') as csvfile:
        player_info = csv.reader(csvfile)
        rows = list(player_info)
        for row in rows[1:]:
            if (row[2] == 'YES'):
                list = [row[0], row[2], row[3]]
                exp.append(list)
            else:
                list = [row[0], row[2], row[3]]
                nonexp.append(list)

# Three teams empty list
Sharks = []
Dragons = []
Raptors = []
# Creating experienced player list
index_ex = 0
for ex in exp:
    if len(Sharks) != 3:
        Sharks.append(exp[index_ex])
        index_ex += 1
    else:
        if len(Dragons) != 3:
            Dragons.append(exp[index_ex])
            index_ex += 1
        else:
            Raptors.append(exp[index_ex])
            index_ex += 1

# Creating Unexperienced player list
index_nonex = 0
for nonex in nonexp:
    if len(Sharks) != 6:
        Sharks.append(nonexp[index_nonex])
        index_nonex += 1
    else:
        if len(Dragons) != 6:
            Dragons.append(nonexp[index_nonex])
            index_nonex += 1
        else:
            Raptors.append(nonexp[index_nonex])
            index_nonex += 1

# Creating Output file for team allocation
with open('teams.txt', 'w') as file:
    file.write("Sharks:")
    for shr in Sharks:
        Sharks_ = ", ".join(shr)
        file.write("\n" + Sharks_)
    file.write("\n\n")
    file.write("---------------------------------------------------------------------------->")
    file.write("\n\n")

    file.write("Dragons:")
    for drg in Dragons:
        Dragons_ = ", ".join(drg)
        file.write("\n" + Dragons_)
    file.write("\n\n")
    file.write("---------------------------------------------------------------------------->")
    file.write("\n\n")

    file.write("Raptors:")
    for rapt in Raptors:
        Raptors_ = ", ".join(rapt)
        file.write("\n" + Raptors_)
    file.write("\n\n")
    file.write("----------------------------------------------------------------------------")

# Extra Credit:-Creating 18 Output text file for Letters to parents
for shark in Sharks:
    st = "".join(shark[0])
    underscore_string = st.replace(" ", "_")
    final_string = underscore_string.lower()
    guardian_name = shark[2]
    date = "12-5-2019 14:00"
    with open(final_string + ".txt", "w") as file:
        file.write("\nDear " + guardian_name)
        file.write("\nWelcome!!!!!!!!!!!!!!!!!\nCongratulation on selection of your childern!!!")
        file.write("\nPlayer Name: " + shark[0])
        file.write("\nTeam Name: Sharks")
        file.write("\nDate and Time for Practice: " + date)

for raptor in Raptors:
    st = "".join(raptor[0])
    underscore_string = st.replace(" ", "_")
    final_string = underscore_string.lower()
    guardian_name = raptor[2]
    date = "12-6-2019 14:00"
    with open(final_string + ".txt", "w") as file:
        file.write("\nDear " + guardian_name)
        file.write("\nWelcome!!!!!!!!!!!!!!!!!\nCongratulation on selection of your childern!!!")
        file.write("\nPlayer Name: " + raptor[0])
        file.write("\nTeam Name: Raptors")
        file.write("\nDate and Time for Practice: " + date)

for dragon in Dragons:
    st = "".join(dragon[0])
    underscore_string = st.replace(" ", "_")
    final_string = underscore_string.lower()
    guardian_name = dragon[2]
    date = "12-7-2019 14:00"
    with open(final_string + ".txt", "w") as file:
        file.write("\nDear " + guardian_name)
        file.write("\nWelcome!!!!!!!!!!!!!!!!!\nCongratulation on selection of your childern!!!")
        file.write("\nPlayer Name: " + dragon[0])
        file.write("\nTeam Name: Dragons")
        file.write("\nDate and Time for Practice: " + date)