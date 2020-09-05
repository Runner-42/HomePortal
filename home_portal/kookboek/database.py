'''Database Models for the Kookboek application'''
from home_portal.extensions import db_kookboek as db


class RecipesIngredients(db.Model):
    '''
    The RecipiesIngredients class defines the attributes
    required to create a many-to-many relationship between recipes
    and ingredients.
    It also contains the amount and unit information for the required ingredients
    related to the recipe.
    '''
    __bind_key__ = 'kookboek_db'
    __tablename__ = 'RecipesIngredients'
    recipe_id = db.Column(
        db.Integer,
        db.ForeignKey('Recipes.id'),
        primary_key=True
    )
    ingredient_id = db.Column(
        db.Integer,
        db.ForeignKey('Ingredients.id'),
        primary_key=True
    )
    amount = db.Column(
        db.Numeric,
        nullable=False
    )
    unit = db.Column(
        db.String(64),
        unique=False,
        nullable=False
    )
    unit_description = db.Column(
        db.Text(),
        unique=False,
        nullable=True
    )


class Recipe(db.Model):
    '''
    The recipe class defines the attributes of the
    Recipes table
    '''
    __bind_key__ = 'kookboek_db'
    __tablename__ = 'Recipes'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(128),
        unique=True,
        nullable=False
    )
    category = db.Column(
        db.String(64),
        nullable=False
    )
    preparation = db.Column(
        db.Text(),
        nullable=True,
        unique=False
    )
    picture = db.Column(
        db.LargeBinary,
        nullable=True
    )
    ingredients = db.relationship('Ingredient',
                                  secondary=lambda: RecipesIngredients.__table__,
                                  backref='Recipe')

    def __repr__(self):
        return "testeke {} {}".format(self.id, self.name)

    @property
    def get_recipe_id(self):
        if self.id:
            return self.id
        else:
            return 0

    @property
    def get_ingredients_list(self):
        '''
        Function returns the ingredients related to a recipe
        Recipe information is provided via it's ID
        '''
        ingredients = Ingredient.query.join(
            RecipesIngredients,
            RecipesIngredients.recipe_id == self.id)\
            .filter(RecipesIngredients.ingredient_id == Ingredient.id)\
            .all()
        return ingredients


class Unit(db.Model):
    '''
    The Unit class defines the attributes of the unit
    table.
    '''
    __bind_key__ = 'kookboek_db'
    __tablename__ = 'Units'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(64),
        unique=True,
        nullable=False
    )
    description = db.Column(
        db.Text(),
        unique=False,
        nullable=True
    )


class Category(db.Model):
    '''
    The Category class defines the attributes of the category
    table.
    '''
    __bind_key__ = 'kookboek_db'
    __tablename__ = 'Categories'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(64),
        unique=True,
        nullable=False
    )
    description = db.Column(
        db.Text(),
        unique=False,
        nullable=True
    )


class Ingredient(db.Model):
    '''
    The Ingredient class defines the attributes of the ingredient
    table.
    '''
    __bind_key__ = 'kookboek_db'
    __tablename__ = 'Ingredients'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(64),
        unique=True,
        nullable=False
    )
    picture = db.Column(
        db.LargeBinary,
        nullable=True
    )
    default_unit = db.Column(
        db.String(32),
        nullable=False
    )
    unit_description = db.Column(
        db.String(128),
        nullable=True
    )
    default_amount = db.Column(
        db.Numeric,
        nullable=True
    )
    recipes = db.relationship('Recipe',
                              secondary=lambda: RecipesIngredients.__table__,
                              backref='Ingredient'
                              )
