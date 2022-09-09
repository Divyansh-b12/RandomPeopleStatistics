# RandomPeopleStatistics

The goal of this test is to create an python API client for the following user api: https://random-data-api.com/api/v2/users. The documentation is https://random-data-api.com/documentation.

Use the API client to call the api 10 times.

Convert the returned responses into instances of a python class. Serialize the objects and store them in a local file. You should be able to serialize and de-serialize the serialization to and from a python class. The python class doesn't need to have all properties from the API but should have most. 

Add an option to your client to use the file as a cache instead of calling the API directly.

Use your client to return statistics on the stored objects. Give the average age of the 10 users (use the date_of_birth property to determine age). Return the top 5 oldest from the cache and the top 5 youngest from the cache.

Please use the `typing` module and provide docstrings for all functions.