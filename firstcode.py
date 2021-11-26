import wget
#for downloading year wise
#url = "https://cve.mitre.org/data/downloads/allitems-cvrf-year-1999.xml"
#wget.download(url)
#for loop for downloading all years
for i in range(1999, 2022):
    url = "https://cve.mitre.org/data/downloads/allitems-cvrf-year-{}.xml".format(i)
    wget.download(url)
    print("downloaded", i)
print("ALL xml files downloaded")
