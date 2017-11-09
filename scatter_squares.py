import matplotlib.pyplot as plt

#x_values = [1,2,3,4,5]
#y_value = [1,4,9,16,25]
x_values = list(range(1,1001))
y_value = [x**2 for x in x_values]

#plt.scatter(x_values, y_value, c='red', edgecolors='None', s=20)
#plt.scatter(x_values, y_value, c=(0,0,0.8), edgecolors='None', s=20)
plt.scatter(x_values, y_value, c=y_value,cmap=plt.cm.Blues , edgecolors='None', s=20)

#Назначение загаловка диаграмм и меток осей
plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#Назначение диапазона для каждой оси
plt.axis([0,1100,0,1100000])

#Назначение размера шрифта делений на осях
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()

#Автоматическое сохранение диаграмм
#plt.savefig('sq_plot.png', bbox_inches='tight')