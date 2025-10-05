import requests
from requests.exceptions import HTTPError
from time import perf_counter
from functools import wraps


# Function Timer
def time_this(func):
    """
    This decorator times the execution
    of the wrapped function and
    returns the elapsed time!
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        func(*args, **kwargs)
        end = perf_counter()
        elapsed_time = end - start
        print(f"(Request finished in: {elapsed_time:.4f} seconds.)\n\n")
        return func(*args, **kwargs)
    return wrapper


class NASAClient:

    def __init__(self, api_key: str = "DEMO_KEY"):
        """
        This is where you enter your NASA API key
        for handling requests made to the NASA API. If
        you do not have an API key, you can generate
        your own by clicking this link: https://api.nasa.gov/#signUp.

        Having your own NASA API key will increase the limit
        of requests to 1000 requests per hour!

        :param api_key: Your NASA API key.
            This defaults to the DEMO_KEY.
            (DEMO_KEY is limited to 30 requests per hour!)
        """

        self._api_key = api_key
        self._session = requests.Session()

        # APOD, NeoWs, and DONKI Base Url
        self._base_nasa_url = "https://api.nasa.gov"

    # Astronomy Picture of the Day API ( APOD )
    @time_this
    def apod(self,
             date: str | None = None,
             start_date: str | None = None,
             end_date: str | None = None,
             count: int | None = None,
             thumbs: bool | None = None) -> dict:
        """
        Retrieve the NASA Astronomy Picture of the Day (APOD)
        within a specific time frame and/or count!

        Date Format: YYYY-MM-DD

        :param date: The date of the APOD image to retrieve.
            This defaults to the current date.

        :param start_date: The start of a date range,
            when requesting for a range of dates.
            Cannot be used with date.
            This defaults to None.

        :param end_date: The end of a date range,
            when used with start_date.
            This defaults to the current date.

        :param count: If this is specified, the chosen
            number of random images will be returned.
            Cannot be used with date or start_date and end_date.
            This defaults to None.

        :param thumbs: Return the URL of a video thumbnail.
            If an APOD is not a video, this parameter is ignored.
            This defaults to False.
        """

        url = f"{self._base_nasa_url}/planetary/apod"
        params = {"api_key": self._api_key}

        if date:
            params["date"] = date
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date
        if count:
            params["count"] = str(count)
        if thumbs:
            params["thumbs"] = str(thumbs)

        try:
            response = self._session.get(url, params=params)
            response.raise_for_status()
        except HTTPError as e:
            print(
                "HTTP error occurred:"
                f"\n\n{e}"
            )
            return {}

        return response.json()

    # Near Earth Object Web Service ( NeoWs )
    @time_this
    def neows_feed(self,
                 start_date: str | None = None,
                 end_date: str | None = None) -> dict:
        """
        Retrieve a list of Asteroids based on their closest approach date to Earth!

        Date Format: YYYY-MM-DD

        :param start_date: Starting date for the asteroid search.
            This defaults to None.

        :param end_date: Ending date for the asteroid search.
            This defaults to 7 days after start_date.
        """

        url = f"{self._base_nasa_url}/neo/rest/v1/feed"
        params = {"api_key": self._api_key}

        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date

        try:
            response = self._session.get(url, params=params)
            response.raise_for_status()
        except HTTPError as e:
            print(
                "HTTP error occurred:"
                f"\n\n{e}"
            )
            return {}

        return response.json()

    @time_this
    def neows_lookup(self,
                     asteroid_id: int) -> dict:
        """
        Lookup a specific asteroid based on its NASA JPL small body (SPK-ID) ID!

        :param asteroid_id: Asteroid SPK-ID correlates to the NASA JPL small body.
            This defaults to None.
        """

        url = f"{self._base_nasa_url}/neo/rest/v1/neo/{asteroid_id}"
        params = {"api_key": self._api_key}

        try:
            response = self._session.get(url, params=params)
            response.raise_for_status()
        except HTTPError as e:
            print(
                "HTTP error occurred:"
                f"\n\n{e}"
            )
            return {}

        return response.json()

    @time_this
    def neows_browse(self) -> dict:
        """
        Browse the overall Asteroid data-set!
        """

        url = f"{self._base_nasa_url}/neo/rest/v1/neo/browse"
        params = {"api_key": self._api_key}

        try:
            response = self._session.get(url, params=params)
            response.raise_for_status()
        except HTTPError as e:
            print(
                "HTTP error occurred:"
                f"\n\n{e}"
            )
            return {}

        return response.json()

    # Space Weather Database Of Notifications, Knowledge, Information ( DONKI )
    @time_this
    def donki_cme(self,
                  start_date: str | None = None,
                  end_date: str | None = None) -> dict:
        """
        Retrieves basic DONKI Coronal Mass Injection analyses (CMEs)
        within a specific time frame!

        Date Format: YYYY-MM-DD

        :param start_date: The starting date for the CME search.
            This defaults to 30 days prior to the current UTC date.

        :param end_date: The ending date for the CME search.
            This defaults to the current UTC date.
        """

        url = f"{self._base_nasa_url}/DONKI/CME"
        params = {"api_key": self._api_key}

        if start_date:
            params["startDate"] = start_date
        if end_date:
            params["endDate"] = end_date

        try:
            response = self._session.get(url, params=params)
            response.raise_for_status()
        except HTTPError as e:
            print(
                "HTTP error occurred:"
                f"\n\n{e}"
            )
            return {}

        return response.json()

    @time_this
    def donki_cme_analysis(self,
                           start_date: str | None = None,
                           end_date: str | None = None,
                           most_accurate_only: bool = True,
                           complete_entry_only: bool = True,
                           speed: int = 0,
                           half_angle: int = 0,
                           catalog: str | None = None,
                           keyword: str | None = None) -> dict:
        """
        Retrieves more robust analyses from DONKI Coronal Mass Injections (CMEs)
        within a specific time frame, accuracy, catalog, and/or keyword!

        Date Format: YYYY-MM-DD

        :param start_date: The starting date for the CME search.
            This defaults to 30 days prior to the current UTC date.

        :param end_date: The ending date for the CME search.
            This defaults to the current UTC date.

        :param most_accurate_only: Whether or not to only return the CME analysis
            marked as "best fit" for each CME entry.
            This defaults to True.

        :param complete_entry_only: Whether or not to only return CME analyses
            with all required fields being filled.
            This defaults to True.

        :param speed: (Lower Limit) Will only return CME analyses greater than,
            or equal to the chosen speed (Measured in km/s).
            This defaults to 0 (No Filtering).

        :param half_angle: (Lower Limit) Filter the angular half-width of the returned CME's.
            This defaults to 0 (No Filtering).

        :param catalog: The catalog from which to retrieve CME analyses.
            This defaults to ALL catalogs.
            (Choices: SWRC_CATALOG, JANG_ET_AL_CATALOG)

        :param keyword: Filter CME results by specific subsets with a keyword.
            This defaults to None.
        """

        url = f"{self._base_nasa_url}/DONKI/CMEAnalysis"
        params = {"api_key": self._api_key}

        if start_date:
            params["startDate"] = start_date
        if end_date:
            params["endDate"] = end_date
        if most_accurate_only:
            params["most_accurate_only"] = str(most_accurate_only)
        if complete_entry_only:
            params["complete_entry_only"] = str(complete_entry_only)
        if speed:
            params["speed"] = str(speed)
        if half_angle:
            params["half_angle"] = str(half_angle)
        if catalog:
            params["catalog"] = catalog
        if keyword:
            params["keyword"] = keyword

        try:
            response = self._session.get(url, params=params)
            response.raise_for_status()
        except HTTPError as e:
            print(
                "HTTP error occurred:"
                f"\n\n{e}"
            )
            return {}

        return response.json()

    @time_this
    def donki_gst(self,
                  start_date: str | None = None,
                  end_date: str | None = None) -> dict:
        """
        Retrieves DONKI Geomagnetic Storm analyses (GSTs)
        within a specific time frame!

        Date Format: YYYY-MM-DD

        :param start_date: The starting date for the GST search.
            This defaults to 30 days prior to the current UTC date.

        :param end_date: The ending date for the GST search.
            This defaults to the current UTC date.
        """

        url = f"{self._base_nasa_url}/DONKI/GST"
        params = {"api_key": self._api_key}

        if start_date:
            params["startDate"] = start_date
        if end_date:
            params["endDate"] = end_date

        try:
            response = self._session.get(url, params=params)
            response.raise_for_status()
        except HTTPError as e:
            print(
                "HTTP error occurred:"
                f"\n\n{e}"
            )
            return {}

        return response.json()

    @time_this
    def donki_ips(self,
                  start_date: str | None = None,
                  end_date: str | None = None,
                  location: str | None = None,
                  catalog: str | None = None) -> dict:
        """
        Retrieves DONKI Interplanetary Shock analyses (IPSs)
        within a specific time frame, location, and/or catalog!

        Date Format: YYYY-MM-DD

        :param start_date: The starting date for the IPS search.
            This defaults to 30 days prior to the current UTC date.

        :param end_date: The ending date for the IPS search.
            This defaults to the current UTC date.

        :param location: The location from which to retrieve IPS analyses.
            This defaults to ALL locations.
            (Options: Earth, MESSENGER, STEREO A, STEREO B)

        :param catalog: The catalog from which to retrieve IPS analyses.
            This defaults to ALL catalogs.
            (Options: SWRC_CATALOG, WINSLOW_MESSENGER_ICME_CATALOG)
        """

        url = f"{self._base_nasa_url}/DONKI/IPS"
        params = {"api_key": self._api_key}

        if start_date:
            params["startDate"] = start_date
        if end_date:
            params["endDate"] = end_date
        if location:
            params["location"] = location
        if catalog:
            params["catalog"] = catalog

        try:
            response = self._session.get(url, params=params)
            response.raise_for_status()
        except HTTPError as e:
            print(
                "HTTP error occurred:"
                f"\n\n{e}"
            )
            return {}

        return response.json()

    @time_this
    def donki_flr(self,
                  start_date: str | None = None,
                  end_date: str | None = None) -> dict:
        """
        Retrieves DONKI Solar Flare analyses (FLRs)
        within a specific time frame!

        Date Format: YYYY-MM-DD

        :param start_date: The starting date for the FLR search.
            This defaults to 30 days prior to the current UTC date.

        :param end_date: The ending date for the FLR search.
            This defaults to the current UTC date.
        """

        url = f"{self._base_nasa_url}/DONKI/FLR"
        params = {"api_key": self._api_key}

        if start_date:
            params["startDate"] = start_date
        if end_date:
            params["endDate"] = end_date

        try:
            response = self._session.get(url, params=params)
            response.raise_for_status()
        except HTTPError as e:
            print(
                "HTTP error occurred:"
                f"\n\n{e}"
            )
            return {}

        return response.json()

    @time_this
    def donki_sep(self,
                  start_date: str | None = None,
                  end_date: str | None = None) -> dict:
        """
        Retrieves DONKI Solar Energetic Particle analyses (SEP)
        within a specific time frame!

        Date Format: YYYY-MM-DD

        :param start_date: The starting date for the SEP search.
            This defaults to 30 days prior to the current UTC date.

        :param end_date: The ending date for the SEP search.
            This defaults to the current UTC date.
        """

        url = f"{self._base_nasa_url}/DONKI/SEP"
        params = {"api_key": self._api_key}

        if start_date:
            params["startDate"] = start_date
        if end_date:
            params["endDate"] = end_date

        try:
            response = self._session.get(url, params=params)
            response.raise_for_status()
        except HTTPError as e:
            print(
                "HTTP error occurred:"
                f"\n\n{e}"
            )
            return {}

        return response.json()

    @time_this
    def donki_mpc(self,
                  start_date: str | None = None,
                  end_date: str | None = None) -> dict:
        """
        Retrieves DONKI Magnetopause Crossing analyses (MPC)
        within a specific time frame!

        Date Format: YYYY-MM-DD

        :param start_date: The starting date for the MPC search.
            This defaults to 30 days prior to the current UTC date.

        :param end_date: The ending date for the MPC search.
            This defaults to the current UTC date.
        """

        url = f"{self._base_nasa_url}/DONKI/MPC"
        params = {"api_key": self._api_key}

        if start_date:
            params["startDate"] = start_date
        if end_date:
            params["endDate"] = end_date

        try:
            response = self._session.get(url, params=params)
            response.raise_for_status()
        except HTTPError as e:
            print(
                "HTTP error occurred:"
                f"\n\n{e}"
            )
            return {}

        return response.json()

    @time_this
    def donki_rbe(self,
                  start_date: str | None = None,
                  end_date: str | None = None) -> dict:
        """
        Retrieves DONKI Radiation Belt Enhancement analyses (RBE)
        within a specific time frame!

        Date Format: YYYY-MM-DD

        :param start_date: The starting date for the RBE search.
            This defaults to 30 days prior to the current UTC date.

        :param end_date: The ending date for the RBE search.
            This defaults to the current UTC date.
        """

        url = f"{self._base_nasa_url}/DONKI/RBE"
        params = {"api_key": self._api_key}

        if start_date:
            params["startDate"] = start_date
        if end_date:
            params["endDate"] = end_date

        try:
            response = self._session.get(url, params=params)
            response.raise_for_status()
        except HTTPError as e:
            print(
                "HTTP error occurred:"
                f"\n\n{e}"
            )
            return {}

        return response.json()

    @time_this
    def donki_hss(self,
                  start_date: str | None = None,
                  end_date: str | None = None) -> dict:
        """
        Retrieves DONKI Hight Speed Stream analyses (HSS)
        within a specific time frame!

        Date Format: YYYY-MM-DD

        :param start_date: The starting date for the HSS search.
            This defaults to 30 days prior to the current UTC date.

        :param end_date: The ending date for the HSS search.
            This defaults to the current UTC date.
        """

        url = f"{self._base_nasa_url}/DONKI/HSS"
        params = {"api_key": self._api_key}

        if start_date:
            params["startDate"] = start_date
        if end_date:
            params["endDate"] = end_date

        try:
            response = self._session.get(url, params=params)
            response.raise_for_status()
        except HTTPError as e:
            print(
                "HTTP error occurred:"
                f"\n\n{e}"
            )
            return {}

        return response.json()

    @time_this
    def donki_wsa_es(self,
                     start_date: str | None = None,
                     end_date: str | None = None) -> dict:
        """
        Retrieves DONKI WSA+EnlilSimulation analyses
        within a specific time frame!

        Date Format: YYYY-MM-DD

        :param start_date: The starting date for the WSA+EnlilSimulation search.
            This defaults to 7 days prior to the current UTC date.

        :param end_date: The ending date for the WSA+EnlilSimulation search.
            This defaults to the current UTC date.
        """

        url = f"{self._base_nasa_url}/DONKI/WSAEnlilSimulations"
        params = {"api_key": self._api_key}

        if start_date:
            params["startDate"] = start_date
        if end_date:
            params["endDate"] = end_date

        try:
            response = self._session.get(url, params=params)
            response.raise_for_status()
        except HTTPError as e:
            print(
                "HTTP error occurred:"
                f"\n\n{e}"
            )
            return {}

        return response.json()

    @time_this
    def donki_notifications(self,
                            start_date: str | None = None,
                            end_date: str | None = None,
                            notification_type: str | None = None) -> dict:
        """
        Retrieve DONKI Notifications within a specific time frame
        and/or a notification type!

        Date Format: YYYY-MM-DD

        :param start_date: The starting date for the DONKI Notifications search.
            This defaults to 7 days prior to the current UTC date.

        :param end_date: The ending date for the DONKI Notifications search.
            This defaults to the current UTC date.

        :param notification_type: The notification type to retrieve.
            This defaults to ALL notification types.
            (Options: FLR, SEP, CME, IPS, MPC, GST, RBE, report)
        """

        url = f"{self._base_nasa_url}/DONKI/notifications"
        params = {"api_key": self._api_key}

        if start_date:
            params["startDate"] = start_date
        if end_date:
            params["endDate"] = end_date
        if notification_type:
            params["type"] = notification_type

        try:
            response = self._session.get(url, params=params)
            response.raise_for_status()
        except HTTPError as e:
            print(
                "HTTP error occurred:"
                f"\n\n{e}"
            )
            return {}

        return response.json()
