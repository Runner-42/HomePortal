'''
Implmentation of the kookboek routes
'''
from flask import Blueprint
from flask import render_template, session, redirect, url_for, request, make_response
from sqlalchemy import exc

from home_portal.kookboek.database import Unit, Category, Ingredient, Recipe
from home_portal.extensions import db_kookboek as db
from home_portal.kookboek.kookboek_forms import CategoryForm, UnitForm, IngredientForm, RecipeForm

# Blueprint Configuration
kookboek_bp = Blueprint('kookboek_bp', __name__,
                        template_folder='templates',
                        static_folder='static')


@kookboek_bp.route('/')
def kookboek():
    '''homepage'''
    status = "Under construction"
    return render_template('kookboek/view.html',
                           kookboek_site_status=status)

# --- Manage Units routes ---
@kookboek_bp.route('/manage_units', methods=['GET'])
def manage_units():
    '''Units Management Page'''
    units = Unit.query.order_by('name').all()
    session['kookboek_status'] = str("Under construction")
    form_manage_unit = UnitForm()
    return render_template('kookboek/manage_units.html',
                           form=form_manage_unit,
                           units_list=units,
                           kookboek_site_status=session.get(
                               'kookboek_status'))


@kookboek_bp.route('/manage_units', methods=['POST'])
def manage_units_update():
    '''Units Management Page'''
    units = Unit.query.order_by('name').all()
    session['kookboek_status'] = str("Under construction")
    form_manage_unit = UnitForm()
    if form_manage_unit.validate_on_submit():
        unit_name = request.form.get('name')
        unit_description = request.form.get('description')
        existing_unit = Unit.query.filter_by(name=unit_name).first()
        if existing_unit:
            unit = Unit.query.get_or_404(existing_unit.id)
            try:
                unit.name = unit_name
                unit.description = unit_description
                db.session.commit()
            except exc.SQLAlchemyError as err:
                db.session.rollback()
                session['kookboek_status'] = str(
                    "-ERROR- Kan {} niet in DB bewaren ({})!".format(unit.name,
                                                                     str(err.args)))
                return render_template('kookboek/manage_categories.html',
                                       form=form_manage_unit,
                                       units_list=units,
                                       kookboek_site_status=session.get(
                                           'kookboek_status'))
        else:
            unit_record = Unit(name=form_manage_unit.name.data,
                               description=form_manage_unit.description.data)
            try:
                db.session.add(unit_record)
                db.session.commit()
            except exc.SQLAlchemyError as err:
                db.session.rollback()
                session['kookboek_status'] = str(
                    "-ERROR- Kan {} niet in DB bewaren ({})!".format(unit_record.name,
                                                                     str(err.args)))
                return render_template('kookboek/manage_units.html',
                                       form=form_manage_unit,
                                       categories_list=units,
                                       kookboek_site_status=session.get(
                                           'kookboek_status'))
        return redirect(url_for('kookboek_bp.manage_units'))
    return render_template('kookboek/manage_units.html',
                           form=form_manage_unit,
                           units_list=units,
                           kookboek_site_status=session.get(
                               'kookboek_status'))


@kookboek_bp.route('/manage_units/delete_unit/<int:unit_id>')
def delete_unit(unit_id):
    unit = Unit.query.get_or_404(unit_id)
    db.session.delete(unit)
    db.session.commit()

    return redirect(url_for('kookboek_bp.manage_units'))


@kookboek_bp.route('/manage_units/edit_unit/<int:unit_id>')
def edit_unit(unit_id):
    units = Unit.query.order_by('name').all()
    unit = Unit.query.get_or_404(unit_id)
    session['kookboek_status'] = str("Under construction")
    form_manage_unit = UnitForm(unit)

    return render_template('kookboek/manage_units.html',
                           form=form_manage_unit,
                           units_list=units,
                           kookboek_site_status=session.get(
                               'kookboek_status'))

