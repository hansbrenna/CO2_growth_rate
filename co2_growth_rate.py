# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 14:28:32 2016

@author: hanbre
"""
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

matplotlib.rcParams['xtick.labelsize']=14
matplotlib.rcParams['ytick.labelsize']=14

Ma = 5.15e18 #mass of atmosphere from wikipedia

conc = pd.read_excel('mauna_loa_co2_annual_mean.xlsx') #Mauna Loa CO2 concentration in ppmv from ftp://aftp.cmdl.noaa.gov/products/trends/co2/co2_annmean_mlo.txt
conc = conc.iloc[1:55] #getting 1960:2013
emis = pd.read_excel('global_co2_emissions.xlsx') #Global emissions in kiltons (kt) from http://data.worldbank.org/indicator/EN.ATM.CO2E.KT
emis = emis['World (kt)']*1e6 #converting to kg

Mco2 = Ma*conc['mean']/1.0e6 #Mass of CO2 in atmosphere assuming ML is representative (WMGHG)
dMco2 = pd.DataFrame(Mco2.values[1:54]-Mco2.values[0:53]) #Change in CO2 mass from year to year
ratio=emis.values[1:]/dMco2.values.transpose() #ration of emissions to change in mass

#Plotting
plt.plot(conc['year'],emis,label='Emissions',linewidth=2)
plt.plot(conc['year'].iloc[1:],dMco2,label='change in Mco2',linewidth=2)
plt.legend(loc='upper left',fontsize=14)
plt.xlabel('year',fontsize=16)
plt.ylabel('CO2 mass (kg)',fontsize=16)
plt.savefig('co2_emissions_vs_growth_rate.png',dpi=100,bbox_inches='tight')
plt.figure()
plt.plot(conc['year'].iloc[1:],ratio.transpose(),label='Emis/dMco2',linewidth=2)
plt.xlabel('year',fontsize=16)
plt.legend(loc = 'upper left',fontsize=14)
plt.savefig('co2_emissions_growth_rate_ratio.png',dpi=100,bbox_inches='tight')