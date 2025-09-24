import numpy as np

m_dot_fuel = 6
m_dot_oxidiser = 9
p_c = 120 * 1e5 # Pa

rho_oxi = 1141
rho_fuel = 792

delta_P = 0.2 * p_c
C_d = 0.6

area_ox = m_dot_fuel / C_d / np.sqrt(2 * rho_oxi * delta_P)
area_fuel = m_dot_fuel / C_d / np.sqrt(2 * rho_fuel * delta_P)

print(f"Area lox = {area_ox}")
print(f"Area fuel = {area_fuel}")