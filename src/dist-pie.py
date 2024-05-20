import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams.update({'font.size': 22})

plt.figure(figsize=(8, 8))

labels = ['Ubuntu', 'Debian', 'RHEL', 'Gentoo', 'Others']
percentage = [33.9, 16, 10.3,0.5, 39.3]
plt.pie(percentage, labels=labels, autopct='%1.0f%%', colors=sns.color_palette('mako_r'))

# Title of the chart
plt.title('Linux Distributions Share')

# Save the chart as an SVG file
for ext in ["pdf", "svg", "png"]:
    plt.savefig(f'../images/{ext}/dist-chart.{ext}', format=ext, bbox_inches='tight')

plt.show()
