from app import db, ma
from marshmallow import fields
# from controllers import recipes, users, comments

class Ingredient(db.Model):

    __tablename__ = 'ingredients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    nutrition_information = db.Column(db.String(500), nullable=False)

class IngredientSchema(ma.ModelSchema):

    recipe = fields.Nested('RecipeSchema', many=True, exclude=('ingredients'))

    class Meta:
        model = Ingredient
