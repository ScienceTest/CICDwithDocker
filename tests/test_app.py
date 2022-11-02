import sys
sys.path.append('./')

from src import app 

def test_index():
    assert app.index()=="this the second deploy"
