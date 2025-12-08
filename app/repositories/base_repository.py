from sqlalchemy.orm  import Session

class BaseRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, obj):
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj

    def get(self, model, id: int):
        return self.session.query(model).filter(model.id == id).first()

    def delete(self, obj):
        self.session.delete(obj)
        self.session.commit()


