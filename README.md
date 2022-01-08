# darmstadt-opendata-exporter

Scrapes data from https://datenplattform.darmstadt.de and presents it in the Prometheus Exposition format.

Pull requests welcome.

## Example

```
# HELP darmstadt_environment_no2_micrograms_per_cubic_meter Environment measurement for no2
# TYPE darmstadt_environment_no2_micrograms_per_cubic_meter gauge
darmstadt_environment_no2_micrograms_per_cubic_meter{sensor="3ac073c4-b5b8-421d-b91a-5aa001234f7e"} 9.5615
# HELP darmstadt_environment_o3_micrograms_per_cubic_meter Environment measurement for o3
# TYPE darmstadt_environment_o3_micrograms_per_cubic_meter gauge
darmstadt_environment_o3_micrograms_per_cubic_meter{sensor="3ac073c4-b5b8-421d-b91a-5aa001234f7e"} 70.83670000000001
# HELP darmstadt_environment_pm2_5_micrograms_per_cubic_meter Environment measurement for dust_pm2.5
# TYPE darmstadt_environment_pm2_5_micrograms_per_cubic_meter gauge
darmstadt_environment_pm2_5_micrograms_per_cubic_meter{sensor="3ac073c4-b5b8-421d-b91a-5aa001234f7e"} 0.1
# HELP darmstadt_environment_so2_micrograms_per_cubic_meter Environment measurement for so2
# TYPE darmstadt_environment_so2_micrograms_per_cubic_meter gauge
darmstadt_environment_so2_micrograms_per_cubic_meter{sensor="3ac073c4-b5b8-421d-b91a-5aa001234f7e"} 0.8
# HELP darmstadt_environment_pm10_micrograms_per_cubic_meter Environment measurement for dust_pm10
# TYPE darmstadt_environment_pm10_micrograms_per_cubic_meter gauge
darmstadt_environment_pm10_micrograms_per_cubic_meter{sensor="3ac073c4-b5b8-421d-b91a-5aa001234f7e"} 0.1
# HELP darmstadt_environment_co_milligrams_per_cubic_meter Environment measurement for co
# TYPE darmstadt_environment_co_milligrams_per_cubic_meter gauge
darmstadt_environment_co_milligrams_per_cubic_meter{sensor="3ac073c4-b5b8-421d-b91a-5aa001234f7e"} 0.10592399999999999
```
