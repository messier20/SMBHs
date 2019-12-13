# SMBHs

## Notes
with iterations number = 20:  
exec time --- 45.99974203109741 seconds --- ;  
plot time --- 10.894582033157349 seconds ---

## Models
### v1
bulge_mass | bulge_scale | total_mass | virial_radius | bulge_disc_totalmass_fractions | bulge_disc_gas_fractions | bulge_totalmas | quasar_duration
------------ | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- 
2.e10 | 1.1645 | 1.e13 | 626 | 0.002 | 0.05 | 1 | 5.e9
3.e10 | 1.6638| 1.e13 | 626 | 0.003 | 0.1 | 1 | 5.e9
6.5e10 | 3.2855| 1.e13 | 626 | 0.0065 | 0.25 | 1 | 5.e9
1.e11 | 4.800| 1.e13 | 626 | 0.01 | 0.5 | 1 | 5.e9
3.e11 | 12.6214| 1.e13 | 626 | 0.03 | 1. | 1 | 5.e9

- smbh_grows = False 

## Parameters legend

### Program parameters
disc_mass = mdisc 

### Program arrays
mtot = total_mass  
fbt = bulge_disc_totalmass_fraction  

bt = bulge_totalmass  
fgh = halo_gas_fraction  
fgb = bulge_disc_gas_fraction  
bt = bulge_totalmass  
rvir = virial_radius  
conc = halo_concentration_parameters  
fdg = disc_gasfraction

a1 = dot_t1 #figure better naming  
repeating = repeating_equation  
teff = time_eff  
trep = quasar_dts  #figure out better naming  
tq = quasar_duration
  
lum = luminosity  
l = luminosity_coef  
ledd = luminosity_edd  
lagn_arr = luminosity_arr  
mbh = smbh_masses(array)/smbh_mass  
bhg = smbh_grows  
t_sal = salpeter_timescale
