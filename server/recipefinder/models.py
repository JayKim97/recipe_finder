from recipefinder import db, ma
from datetime import datetime

likes = db.Table('likes',
                 db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                 db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')))

dislikes = db.Table('dislikes',
                    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')))

saves = db.Table('saves',
                 db.Column('user_id', db.Integer,
                           db.ForeignKey('user.id')),
                 db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')))

tags = db.Table('tags',
                db.Column('recipe_id', db.Integer,
                          db.ForeignKey('recipe.id')),
                db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')))

categories = db.Table('categories',
                      db.Column('recipe_id', db.Integer,
                                db.ForeignKey('recipe.id')),
                      db.Column('category', db.Integer, db.ForeignKey('category.id')))


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    recipe_tags = db.relationship(
        'Recipe', secondary=tags, backref=db.backref('tags', lazy='dynamic'))


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    recipe_category = db.relationship(
        'Recipe', secondary=categories, backref=db.backref('category', lazy='dynamic'))


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), unique=True, nullable=False)
    name = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    liked_recipes = db.relationship(
        'Recipe', secondary=likes, backref=db.backref('liked_users', lazy='dynamic'))
    disliked_recipes = db.relationship(
        'Recipe', secondary=dislikes, backref=db.backref('disliked_users', lazy='dynamic'))
    saved_recipes = db.relationship(
        'Recipe', secondary=saves, backref=db.backref('saved_users', lazy='dynamic'))
    recipes = db.relationship('Recipe', backref='creator', lazy=True)

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'name')


class Recipe(db.Model):
    __tablename__ = 'recipe'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    link = db.Column(db.String())
    num_likes = db.Column(db.Integer, nullable=False, default=0)
    num_dislike = db.Column(db.Integer, nullable=False, default=0)
    rating = db.Column(db.Float, nullable=False, default=0)
    instruction = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def update_like(self, current_user):
        already_liked = self.check_liked(current_user.id)
        already_disliked = self.check_disliked(current_user.id)
        if already_liked:
            self.decrease_like(current_user)
        else:
            self.increase_like(current_user)
            if already_disliked:
                self.decrease_dislike(current_user)

    def check_liked(self, user_id):
        liked = db.session.query(likes).filter_by(
            recipe_id=self.id, user_id=user_id).first()
        if liked:
            return True
        return False

    def increase_like(self, current_user):
        self.num_likes += 1
        self.liked_users.append(current_user)

    def decrease_like(self, current_user):
        self.num_likes -= 1
        self.liked_users.remove(current_user)

    def update_dislike(self, current_user):
        already_disliked = self.check_disliked(current_user.id)
        already_liked = self.check_liked(current_user.id)
        if already_disliked:
            self.decrease_dislike(current_user)
        else:
            self.increase_dislike(current_user)
            if already_liked:
                self.decrease_like(current_user)

    def check_disliked(self, user_id):
        disliked = db.session.query(dislikes).filter_by(
            recipe_id=self.id, user_id=user_id).first()
        if disliked:
            return True
        return False

    def increase_dislike(self, current_user):
        self.num_dislike += 1
        self.disliked_users.append(current_user)

    def decrease_dislike(self, current_user):
        self.num_dislike -= 1
        self.disliked_users.remove(current_user)

    def update_saved(self, current_user):
        already_saved = self.check_saved(current_user.id)
        if already_saved:
            self.saved_users.remove(current_user)
        else:
            self.saved_users.append(current_user)

    def check_saved(self, user_id):
        saved = db.session.query(saves=user_id).first()
        if saved:
            return True
        return False


class RecipeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'link', 'num_likes',
                  'num_dislike', 'rating', 'instruction', 'created_at', 'user_id')
