# | PySpaceAPI Wrapper! 🚀

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
(out of MANY) planned endpoints
from NASA APIs!

## | Currently Supported Endpoints:

*These explanations are sourced from
the [**official NASA APIs page**](https://api.nasa.gov)*

- [**Astronomy Picture of the Day**](https://apod.nasa.gov/apod/astropix.html) (APOD)

  - This endpoint structures the APOD
imagery and associated metadata so
that it can be repurposed
for other applications. The full
documentation for this API can
be found in the [**APOD
API GitHub repository**](https://github.com/nasa/apod-api)


- [**Near Earth Object Web Service**](https://cneos.jpl.nasa.gov) (Asteroids NeoWs)

  - Neo - Feed
    - Retrieve a list of Asteroids based on their closest approach date to Earth.

  - Neo - Lookup
    - Look up a specific Asteroid based on its [**NASA JPL small body (SPK-ID) ID**](http://ssd.jpl.nasa.gov/sbdb_query.cgi)

  - Neo - Browse
    - Browse the overall Asteroid data-set


- [**Space Weather Database Of Notifications, Knowledge, Information**](https://ccmc.gsfc.nasa.gov/tools/DONKI) (DONKI)

*Unfortunately, there is not much
documentation provided for these endpoints
on the API's page (That
I could find), so I've
opted here instead for simple
explanations rather than risking misleading
information.*

  - Coronal Mass Ejection (CME)
    - Retrieves basic DONKI Coronal Mass Injection analyses (CMEs)
    within a specific time frame!


  - Coronal Mass Ejection Analysis
    - Retrieves more robust analyses from DONKI Coronal Mass Injections (CMEs)
    within a specific time frame, accuracy, catalog, and/or keyword!
  

  - Geomagnetic Storm (GST)
    - Retrieves DONKI Geomagnetic Storm analyses (GSTs)
    within a specific time frame!


  - Interplanetary Shock (IPS)
    - Retrieves DONKI Interplanetary Shock analyses (IPSs)
    within a specific time frame, location, and/or catalog!


  - Solar Flare (FLR)
    - Retrieves DONKI Solar Flare analyses (FLRs)
    within a specific time frame!


  - Solar Energetic Particle (SEP)
    - Retrieves DONKI Solar Energetic Particle analyses (SEP)
    within a specific time frame!


  - Magnetopause Crossing (MCP)
    - Retrieves DONKI Magnetopause Crossing analyses (MPC)
    within a specific time frame!


  - Radiation Belt Enhancement (RBE)
    - Retrieves DONKI Radiation Belt Enhancement analyses (RBE)
    within a specific time frame!


  - Hight Speed Stream (HSS)
    - Retrieves DONKI Hight Speed Stream analyses (HSS)
    within a specific time frame!


  - WSA+EnlilSimulation
    - Retrieves DONKI WSA+EnlilSimulation analyses
    within a specific time frame!


  - Notifications
    - Retrieve DONKI Notifications within a specific time frame
    and/or a notification type!


## | Installing The Package:

> [!NOTE]
> As of now, this project
> is NOT on PyPI, but
> it will be very soon
> once the necessary implementations are
> made! Until then, I plan
> to make releases available which
> include the tar.gz and .whl
> files for direct installation! (will
> probably continue to do this
> alongside PyPI updates.)
> 
> ### the FUTURE PIP install method:
> **(Not yet implemented)**
> 
> ```
> shell
> 
> pip install pyspaceapi
> ```
> 
> There is only ONE dependency,
> which is the 'requests' library.
> Dependencies can be viewed on
> Line #8, inside [**'pyproject.toml'**](pyproject.toml).

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
NASA API key or ignore
this step if you plan
on only using the Demo
Key. This is done like
so:

```
python

from pyspaceapi import NASAClient


# Replace 'DEMO_KEY' if you plan to use your own NASA API key!
client = NASAClient("DEMO_KEY")
```

After this, you are ready
to make requests to the
NASA endpoints!

### Example API Request:

*This program will search the
Near Earth Object Web Service
API for the specified asteroid
ID!*

```
python

from pyspaceapi import NASAClient


# Replace 'DEMO_KEY' if you plan to use your own NASA API key!
client = NASAClient("DEMO_KEY")

# Look up a specific asteroid in the NeoWs API by Neo Reference ID
data = client.neows_lookup(2001620)
print(data)
```

The program will then return
and print a raw python
dict including all retrieved data
from the searched asteroid (if
it exists).

<details>
    <summary>Returned Data Example</summary>
    
    python
    
    {
      'links': {
        'self': 'http://api.nasa.gov/neo/rest/v1/neo/2001620?api_key=bUCCZgLQLDEzgb9rG41xAidN6wWtgU8Vbl6ezne7'
      },
      'id': '2001620',
      'neo_reference_id': '2001620',
      'name': '1620 Geographos (1951 RA)',
      'name_limited': 'Geographos',
      'designation': '1620',
      'nasa_jpl_url': 'https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=2001620',
      'absolute_magnitude_h': 15.27,
      'estimated_diameter': {
        'kilometers': {
          'estimated_diameter_min': 2.3472263753,
          'estimated_diameter_max': 5.2485577338
        },
        'meters': {
          'estimated_diameter_min': 2347.2263753125,
          'estimated_diameter_max': 5248.5577337793
        },
        'miles': {
          'estimated_diameter_min': 1.4584984001,
          'estimated_diameter_max': 3.2613015676
        },
        'feet': {
          'estimated_diameter_min': 7700.8741811804,
          'estimated_diameter_max': 17219.6781552924
        }
      },
      'is_potentially_hazardous_asteroid': True,
      'close_approach_data': [
        {
          'close_approach_date': '1901-08-23',
          'close_approach_date_full': '1901-Aug-23 17:36',
          'epoch_date_close_approach': -2157171840000,
          'relative_velocity': {
            'kilometers_per_second': '11.762811574',
            'kilometers_per_hour': '42346.1216664688',
            'miles_per_hour': '26312.2332099233'
          },
          'miss_distance': {
            'astronomical': '0.0338992189',
            'lunar': '13.1867961521',
            'kilometers': '5071250.942103743',
            'miles': '3151129.2156199334'
          },
          'orbiting_body': 'Earth'
        },
        {
          'close_approach_date': '1915-03-14',
          'close_approach_date_full': '1915-Mar-14 16:15',
          'epoch_date_close_approach': -1729410300000,
          'relative_velocity': {
            'kilometers_per_second': '12.1053300941',
            'kilometers_per_hour': '43579.1883388493',
            'miles_per_hour': '27078.4128875478'
          },
          'miss_distance': {
            'astronomical': '0.0815995175',
            'lunar': '31.7422123075',
            'kilometers': '12207114.011027725',
            'miles': '7585148.918423605'
          },
          'orbiting_body': 'Earth'
        },
        {
          'close_approach_date': '1926-08-21',
          'close_approach_date_full': '1926-Aug-21 06:24',
          'epoch_date_close_approach': -1368466560000,
          'relative_velocity': {
            'kilometers_per_second': '10.5595593618',
            'kilometers_per_hour': '38014.4137023443',
            'miles_per_hour': '23620.6783363261'
          },
          'miss_distance': {
            'astronomical': '0.0664845066',
            'lunar': '25.8624730674',
            'kilometers': '9945940.575360942',
            'miles': '6180120.8975153196'
          },
          'orbiting_body': 'Earth'
        },
        {
          'close_approach_date': '1940-03-09',
          'close_approach_date_full': '1940-Mar-09 21:19',
          'epoch_date_close_approach': -940819260000,
          'relative_velocity': {
            'kilometers_per_second': '14.9940526483',
            'kilometers_per_hour': '53978.589534033',
            'miles_per_hour': '33540.1963690773'
          },
          'miss_distance': {
            'astronomical': '0.1470295848',
            'lunar': '57.1945084872',
            'kilometers': '21995312.713064376',
            'miles': '13667253.5609293488'
          },
          'orbiting_body': 'Earth'
        },
        {
          'close_approach_date': '1944-09-02',
          'close_approach_date_full': '1944-Sep-02 03:37',
          'epoch_date_close_approach': -799359780000,
          'relative_velocity': {
            'kilometers_per_second': '16.7374295012',
            'kilometers_per_hour': '60254.74620437',
            'miles_per_hour': '37439.9560512654'
          },
          'miss_distance': {
            'astronomical': '0.1916377262',
            'lunar': '74.5470754918',
            'kilometers': '28668595.651163194',
            'miles': '17813839.2989283172'
          },
          'orbiting_body': 'Earth'
        },
        {
          'close_approach_date': '1951-08-08',
          'close_approach_date_full': '1951-Aug-08 15:38',
          'epoch_date_close_approach': -580638120000,
          'relative_velocity': {
            'kilometers_per_second': '7.9958930214',
            'kilometers_per_hour': '28785.2148771606',
            'miles_per_hour': '17886.0130996446'
          },
          'miss_distance': {
            'astronomical': '0.1936526722',
            'lunar': '75.3308894858',
            'kilometers': '28970027.280928214',
            'miles': '18001140.2284047932'
          },
          'orbiting_body': 'Earth'
        },
        {
          'close_approach_date': '1958-03-18',
          'close_approach_date_full': '1958-Mar-18 04:43',
          'epoch_date_close_approach': -372107820000,
          'relative_velocity': {
            'kilometers_per_second': '9.0553681818',
            'kilometers_per_hour': '32599.3254546517',
            'miles_per_hour': '20255.9530859751'
          },
          'miss_distance': {
            'astronomical': '0.1515042066',
            'lunar': '58.9351363674',
            'kilometers': '22664706.603399942',
            'miles': '14083195.6368935196'
          },
          'orbiting_body': 'Earth'
        },
        {
          'close_approach_date': '1969-08-27',
          'close_approach_date_full': '1969-Aug-27 00:06',
          'epoch_date_close_approach': -10972440000,
          'relative_velocity': {
            'kilometers_per_second': '13.1765371139',
            'kilometers_per_hour': '47435.5336099763',
            'miles_per_hour': '29474.5958700433'
          },
          'miss_distance': {
            'astronomical': '0.0606033673',
            'lunar': '23.5747098797',
            'kilometers': '9066134.662907651',
            'miles': '5633434.8536855438'
          },
          'orbiting_body': 'Earth'
        },
        {
          'close_approach_date': '1983-03-16',
          'close_approach_date_full': '1983-Mar-16 10:22',
          'epoch_date_close_approach': 416658120000,
          'relative_velocity': {
            'kilometers_per_second': '11.0596560539',
            'kilometers_per_hour': '39814.7617939748',
            'miles_per_hour': '24739.3446269284'
          },
          'miss_distance': {
            'astronomical': '0.0894588499',
            'lunar': '34.7994926111',
            'kilometers': '13382853.397689713',
            'miles': '8315719.4962875194'
          },
          'orbiting_body': 'Earth'
        },
        {
          'close_approach_date': '1994-08-25',
          'close_approach_date_full': '1994-Aug-25 10:10',
          'epoch_date_close_approach': 777809400000,
          'relative_velocity': {
            'kilometers_per_second': '12.2172333975',
            'kilometers_per_hour': '43982.04023082',
            'miles_per_hour': '27328.7293867559'
          },
          'miss_distance': {
            'astronomical': '0.0333047312',
            'lunar': '12.9555404368',
            'kilometers': '4982316.848442544',
            'miles': '3095868.1323093472'
          },
          'orbiting_body': 'Earth'
        },
        {
          'close_approach_date': '2008-03-17',
          'close_approach_date_full': '2008-Mar-17 11:41',
          'epoch_date_close_approach': 1205754060000,
          'relative_velocity': {
            'kilometers_per_second': '9.7438577021',
            'kilometers_per_hour': '35077.8877274941',
            'miles_per_hour': '21796.0352937865'
          },
          'miss_distance': {
            'astronomical': '0.1251027026',
            'lunar': '48.6649513114',
            'kilometers': '18715097.840203462',
            'miles': '11629022.5529612956'
          },
          'orbiting_body': 'Earth'
        },
        {
          'close_approach_date': '2019-08-31',
          'close_approach_date_full': '2019-Aug-31 17:20',
          'epoch_date_close_approach': 1567272000000,
          'relative_velocity': {
            'kilometers_per_second': '15.2835382762',
            'kilometers_per_hour': '55020.7377944381',
            'miles_per_hour': '34187.7467701052'
          },
          'miss_distance': {
            'astronomical': '0.1372576208',
            'lunar': '53.3932144912',
            'kilometers': '20533447.712947696',
            'miles': '12758892.7711063648'
          },
          'orbiting_body': 'Earth'
        },
        {
          'close_approach_date': '2026-08-12',
          'close_approach_date_full': '2026-Aug-12 08:35',
          'epoch_date_close_approach': 1786523700000,
          'relative_velocity': {
            'kilometers_per_second': '8.3615352663',
            'kilometers_per_hour': '30101.5269585147',
            'miles_per_hour': '18703.9182370838'
          },
          'miss_distance': {
            'astronomical': '0.1704372833',
            'lunar': '66.3001032037',
            'kilometers': '25497054.550266571',
            'miles': '15843135.0416018398'
          },
          'orbiting_body': 'Earth'
        },
        {
          'close_approach_date': '2040-03-12',
          'close_approach_date_full': '2040-Mar-12 10:58',
          'epoch_date_close_approach': 2215162680000,
          'relative_velocity': {
            'kilometers_per_second': '13.7430092955',
            'kilometers_per_hour': '49474.833463854',
            'miles_per_hour': '30741.7374931375'
          },
          'miss_distance': {
            'astronomical': '0.1136386637',
            'lunar': '44.2054401793',
            'kilometers': '17000102.039166319',
            'miles': '10563373.5769964422'
          },
          'orbiting_body': 'Earth'
        },
        {
          'close_approach_date': '2051-08-23',
          'close_approach_date_full': '2051-Aug-23 03:35',
          'epoch_date_close_approach': 2576374500000,
          'relative_velocity': {
            'kilometers_per_second': '11.0130375865',
            'kilometers_per_hour': '39646.9353113928',
            'miles_per_hour': '24635.0637772374'
          },
          'miss_distance': {
            'astronomical': '0.0478817187',
            'lunar': '18.6259885743',
            'kilometers': '7163003.129459169',
            'miles': '4450883.7544237722'
          },
          'orbiting_body': 'Earth'
        },
        {
          'close_approach_date': '2065-03-13',
          'close_approach_date_full': '2065-Mar-13 19:56',
          'epoch_date_close_approach': 3004199760000,
          'relative_velocity': {
            'kilometers_per_second': '12.9517022623',
            'kilometers_per_hour': '46626.128144312',
            'miles_per_hour': '28971.6627905588'
          },
          'miss_distance': {
            'astronomical': '0.0965980624',
            'lunar': '37.5766462736',
            'kilometers': '14450864.381167088',
            'miles': '8979350.7484302944'
          },
          'orbiting_body': 'Earth'
        },
        {
          'close_approach_date': '2076-08-20',
          'close_approach_date_full': '2076-Aug-20 09:35',
          'epoch_date_close_approach': 3365141700000,
          'relative_velocity': {
            'kilometers_per_second': '10.224834626',
            'kilometers_per_hour': '36809.4046536767',
            'miles_per_hour': '22871.932574947'
          },
          'miss_distance': {
            'astronomical': '0.0783701758',
            'lunar': '30.4859983862',
            'kilometers': '11724011.371205546',
            'miles': '7284962.8578506948'
          },
          'orbiting_body': 'Earth'
        },
        {
          'close_approach_date': '2090-03-11',
          'close_approach_date_full': '2090-Mar-11 06:39',
          'epoch_date_close_approach': 3792897540000,
          'relative_velocity': {
            'kilometers_per_second': '15.0059357939',
            'kilometers_per_hour': '54021.3688579219',
            'miles_per_hour': '33566.7777773015'
          },
          'miss_distance': {
            'astronomical': '0.1508073049',
            'lunar': '58.6640416061',
            'kilometers': '22560451.593480563',
            'miles': '14018414.5776672494'
          },
          'orbiting_body': 'Earth'
        },
        {
          'close_approach_date': '2094-09-03',
          'close_approach_date_full': '2094-Sep-03 10:34',
          'epoch_date_close_approach': 3934348440000,
          'relative_velocity': {
            'kilometers_per_second': '16.6942589136',
            'kilometers_per_hour': '60099.3320890993',
            'miles_per_hour': '37343.3877639184'
          },
          'miss_distance': {
            'astronomical': '0.1900233738',
            'lunar': '73.9190924082',
            'kilometers': '28427091.970693806',
            'miles': '17663775.8704182828'
          },
          'orbiting_body': 'Earth'
        },
        {
          'close_approach_date': '2101-08-07',
          'close_approach_date_full': '2101-Aug-07 02:26',
          'epoch_date_close_approach': 4152824760000,
          'relative_velocity': {
            'kilometers_per_second': '8.0119290255',
            'kilometers_per_hour': '28842.9444917094',
            'miles_per_hour': '17921.8840370847'
          },
          'miss_distance': {
            'astronomical': '0.1980370833',
            'lunar': '77.0364254037',
            'kilometers': '29625925.842692571',
            'miles': '18408696.6960406398'
          },
          'orbiting_body': 'Earth'
        },
        {
          'close_approach_date': '2108-03-18',
          'close_approach_date_full': '2108-Mar-18 23:57',
          'epoch_date_close_approach': 4361558220000,
          'relative_velocity': {
            'kilometers_per_second': '9.3905190941',
            'kilometers_per_hour': '33805.8687387005',
            'miles_per_hour': '21005.6521615553'
          },
          'miss_distance': {
            'astronomical': '0.1395653651',
            'lunar': '54.2909270239',
            'kilometers': '20878681.344732337',
            'miles': '12973411.0025547706'
          },
          'orbiting_body': 'Earth'
        },
        {
          'close_approach_date': '2119-08-27',
          'close_approach_date_full': '2119-Aug-27 16:11',
          'epoch_date_close_approach': 4722595860000,
          'relative_velocity': {
            'kilometers_per_second': '12.3889919953',
            'kilometers_per_hour': '44600.3711830228',
            'miles_per_hour': '27712.936194251'
          },
          'miss_distance': {
            'astronomical': '0.0336165498',
            'lunar': '13.0768378722',
            'kilometers': '5028964.246828926',
            'miles': '3124853.4815981388'
          },
          'orbiting_body': 'Earth'
        },
        {
          'close_approach_date': '2133-03-18',
          'close_approach_date_full': '2133-Mar-18 05:51',
          'epoch_date_close_approach': 5150411460000,
          'relative_velocity': {
            'kilometers_per_second': '10.694423251',
            'kilometers_per_hour': '38499.9237036709',
            'miles_per_hour': '23922.355370206'
          },
          'miss_distance': {
            'astronomical': '0.1005941726',
            'lunar': '39.1311331414',
            'kilometers': '15048673.955372362',
            'miles': '9350812.3929361156'
          },
          'orbiting_body': 'Earth'
        },
        {
          'close_approach_date': '2144-08-29',
          'close_approach_date_full': '2144-Aug-29 08:08',
          'epoch_date_close_approach': 5511744480000,
          'relative_velocity': {
            'kilometers_per_second': '13.5183022163',
            'kilometers_per_hour': '48665.8879788366',
            'miles_per_hour': '30239.0902277388'
          },
          'miss_distance': {
            'astronomical': '0.0705258081',
            'lunar': '27.4345393509',
            'kilometers': '10550510.671788747',
            'miles': '6555783.3357368286'
          },
          'orbiting_body': 'Earth'
        },
        {
          'close_approach_date': '2158-03-20',
          'close_approach_date_full': '2158-Mar-20 02:29',
          'epoch_date_close_approach': 5939490540000,
          'relative_velocity': {
            'kilometers_per_second': '8.6455572701',
            'kilometers_per_hour': '31124.006172293',
            'miles_per_hour': '19339.2470574451'
          },
          'miss_distance': {
            'astronomical': '0.1750878023',
            'lunar': '68.1091550947',
            'kilometers': '26192762.287061101',
            'miles': '16275427.7835651538'
          },
          'orbiting_body': 'Earth'
        },
        {
          'close_approach_date': '2165-03-11',
          'close_approach_date_full': '2165-Mar-11 12:24',
          'epoch_date_close_approach': 6159673440000,
          'relative_velocity': {
            'kilometers_per_second': '15.8836924368',
            'kilometers_per_hour': '57181.292772376',
            'miles_per_hour': '35530.2316118133'
          },
          'miss_distance': {
            'astronomical': '0.1803815404',
            'lunar': '70.1684192156',
            'kilometers': '26984694.231158948',
            'miles': '16767511.4754035624'
          },
          'orbiting_body': 'Earth'
        },
        {
          'close_approach_date': '2176-08-20',
          'close_approach_date_full': '2176-Aug-20 12:13',
          'epoch_date_close_approach': 6520824780000,
          'relative_velocity': {
            'kilometers_per_second': '9.872506011',
            'kilometers_per_hour': '35541.0216396586',
            'miles_per_hour': '22083.8086960423'
          },
          'miss_distance': {
            'astronomical': '0.0936338731',
            'lunar': '36.4235766359',
            'kilometers': '14007427.975610297',
            'miles': '8703812.1429122186'
          },
          'orbiting_body': 'Earth'
        },
        {
          'close_approach_date': '2190-03-16',
          'close_approach_date_full': '2190-Mar-16 04:16',
          'epoch_date_close_approach': 6948994560000,
          'relative_velocity': {
            'kilometers_per_second': '12.7193171346',
            'kilometers_per_hour': '45789.5416846126',
            'miles_per_hour': '28451.8404984194'
          },
          'miss_distance': {
            'astronomical': '0.0965581509',
            'lunar': '37.5611207001',
            'kilometers': '14444893.705778583',
            'miles': '8975640.7427791254'
          },
          'orbiting_body': 'Earth'
        }
      ],
      'orbital_data': {
        'orbit_id': '771',
        'orbit_determination_date': '2025-10-06 06:19:28',
        'first_observation_date': '1951-09-14',
        'last_observation_date': '2025-10-05',
        'data_arc_in_days': 27050,
        'observations_used': 8206,
        'orbit_uncertainty': '0',
        'minimum_orbit_intersection': '.029359',
        'jupiter_tisserand_invariant': '5.074',
        'epoch_osculation': '2461000.5',
        'eccentricity': '.3355121972702853',
        'semi_major_axis': '1.245776928209864',
        'inclination': '13.33579272086494',
        'ascending_node_longitude': '337.1407922247628',
        'orbital_period': '507.8773584487923',
        'perihelion_distance': '.827803573717546',
        'perihelion_argument': '277.0183902829851',
        'aphelion_distance': '1.663750282702182',
        'perihelion_time': '2461207.995482869838',
        'mean_anomaly': '212.9204490208176',
        'mean_motion': '.7088325439423928',
        'equinox': 'J2000',
        'orbit_class': {
          'orbit_class_type': 'APO',
          'orbit_class_description': 'Near-Earth asteroid orbits which cross the Earth’s orbit similar to that of 1862 Apollo',
          'orbit_class_range': 'a (semi-major axis) > 1.0 AU; q (perihelion) < 1.017 AU'
        }
      },
      'is_sentry_object': False
    }

</details>



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
repository, and I will try
to implement as soon as
possible! (If it makes sense
to implement in the first
place.)

✅ Pull Requests are also welcome!