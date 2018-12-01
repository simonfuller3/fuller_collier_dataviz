import matplotlib.pyplot as plt

countries = ["canada", "usa"]
total_medals = [625, 653]

plt.bar(countries, total_medals)
plt.show()

gender = ['men', 'women']
can_medals = [61.6, 38.4]
plt.pie(can_medals, labels=gender)
plt.title("Gender Medals CA")
plt.show()

gender = ['men', 'women']
usa_medals = [410, 243]
plt.bar(gender, usa_medals)
plt.title("Gender Medals US")
plt.show()


can_gender = ["CAN Men", "CAN Women"]
can_hockey_medals = [370, 183]
plt.bar(can_gender, can_hockey_medals)
usa_gender = ["USA Men", "USA Women"]
usa_hockey_medals = [166, 101]
plt.bar(usa_gender, usa_hockey_medals)
plt.title("Gender Hockey Medals")
plt.show()
