# 📡 | PySpaceAPI Wrapper!

PySpaceAPI is a fairly thin
(for now at least) API
wrapper, which aims to provide
some more ease when it
comes to retrieving astronomical data
from available public APIs! The
goal is to add support
for all, if not as
many endpoints as possible that
fall within the scope of
astronomical data. And possibly in
the future add more functionality
to the wrapper to achieve
more than simply retrieving data
and returning it as a
python dict, as well as
adding support for multiple other
non-NASA APIs!

Currently, this wrapper contains **nineteen**
endpoints (out of the many
planned) from NASA, but there
will be more in the
future!

## | Currently Supported Endpoints:

> ### 💡
> 
> *Most explanations and in-depth documentation
> seen here are provided by 
> the [**official NASA APIs page**](https://api.nasa.gov)*.

### [**Astronomy Picture of the Day**](https://apod.nasa.gov/apod/astropix.html) (APOD)

"The full documentation for this
API can be found in
the [**APOD API GitHub
repository**](https://github.com/nasa/apod-api)"

  - [**apod**](https://github.com/Py-Kat/py-space-api/blob/d2e1f2e4bef5e9aef19d35876546a359ee38f0d9/pyspaceapi/nasa.py#L32)
    - "This endpoint structures the APOD
    imagery and associated metadata so
    that it can be repurposed
    for other applications."

### [**Near Earth Object Web Service**](https://cneos.jpl.nasa.gov) (Asteroids NeoWs)

"NeoWs (Near Earth Object Web
Service) is a RESTful web
service for near earth Asteroid
information. With NeoWs a user
can: search for Asteroids based
on their closest approach date
to Earth, lookup a specific
Asteroid with its NASA JPL
small body id, as well
as browse the overall data-set."

  - [**Neo - Feed**](https://github.com/Py-Kat/py-space-api/blob/d2e1f2e4bef5e9aef19d35876546a359ee38f0d9/pyspaceapi/nasa.py#L93)
    - "Retrieve a list of Asteroids based on their closest approach date to Earth."


  - [**Neo - Lookup**](https://github.com/Py-Kat/py-space-api/blob/d2e1f2e4bef5e9aef19d35876546a359ee38f0d9/pyspaceapi/nasa.py#L128)
    - "Look up a specific Asteroid based on its [**NASA JPL small body (SPK-ID) ID**](http://ssd.jpl.nasa.gov/sbdb_query.cgi)"


  - [**Neo - Browse**](https://github.com/Py-Kat/py-space-api/blob/d2e1f2e4bef5e9aef19d35876546a359ee38f0d9/pyspaceapi/nasa.py#L151)
    - "Browse the overall Asteroid data-set"

### [**Space Weather Database Of Notifications, Knowledge, Information**](https://ccmc.gsfc.nasa.gov/tools/DONKI) (DONKI)

"The Space Weather Database Of
Notifications, Knowledge, Information (DONKI) is
a comprehensive on-line tool for
space weather forecasters, scientists, and
the general space science community.
DONKI chronicles the daily interpretations
of space weather observations, analysis,
models, forecasts, and notifications provided
by the Space Weather Research
Center (SWRC), comprehensive knowledge-base search
functionality to support anomaly resolution
and space science research, intelligent
linkages, relationships, cause-and-effects between space
weather activities and comprehensive webservice
API access to information stored
in DONKI."

  - [**Coronal Mass Ejection**](https://github.com/Py-Kat/py-space-api/blob/d2e1f2e4bef5e9aef19d35876546a359ee38f0d9/pyspaceapi/nasa.py#L172) (CME)
    - Retrieves basic DONKI Coronal Mass Injection analyses (CMEs)
    within a specific time frame!


  - [**Coronal Mass Ejection Analysis**](https://github.com/Py-Kat/py-space-api/blob/d2e1f2e4bef5e9aef19d35876546a359ee38f0d9/pyspaceapi/nasa.py#L208)
    - Retrieves more robust analyses from DONKI Coronal Mass Injections (CMEs)
    within a specific time frame, accuracy, catalog, and/or keyword!
  

  - [**Geomagnetic Storm**](https://github.com/Py-Kat/py-space-api/blob/d2e1f2e4bef5e9aef19d35876546a359ee38f0d9/pyspaceapi/nasa.py#L284) (GST)
    - Retrieves DONKI Geomagnetic Storm analyses (GSTs)
    within a specific time frame!


  - [**Interplanetary Shock**](https://github.com/Py-Kat/py-space-api/blob/d2e1f2e4bef5e9aef19d35876546a359ee38f0d9/pyspaceapi/nasa.py#L320) (IPS)
    - Retrieves DONKI Interplanetary Shock analyses (IPSs)
    within a specific time frame, location, and/or catalog!


  - [**Solar Flare**](https://github.com/Py-Kat/py-space-api/blob/d2e1f2e4bef5e9aef19d35876546a359ee38f0d9/pyspaceapi/nasa.py#L370) (FLR)
    - Retrieves DONKI Solar Flare analyses (FLRs)
    within a specific time frame!


  - [**Solar Energetic Particle**](https://github.com/Py-Kat/py-space-api/blob/d2e1f2e4bef5e9aef19d35876546a359ee38f0d9/pyspaceapi/nasa.py#L406) (SEP)
    - Retrieves DONKI Solar Energetic Particle analyses (SEP)
    within a specific time frame!


  - [**Magnetopause Crossing**](https://github.com/Py-Kat/py-space-api/blob/d2e1f2e4bef5e9aef19d35876546a359ee38f0d9/pyspaceapi/nasa.py#L442) (MCP)
    - Retrieves DONKI Magnetopause Crossing analyses (MPC)
    within a specific time frame!


  - [**Radiation Belt Enhancement**](https://github.com/Py-Kat/py-space-api/blob/d2e1f2e4bef5e9aef19d35876546a359ee38f0d9/pyspaceapi/nasa.py#L478) (RBE)
    - Retrieves DONKI Radiation Belt Enhancement analyses (RBE)
    within a specific time frame!


  - [**Hight Speed Stream**](https://github.com/Py-Kat/py-space-api/blob/d2e1f2e4bef5e9aef19d35876546a359ee38f0d9/pyspaceapi/nasa.py#L514) (HSS)
    - Retrieves DONKI Hight Speed Stream analyses (HSS)
    within a specific time frame!


  - [**WSA+EnlilSimulation**](https://github.com/Py-Kat/py-space-api/blob/d2e1f2e4bef5e9aef19d35876546a359ee38f0d9/pyspaceapi/nasa.py#L550)
    - Retrieves DONKI WSA+EnlilSimulation analyses
    within a specific time frame!


  - [**Notifications**](https://github.com/Py-Kat/py-space-api/blob/d2e1f2e4bef5e9aef19d35876546a359ee38f0d9/pyspaceapi/nasa.py#L586)
    - Retrieve DONKI Notifications within a specific time frame
    and/or a notification type!

### [**The Earth Observatory Natural Event Tracker**](https://earthobservatory.nasa.gov) (EONET)

"The Earth Observatory Natural Event
Tracker (EONET) is a prototype
web service with the goal
of:

providing a curated source of
continuously updated natural event metadata;
providing a service that links
those natural events to thematically-related
web service-enabled image sources (e.g., via WMS, WMTS, etc.)."

  - [**Events**](https://github.com/Py-Kat/py-space-api/blob/d2e1f2e4bef5e9aef19d35876546a359ee38f0d9/pyspaceapi/nasa.py#L630)
    - Retrieve Earth Observatory Natural Event Tracker (EONET)
    events with up to eleven optional parameters. Such as: Source,
    category, status, limit, days, time frame, magnitude IDs
    and values, and a bounding box!


  - [**Events GeoJSON**](https://github.com/Py-Kat/py-space-api/blob/d2e1f2e4bef5e9aef19d35876546a359ee38f0d9/pyspaceapi/nasa.py#L737)
    - Retrieve Earth Observatory Natural Event Tracker (EONET)
    GeoJSON events with up to eleven optional parameters. Such as:
    Source, category, status, limit, days, time frame, magnitude IDs
    and values, and a bounding box!


  - [**Categories**](https://github.com/Py-Kat/py-space-api/blob/d2e1f2e4bef5e9aef19d35876546a359ee38f0d9/pyspaceapi/nasa.py#L844)
    - "Categories are the types of events by which individual
    events are cataloged. Categories can be used to filter
    the output of the Categories API and the Layers API.
    The acceptable categories can be accessed via the [**categories JSON**](https://eonet.gsfc.nasa.gov/api/v3/categories)."


  - [**Layers**](https://github.com/Py-Kat/py-space-api/blob/d2e1f2e4bef5e9aef19d35876546a359ee38f0d9/pyspaceapi/nasa.py#L919)
    - "A Layer is a reference to a specific web service
      (e.g., WMS, WMTS) that can be used to produce imagery
      of a particular NASA data parameter. Layers are mapped
      to categories within EONET to provide a category-specific
      list of layers (e.g., the ‘Volcanoes’ category is mapped
      to layers that can provide imagery in true color, SO2,
      aerosols, etc.). Web services come in a variety of flavors,
      so it is not possible to include all of the necessary metadata
      here that is required to construct a properly-formulated request
      (URL). The full list of layers can be accessed via the [**layers JSON**](https://eonet.gsfc.nasa.gov/api/v3/layers)."

## | Installing The Package:

This package can be installed
directly from PyPI, or installed
manually via the .tar.gz or
.whl files!

As well, dependencies can be
viewed on [**Line #8 in
'pyproject.toml'**](pyproject.toml).

The PyPI project can also
be viewed by clicking this
link: https://pypi.org/project/pyspaceapis

> ### ⚠️
> 
> Due to a conflict with
> an apparent non-existent package on
> PyPI, the name used for
> installation is *slightly* different than
> the one used when importing.
> Please be sure to correctly
> install 'pyspaceapis'. The exact commands
> for installation can be copied
> below!

### Default Installation Method:

```
shell

pip install pyspaceapis
```

---

### Manual Installation Methods:

Using the .whl:
```
shell

pip install "PATH\TO\pyspaceapis-0.4.0-py3-none-any.whl"
```

Using the .tar.gz:
```
shell

pip install "PATH\TO\pyspaceapis-0.4.0.tar.gz"
```

*The .tar.gz and .whl files
will be made available as
well alongside each release for
those who prefer a manual
installation!*

## | Using The Package:

As noted above, this wrapper
is very much so in
the early stages and supports
just 19 NASA API endpoints
at the moment. However, I
am working to constantly and
consistently add more!

All methods currently return a
python dict. This will be
changed if it is found
to be a problem, or
an annoyance for users. However,
I have not found a
reason to do so yet.

To access these, input your
NASA API key or leave
the parameter empty to use
the NASA Demo Key.

```
python

from pyspaceapi import NASAClient


# This uses the Demo Key by default
client = NASAClient()
```

After this, you are ready
to make requests to the
NASA endpoints!

### Example API Request:

*This program will search the
NASA Astronomy Picture of the
Day endpoint and return a
python dict containing the data
of a single random APOD
entry!*

```
python

from pyspaceapi import NASAClient


# Replace 'DEMO_KEY' if you plan to use your own NASA API key!
client = NASAClient("DEMO_KEY")

# Get one random APOD entry
data = client.apod(count=1)
print(data)
```

The program will then return
and print a dict containing
the retrieved data!

The output:

```
console

[{'copyright': '\n\nJohannes Schedler\n(Panther Observatory)\n\n', 'date': '2005-06-07', 'explanation': 'Galaxies abound in this cosmic scene, a well chosen telescopic view toward the northern constellation of Ursa Major. Most noticeable are the striking pair of spiral galaxies - NGC 3718 (above, right) and NGC 3729 (below center) - a mere 52 million light-years distant. In particular, NGC 3718 has dramatic dust lanes sweeping through its bright central region and extensive but faint spiral arms. Seen about 150 thousand light-years apart, these two galaxies are likely interacting gravitationally, accounting for the warped and peculiar appearance of NGC 3718. While a careful study of the deep image reveals a number of fainter and more distant background galaxies, another remarkable galaxy grouping known as Hickson Group 56 can be found just to the right of NGC 3718. Hickson Group 56 contains five interacting galaxies and lies over 400 million light-years away.', 'hdurl': 'https://apod.nasa.gov/apod/image/0506/ngc3718etc_schedler_full.jpg', 'media_type': 'image', 'service_version': 'v1', 'title': 'Galaxies in View', 'url': 'https://apod.nasa.gov/apod/image/0506/ngc3718etc_schedler_c38.jpg'}]
```

---

### Timeout Handling:

If a request times out
after the initial 10 second
timeout window, the wrapper will
retry two times by default,
once for fifteen seconds, and
then lastly, for thirty seconds.
This behavior can be overridden
in multiple ways to hopefully
fit any use case! This
can be done via the
'default_retry_delays' base class parameter, and
via the 'retry_delays' parameter within
each class method!

#### Default Retry Delays:

Specifying 'default_retry_delays' will **NOT** override
the behavior of the separate
'retry_delays' parameter within each class
method. This allows for configuration
of the global default delays
AND specific class methods at
once with expected behavior!

```
python

from pyspaceapi import NASAClient


client = NASAClient(default_retry_delays=[5, 10, 15])
```

This, for example, will make
the wrapper attempt to request
three times. Once for five
seconds, again for 10 seconds,
and then lastly, for fifteen
seconds.

#### Retry Delays (Class Method Specific):

Specifying the 'retry_delays' parameter **WILL**
override the behavior of the
global 'default_retry_delays' base class parameter.
This means that you can
have multiple different requests with
timeout delays differing from each
other AND differing from the
default timeout delays.

Example using multiple different delays:

```
python

from pyspaceapi import NASAClient


client = NASAClient(default_retry_delays=[10, 20, 30]) # Specifies the default retry delays


eonet_data = client.eonet_events() # Will use the default retry delays since 'retry_delays' is unspecified
apod_data = client.apod(retry_delays=[5, 10, 15]) # Will use 5, 10, and then 15 seconds
neows_data = client.neows_browse(retry_delays=[2, 5, 7.5]) # Will use 2, 5, and then 7.5 seconds
```

#### Timeout Prints:

Along with this, I have
also included a 'timeout_prints' base
class parameter, which when set
to True, will enable some
debug timeout prints. This is
set to false by default.

```
python

from pyspaceapi import NASAClient


client = NASAClient(timeout_print=True)
```

These will look something like
so:

```
console

(Request timed out after 10 seconds. Retrying for 15 seconds.)

(Request timed out after 15 seconds. Retrying for 30 seconds.)
```

---

### Debug Tools:

Along with the endpoint methods,
I have included another separate
module named: '[**debugtools**](https://github.com/Py-Kat/py-space-api/blob/1e1725859abd83743531d76eb4d592371f675054/pyspaceapi/debugtools.py)' which contains
just one tool for now,
being the '[**time_this**](https://github.com/Py-Kat/py-space-api/blob/1e1725859abd83743531d76eb4d592371f675054/pyspaceapi/debugtools.py#L5)' decorator!

Usage would appear something
like this:

```
python

from pyspaceapi.debugtools import time_this
from time import sleep


@time_this
def do_something():
    sleep(1.7)
    print("Did something!")


do_something()
```

The output:

```
console

Did something!


(Finished in: 1.7000 seconds.)
```

# | Final Notes:

Since this package/wrapper is still
very early, please expect there
to possibly be some bugs
or other weirdness! If anything
of the like is noticed
in which you'd like fixed,
or you have any suggestions,
please be sure to make
a submission in the GitHub
repository, and I will attempt
to make implementations as soon
as possible!

✅ Pull Requests are also welcome!
