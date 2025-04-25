from scipy import constants

# Metric Prefixes
print("\n Metric (SI) Prefixes ")
print(constants.yotta, constants.zetta, constants.exa, constants.peta, constants.tera,
      constants.giga, constants.mega, constants.kilo, constants.hecto, constants.deka,
      constants.deci, constants.centi, constants.milli, constants.micro, constants.nano,
      constants.pico, constants.femto, constants.atto, constants.zepto)

# Binary Prefixes
print("\nBinary Prefixes")
print(constants.kibi, constants.mebi, constants.gibi, constants.tebi, constants.pebi,
      constants.exbi, constants.zebi, constants.yobi)

# Mass
print("\nMass")
print(constants.gram, constants.metric_ton, constants.grain, constants.lb, constants.pound,
      constants.oz, constants.ounce, constants.stone, constants.long_ton, constants.short_ton,
      constants.troy_ounce, constants.troy_pound, constants.carat, constants.atomic_mass,
      constants.m_u, constants.u)

# Angle
print("\nAngle")
print(constants.degree, constants.arcmin, constants.arcminute, constants.arcsec, constants.arcsecond)

# Time
print("\nTime")
print(constants.minute, constants.hour, constants.day, constants.week,
      constants.year, constants.Julian_year)

# Length
print("\nLength")
print(constants.inch, constants.foot, constants.yard, constants.mile, constants.mil,
      constants.pt, constants.point, constants.survey_foot, constants.survey_mile,
      constants.nautical_mile, constants.fermi, constants.angstrom, constants.micron,
      constants.au, constants.astronomical_unit, constants.light_year, constants.parsec)

# Pressure
print("\nPressure")
print(constants.atm, constants.atmosphere, constants.bar, constants.torr,
      constants.mmHg, constants.psi)

# Area
print("\nArea")
print(constants.hectare, constants.acre)

# Volume
print("\nVolume")
print(constants.liter, constants.litre, constants.gallon, constants.gallon_US,
      constants.gallon_imp, constants.fluid_ounce, constants.fluid_ounce_US,
      constants.fluid_ounce_imp, constants.barrel, constants.bbl)

# Speed
print("\nSpeed ")
print(constants.kmh, constants.mph, constants.mach,
      constants.speed_of_sound, constants.knot)

# Temperature
print("\nTemperature ")
print(constants.zero_Celsius, constants.degree_Fahrenheit)

# Energy
print("\nEnergy ")
print(constants.eV, constants.electron_volt, constants.calorie, constants.calorie_th,
      constants.calorie_IT, constants.erg, constants.Btu, constants.Btu_IT,
      constants.Btu_th, constants.ton_TNT)

# Power
print("\nPower")
print(constants.hp, constants.horsepower)

# Force
print("\nForce")
print(constants.dyn, constants.dyne, constants.lbf,
      constants.pound_force, constants.kgf, constants.kilogram_force)

# Pi
print("\nMath Constant")
print("PI:", constants.pi)
