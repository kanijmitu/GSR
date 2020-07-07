

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


# =============================================================================
#---------------------------- Analysing Peaksprrespondent theory -----------------------------------
# =============================================================================

#Creating Dataframe with IMotion Data for Galvanic Skin Response 
PeakPerRespondent=pd.read_csv("Peaksprrespondent.csv")
print (PeakPerRespondent)



sns.distplot(PeakPerRespondent['Amplitude'],hist=False, rug=True)
plt.xlabel('Distribution of all values before mapping')


#---------------------- Creating Data frame with OASIS data------------------------------

OasisD=pd.read_csv("OASIS.csv")
oasis=['Theme','Arousal_mean','Arousal_SD']
OasisDATA=OasisD[oasis]
print(OasisDATA)
OasisDATA = OasisDATA.rename(columns={'Theme': 'Stimulus'})
OasisDATA = OasisDATA.rename(columns={'Arousal_mean': 'OASIS_Arousal_mean'})
OasisDATA = OasisDATA.rename(columns={'Arousal_SD': 'OASIS_Arousal_std'})
print(OasisDATA)
sns.distplot(PeakPerRespondent['Amplitude'], hist=True, rug=True)
plt.xlabel('Amplitude distribution Before mapping')


#-------------------Before Mapping : Calculating Mean and Standard deviation of Amplitude column-------------------

iMotions_AmplitudeMean=PeakPerRespondent.groupby('Stimulus')['Amplitude'].mean()*10
print(iMotions_AmplitudeMean)
iMotions_AmplitudeStd=PeakPerRespondent.groupby('Stimulus')['Amplitude'].std()*10
print(iMotions_AmplitudeStd)
#--------------------Creating Datafarme with Amplitude mean and Amplitude Std series before maaping------------------------
Series1={'iMotions_AmplitudeMean':iMotions_AmplitudeMean,'iMotions_AmplitudeStd':iMotions_AmplitudeStd}
df=pd.DataFrame(Series1).reset_index()
df.columns=['Stimulus','iMotions_AmplitudeMean','iMotions_AmplitudeStd']
print(df)

#-------------------------Plotting Graph to show Amplitude mean and Std Distribution  before mapping----------------------

sns.distplot(df['iMotions_AmplitudeMean'], hist=True, rug=True)
sns.distplot(df['iMotions_AmplitudeStd'],  hist=True, rug=True)
plt.xlabel('Amplitude distribution Before mapping')


#-------------------Merging OASIS AND iMotions Data ---------------------



Merged_Data= pd.merge(df,OasisDATA, how='inner', on=['Stimulus'])

#----------------------------------Plotting error bar graph to show Amplitude mean and Std-------------------------
iMotions_AmplitudeMean=(Merged_Data.iMotions_AmplitudeMean)
iMotions_AmplitudeStd=(Merged_Data.iMotions_AmplitudeStd)
materials= (Merged_Data['Stimulus'])
x_pos = np.arange(len(materials))
fig, ax = plt.subplots(figsize=(10,5))
ax.bar(x_pos, iMotions_AmplitudeMean,yerr=iMotions_AmplitudeStd, align='center', alpha=0.30, ecolor='red', capsize=20)
ax.set_ylabel('values')
ax.set_xticks(x_pos)
ax.set_xticklabels(materials, rotation=90)
ax.set_title('error bar graph with Amplitude Mean and Std for each image')
ax.yaxis.grid(True)

#-----------------------------Comparing OASIS AND iMotions data before Mapping-------------------------------------
fig, ax = plt.subplots()
ax=Merged_Data.plot.bar(x='Stimulus',
                 y=['OASIS_Arousal_mean','iMotions_AmplitudeMean'],
                 yerr=Merged_Data[['OASIS_Arousal_std', 'iMotions_AmplitudeStd']].T.values,capsize=8,
                 align='center', alpha=0.5, ecolor='black',figsize=(16,7))
plt.show()
plt.savefig('Comparison of iMotions and OASIS Before Map')


# =============================================================================
#----------------------------GSR SUMMARY SCORE-----------------------------------
# =============================================================================

GSRSummaryScores=pd.read_csv("GSRSummaryScores.csv")
SummaryScores=['StimulusName/Scene','PeakCount','Peaks/Min']
SummaryScoresNew=GSRSummaryScores[SummaryScores]
print(SummaryScoresNew)

