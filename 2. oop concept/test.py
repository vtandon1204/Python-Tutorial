import public_private_class
from public_private_class import NotPrivate

test = NotPrivate('tim')
test.display()
test._display()