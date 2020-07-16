'''Kookboek forms'''
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import Length, DataRequired
from wtforms_alchemy.fields import QuerySelectField
from database import Unit, Ingredient


class AddUnitsForm(FlaskForm):
    '''
    The AddUnitsForm class defines the fields on the form
    to enter new units
    '''
    unit_name = StringField('Unit Name:',
                            validators=[DataRequired(message='Provide name for the unit'),
                                        Length(max=32,
                                               message='Max number of characters = %(max)d')])
    unit_description = StringField('Unit Description:',
                                   validators=[DataRequired(message='Provide description'),
                                               Length(max=128,
                                                      message='Maximum length = %(max)d')])
    submit_add = SubmitField('Add')


def get_unit_list():
    '''
    Function used as query_factory for QuerySelectField
    '''
    return Unit.query


class DelUnitsForm(FlaskForm):
    '''
    The DelUnitsForm class defines a field on the form
    representing a unit name and a "delete" button
    '''
    units = QuerySelectField(
        query_factory=get_unit_list, allow_blank=True, get_label='unit_name')
    submit_del = SubmitField('Remove')


def get_ingredient_list():
    '''
    Function used as query_factory for QuerySelectField
    '''
    return Ingredient.query


class AddIngredientsForm(FlaskForm):
    '''
    The AddIngredientsForm class defines the fields on the form
    to enter new ingredients
    '''
    ingredient_name = StringField('Ingredient Name:',
                                  validators=[DataRequired(message='Provide ingredient name'),
                                              Length(max=32,
                                                     message='Max number of characters = %(max)d')])
    ingredient_unit = QuerySelectField(
        query_factory=get_unit_list, allow_blank=False, get_label='unit_name')
    ingredient_default_amount = IntegerField('Default Amount')
    ingredient_picture = FileField('Picture', validators=[FileAllowed(['jpg', 'jpeg', 'png'],
                                                                      'Images only!')])
    submit_add = SubmitField('Add')


class DelIngredientsForm(FlaskForm):
    '''
    The DelIngredientsForm class defines a field on the form
    representing a ingredient name and a "delete" button
    '''
    ingredients = QuerySelectField(
        query_factory=get_ingredient_list, allow_blank=True, get_label='ingredient_name')
    submit_del = SubmitField('Remove')
