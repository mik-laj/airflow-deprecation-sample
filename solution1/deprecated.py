import warnings

from solution1.new import *

warnings.warn("solution1.deprecated has moved to solution1.new. Import of "
              "solution.new will become unsupported in version 2",
              DeprecationWarning, 2)
