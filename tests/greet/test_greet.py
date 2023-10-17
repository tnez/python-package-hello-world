from python_package_hello_world.greet import greet

def test_greet():
    assert greet() == "Hello You!"
    assert greet("World") == "Hello World!"
    assert greet(name="World") == "Hello World!"
    assert greet(shout=False) == "Hello You"
    assert greet("World", shout=False) == "Hello World"