# --- Manage Categories routes ---
@kookboek_bp.route('/manage_categories', methods=['GET'])
def manage_categories():
    '''Categories Management Page'''
    categories = Category.query.order_by('name').all()
    session['kookboek_status'] = str("Under construction")
    form_manage_category = CategoryForm()
    return render_template('kookboek/manage_categories.html',
                           form=form_manage_category,
                           categories_list=categories,
                           kookboek_site_status=session.get(
                               'kookboek_status'))


@kookboek_bp.route('/manage_categories', methods=['POST'])
def manage_categories_update():
    '''Categories Management Page'''
    categories = Category.query.order_by('name').all()
    session['kookboek_status'] = str("Under construction")
    form_manage_category = CategoryForm()
    if form_manage_category.validate_on_submit():
        category_name = request.form.get('name')
        category_description = request.form.get('description')
        existing_category = Category.query.filter_by(
            name=category_name).first()
        if existing_category:
            category = Category.query.get_or_404(existing_category.id)
            try:
                category.name = category_name
                category.description = category_description
                db.session.commit()
            except exc.SQLAlchemyError as err:
                db.session.rollback()
                session['kookboek_status'] = str(
                    "-ERROR- Kan {} niet in DB bewaren ({})!".format(category.name,
                                                                     str(err.args)))
                return render_template('kookboek/manage_categories.html',
                                       form=form_manage_category,
                                       categories_list=categories,
                                       kookboek_site_status=session.get(
                                           'kookboek_status'))
        else:
            category_record = Category(name=form_manage_category.name.data,
                                       description=form_manage_category.description.data)
            try:
                db.session.add(category_record)
                db.session.commit()
            except exc.SQLAlchemyError as err:
                db.session.rollback()
                session['kookboek_status'] = str(
                    "-ERROR- Kan {} niet in DB bewaren ({})!".format(category_record.name,
                                                                     str(err.args)))
                return render_template('kookboek/manage_categories.html',
                                       form=form_manage_category,
                                       categories_list=categories,
                                       kookboek_site_status=session.get(
                                           'kookboek_status'))
        return redirect(url_for('kookboek_bp.manage_categories'))
    return render_template('kookboek/manage_categories.html',
                           form=form_manage_category,
                           categories_list=categories,
                           kookboek_site_status=session.get(
                               'kookboek_status'))


@kookboek_bp.route('/manage_categories/delete_category/<int:category_id>')
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()

    return redirect(url_for('kookboek_bp.manage_categories'))


@kookboek_bp.route('/manage_categories/edit_category/<int:category_id>')
def edit_category(category_id):
    categories = Category.query.order_by('name').all()
    category = Category.query.get_or_404(category_id)
    session['kookboek_status'] = str("Under construction")
    form_manage_category = CategoryForm(category)

    return render_template('kookboek/manage_categories.html',
                           form=form_manage_category,
                           categories_list=categories,
                           kookboek_site_status=session.get(
                               'kookboek_status'))

# --- Manage Ingredients routes ---
@kookboek_bp.route('/manage_ingredients', methods=['GET'])
def manage_ingredients():
    '''Ingredients Management Page'''
    ingredients = Ingredient.query.order_by('name').all()
    session['kookboek_status'] = str("Under construction")
    form_manage_ingredient = IngredientForm()
    return render_template('kookboek/manage_ingredients.html',
                           form=form_manage_ingredient,
                           ingredients_list=ingredients,
                           kookboek_site_status=session.get(
                               'kookboek_status'))


