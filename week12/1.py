#Freely explore the following datasets and present meaningful outcomes.#有个数据集Health_AnimalBites。csv.
#bite_date,SpeciesIDDesc,BreedIDDesc,GenderIDDesc,color,vaccination_yrs,vaccination_date,victim_zip,AdvIssuedYNDesc,WhereBittenIDDesc,quarantine_date,DispositionIDDesc,head_sent_date,release_date,ResultsIDDesc
#1985-05-05 00:00:00,DOG,,FEMALE,LIG. BROWN,1,1985-06-20 00:00:00,40229,NO,BODY,1985-05-05 00:00:00,UNKNOWN,,,UNKNOWN

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Health_AnimalBites.csv")

#对于不同SpeciesIDDesc的动物，统计其WhereBittenIDDesc的情况，画Stacked Bar/Column
data = data[['SpeciesIDDesc', 'WhereBittenIDDesc']]
data = data.groupby(['SpeciesIDDesc', 'WhereBittenIDDesc']).size().unstack()
data.plot(kind='bar', stacked=True)
plt.show()