SummaryScoresNew= SummaryScoresNew.rename(columns={'StimulusName/Scene': 'Stimulus'})

sns.distplot(SummaryScoresNew['PeakCount'], hist=False, rug=True)
plt.xlabel('PeakCount distribution arcoss all data before mapping')

sns.distplot(SummaryScoresNew['Peaks/Min'], hist=False, rug=True)
plt.xlabel('Peaks/Min distribution before mapping')

iMotions_PeakCountMean=SummaryScoresNew.groupby('Stimulus')['PeakCount'].mean()*10
print(iMotions_PeakCountMean)
iMotions_PeakCountStd=SummaryScoresNew.groupby('Stimulus')['PeakCount'].std()*10
print(iMotions_PeakCountStd)
iMotions_PeakPerMinuteMean=SummaryScoresNew.groupby('Stimulus')['Peaks/Min'].mean()*10
print(iMotions_PeakPerMinuteMean)
iMotions_PeakPerMinuteStd=SummaryScoresNew.groupby('Stimulus')['Peaks/Min'].std()*10
print(iMotions_PeakPerMinuteStd)


#-------------------Creating Dataframe with Peakcount mean std and peaks/min mean and std series ---------------------
Series2={'iMotions_PeakCountMean':iMotions_PeakCountMean, 'iMotions_PeakCountStd':iMotions_PeakCountStd,'iMotions_PeakPerMinuteMean':iMotions_PeakPerMinuteMean,'iMotions_PeakPerMinuteStd':iMotions_PeakPerMinuteStd}
df2=pd.DataFrame(Series2).reset_index()
df2.columns=['Stimulus','iMotions_PeakCountMean','iMotions_PeakCountStd','iMotions_PeakPerMinuteMean','iMotions_PeakPerMinuteStd']
print(df2)


#-------------------Merging OASIS AND iMotions Data ---------------------



Merged_Data1= pd.merge(df2,OasisDATA, how='inner', on=['Stimulus'])

#----------------------------------Plotting error bar graph to show PeakCount mean and Std -------------------------
iMotions_PeakCountMean=(Merged_Data1.iMotions_PeakCountMean)
iMotions_PeakCountStd=(Merged_Data1.iMotions_PeakCountStd)
materials= (Merged_Data1['Stimulus'])
x_pos = np.arange(len(materials))
fig, ax = plt.subplots(figsize=(10,5))
ax.bar(x_pos, iMotions_PeakCountMean,yerr=iMotions_PeakCountStd, align='center', alpha=0.30, ecolor='red', capsize=20)
ax.set_ylabel('values')
ax.set_xticks(x_pos)
ax.set_xticklabels(materials, rotation=90)
ax.set_title('error bar graph with PeakCount Mean and Std for each image')
ax.yaxis.grid(True)
#----------------------------------Plotting error bar graph to show Peaks/Min mean and Std -------------------------
iMotions_PeakPerMinuteMean=(Merged_Data1.iMotions_PeakPerMinuteMean)
iMotions_PeakPerMinuteStd=(Merged_Data1.iMotions_PeakPerMinuteStd)
materials= (Merged_Data1['Stimulus'])
x_pos = np.arange(len(materials))
fig, ax = plt.subplots(figsize=(10,5))
ax.bar(x_pos, iMotions_PeakPerMinuteMean,yerr=iMotions_PeakPerMinuteStd, align='center', alpha=0.30, ecolor='red', capsize=20)
ax.set_ylabel('values')
ax.set_xticks(x_pos)
ax.set_xticklabels(materials, rotation=90)
ax.set_title('error bar graph with Peaks/Min Mean and Std for each image')
ax.yaxis.grid(True)



#-----------------------------Comparing OASIS AND iMotions data before Mapping-------------------------------------
fig, ax = plt.subplots()
ax=Merged_Data1.plot.bar(x='Stimulus',
                 y=['OASIS_Arousal_mean','iMotions_PeakCountMean','iMotions_PeakPerMinuteMean'],
                 yerr=Merged_Data1[['OASIS_Arousal_std', 'iMotions_PeakCountMean','iMotions_PeakPerMinuteStd']].T.values,capsize=8,
                 align='center', alpha=0.5, ecolor='black',figsize=(16,7))
ax.set_title('Comparing iMotions Peakcount and peaks/Min with OASIS Arousal')
plt.show()
plt.savefig('Comparison of iMotions and OASIS Before Map')


