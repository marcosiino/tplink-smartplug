import xlsxwriter
import tplink_smartplug_module
import json

devices = [
    ["192.168.0.106", "Sogg. Lato Clima"],
    ["192.168.0.102", "Scaldabagno"],
    ["192.168.0.103", "Presa Lavatrice"],
    ["192.168.0.100", "Prese Letto"],
    ["192.168.0.104", "Prese TV Cam. Letto"],
    ["192.168.0.101", "Sogg. Lato Frigo"],
    ["192.168.0.105", "Sogg. PC e TV"]
]

dates = [
    {"month": 12, "year":2016},
    {"month": 1, "year":2017},
    {"month": 2, "year":2017}
]

# Returns an array of dictionary, where each items is a day of the specified month/year, with the following keys:
# 'energy': energy consumed in kWh, 'month': the specified month, 'day': the number of the day, 'year': the specified year
def get_emeter_daily(device_ip, month, year):
    command = "{\"emeter\":{\"get_daystat\":{\"month\":%d,\"year\":%d}}}}" % (month, year)

    response = tplink_smartplug_module.sendCommand(device_ip, command)
    #print("IP: %s @ %d/%d" % (device_ip, month, year))
    #print(response)

    if response is not None:
        deserializedJson = json.loads(response)
        return deserializedJson['emeter']['get_daystat']['day_list']
    else:
        return None

def write_xlsx(filename, months_years_array):

    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()

    worksheet.set_column(0, 0, 12)

    bold = workbook.add_format({'bold': True})

    worksheet.write(0, 0, 'Date', bold)

    for i in range(len(devices)):
        row = 1
        worksheet.write(0, i + 1, '%s (kWh)' % (devices[i][1]), bold)
        worksheet.set_column(i+1, i+1, 25)

        for month_year in months_years_array:

            deserializedDays = get_emeter_daily(devices[i][0], month_year["month"], month_year["year"])
            if deserializedDays is None:
                print("ERROR: Cannot get data from device for Month: %d, Year: %d" % (month_year["month"], month_year["year"]))
                continue

            for day in deserializedDays:
                date = "%d/%d/%d" % (day['day'], day['month'], day['year'])
                energy = day['energy']

                worksheet.write(row, 0, date)
                worksheet.write(row, i + 1, energy)

                row = row + 1

    print("Output: %s" % (filename))

write_xlsx("test.xlsx", dates)