@kookboek_bp.route('/manage_ingredients', methods=['POST'])
def manage_ingredients_update():
    '''Ingredients Management Page'''
    ingredients = Ingredient.query.order_by('name').all()
    session['kookboek_status'] = str("Under construction")
    form_manage_ingredient = IngredientForm()
    if form_manage_ingredient.validate_on_submit():
        ingredient_name = request.form.get('name')
        ingredient_amount = request.form.get('default_amount')
        ingredient_unit = Unit.query.filter_by(
            id=request.form.get('default_unit')).first().name
        ingredient_unit_description = Unit.query.filter_by(
            id=request.form.get('default_unit')).first().description
        if form_manage_ingredient.picture_file_picker.data is not None:
            image_data = form_manage_ingredient.picture_file_picker.data.read()
        else:
            image_data = None
        existing_ingredient = Ingredient.query.filter_by(
            name=ingredient_name).first()
        if existing_ingredient:
            ingredient = Ingredient.query.get_or_404(existing_ingredient.id)
            try:
                ingredient.name = ingredient_name
                ingredient.default_amount = ingredient_amount
                ingredient.default_unit = ingredient_unit
                ingredient.unit_description = ingredient_unit_description
                if image_data:
                    ingredient.picture = image_data
                db.session.commit()
            except exc.SQLAlchemyError as err:
                db.session.rollback()
                session['kookboek_status'] = str(
                    "-ERROR- Kan (bestaande) {} niet in DB bewaren ({})!".format(ingredient.name,
                                                                                 str(err.args)))
                return render_template('kookboek/manage_ingredients.html',
                                       form=form_manage_ingredient,
                                       ingredients_list=ingredients,
                                       kookboek_site_status=session.get(
                                           'kookboek_status'))
        else:
            ingredient_record = Ingredient(name=ingredient_name,
                                           default_amount=ingredient_amount,
                                           default_unit=ingredient_unit,
                                           unit_description=ingredient_unit_description,
                                           picture=image_data)
            try:
                db.session.add(ingredient_record)
                db.session.commit()
            except exc.SQLAlchemyError as err:
                db.session.rollback()
                session['kookboek_status'] = str(
                    "ERROR- Kan (nieuwe) {} niet in DB bewaren ({})!".format(ingredient_record.name,
                                                                             str(err.args)))
                return render_template('kookboek/manage_ingredients.html',
                                       form=form_manage_ingredient,
                                       ingredients_list=ingredients,
                                       kookboek_site_status=session.get(
                                           'kookboek_status'))
        return redirect(url_for('kookboek_bp.manage_ingredients'))
    return render_template('kookboek/manage_ingredients.html',
                           form=form_manage_ingredient,
                           ingredients_list=ingredients,
                           kookboek_site_status=session.get(
                               'kookboek_status'))


@kookboek_bp.route('/manage_ingredients/delete_ingredient/<int:ingredient_id>')
def delete_ingredient(ingredient_id):
    ingredient = Ingredient.query.get_or_404(ingredient_id)
    db.session.delete(ingredient)
    db.session.commit()

    return redirect(url_for('kookboek_bp.manage_ingredients'))


@kookboek_bp.route('/manage_ingredients/edit_ingredient/<int:ingredient_id>')
def edit_ingredient(ingredient_id):
    ingredients = Ingredient.query.order_by('name').all()
    ingredient = Ingredient.query.get_or_404(ingredient_id)
    session['kookboek_status'] = str("Under construction")
    form_manage_ingredient = IngredientForm(ingredient)

    return render_template('kookboek/manage_ingredients.html',
                           form=form_manage_ingredient,
                           ingredients_list=ingredients,
                           kookboek_site_status=session.get(
                               'kookboek_status'))


@kookboek_bp.route('/manage_ingredients/ingredient_picture/<int:ingredient_id>')
def get_ingredient_picture(ingredient_id):
    '''
    Function returns the image of an ingredient, based on the record id,
    stored in the database
    '''
    image = Ingredient.query.filter_by(id=ingredient_id).first()
    if image is not None:
        if image.picture is not None:
            response = make_response(image.picture)
            response.headers.set('Content-Type', 'image/jpeg')
        else:
            response = make_response("-")
            response.headers.set('Content-Type', 'text/plain')
    return response

