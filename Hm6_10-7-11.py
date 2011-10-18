import csv, urllib

url = 'https://raw.github.com/ctb/edda/master/doc/beacon-2011/tutorial5/fishies.csv'

def load_csv(url):
	fish_d = {}
	fp = urllib.urlopen(url)
	for row in csv.DictReader(fp):
		key = row['date']
		value = row['fish']
		
		x = fish_d.get(key, [])
		x.append(value)
		fish_d[key] = x
		
	return fish_d

#fish_d = load_csv('https://raw.github.com/ctb/edda/master/doc/beacon-2011/tutorial5/fishies.csv')

#print fish_d

def make_dates_dict(fish_d):
	dates_d = {}
	
	fishes=[]
	for key in fish_d.keys():
		for fish in fish_d[key]:
			fishes.append(fish)
	
	fish_set=set(fishes)
	
	for fish in fish_set:
		dates_d[fish] = []
		for key in fish_d:
			if fish in fish_d[key]:
				dates_d[fish].append(key)
		
	return dates_d

#dates_d = make_dates_dict(fish_d)

#print dates_d

def get_fishes_by_date(fish_d, date):
	fishlist = []
	if date in fish_d.keys():
		fishlist = fish_d[date]
	
	return fishlist

#print get_fishes_by_date(fish_d, '1/24')
#print get_fishes_by_date(fish_d, '2/29')

def get_dates_by_fish(dates_d, fish):
	dateslist = []
	if fish in dates_d.keys():
		dateslist = dates_d[fish]
	
	return dateslist

#print get_dates_by_fish(dates_d, 'salmon')
#print get_dates_by_fish(dates_d, 'zebrafish')

# this code is outside the functions and USES the functions to
# load data and ask questions of the data.

fish_d = load_csv('https://raw.github.com/ctb/edda/master/doc/beacon-2011/tutorial5/fishies.csv')
dates_d = make_dates_dict(fish_d)

print get_fishes_by_date(fish_d, '1/1')
print get_dates_by_fish(dates_d, 'plaice')


########
def get_fishes_by_datelist(fish_d, datelist):
	fishlist = []
	for date in datelist: 
		fishlist.extend(get_fishes_by_date(fish_d, date))
	
	return fishlist

#print get_fishes_by_datelist(fish_d, ['1/1', '3/5', '6/7'])

def get_dates_by_fishlist(dates_d, fishlist):
	datelist = []
	for fish in fishlist: 
		datelist.extend(get_dates_by_fish(dates_d, fish))
	
	return datelist

#print get_dates_by_fishlist(dates_d, ['plaice', 'sole', 'salmon'])

