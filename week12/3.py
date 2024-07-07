#现在有2015.csv，2016.csv,2017.csv,2018.csv,2019.csv,2020.csv,其内容大致为Country,Region,Happiness Rank,Happiness Score,Standard Error,Economy (GDP per Capita),Family,Health (Life Expectancy),Freedom,Trust (Government Corruption),Generosity,Dystopia Residual
#Switzerland,Western Europe,1,7.587,0.03411,1.39651,1.34951,0.94143,0.66557,0.41978,0.29678,2.51738

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("2015.csv")
data1 = pd.read_csv("2016.csv")
data2 = pd.read_csv("2017.csv")
data3 = pd.read_csv("2018.csv")
data4 = pd.read_csv("2019.csv")
data5 = pd.read_csv("2020.csv")
# 加一列代表年份
data['Year'] = 2015
data1['Year'] = 2016
data2['Year'] = 2017
data3['Year'] = 2018
data4['Year'] = 2019
data5['Year'] = 2020
# 选特征
# 重命名列以匹配不同年份的文件结构
data2.rename(columns={'Happiness.Score': 'Happiness Score'}, inplace=True)
data3.rename(columns={'Country or region': 'Country', 'Score': 'Happiness Score', 'Freedom to make life choices': 'Freedom'}, inplace=True)
data4.rename(columns={'Country or region': 'Country', 'Score': 'Happiness Score', 'Freedom to make life choices': 'Freedom'}, inplace=True)
data5.rename(columns={'Country name': 'Country', 'Ladder score': 'Happiness Score', 'Freedom to make life choices': 'Freedom'}, inplace=True)

# 选择特征列
common_columns = ['Country', 'Happiness Score', 'Year','Freedom']
df_all = pd.concat([
    data[common_columns],
    data1[common_columns],
    data2[common_columns],
    data3[common_columns],
    data4[common_columns],
    data5[common_columns]
])
print(df_all)
#对于2015年 Happiness Score  前3的国家 绘制Dual-Axis，两个y指标为Happiness Score和Freedom ，X为Year
top_countries_2015 = data.nlargest(3, 'Happiness Score')

# 筛选这些国家在所有年份的数据
top_countries_all_years = df_all[df_all['Country'].isin(top_countries_2015['Country'])]

# 创建一个双轴图
fig, ax1 = plt.subplots()

# 绘制Happiness Score
for country in top_countries_2015['Country'].unique():
    country_data = top_countries_all_years[top_countries_all_years['Country'] == country]
    ax1.plot(country_data['Year'], country_data['Happiness Score'], label=f'{country} - Happiness Score')

ax1.set_xlabel('Year')
ax1.set_ylabel('Happiness Score', color='b')
ax1.tick_params('y', colors='b')
ax1.set_title('Happiness Score and Freedom Trends for Top 3 Countries')
ax1.set_xticks(range(2015, 2021))
ax1.legend(loc='upper left')

# 创建第二个y轴来绘制Freedom
ax2 = ax1.twinx()

# 绘制Freedom
for country in top_countries_2015['Country'].unique():
    country_data = top_countries_all_years[top_countries_all_years['Country'] == country]
    ax2.plot(country_data['Year'], country_data['Freedom'], marker='o', color='r', label=f'{country} - Freedom')

ax2.set_ylabel('Freedom', color='r')
ax2.tick_params('y', colors='r')

# 绘制图例
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='lower right')

# 显示图表
plt.show()