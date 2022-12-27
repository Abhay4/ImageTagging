import json

from db.dbaccess import dbAccess


class imageService():
    def __init__(self):
        self.db = dbAccess()

    def save(self,object_dict):
        id = object_dict["id"]
        name = object_dict["location"].split('/')[-1]
        photo = object_dict["location"]
        self.db.insert_blob(id,name,photo)

    def get(self,id):
        print(id)
        dbres = self.db.get_by_id(id)
        #print(dbres)
        #res_dict = {"id":dbres[0][0], "name":dbres[0][1]}
        return json.dumps(dbres)

    def getall(self):
        dbres = self.db.get_all()
        #print(dbres)
        return json.dumps(dbres)

    def add_tag(self,id,tags):
        dbres = self.db.update_tags(id,tags)
        return dbres