from read import load_data

def remove_subdomain(url):
    url = str(url)
    pieces = url.split('.')
    domain = url
    if len(pieces) > 2:
        domain = pieces[1] + '.' + pieces[2]
        
    return(domain)


df = load_data()
df['url'] = df['url'].apply(remove_subdomain)
domains = df.loc[:,'url'].value_counts()


for name, count in domains[:100].items():
    print("{0}: {1}".format(name, count))
#print(domains[:100])

remove_subdomain('groups.google.com')