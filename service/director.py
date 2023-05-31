from models.director import Director as DirectorModel


class DirectorService():
    def __init__(self, db):
        self.db = db
    
    def get_director(self):
        result = self.db.query(DirectorModel).all()
        return result

    def create_director(self, director: DirectorModel):
        new_director = DirectorModel(
            dir_fname = director.dir_fname,
            dir_lname = director.dir_lname.upper()
        )
        self.db.add(new_director)
        self.db.commit()
        return
    
    def get_director_by_id(self, id: int):
        result = self.db.query(DirectorModel).filter(DirectorModel.id == id).first()
        return result

    def update_director(self, data: DirectorModel):
        director = self.db.query(DirectorModel).filter(DirectorModel.id == data.id).first()
        director.dir_fname = data.dir_fname
        director.dir_lname = data.dir_lname
        self.db.commit()
        return 

    def delete_director(self, id: int):
        self.db.query(DirectorModel).filter(DirectorModel.id == id).delete()
        self.db.commit()