# --- Manage Recipes routes ---
@kookboek_bp.route('/manage_recipes', methods=['GET'])
def manage_recipes():
    '''Recipes Management Page'''
    recipes = Recipe.query.order_by('name').all()
    session['kookboek_status'] = str("Under construction")
    form_manage_recipe = RecipeForm()
    return render_template('kookboek/manage_recipes.html',
                           form=form_manage_recipe,
                           recipes_list=recipes,
                           kookboek_site_status=session.get(
                               'kookboek_status'))


@kookboek_bp.route('/manage_recipes', methods=['POST'])
def manage_recipes_update():
    '''Recipes Management Page'''
    recipes = Recipe.query.order_by('name').all()
    session['kookboek_status'] = str("Under construction")
    form_manage_recipe = RecipeForm()
    if form_manage_recipe.validate_on_submit():
        recipe_id = request.form.get('id')
        print('<<<<<<<<<<<<<<<<< recipe id: {}'.format(recipe_id))
        recipe_name = request.form.get('name')
        recipe_category = Category.query.filter_by(
            id=request.form.get('category')).first().name
        recipe_preparation = request.form.get('preparation')
        if form_manage_recipe.picture_file_picker.data is not None:
            image_data = form_manage_recipe.picture_file_picker.data.read()
        else:
            image_data = None
        existing_recipe = Recipe.query.filter_by(
            name=recipe_name).first()
        if existing_recipe:
            recipe = Recipe.query.get_or_404(existing_recipe.id)
            try:
                recipe.name = recipe_name
                recipe.category = recipe_category
                recipe.preparation = recipe_preparation
                if image_data:
                    recipe.picture = image_data
                db.session.commit()
            except exc.SQLAlchemyError as err:
                db.session.rollback()
                session['kookboek_status'] = str(
                    "-ERROR- Kan (bestaande) {} niet in DB bewaren ({})!".format(recipe.name,
                                                                                 str(err.args)))
                return render_template('kookboek/manage_recipes.html',
                                       form=form_manage_recipe,
                                       recipes_list=recipes,
                                       kookboek_site_status=session.get(
                                           'kookboek_status'))
        else:
            recipe_record = Recipe(name=recipe_name,
                                   category=recipe_category,
                                   preparation=recipe_preparation,
                                   picture=image_data)
            try:
                db.session.add(recipe_record)
                db.session.commit()
            except exc.SQLAlchemyError as err:
                db.session.rollback()
                session['kookboek_status'] = str(
                    "-ERROR- Kan (nieuwe) {} niet in DB bewaren ({})!".format(recipe_record.name,
                                                                              str(err.args)))
                return render_template('kookboek/manage_recipes.html',
                                       form=form_manage_recipe,
                                       recipes_list=recipes,
                                       kookboek_site_status=session.get(
                                           'kookboek_status'))
        return redirect(url_for('kookboek_bp.manage_recipes'))
    return render_template('kookboek/manage_recipes.html',
                           form=form_manage_recipe,
                           recipes_list=recipes,
                           kookboek_site_status=session.get(
                               'kookboek_status'))


@kookboek_bp.route('/manage_recipes/recipe_picture/<int:recipe_id>')
def get_recipe_picture(recipe_id):
    '''
    Function returns the image of a recipe, based on the record id,
    stored in the database
    '''
    image = Recipe.query.filter_by(id=recipe_id).first()
    if image is not None:
        if image.picture is not None:
            response = make_response(image.picture)
            response.headers.set('Content-Type', 'image/jpeg')
        else:
            response = make_response("-")
            response.headers.set('Content-Type', 'text/plain')
    return response


@kookboek_bp.route('/manage_recipes/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()

    return redirect(url_for('kookboek_bp.manage_recipes'))


@kookboek_bp.route('/manage_recipes/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    recipes = Recipe.query.order_by('name').all()
    recipe = Recipe.query.get_or_404(recipe_id)
    session['kookboek_status'] = str("Under construction")
    form_manage_recipe = RecipeForm(recipe)

    return render_template('kookboek/manage_recipes.html',
                           form=form_manage_recipe,
                           recipes_list=recipes,
                           kookboek_site_status=session.get(
                               'kookboek_status'))
