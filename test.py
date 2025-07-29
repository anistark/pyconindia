from pyconindia.conference import Conference

conf = Conference()

print("Current year:", conf.year())
print("Current city:", conf.city())
print("Current state:", conf.state())
print("Current venue:", conf.venue())
print("Current location:", conf.location())
print("Current month:", conf.month())
print("Current dates:", conf.dates())
print("Current status:", conf.status())
print("Current CFP:", conf.cfp())
print("Current website:", conf.website())

print("\nHistorical data:")
print("2023 city:", conf.city(2023))
print("2023 venue:", conf.venue(2023))
print("2023 status:", conf.status(2023))
print("2023 cfp:", conf.cfp(2023))

print("\nAll conference info for 2024:")
info_2024 = conf.get_conference_info(2024)
for key, value in info_2024.items():
    print(f"{key}: {value}")

print("\nAll available years:", conf.get_all_years())
