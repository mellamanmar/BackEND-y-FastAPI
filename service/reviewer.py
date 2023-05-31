from models.reviewer import Reviewer as ReviewerModel

class ReviewerService(): 
    def __init__(self,db): 
        self.db = db

    def get_reviewer(self): 
        result = self.db.query(ReviewerModel).all()
        return result

    def create_reviewer(self, reviewer: ReviewerModel): 
        new_reviewer = ReviewerModel( 
            rev_name = reviewer.rev_name.upper()
        )
        self.db.add(new_reviewer)
        self.db.commit()
        return    

    def get_reviewer_for_id(self, id:int):
        result = self.db.query(ReviewerModel).filter(ReviewerModel.id ==id).first()
        return result

    def update_reviewer(self, data:ReviewerModel): 
        reviewer = self.db.query(ReviewerModel).filter(ReviewerModel.id == data.id).first()
        reviewer.rev_name = data.rev_name
        self.db.commit()
        return 

    def delete_reviewer(self, id  :int ): 
        self .db.query(ReviewerModel).filter(ReviewerModel.id == id).delete()
        self.db.commit()
