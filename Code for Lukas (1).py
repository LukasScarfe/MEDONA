import math

#inputs are: solution, electric field strength and flow rate  
def solution_props_list(): #only o-xylene as of now
    proplist = [9,9,9,9,9,99,9,9] #initialize list with correct number of spaces
    proplist[0] = 1.00E-10 #electrical conductivity
    proplist[1] = 875.23 #liquid mass density
    proplist[2] = 30.10 #surface tension
    proplist[3] = 7.5e4 #diffusion coeff/mass diffusivity
    proplist[4] = 3.7 #vapour density
    proplist[5] = 8.715E-5 #pressure ratio
    proplist[6] = 1.85E-3 #viscosity of air
    proplist[7] = 2.56 #dielectric c6onstant
    return proplist

def init_drop_size(props, Q): 
    #Calculates intial droplet size in um!!
    eps_0 = 8.85E-12 #constant (units???)
    #Q = 0.5E-3 #liquid flow rate
    k = props[0] #electrical conductivity
    rho = props[1] #liquid mass density
    gamma = props[2] #liquid-air interfacial tension
    #kappa = props[7] #dielectric constant
    C_d = 1
    #C_d = 10.87*pow(kappa, -6/5)+4.08*pow(kappa, -1/3) #scaling constant (dielctric constant)
    Q_cube = pow(Q, 3)
    insideBracks = rho*Q_cube*eps_0/(gamma*k)
    pow6 = pow(insideBracks, 1/6)
    initialDropSize = C_d*pow6
    return initialDropSize


def K_e(props):
    #calculates evaporation Rate
    D_diff = 1 #mass diffusivity
    rho = props[1] #again the liquid mass density... this should be input?? List of parameters can be always input?
    rho_g = props[4] #ITS SOLVENT VAPOUR DENSITY in my infinite wisdom I forgot to write down what this variable is,,,, time to go paper hunting
    P_rat = props[5]
    Ke = 8*D_diff*(rho/rho_g)*(P_rat) #final equation
    return Ke

def current(props, Q):
    #current of droplet
    gamma = props[2]
    k = props[0]
    #Q = 1E-3 #flow rate
    kappa = props[7]
    scalConst = 1
    #scalConst = -449-0.21*kappa+157*pow(kappa, 1/6)+336*pow(kappa, -1/6)
    I_ins = gamma*k*Q/kappa
    I = scalConst*math.pow(I_ins, 1/2)
    return I
    
def evap_time(d_0, K_e):
    #time until evaporation 
    t_e = pow(d_0, 2)/K_e
    return t_e


def drop_charge(d_0, I, Q):
    #charge of droplet
    q_0 = (I/Q)*(math.pi/6)*math.pow(d_0, 3)
    return q_0

def terminal_velocity(d_0, q_0, props, V, H):
    #velcity of droplet inside the electric field
    E = V/H #electric field (V/H)
    mu = props[6]  #viscosity of air
    v_t = q_0*E/(3*math.pi*mu*d_0)
    return v_t

def height_for_varying_volt(d_0, q_0, e_tim, props, V):
    #calculates height based on evaporation time
    #dry particles should be hitting the substrate!
    mu = props[6]
    #d_0 = d_0*math.pow(10,-3)
    inside = e_tim*q_0*V/(3*math.pi*mu*d_0)
    height = math.sqrt(inside)
    return height
    
def drop_tof(v_t, h):
    #calculates time of flight for given stage height
    t_r = h/v_t
    return t_r

def dro_dist_to_evap(t_r,v_t):
    h = t_r/v_t
    return h

def final_calc(flow_input, volt_input):
    soln = solution_props_list()
    dropsize = init_drop_size(soln, flow_input)
    ke = K_e(soln)
    evaptime = evap_time(dropsize,ke)
    cur = current(soln, flow_input)
    dropcharge = drop_charge(dropsize, cur, flow_input)
    #termveloc = terminal_velocity(dropsize, dropcharge, soln, 5e3, 10e-2)
    #timeflight = drop_tof(termveloc, 3)
    final_height = height_for_varying_volt(dropsize,dropcharge,evaptime,soln,volt_input)*1e4
    return final_height
    
    
