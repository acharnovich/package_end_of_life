import requests

# this script will use the end of life api to check the end of life date for the services and versions

# the idea is to run this up against environments and determine when packages are going to be EOL

services = {
    'CMS': ['php-8.1-1.module+el9.3.0.z+21063+f4ccb976.x86_64', 'tomcat-11.0', 'python-3.9', 'java-11-openjdk-headless-11.0.24.0.8-2.el9.x86_64', 'perl-5.32-481.el9.x86_64'],
    'DB System': ['java-11', 'redis-7.0'],
}

for service, values in services.items():

    for value in values:
        product = value.split("-")[0]
        cycle_version = value.split("-")[1]
        url = f"https://endoflife.date/api/{product}.json"
        request = requests.get(url)
        content = request.json()

        for index, version in enumerate(content):
            if version["cycle"] == cycle_version:
              if version["eol"] is not False:
                print(f"Your version of {product} v{cycle_version} for {service} has EOL of " + version["eol"])
              else:
                  print(f"{product} version v{cycle_version} does not have a EOL date")