iMotions= pd.merge(df,df2, how='inner', on=['Stimulus'])
Bdataframe= pd.merge(iMotions,OasisDATA, how='inner', on=['Stimulus'])
fig, ax = plt.subplots(figsize=(25,15))
ax=Bdataframe.plot.bar(x='Stimulus',
                 y=['OASIS_Arousal_mean','iMotions_AmplitudeMean','iMotions_PeakCountMean'],
                 yerr=Bdataframe[['OASIS_Arousal_std','iMotions_AmplitudeStd','iMotions_PeakCountStd']].T.values,capsize=10,
                 align='center', alpha=0.5, ecolor='black',figsize=(18,10))
ax.set_title('Comparing iMotions scores with OASIS scores before Mapping')
plt.show()

#-----------------------------Distribution of values for the columnes used of iMitions-------------------------------------

sns.distplot(Bdataframe['iMotions_AmplitudeMean'], hist=False, rug=True)
sns.distplot(Bdataframe['iMotions_PeakCountMean'], hist=False, rug=True)
sns.distplot(Bdataframe['iMotions_PeakPerMinuteMean'], hist=False, rug=True)

plt.xlabel('Distribution of all data')



#--------------------------------------Rescaling iMotions data to match OASIS data ----------------------------------
#==================================================================================================
#========================MAPPING Amplitude column with Oasis===============
DF_Mapping=PeakPerRespondent[PeakPerRespondent['Amplitude']!=0]

DF_Mapping.loc[(DF_Mapping['Amplitude']>=0) & (DF_Mapping['Amplitude']<.1),'Amplitude']=1
DF_Mapping.loc[(DF_Mapping['Amplitude']>=0.1 ) & (DF_Mapping['Amplitude']<0.2),'Amplitude']=2
DF_Mapping.loc[(DF_Mapping['Amplitude']>=0.2) & (DF_Mapping['Amplitude']<0.3),'Amplitude']=3
DF_Mapping.loc[(DF_Mapping['Amplitude']>=0.3 ) & (DF_Mapping['Amplitude']<0.4),'Amplitude']=4
DF_Mapping.loc[(DF_Mapping['Amplitude']>=0.4 ) & (DF_Mapping['Amplitude']<0.5),'Amplitude']=5
DF_Mapping.loc[(DF_Mapping['Amplitude']>=0.5) & (DF_Mapping['Amplitude']<0.6),'Amplitude']=6
DF_Mapping.loc[(DF_Mapping['Amplitude']>=0.6 ) & (DF_Mapping['Amplitude']<0.8),'Amplitude']=7

#------------------ After mapping: Plotting graph showing Amplitude distribution------------------------------------------


sns.distplot(DF_Mapping['Amplitude'], hist=True, rug=True)
plt.xlabel('Distribution of all values  after mapping')

#--------------------After mapping: Calculating Amplitude mean and Std -------------------------------------------

iMotionsAmplitudeMean=DF_Mapping.groupby('Stimulus')['Amplitude'].mean()
print(iMotionsAmplitudeMean)
iMotionsAmplitudeStd=DF_Mapping.groupby('Stimulus')['Amplitude'].std(ddof=0)
print(iMotionsAmplitudeStd)
#-----------------------Creating Datafarme with Amlitude mean and std----------------------------------------------

Series1_Mapping={'iMotionsAmplitudeMean':iMotionsAmplitudeMean,'iMotionsAmplitudeStd':iMotionsAmplitudeStd}
df_Mapping=pd.DataFrame(Series1_Mapping).reset_index()
df_Mapping.columns=['Stimulus','iMotionsAmplitudeMean','iMotionsAmplitudeStd']
print(df_Mapping)
#-------------------------Plotting Graph to show Amplitude mean and Std Distribution  aefore mapping----------------------

sns.distplot(df_Mapping['iMotionsAmplitudeMean'], hist=True, rug=True)
sns.distplot(df_Mapping['iMotionsAmplitudeStd'],  hist=True, rug=True)
plt.xlabel('Amplitude distribution after mapping')



#----------------------Marging iMotions and OASIS-------------------------

Marged_MappedData= pd.merge(df_Mapping,OasisDATA, how='inner', on=['Stimulus'])

