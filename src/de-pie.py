import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams.update({'font.size': 22})

plt.figure(figsize=(8, 8))

labels = ['Xfce', 'KDE Plasma', 'Gnome Shell', 'Cinnamon', 'Others']
percentage = [35, 27, 17, 11, 8]
plt.pie(percentage, labels=labels, autopct='%1.0f%%', colors=sns.color_palette('mako_r'))

# Title of the chart
plt.title('Desktop Environment Share')

# Save the chart as an SVG file
for ext in ["pdf", "svg", "png"]:
    plt.savefig(f'../images/{ext}/de-chart.{ext}', format=ext, bbox_inches='tight')

plt.show()
