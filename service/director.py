from models.director import Director as DirectorModel

from schemas.director import Director
class DirectorService():
    def init(self, db):
        self.db = db
        
    def get_director(self):
        result = self.db.query(DirectorModel).all()
        return result
    
    def  create_director(self,director:DirectorModel):
        new_director = DirectorModel(
            dir_fname = director.dir_fname,
            dir_lname = director.dir_lname.upper()
            dir_fname = director.dir_fname.upper(),
            dir_iname = director.dir_iname.upper(),
            
        )
        self.db.add(new_director)
        self.db.commit()
        return
    

    def get_director_by_id(self, id: int):
        result = self.db.query(DirectorModel).filter(DirectorModel.id == id).first()
        return result

    def update_director(self, data: DirectorModel):
        director = self.db.query(DirectorModel).filter(DirectorModel.id == data.id).first()

    def get_for_id(self,id:int):
        result = self.db.query(DirectorModel).filter(DirectorModel.id == id). first()
        return result
    
    def update_director(self,data:Director):
        director = self.db.query(DirectorModel).filter(DirectorModel.id ==data.id).first()
        director.dir_fname = data.dir_fname
        director.dir_iname = data.dir_iname
        self.db.commit()
        return
    
    def delete_director(self, id: int):
        self.db.query(DirectorModel).filter(DirectorModel.id == id).delete()
        self.db.commit()
        return

