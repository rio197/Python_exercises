import csv

hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud","10.2.5.6"]]

with open('hosts.csv', 'w', newline='', encoding='utf-8') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
