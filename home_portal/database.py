'''Database Models'''
# from sqlalchemy import Column, Integer, String
# from flask_sqlalchemy import SQLAlchemy
from home_portal import db

# Data Model for the Kookboek applications


class Unit(db.Model):
    '''
    The Unit class defines the attributes of the Units table
    '''
    __tablename__ = 'Units'
    unit_id = db.Column(
        db.Integer,
        primary_key=True
    )
    unit_name = db.Column(
        db.String(32),
        unique=True,
        nullable=False
    )
    unit_description = db.Column(
        db.String(128),
        unique=False,
        nullable=False
    )

    def __repr__(self):
        return '<Kookboek Units: {} - {}/{}>'.format(
            self.unit_id,
            self.unit_name,
            self.unit_description)


class Ingredient(db.Model):
    '''
    The Ingredient class defines the attributes of the
    Ingredients table
    '''
    __tablename__ = 'Ingredients'
    ingredient_id = db.Column(
        db.Integer,
        primary_key=True
    )
    ingredient_name = db.Column(
        db.String(128),
        unique=True,
        nullable=False
    )
    ingredient_picture = db.Column(db.LargeBinary, nullable=True)
    ingredient_unit = db.Column(db.String(32), nullable=False)
    ingredient_unit_description = db.Column(db.String(128), nullable=True)
    ingredient_default_amount = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Kookboek Ingredients: {} - {} {} {}>'.format(
            self.ingredient_id,
            self.ingredient_name,
            self.ingredient_unit,
            self.ingredient_unit_description)


class Category(db.Model):
    '''
    The Category class defines the attributes of the category
    table.
    '''
    __tablename__ = 'Categories'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(32),
        unique=True,
        nullable=False
    )
    description = db.Column(
        db.String(128),
        unique=False,
        nullable=True
    )

    def __repr__(self):
        return '<Kookboek Categories: {} - {} {}>'.format(
            self.id,
            self.name,
            self.description)


class Recipe(db.Model):
    '''
    The recipe class defines the attributes of the
    Recipes table
    '''
    __tablename__ = 'Recipes'
    RecipeId = db.Column(
        db.Integer,
        primary_key=True
    )
    RecipeName = db.Column(
        db.String(128),
        unique=True,
        nullable=False
    )

    def __repr__(self):
        return '<Kookboek Recipes: {} - {}>'.format(
            self.RecipeId,
            self.RecipeName)
