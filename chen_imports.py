#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
-- PACKAGES --
Required packages for use with this module:
scipy
numpy
sympy
pint

-- UNITS --
For unit support add "u." in front of the unit name and multiply by the 
magnitude.

Examples:

distance = 25.5 * u.meter
distance = 25.5 * u.m
m = u.meter ;distance = 25 * m
area = 25.5 u.m**2

Units were used with python pint module. Complete documentation for use with
this module can be found at:

    https://pint.readthedocs.io/en/0.7.2/

-- CONSTANTS --
defined constants:

c    = 299792458.0 * u.m/u.sec             # Speed of Light
grav = 9.80665 * u.m / u.sec**2            # gravitational acceleration
R_g  = 8.314462175 * u.J/u.mol/u.K         # Ideal Gas constant
Na   = 6.0221409 * 10**23 / u.mol          # Avagadro's number
k_B  = 1.381648813 * 10**-23 * u.J/u.K     # Boltzmann's constant
h_c  = 6.6260695729 * 10**-34 * u.J*u.sec  # Planck's constant
F_c  = 9.64853399 * 10**4 * u.C/u.mol      # Faraday's Constant
"""
from __future__ import print_function
from sys import version, version_info
print("Running Version:", version)
if version_info[0] == 3:
    print("importing tools...",end="")
elif version_info[0] == 2:    
    print("importing tools...",)

# -- GENERAL -- #
from math import *
# from cmath import *
import numpy as np

# -- SOLVERS/OPTIMIZATION -- #
from scipy.optimize import fsolve
from scipy.integrate import odeint

# -- PLOTTING TOOLS -- #
import matplotlib.pyplot as plt

# -- SYMBOLIC MATH -- #
#import sympy as smp

# -- UNITS -- #
from pint import UnitRegistry
u = UnitRegistry()

# mass
mg = u.mg
gm = u.gram
amu = u.amu
kg = u.kilogram

# length
m = u.meter
ft = u.foot

cm = u.centimeter
inch = u.inch

km = u.kilometer
mile = u.mile

# time
sec = u.second
min = u.minute
hr = u.hour

# substance
mol = u.mol
kmol = 1000.0 * mol
lbmol = 453.59237 * mol

# temperature
K = u.kelvin

# energy
eV = u.eV
J = u.joule
kJ = u.kilojoule

# pressure
atm = u.atm
psi = u.psi
Pa = u.pascal

# power
W = u.watt
MW = u.megawatt

# activity
Bq = u.Bq

# charge
C = u.coulomb

# -- CONSTANTS -- #
c    = 299792458.0 * u.m/u.sec             # Speed of Light
grav = 9.80665 * u.m / u.sec**2            # gravitational acceleration
R_g  = 8.314462175 * u.J/u.mol/u.K         # Ideal Gas constant
Na   = 6.0221409 * 10**23 / u.mol          # Avagadro's number
k_B  = 1.381648813 * 10**-23 * u.J/u.K     # Boltzmann's constant
h_c  = 6.6260695729 * 10**-34 * u.J*u.sec  # Planck's constant
F_c  = 9.64853399 * 10**4 * u.C/u.mol      # Faraday's Constant

# -- FINISH IMPORTS -- #
print("Done.")