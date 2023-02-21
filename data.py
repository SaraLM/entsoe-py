from entsoe import EntsoeRawClient
import pandas as pd

client = EntsoeRawClient(api_key='5ee803f0-06f2-4a0c-bcea-414db1dd927a')
start = pd.Timestamp('20201201', tz ='UTC')
end = pd.Timestamp('20201202', tz ='UTC')
country_code_1 = 'DK'  # 
country_code_2 = 'DE_LU'  # 
country_code_3 = 'CZ'  # 

#day-ahead market prices (€/MWh)
DA_prices = client.query_day_ahead_prices(country_code_1, start=start,end=end)

#generation (MW)
generation = client.query_generation(country_code_1, start=start,end=end)
generation_per_plant = client.query_generation_per_plant(country_code_1, start=start,end=end)
generation_forecast = client.query_generation_forecast(country_code_1, start=start,end=end)
wind_solar_forecast = client.query_wind_and_solar_forecast(country_code_1, start=start,end=end, psr_type=None)
installed_generation_capacity = client.query_installed_generation_capacity(country_code_1, start=start,end=end)
installed_generation_capacity_per_unit = client.query_installed_generation_capacity_per_unit(country_code_1, start=start,end=end)

#load and load forecast (MW)
load = client.query_load(country_code_1, start=start,end=end)
load_forecast = client.query_load_forecast(country_code_1, start=start,end=end)

#day-ahead scheduled (commercial) exchanges (MW)
scheduled_exchanges = client.query_scheduled_exchanges(country_code_1, country_code_2, start=start,end=end)

#works only for countries without flow-based border (MW)

#contracted reserves (MW) and prices (€/MW/period)
contracted_reserve_amount = client.query_contracted_reserve_amount(country_code_1, start=start, end=end, type_marketagreement_type='A01')
contracted_reserve_prices = client.query_contracted_reserve_prices(country_code_1, start=start, end=end, type_marketagreement_type='A01')

#unavailability of generation and production units
unavailability_of_generation_units = client.query_unavailability_of_generation_units(country_code_1, start=start,end=end)
unavailability_of_production_units = client.query_unavailability_of_production_units(country_code_1, start=start,end=end)


df_plz = client.query_generation(country_code_1, start=start,end=end, psr_type=None)
test2 = client.query_generation_per_plant(country_code_1, start=start,end=end, psr_type=None)

