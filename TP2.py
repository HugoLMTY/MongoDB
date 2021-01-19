#!/usr/bin/env python
# coding: utf-8

# In[28]:


from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
db = client.gym
gym = db.Gymnases
sportifs = db.Sportifs
print("ok")


# In[224]:


gym.find()


# In[215]:


sportifs.find()


# In[216]:


for item in gym.find():
    print(item, "\n")


# In[42]:


for item in sportifs.find({ "Nom": "KERVADEC" }, {"_id":0, "Nom":1}):
    print(item)


# In[45]:


for item in sportifs.find({ "Age": {"$in": [32, 40]} }, {"_id":0, "Nom":1, "Age":1}):
    print(item)


# In[58]:


for item in sportifs.find({ "Sports.Jouer": "Basket ball"}, {"_id":0, "Nom":1, "Sports.Jouer":1}):
    print(item)


# In[61]:


for item in sportifs.find({"$or":[{ "Age": 32}, {"Sexe": "F"}]}, {"_id":0, "Nom":1, "Age":1}):
    print(item)


# In[63]:


sportifs.count_documents({"Sexe":"F"})


# In[86]:


for item in sportifs.find({ "Age": {"$gte": 20}, "Age":{"$lte": 30} }, {"_id":0, "Nom":1, "Age":1}):
    print(item)


# In[94]:


for item in sportifs.find({ "Sports.Jouer": "Hand ball" }, {"_id":1, "Nom":1}):
    print(item)


# In[121]:


for item in gym.find({ 
    "Surface": {"$gte":400}, 
    "$or":[{"Ville": "SARCELLES"}, {"Ville": "VILLETANEUSE"}] 
} ,{"_id":0, "NomGymnase":1, "Ville":1, "Surface":1}):
    print(item)


# In[171]:


for item in gym.aggregate([
    { "$match": { "Seances.Jour": "Mercredi"} },
    { "$limit": 1 },
    { "$unwind": "$Seances" }
]):
    print(item, "\n")


# In[177]:


for item in gym.find(
    { 
        "Seances.Libelle": "Hockey", 
        "Seances.Jour" : "mercredi",
        "Seances.Horaire": { "$gte" : 15 } },
    { 
        "_id": 0, "NomGymnase": 1, "Ville": 1, "Seances.Jour": 1, "Seances.Libelle": 1, "Seances.Horaire": 1 }
):
    print(item, "\n")


# In[183]:


for item in sportifs.find({
    "Sports.Jouer": {"$exists": False}
},{
    "id_":1,
    "Nom":1
}):
    print(item, "\n")


# In[185]:


for item in gym.find({
    "Seances.Jour": {"$nin": ["Dimanche","dimanche"]}
}, {
    "_id":0, "NomGymnase":1
}):
    print(item)


# In[200]:


for item in gym.find({
     "$and": [{"Seances.Libelle": "Basket ball"},{"Seances.Libelle": "Volley ball"}]}
,{
    "_id":0, "NomGymnase":1, "Seances.Libelle":1
}):
    print(item, "\n")


# In[203]:


for item in sportifs.find({
    "Sports.Jouer": {"$exists": True},
    "Sports.Entrainer": {"$exists": True}
},{
    "_id":0, "Nom":1
}):
    print(item)


# In[205]:


for item in sportifs.find({
    "Sports.Jouer": {"$exists": True},
    "IdSportifConseiller": {"$exists": True}
},{
    "_id":0, "Nom":1
}):
    print(item)


# In[210]:


for item in sportifs.find({
    "IdSportif": 
    list(db.Sportifs.find({ 
        "Nom": "KERVADEC" }))[0]["IdSportifConseiller"]
},{
    "_id":0, "Nom":1
}):
    print(item)


# In[212]:


for item in sportifs.find({
    "$and":[{"Sports.Entrainer": "Hand ball"}, {"Sports.Entrainer": "Basket ball"}]
},{
    "_id":0, "Nom":1
}):
    print(item)


# In[214]:


for item in sportifs.find({
    "IdSportifConseiller": {"$exists": False}    
},{
    "_id":0, "Nom":1
}):
    print(item)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




