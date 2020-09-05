'''Kookboek forms'''
from wtforms_alchemy.fields import QuerySelectField
from wtforms.validators import Length, DataRequired
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, DecimalField,\
    TextAreaField, IntegerField
from home_portal.kookboek.database import Recipe, Category, Unit


def get_recipe_list():
    '''
    Function used as query_factory for QuerySelectField
    '''
    return Recipe.query


def get_category_list():
    '''
    Function used as query_factory for QuerySelectField
    '''
    return Category.query


def get_unit_list():
    '''
    Function used as query_factory for QuerySelectField
    '''
    return Unit.query


class UnitForm(FlaskForm):
    '''
    The  UnitForm class defines the unit specific fields
    '''

    name = StringField('Naam: ', validators=[
        DataRequired(),
        Length(max=64, message="Max length=%(max)d")])
    description = TextAreaField('Beschrijving: ')

    def __init__(self, unit: list = None, *args, **kwargs):
        '''
        Modified constructure to pre-populate the name and description field
        to allow updates to existing records
        '''
        super().__init__(*args, **kwargs)
        if unit:
            self.name.data = unit.name
            self.description.data = unit.description


class CategoryForm(FlaskForm):
    '''
    The  CategroyForm class defines the category specific fields
    '''

    name = StringField('Naam: ', validators=[
        DataRequired(),
        Length(max=64, message="Max length=%(max)d")])
    description = TextAreaField('Beschrijving: ')

    def __init__(self, category: list = None, *args, **kwargs):
        '''
        Modified constructure to pre-populate the name and description field
        to allow updates to existing records
        '''
        super().__init__(*args, **kwargs)
        if category:
            self.name.data = category.name
            self.description.data = category.description


class IngredientForm(FlaskForm):
    '''
    The  IngredientForm class defines the ingredient specific fields
    '''
    name = StringField('Naam: ', validators=[
        DataRequired(),
        Length(max=128, message="Max length=%(max)d")])
    default_unit = QuerySelectField('Eenheid: ',
                                    query_factory=get_unit_list,
                                    allow_blank=False,
                                    get_label='name')
    default_amount = DecimalField('Hoeveelheid: ',
                                  places=2)
    picture_file_picker = FileField('Foto: ',
                                    validators=[FileAllowed(['jpg', 'jpeg', 'png'],
                                                            'Images only!')])

    def __init__(self, ingredient: list = None, *args, **kwargs):
        '''
        Modified constructure to pre-populate the name and description field
        to allow updates to existing records
        '''
        super().__init__(*args, **kwargs)
        if ingredient:
            self.name.data = ingredient.name
            """ TO DO - Update value select field automatically """
            self.default_unit.data = ingredient.default_unit
            self.default_amount.data = ingredient.default_amount
            # self.picture_file_picker.data = None


class RecipeForm(FlaskForm):
    '''
    The  RecipeForm class defines the recipe specific fields
    '''
    id = IntegerField(id="recipe_id_field")
    name = StringField('Naam: ', validators=[
        DataRequired(),
        Length(max=128, message="Max length=%(max)d")])
    category = QuerySelectField('Categorie:',
                                query_factory=get_category_list,
                                allow_blank=False,
                                get_label='name')
    preparation = TextAreaField('Bereidingswijze:', render_kw={
                                'cols': 22, 'rows': 5})
    picture_file_picker = FileField('Foto:',
                                    validators=[FileAllowed(['jpg', 'jpeg', 'png'],
                                                            'Images only!')])

    def __init__(self, recipe: list = None, *args, **kwargs):
        '''
        Modified constructure to pre-populate the name, category and
        preparation fields to allow updates to existing records
        '''
        super().__init__(*args, **kwargs)
        if recipe:
            self.id.data = recipe.id
            self.name.data = recipe.name
            self.category.data = recipe.category
            self.preparation.data = recipe.preparation
