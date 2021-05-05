import pytest 
from app import create_app
from app import db 
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app({"TESTING": True})
    print(app.app_context())
    print("heidi")
    
    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_planets(app): 
    venus_planet = Planet(name="Venus",
                    description="Goddess of love and beauty", 
                    founder="Heidi and Manu")
    earth_planet = Planet(name="Earth",
                        description="Mother Earth",
                        founder="Jesus")
    
    db.session.add_all([venus_planet,earth_planet])
    db.session.commit()

@pytest.fixture
def planet_data(app): 
    return {
        "name": "Venus", 
        "description": "Goddess of love and beauty",
        "founder": "Heidi and Manu"
    }
