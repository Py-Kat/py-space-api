# PySpaceAPI Changelogs!

## 0.1.0 - 2025-10-03

- This was the Initial Commit!

## 0.2.0 - 2025-10-06

- Added support for all NASA
EONET endpoints


- Rephrased some text and fixed
typos in docstrings

## 0.2.1 - 2025-10-07

- Removed an extra second newline
from HTTP Error messages

## 0.3.0 - 2025-10-10

- Removed the `time_this` decorator
from class methods by default


- Moved the `time_this` decorator
into its own importable 'debugtools'
module

## 0.4.0 - 2025-10-11

- Made errors now raise tracebacks
instead of simply printing an
error message with an empty
dict


- Added missing documentation of NASA
EONET endpoints to the README


- Slightly improved the contents of
some docstrings

## 0.5.0 - 2025-10-20

- Changed PyPI/installation name to `pyspaceapis`
due to a non-existent package
apparently already owning it, and
updated the README example accordingly


- Added customizable timeout handling and
refactored error handling method for
easier scalability


- Added the ability to retrieve
HTTP header data as a
dict and added documentation to
the README accordingly


- Updated the type annotation for
the 'api_key' class parameter


- Made the base URLs class
attributes rather than instance
attributes