''' 
Hi Lukas I left all this garbage in which will do things I want it to do but you probably dont need to touch it




#This section used for testing code
#parameters for calcs
flwRt = 0.065e-6
soln = solution_props_list()

dropsize = init_drop_size(soln, flwRt)
ke = K_e(soln)
evaptime = evap_time(dropsize,ke)
cur = current(soln, flwRt)
dropcharge = drop_charge(dropsize, cur, flwRt)
termveloc = terminal_velocity(dropsize, dropcharge, soln, 5e3, 10e-2)
timeflight = drop_tof(termveloc, 3)



print("The initial droplet size should be", dropsize, "mm")
print("Evaporation time", evaptime, "s")
print("Droplet Terminal velocity", termveloc, "m/s")
print("Droplet Time of Flight", timeflight, "s")



#generate list of voltages to plug into functions
volt_list = []
volt = 1e3
while volt <= 5e3:
    volt = round(volt, 2)
    volt_list.append(volt)
    volt += 0.1e3

#convert from volts to kV, use volts for calcs, kV for plots
plt_vlt = []
for i in range(len(volt_list)):
    vlt = volt_list[i]/1000
    plt_vlt.append(vlt)

#generate list of flow rates to plug into functions!
flow_rates = []
flow = 0.01e-6
while flow <= 0.1e-6:
    flow = round(flow, 8)
    flow_rates.append(flow)
    flow += 0.01e-6

#convert flow for plotting later
flow_cnvt = []
for i in range(len(flow_rates)):
    flw = flow_rates[i]*1e6
    flw = round(flw, 3)
    flow_cnvt.append(flw)


    

#print(flow_rates)
#show droplet sizes at various flow rates
drop_sizes = []
drop_cnvt = []
big_height_list = []
  
for i in range(len(flow_rates)):
    
    flw = flow_rates[i]       
    #print(volt_list)    
    #calcs for varying voltage!!
    dropsize = init_drop_size(soln, flw)
    drop_sizes.append(dropsize)
    ke = K_e(soln)
    evaptime = evap_time(dropsize,ke)
    cur = current(soln, flw)
    dropcharge = drop_charge(dropsize, cur, flw)
    drp = drop_sizes[i]*1e3
    drop_cnvt.append(drp)
    
    #generate list of the heights for these voltages
    height_list = []
    for j in range(len(volt_list)):
        volt = volt_list[j]
        h = height_for_varying_volt(dropsize,dropcharge,evaptime,soln,volt)*1e4
        height_list.append(h)
    big_height_list.append(height_list)
        
    #print(height_list) 
    #Film Radius Calculation
    rad_list = []
    for k in range(len(height_list)):
        r = (1.2*(height_list[k]**2)+1.14*(height_list[k])-0.0010)
        rad_list.append(r) #already in units of cm
    
    #convert from m to cm
    plt_h = []
    for l in range(len(height_list)):
        h = height_list[l] #*100
        plt_h.append(h)   
    

    #set path and filename with the flowrate (changing across all graphs)
    fname1 = str(flow_cnvt[i]) + "flowratesubdist.png"
    path1 = 'C:/Users/jenni/Documents/University/FINAL YEAR!!!!/4A06 Capstone/Rev0Graphs/flow rate/' + fname1
    
    fname2 = str(flow_cnvt[i]) + "flowratesprayrad.png"
    path2 = 'C:/Users/jenni/Documents/University/FINAL YEAR!!!!/4A06 Capstone/Rev0Graphs/spray radius/' + fname2
    
    #plot each figure and then save to the 
    fig1 = mpl.plot(plt_vlt,plt_h, 'r.')
    mpl.xlabel('Voltage (kV)')
    mpl.ylabel('Distance to Substrate (cm)')
    title1 = 'Optimum Substrate Distance for Flow Rate ' + str(flow_cnvt[i]) + ' uL/s'
    mpl.title(title1)
    mpl.savefig(path1) 
    mpl.show()
    
    
    
    fig2 = mpl.plot(plt_h,rad_list, 'g.')
    mpl.xlabel('Distance to Substrate (cm)')
    mpl.ylabel('Radius of Desposition Area (cm)')
    title2 = 'Radius of Spray Area for Flow Rate ' + str(flow_cnvt[i]) + ' uL/s'
    mpl.title(title2)
    mpl.savefig(path2) 
    mpl.show()    
    



fig3 = mpl.plot(flow_cnvt, drop_cnvt, 'b.')
mpl.xlabel('Flow rate (uL/s)')
mpl.ylabel('Droplet Diameter (um)')
title = 'Initial Droplet Diameter for Varying Flow Rates'
mpl.title(title)
mpl.savefig('C:/Users/jenni/Documents/University/FINAL YEAR!!!!/4A06 Capstone/Rev0Graphs/DropletSizePlot') 
mpl.show()

'''