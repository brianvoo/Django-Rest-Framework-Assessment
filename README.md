# Horizons 45 Backend Test

A Django REST API server that exposes a list of drivers and trucks built using Python 3.10, pipenv, Django REST Framework and Postgresql.

## Libraries Used
- **Python 3.10:** Used as it was the last version I had installed in mid 2022.
- **pipenv:** Managing Python dependencies and virtual environments, much easier to use than venv as it auto generates the Pipfile and Pipfile.lock for other users who clone to quickly get the project up and running.
- **Django REST Framework:** Toolkit to build web API, easy to output web api views.
- **Postresql:** Easy to implement with Django.

## Potential improvements
- User authentication to protect API endpoints from add/update/delete.
- Pagination for driver/truck list.
### Dependant on usecase: 
- Additional query filters where required, eg, if a single driver has access to multiple trucks. 
- Additional fields for if trucks are shared, eg, showing when truck_id = 1 being used and its next available date. 
- City, district and language could implement choice based on userbase to reduce user input errors.
- Included date added for both models for filtering (filter not implemented, but best case would be to filter year and/or month to get accurate data).
- Combine driver/id to also show driver's assigned truck/id details in 1 page for better information flow. 

## Production considerations
*Unsure what to write here*

## Assumptions
### Schema design
- 1 truck could be shared with multiple drivers
- Possible for drivers not to have an assigned_truck, also in the event a truck is deleted, driver's assigned_truck is set to a default "Not assigned".
- Validation for input such as mobile_number and truck.number_plate and truck.registration_number so database is cleaner. 

### Views
As the user could create drivers, it made sense that the same user can create trucks. Dependant on use case, auth for access of trucks could be provided. 
- Provided additional views
  - domain/driver/id/update -> Update/delete single driver
  - domain/truck/ -> Show list of trucks
  - domain/truck/create -> Create single truck
  - domain/truck/id/ -> Show single truck
  - domain/truck/id/update -> Update/delete single truck
