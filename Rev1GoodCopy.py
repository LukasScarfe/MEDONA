import math

class solution:
    def __init__(self, elec_cond, liq_mass_dens, surf_tens, diff_coeff, vap_dens, press_rat, air_visc, dielec_const):
        self.elec_cond = elec_cond
        self.liq_mass_dens = liq_mass_dens
        self.surf_tens = surf_tens
        self.diff_coeff = diff_coeff
        self.vap_dens = vap_dens
        self.press_rat = press_rat
        self.air_visc = air_visc
        self.dielec_const = dielec_const
        
#oxylene = solution(1.00E-10, 875.23, 30.10, 7.5e4, 3.7, 8.7425E-3, 1.85E-3, 2.57)
#toluene = solution(100e-10, 862.36, 28.40, 7.3e4, 3.1, 3.87e-2, 1.85e-3, 2.38)
#mxylene = solution(100e-10, 860.02, 28.90, 6.8e4, 3.7, 1.109e-2, 1.85e-3, 2.36)


def init_drop_size(Q, soln): 
    #Calculates intial droplet size in um!!
    eps_0 = 8.85E-12 #constant (units???)
    #Q = 0.5E-3 #liquid flow rate
    k = soln.elec_cond #electrical conductivity
    rho = soln.liq_mass_dens #liquid mass density
    gamma = soln.surf_tens #liquid-air interfacial tension
    C_d = 1
    Q_cube = pow(Q, 3)
    insideBracks = (rho*Q_cube*eps_0)/(gamma*k)
    pow6 = pow(insideBracks, 1/6)
    initialDropSize = C_d*pow6
    return initialDropSize


def K_e(soln):
    #calculates evaporation Rate
    D_diff = soln.diff_coeff #mass diffusivity
    rho = soln.liq_mass_dens #again the liquid mass density... this should be input?? List of parameters can be always input?
    rho_g = soln.vap_dens #ITS SOLVENT VAPOUR DENSITY in my infinite wisdom I forgot to write down what this variable is,,,, time to go paper hunting
    P_rat = soln.press_rat #pressure ratio
    Ke = 8*D_diff*(rho_g/rho)*(P_rat) #final equation
    return Ke

def current(Q,soln):
    #current of droplet
    gamma = soln.surf_tens #surface tension
    k = soln.elec_cond #electrical Conductivity
    #Q = 1E-3 #flow rate
    kappa = soln.dielec_const #dielectric constant
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

def height_for_varying_volt(d_0, q_0, e_tim, V, soln):
    #calculates height based on evaporation time
    #dry particles should be hitting the substrate!
    mu = soln.air_visc #viscosity of air
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

def soln_choice(choice):
    if choice == "oxylene":
        soln = solution(1.00E-10, 875.23, 30.10, 7.5e4, 3.7, 8.7425E-3, 1.85E-3, 2.57)
    elif choice == "toluene":
        soln = solution(100e-10, 862.36, 28.40, 7.3e4, 3.1, 3.87e-2, 1.85e-3, 2.38)
    elif choice == "mxylene":
        soln = solution(100e-10, 860.02, 28.90, 6.8e4, 3.7, 1.109e-2, 1.85e-3, 2.36)
    else:
        print("error")
        soln = 0
    return soln

def final_calc(flow_input, volt_input, soln_choi):

    '''Hello this explains what the funtion does in the help function
    EITHER: I have the solutiuon parameters as a sting? 
    OR: I have a st4ring that somehow calls the object - could this be another fucntion?
    Python will send either floats or strings to python
    Lukas can do a dropdown menu: it will send a number OR string to the python
    '''
    soln = soln_choice(soln_choi)
    dropsize = init_drop_size(flow_input, soln)
    ke = K_e(soln)
    evaptime = evap_time(dropsize,ke)
    cur = current(flow_input, soln)
    dropcharge = drop_charge(dropsize, cur, flow_input)
    final_height = height_for_varying_volt(dropsize,dropcharge,evaptime,volt_input, soln)*1e4
    return final_height


print(final_calc(5e-6, 5e3, "oxylene"), "mm")
    