#----------------------------------Plotting error bar graph to show Amplitude mean and Std-------------------------
iMotionsAmplitudeMean=(Marged_MappedData.iMotionsAmplitudeMean)
iMotionsAmplitudeStd=(Marged_MappedData.iMotionsAmplitudeStd)
materials= (Marged_MappedData['Stimulus'])
x_pos = np.arange(len(materials))
fig, ax = plt.subplots(figsize=(10,5))
ax.bar(x_pos, iMotionsAmplitudeMean,yerr=iMotionsAmplitudeStd, align='center', alpha=0.30, ecolor='red', capsize=20)
ax.set_ylabel('values')
ax.set_xticks(x_pos)
ax.set_xticklabels(materials, rotation=90)
ax.set_title('error bar graph with Amplitude Mean and Std ')
ax.yaxis.grid(True)

#-----------------------------Comparing OASIS AND iMotions data after Mapping-------------------------------------
fig, ax = plt.subplots()
ax=Marged_MappedData.plot.bar(x='Stimulus',
                 y=['OASIS_Arousal_mean','iMotionsAmplitudeMean'],
                 yerr=Marged_MappedData[['OASIS_Arousal_std', 'iMotionsAmplitudeStd']].T.values,capsize=8,
                 align='center', alpha=0.5, ecolor='black',figsize=(16,7))
plt.show()
plt.savefig('Comparison of iMotions and OASIS after Map')


#========================MAPPING PeakCount and Peaks/mean colums with Oasis===============

DF_Mapping1=SummaryScoresNew[SummaryScoresNew['PeakCount']!=0]

DF_Mapping1.loc[(DF_Mapping1['PeakCount']>=0.06 ) & (DF_Mapping1['PeakCount']<1.48),'PeakCount']=1
DF_Mapping1.loc[(DF_Mapping1['PeakCount']>=1.48 ) & (DF_Mapping1['PeakCount']<2.9),'PeakCount']=2
DF_Mapping1.loc[(DF_Mapping1['PeakCount']>=2.9 ) & (DF_Mapping1['PeakCount']<4.32),'PeakCount']=3
DF_Mapping1.loc[(DF_Mapping1['PeakCount']>=4.32 ) & (DF_Mapping1['PeakCount']<5.74),'PeakCount']=4
DF_Mapping1.loc[(DF_Mapping1['PeakCount']>=5.74 ) & (DF_Mapping1['PeakCount']<7.16),'PeakCount']=5
DF_Mapping1.loc[(DF_Mapping1['PeakCount']>=7.16 ) & (DF_Mapping1['PeakCount']<8.58),'PeakCount']=6
DF_Mapping1.loc[(DF_Mapping1['PeakCount']>=8.58 ) & (DF_Mapping1['PeakCount']<11),'PeakCount']=7



sns.distplot(SummaryScoresNew['Peaks/Min'], hist=False, rug=True)
plt.xlabel('Peaks/Min distribution Before mapping')

DF_Mapping1.loc[(DF_Mapping1['Peaks/Min']>=0.05 ) & (DF_Mapping1['Peaks/Min']<2.62),'Peaks/Min']=1
DF_Mapping1.loc[(DF_Mapping1['Peaks/Min']>=2.62 ) & (DF_Mapping1['Peaks/Min']<5.19),'Peaks/Min']=2
DF_Mapping1.loc[(DF_Mapping1['Peaks/Min']>=5.19 ) & (DF_Mapping1['Peaks/Min']<7.76),'Peaks/Min']=3
DF_Mapping1.loc[(DF_Mapping1['Peaks/Min']>=7.76 ) & (DF_Mapping1['Peaks/Min']<10.33),'Peaks/Min']=4
DF_Mapping1.loc[(DF_Mapping1['Peaks/Min']>=10.33) & (DF_Mapping1['Peaks/Min']<12.9),'Peaks/Min']=5
DF_Mapping1.loc[(DF_Mapping1['Peaks/Min']>=12.9 ) & (DF_Mapping1['Peaks/Min']<15.47),'Peaks/Min']=6
DF_Mapping1.loc[(DF_Mapping1['Peaks/Min']>=15.47) & (DF_Mapping1['Peaks/Min']<19),'Peaks/Min']=7


sns.distplot(DF_Mapping1['PeakCount'], hist=False, rug=True)
plt.xlabel('PeakCount distribution after mapping')

sns.distplot(DF_Mapping1['Peaks/Min'], hist=False, rug=True)
plt.xlabel('Peaks/Min distribution after mapping')

