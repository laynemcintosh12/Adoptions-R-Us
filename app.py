from flask import Flask, render_template, redirect, request, flash
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.debug = True
app.config['SECRET_KEY'] = 'SEcreTT'
toolbar = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_RECORD_QUERIES'] = True

connect_db(app)


@app.route('/')
def get_homepage():
    """Get the homepage with a list of all pets"""
    pets = Pet.query.all()
    return render_template('homepage.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Add a New Pet"""
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        pic = form.pic.data
        age = form.age.data
        notes = form.notes.data
        
        new_pet = Pet(name=name,
                      species=species,
                      pic=pic,
                      age=age,
                      notes=notes,
                      avb=True)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added.")
        return redirect("/")
    else:
        return render_template('pet_form.html', form=form)
    

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.avb = form.avb.data
        pet.pic = form.pic.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect('/')
    else:
        return render_template("pet_edit_form.html", form=form, pet=pet)