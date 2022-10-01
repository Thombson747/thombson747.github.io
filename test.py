
from smrt import *
from smrt.inputs.sensor_list import passive
from smrt.atmosphere.simple_isotropic_atmosphere import SimpleIsotropicAtmosphere

# prepare inputs
ice_type = "firstyear"
thickness_snow = [10]
thickness_ice = [2.25]
corr_length_snow = [5e-5]
corr_length_ice = [25e-5]
salinity = [2.5e-3]
temperature_snow = [270]
temperature_ice = [270]
density_snow = [320]
density_ice = [910]
atmos = SimpleIsotropicAtmosphere(tbdown=30.,tbup=6.,trans=0.9)
# create the snowpack
snowpack = make_snowpack(thickness=thickness_snow,
                         microstructure_model="exponential",
                         density=density_snow,
                         temperature=temperature_snow,
                         corr_length=corr_length_snow,
			atmosphere=atmos)
ice_column = make_ice_column(ice_type=ice_type,
			thickness=thickness_ice,
			temperature=temperature_ice,
			microstructure_model="exponential",
			salinity=salinity,
			density=density_ice,
			corr_length=corr_length_ice)

#create a complex medium
medium = snowpack+ice_column
#medium = ice_column
# create the sensor
radiometer = sensor_list.amsr2('23' )
#radiometer = passive(21e9,35)
# create the model
m = make_model("iba", "dort")

# run the model
print ('FY ice Tbs of 23 at V and H:',m.run(radiometer, medium).Tb())

# outputs
#print(result.Tb())