iMotionsPeakCountMean=DF_Mapping1.groupby('Stimulus')['PeakCount'].mean()
print(iMotionsPeakCountMean)
iMotionsPeakCountStd=DF_Mapping1.groupby('Stimulus')['PeakCount'].std(ddof=0)
print(iMotionsPeakCountStd)

iMotionsPeakPerMinuteMean=DF_Mapping1.groupby('Stimulus')['Peaks/Min'].mean()
print(iMotionsPeakPerMinuteMean)
iMotionsPeakPerMinuteStd=DF_Mapping1.groupby('Stimulus')['Peaks/Min'].std(ddof=0)
print(iMotionsPeakPerMinuteStd)


Series3={'iMotionsPeakCountMean':iMotionsPeakCountMean,'iMotionsPeakCountStd':iMotionsPeakCountStd,'iMotionsPeakPerMinuteMean':iMotionsPeakPerMinuteMean,'iMotionsPeakPerMinuteStd':iMotionsPeakPerMinuteStd}
df3=pd.DataFrame(Series3).reset_index()
df3.columns=['Stimulus','iMotionsPeakCountMean','iMotionsPeakCountStd','iMotionsPeakPerMinuteMean','iMotionsPeakPerMinuteStd']
print(df3)



Marged_MappedData2= pd.merge(df3,OasisDATA, how='inner', on=['Stimulus'])

#----------------------------------Plotting error bar graph to show Peak Count mean and Std------------------------------
iMotionsPeakCountMean=(Marged_MappedData2.iMotionsPeakCountMean)
iMotionsPeakCountStd=(Marged_MappedData2.iMotionsPeakCountStd)
materials= (Marged_MappedData2['Stimulus'])
x_pos = np.arange(len(materials))
fig, ax = plt.subplots(figsize=(10,5))
ax.bar(x_pos, iMotionsPeakCountMean,yerr=iMotionsPeakCountStd, align='center', alpha=0.30, ecolor='red', capsize=20)
ax.set_ylabel('values')
ax.set_xticks(x_pos)
ax.set_xticklabels(materials, rotation=90)
ax.set_title('error bar graph with PeakCount Mean and Std for each image')
ax.yaxis.grid(True)

#----------------------------------Plotting error bar graph to show Peaks/Min mean and Std------------------------------
iMotionsPeakPerMinuteMean=(Marged_MappedData2.iMotionsPeakPerMinuteMean)
iMotionsPeakPerMinuteStd=(Marged_MappedData2.iMotionsPeakPerMinuteStd)
materials= (Marged_MappedData2['Stimulus'])
x_pos = np.arange(len(materials))
fig, ax = plt.subplots(figsize=(10,5))
ax.bar(x_pos, iMotionsPeakPerMinuteMean,yerr=iMotionsPeakPerMinuteStd, align='center', alpha=0.30, ecolor='red', capsize=20)
ax.set_ylabel('values')
ax.set_xticks(x_pos)
ax.set_xticklabels(materials, rotation=90)
ax.set_title('error bar graph with Peaks/Min Mean and Std for each image')
ax.yaxis.grid(True)



fig, ax = plt.subplots()
ax=Marged_MappedData2.plot.bar(x='Stimulus',
                 y=['OASIS_Arousal_mean','iMotionsPeakCountMean','iMotionsPeakPerMinuteMean'],
                 yerr=Marged_MappedData2[['OASIS_Arousal_std', 'iMotionsPeakCountMean','iMotionsPeakPerMinuteStd']].T.values,capsize=8,
                 align='center', alpha=0.5, ecolor='black',figsize=(16,7))
ax.set_title('Error Graph represents OASIS and iMotions peakcount and peaks/min (mean and std)  next to each other ')
plt.show()


#-----------------------------Comparing OASIS AND  all iMotions data after Mapping-------------------------------------



iMotions_Mapping= pd.merge(df_Mapping,df3, how='inner', on=['Stimulus'])
Adataframe= pd.merge(iMotions_Mapping,OasisDATA, how='inner', on=['Stimulus'])
fig, ax = plt.subplots(figsize=(25,15))
ax=Adataframe.plot.bar(x='Stimulus',
                 y=['OASIS_Arousal_mean','iMotionsAmplitudeMean','iMotionsPeakCountMean','iMotionsPeakPerMinuteMean'],
                 yerr=Adataframe[['OASIS_Arousal_std','iMotionsAmplitudeStd','iMotionsPeakCountStd','iMotionsPeakPerMinuteStd']].T.values,capsize=10,
                 align='center', alpha=0.5, ecolor='black',figsize=(15,7))
