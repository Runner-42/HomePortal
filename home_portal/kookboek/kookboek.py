'''Kookboek routes'''
from flask import Blueprint
from flask import render_template, session, redirect, url_for, make_response
from sqlalchemy import exc
from .kookboek_forms import AddUnitsForm, DelUnitsForm, AddIngredientsForm, DelIngredientsForm
from database import db, Unit, Ingredient

# Blueprint Configuration
kookboek_bp = Blueprint('kookboek_bp', __name__,
                        template_folder='templates',
                        static_folder='static')


@kookboek_bp.route('/')
def kookboek():
    '''homepage'''
    status = "Under construction"
    return render_template('kookboek/kookboek.html',
                           kookboek_site_status=status)


@kookboek_bp.route('/manage_units', methods=['GET', 'POST'])
def manage_units():
    '''Page to manage units'''
    form_add_unit = AddUnitsForm()
    form_del_unit = DelUnitsForm()
    units = Unit.query.order_by('unit_name').all()
    if form_add_unit.submit_add.data and form_add_unit.validate():
        new_unit = Unit(unit_name=form_add_unit.unit_name.data,
                        unit_description=form_add_unit.unit_description.data)
        try:
            db.session.add(new_unit)
            session['kookboek_status'] = str(
                "Unit {} added".format(new_unit.unit_name))
            db.session.commit()
        except exc.SQLAlchemyError as err:
            db.session.rollback()
            session['kookboek_status'] = str(
                "-Add Error- unable to add {} in DB {}!".format(new_unit.unit_name, str(err.args)))
            return render_template('kookboek/units.html',
                                   form_add=form_add_unit,
                                   form_del=form_del_unit,
                                   units_list=units,
                                   kookboek_site_status=session.get(
                                       'kookboek_status')
                                   )
        return redirect(url_for('kookboek_bp.manage_units'))
    if form_del_unit.submit_del.data and form_del_unit.validate():
        try:
            if form_del_unit.units.data is not None:
                session['kookboek_status'] = str("Removing Unit: {}".format(
                    form_del_unit.units.data.unit_name))
                db.session.delete(form_del_unit.units.data)
                db.session.commit()
            else:
                session['kookboek_status'] = str(
                    "-Remove Error- Please select a valid Unit!")
                return render_template('kookboek/units.html',
                                       form_add=form_add_unit,
                                       form_del=form_del_unit,
                                       units_list=units,
                                       kookboek_site_status=session.get('kookboek_status'))
        except exc.SQLAlchemyError as err:
            session['kookboek_status'] = str(
                "-Remove Error- Unable to delete record from DB ({})!".format(str(err.args)))
            db.session.rollback()
            return render_template('kookboek/units.html',
                                   form_add=form_add_unit,
                                   form_del=form_del_unit,
                                   units_list=units,
                                   kookboek_site_status=session.get('kookboek_status'))
        return redirect(url_for('kookboek_bp.manage_units'))
    return render_template('kookboek/units.html',
                           form_add=form_add_unit,
                           form_del=form_del_unit,
                           units_list=units,
                           kookboek_site_status=session.get('kookboek_status'))


@kookboek_bp.route('/manage_ingredients/ingredient_picture/<id_ingredient>',
                   methods=['GET', 'POST'])
def get_ingredient_picture(id_ingredient):
    '''
    Function returns the image of an ingredient, based on the record id,
    stired in the database
    '''
    image = Ingredient.query.filter_by(ingredient_id=id_ingredient).first()
    if image.ingredient_picture is not None:
        response = make_response(image.ingredient_picture)
        response.headers.set('Content-Type', 'image/jpeg')
    else:
        response = make_response("None")
        response.headers.set('Content-Type', 'text/plain')
    return response


@kookboek_bp.route('/manage_ingredients', methods=['GET', 'POST'])
def manage_ingredients():
    '''Page to manage ingredients'''
    form_add_ingredient = AddIngredientsForm()
    form_del_ingredient = DelIngredientsForm()
    ingredients = Ingredient.query.order_by('ingredient_name').all()
    units = Unit.query.order_by('unit_name').all()
    if form_add_ingredient.submit_add.data and form_add_ingredient.validate():
        if form_add_ingredient.ingredient_picture.data is not None:
            image_data = form_add_ingredient.ingredient_picture.data.read()
        else:
            image_data = None
        new_ingredient = \
            Ingredient(ingredient_name=form_add_ingredient.ingredient_name.data,
                       ingredient_default_amount=form_add_ingredient.ingredient_default_amount.data,
                       ingredient_unit=form_add_ingredient.ingredient_unit.data.unit_name,
                       ingredient_unit_description=form_add_ingredient.ingredient_unit.data.unit_description,
                       ingredient_picture=image_data)
        try:
            db.session.add(new_ingredient)
            session['kookboek_status'] = str(
                "Ingredient {} added".format(new_ingredient.ingredient_name))
            db.session.commit()
        except exc.SQLAlchemyError as err:
            db.session.rollback()
            session['kookboek_status'] = str(
                "-Add Error- unable to add {} in DB {}!".format(
                    new_ingredient.ingredient_name, str(err.args)))
            return render_template('kookboek/ingredients.html',
                                   form_add=form_add_ingredient,
                                   form_del=form_del_ingredient,
                                   ingredients_list=ingredients,
                                   units_list=units,
                                   kookboek_site_status=session.get(
                                       'kookboek_status')
                                   )
        return redirect(url_for('kookboek_bp.manage_ingredients'))
    if form_del_ingredient.submit_del.data and form_del_ingredient.validate():
        try:
            if form_del_ingredient.ingredients.data is not None:
                session['kookboek_status'] = str("Removing Ingredient: {}".format(
                    form_del_ingredient.ingredients.data.ingredient_name))
                db.session.delete(form_del_ingredient.ingredients.data)
                db.session.commit()
            else:
                session['kookboek_status'] = str(
                    "-Remove Error- Please select a valid Ingredient!")
                return render_template('kookboek/ingredients.html',
                                       form_add=form_add_ingredient,
                                       form_del=form_del_ingredient,
                                       ingredients_list=ingredients,
                                       units_list=units,
                                       kookboek_site_status=session.get('kookboek_status'))
        except exc.SQLAlchemyError as err:
            session['kookboek_status'] = str(
                "-Remove Error- Unable to delete record from DB ({})!".format(str(err.args)))
            db.session.rollback()
            return render_template('kookboek/ingredients.html',
                                   form_add=form_add_ingredient,
                                   form_del=form_del_ingredient,
                                   ingredients_list=ingredients,
                                   units_list=units,
                                   kookboek_site_status=session.get('kookboek_status'))
        return redirect(url_for('kookboek_bp.manage_ingredients'))
    return render_template('kookboek/ingredients.html',
                           form_add=form_add_ingredient,
                           form_del=form_del_ingredient,
                           ingredients_list=ingredients,
                           units_list=units,
                           kookboek_site_status=session.get('kookboek_status'))


@kookboek_bp.route('/search')
def search():
    '''Page to look for recipes'''
    status = "Browsing recipe information"
    return render_template('kookboek/ingredients.html',
                           kookboek_site_status=status)
