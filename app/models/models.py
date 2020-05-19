#-*-coding:utf-8-*-

from app.extensions import db
from datetime import datetime

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    is_visible = db.Column(db.Boolean, default=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


class BlogModel(BaseModel):
    __tablename__ = "blog"
    is_public = db.Column(db.Boolean, default=True)
    title = db.Column(db.String(128))
    subtitle = db.Column(db.String(128), default="")
    content = db.Column(db.Text)


    @staticmethod
    def new_post(title, subtitle, content):
        newdata = BlogModel(title=title,
                            subtitle=subtitle,
                            content=content)
        db.session.add(newdata)
        db.session.commit()
    @staticmethod
    def get_all_public():
        results = db.session.query(BlogModel).filter(BlogModel.is_visible == True).order_by(BlogModel.create_time.desc()).all()
        alldata = []
        for data in results:
            temp = {}
            data2dict = data.to_dict()
            temp["title"] = data2dict["title"]
            temp["subtitle"] = data2dict["subtitle"]
            temp["content"] = data2dict["content"]
            temp["year"] = data2dict["create_time"].year
            temp["month"] = data2dict["create_time"].month
            temp["day"] = data2dict["create_time"].day
            temp["time"] = data2dict["create_time"].strftime("%H:%M:%S")
            temp["update_time"] = data2dict["update_time"]
            temp["id"] = data2dict["id"]
            alldata.append(temp)
        return alldata
    @staticmethod
    def get_article_by_id(id):
        article = db.session.query(BlogModel).get(id)
        if article is None:
            return None, None
        result = {}
        result["title"] = article.title
        result["subtitle"] = article.subtitle
        result["content"] = article.content
        result["year"] = article.update_time.year
        result["month"] = article.update_time.month
        result["day"] = article.update_time.day
        result["time"] = article.update_time.strftime("%H:%M:%S")
        result["id"] = article.id
        result["create_time"] = article.create_time
        return result
    @staticmethod
    def get_manage_list():
        results = db.session.query(BlogModel).filter(BlogModel.is_visible == True).order_by(BlogModel.create_time.desc()).all()
        alldata = []
        for data in results:
            data2dict = data.to_dict()
            alldata.append(data2dict)
        return alldata
    @staticmethod
    def delete_by_id(id):
        article = db.session.query(BlogModel).get(id)
        if article is None:
            return False
        else:
            article.is_visible = False
            db.session.commit()
            return True

