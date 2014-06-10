from app import db, models



firstname = ["Bobby Joe", "Kathy", "Dago", "Selina", "Elaine"]

lastname = ["Smith III", "Ortiz", "Bailon", "Musuta", "Kammley"]

username = ["bsmith", "kortiz", "dbailon", "smusuta", "ekammley"]

location = ["Minnesota","New York","Arizona","Washington, DC","California"]

email = ["bobbyjoe@codeforprogress", "kathy@codeforprogress.org", "dago@codeforprogress.org", "selina@codeforprogress.org", "elaine@codeforprogress.org"]

password =["bsmith1", "kortiz1", "dbailon1", "smusuta1", "ekammley1"]

role = ["community organizer","community organizer", "policy maker","community organizer", "policy maker"]

#Don't worry about indentation for dictionaries
for u in [0,1,2,3,4]:
	advocates = {"firstname": firstname[u], 
			 "lastname": lastname[u], 
			 "username": username[u], 
			 "location": location[u], 
			 "email": email[u], 
			 "password": password[u],
			 "role": role[u]
			 }

	u = models.User(**advocates)

	db.session.add(u)
	db.session.commit()

#for u in [0,1,2,3,4,5,6]:
#	newuser = models.User(id, firstname[u], lastname[u], username[u], location[u], email[u], password[u], role[u])
#db.session.add(u)
#db.session.commit()
