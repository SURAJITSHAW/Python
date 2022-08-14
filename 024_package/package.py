# package is a container for related module. In file system package is a directory or folder.
# Every packages must have __init__.py file.
# ecommerce is a example of python package. Now let's import calc_shipping() funct from a shipping module lies inside ecommerce package.

# case 1
from ecommerce import shipping

shipping.calc_shipping()

# case 2
import ecommerce.shipping

ecommerce.shipping.calc_shipping()

# case 3
from ecommerce.shipping import calc_shipping

calc_shipping()