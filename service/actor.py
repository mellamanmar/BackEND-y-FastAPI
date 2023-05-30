from models.actor import Actor as ActorModel
from schemas.actor import Actor as ActorSchema

class ActorService():
    def __init__(self,db):
        self.db = db
    
    def get_actor(self):
        result = self.db.query(ActorModel).all()
        return result
    
    def create_actor(self, actor:ActorModel):
        new_actor = ActorModel(
            act_fname = actor.act_fname,
            act_lname = actor.act_lname,
            act_gender = actor.act_gender.upper()
        )
        self.db.add(new_actor)
        self.db.commit()
        return

    
    def get_for_id(self, id:int):
        result = self.db.query(ActorModel).filter(ActorModel.id == id).first()
        return result
    
    def update_actor(self,data:ActorModel):
        actor = self.db.query(ActorModel).filter(ActorModel.id == data.id).first()
        actor.act_fname = data.act_fname
        self.db.commit()
        return
    
    def delete_genre(self,id:int):
        self.db.query(ActorModel). filter(ActorModel.id == id). delete()
        self.db.commit()