ax.set_title('Comparing OASIS scores with iMotions scores after Mapping')
plt.show()


iMotions_Mapping= pd.merge(df_Mapping,df3, how='inner', on=['Stimulus'])
Adataframe= pd.merge(iMotions_Mapping,OasisDATA, how='inner', on=['Stimulus'])
fig, ax = plt.subplots(figsize=(25,15))
ax=Adataframe.plot.bar(x='Stimulus',
                 y=['OASIS_Arousal_mean','iMotionsAmplitudeMean','iMotionsPeakCountMean'],
                 yerr=Adataframe[['OASIS_Arousal_std','iMotionsAmplitudeStd','iMotionsPeakCountStd']].T.values,capsize=10,
                 align='center', alpha=0.5, ecolor='black',figsize=(15,7))
ax.set_title('Comparing OASIS scores with iMotions scores after Mapping')
plt.show()


#-----------------------------Distribution of values after mapping  for the columnes used in iMotions data analysis -------------------------------------

sns.distplot(Adataframe['iMotionsPeakCountMean'], hist=True, rug=True)
sns.distplot(Adataframe['iMotionsPeakPerMinuteMean'], hist=True, rug=True)

plt.xlabel('Distribution of iMotions data after mapping')


#fig, ax = plt.subplots()
#ax=Bdataframe.plot.bar(x='Stimulus',
#                 y=['OASIS_Arousal_mean','iMotions_AmplitudeMean','iMotions_PeakCountMean',],
#                 yerr=Bdataframe[['OASIS_Arousal_std','iMotions_AmplitudeStd','iMotions_PeakCountStd']].T.values,capsize=8,
#                 align='center', alpha=0.5, ecolor='black',figsize=(16,7))
#
#plt.show()



#-------------------------



#Marging data frame
#Subtraction Before Mapping

#MeanScore=Bdataframe["OASIS_Arousal_mean"] - Bdataframe["iMotions_AmplitudeMean"]
#Bdataframe['MeanScore']=MeanScore
#
#StdScore=Bdataframe["OASIS_Arousal_std"] - Bdataframe["iMotions_AmplitudeStd"]
#Bdataframe['StdScore']=StdScore
#
#fig, ax = plt.subplots()
#ax=Bdataframe.plot.bar(x='Stimulus',
#                 y=['OASIS_Arousal_mean','iMotions_AmplitudeMean','MeanScore'],
#                 yerr=Bdataframe[['OASIS_Arousal_std','iMotions_AmplitudeStd','StdScore']].T.values,capsize=8,
#                 align='center', alpha=0.5, ecolor='black',figsize=(16,7))
#plt.show()
#PeakPerRespondent=pd.read_csv("Peaksprrespondent.csv")


#-----------------------------Mapping iMotions data and OASIS data using for loop -------------------------------------

#oasis_max=7
#imotions_max=0.8
##imotions_max=PeakPerRespondent['Amplitude'].max()
#for i in range(1, oasis_max):
#        PeakPerRespondent.loc[(PeakPerRespondent['Amplitude']>=((i-1)*imotions_max/oasis_max)) & (PeakPerRespondent['Amplitude']<(i*imotions_max/oasis_max)),'Amplitude']=i
#
#
#


#import numpy as np
#import matplotlib.pyplot as plt
#
#plt.style.use('ggplot')
#
#data = np.random.normal(size=10000)
#
## plt.hist gives you the entries, edges 
## and drawables we do not need the drawables:
#entries, edges, _ = plt.hist(data, bins=25, range=[-5, 5])
#
## calculate bin centers
#bin_centers = 0.5 * (edges[:-1] + edges[1:])
#
## draw errobars, use the sqrt error. You can use what you want there
## poissonian 1 sigma intervals would make more sense
#plt.errorbar(bin_centers, entries, yerr=np.sqrt(entries), fmt='r.')
#
#plt.show()
#
#plt.plot(Bdataframe['iMotions_AmplitudeMean'], Bdataframe['Stimulus'], 'line type', label='label here')
#plt.plot(Bdataframe['OASIS_Arousal_mean'], Bdataframe['Stimulus'], 'line type', label='label here')
#plt.legend(loc='best')
#plt.show()
#







