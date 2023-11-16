## URLS
- `accounts/seeker/` ListCreateAPIView
    - POST: create a seeker profile
    - GET: list a view of shelters
- `accounts/seeker/<int:pk>` RetrieveUpdateDestroyAPIView
    - PATCH: update the profile
    - DELETE: delete the seeker's applications
- `accounts/shelter/` ListCreateAPIView
    - POST: create a shelter profile
    - GET: list a view of shelters
- `accounts/shelter/<int:pk>` RetrieveUpdateDestroyAPIView
    - PATCH: update the profile
    - DELETE: delete the shelter's listings 

## Model
- create a new manager that replaces the User.
- update the auth model using new custom base user
-
