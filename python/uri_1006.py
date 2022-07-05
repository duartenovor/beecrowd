mean_wei = [2, 3, 5]
tot_wei = 0
mean = 0

for i in range(len(mean_wei)):
	mean += float(input()) * mean_wei[i]
	tot_wei += mean_wei[i]

mean /= tot_wei

print("MEDIA = %.1f" %mean)