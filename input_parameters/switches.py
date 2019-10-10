

# TODO change everything to booleans
energy_driving = 1
momentum_driving = 0

#TODO Maybe move to coefficients?
eta_drive = 0.05                        #coupling efficiency between luminosity or momentum and driving power/force ///
######


#TODO maybe move to plot configs
clear_oscillations = 0                  #should we clear out the adiabatic oscillations? 0 - no, 1 - first velocity sign change (outflow starts collapsing), 2 - second velocity sign change (outflow bounces back)
post_cut = 0                            #should we remove the cleared out parts from the plots?
####

#choose integrator, only one allowed! no real difference among the three
# TODO change to one variable!!!
simple_integ = 1
leapfrog_dkd = 0
leapfrog_kdk = 0
######

bhg = 1                                 #toggle whether SMBH grows
repeating = 1.                          #toggle whether quasar outbursts repeat themselves
fade = 'none'                           #AGN episode fading prescription: none/exponential/powerlaw/king
energy_limit = 0                        #stop AGN activity once E_out,total > f_en*E_binding
f_en = 1.5

eta = 0.1                               #radiative efficiency
gamma = 5./3.                           #adiabatic index of the outflowing material

do_sf = 0
sfinst = 1                              #Toggle instantaneous SFR adjustment
sfr_adj = 1                             #Reduction of SFR
old_induction = 0