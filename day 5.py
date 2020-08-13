achives_time = [66,57,54,53,64,52,59]
for i in range(len(achives_time)-1):
    for j in range(len(achives_time)-1):
        if achives_time[j] < achives_time[j+1]:
            achives_time[j],achives_time[j+1] = achives_time[j+1],achives_time[j]

best_score = achives_time[0]
print(best_score)