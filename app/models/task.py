from app import db

# many tasks
class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime, nullable=True)
    goal_id = db.Column(db.Integer, db.ForeignKey("goal.goal_id"), nullable=True)
    goals = db.relationship("Goal", back_populates="tasks")


    def to_dict(self):
        if self.completed_at is None:
            if self.goal_id is None:
                task_dict = {
                    "id" : self.task_id,
                    "title" : self.title,
                    "description" : self.description,
                    "is_complete" : False
                }
            else:
                task_dict = {
                    "id" : self.task_id,
                    "goal_id": self.goal_id,
                    "title" : self.title,
                    "description" : self.description,
                    "is_complete" : False
                } 
        else:
            task_dict = {
                "id" : self.task_id,
                "title" : self.title,
                "description" : self.description,
                "is_complete" : True
            }
        return task_dict

    @classmethod
    def from_dict(cls, data_dict):
        if "title" in data_dict and "description" in data_dict:
            if "completed_at" in data_dict:
                new_task = cls(title=data_dict["title"],
                description=data_dict["description"],
                completed_at=data_dict["completed_at"])

            else:
                new_task = cls(title=data_dict["title"],
                description=data_dict["description"])

        return new_task
