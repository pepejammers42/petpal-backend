# Comments
## URLS
- `shelters/<int:shelter_id>/comments/all/` ListAPIView
    - GET: See comments for a shelter [IsAuthenticated]
- `shelters/<int:shelter_id>/comments/` CreateAPIView
    - POST: Create a comment for a shelter [IsAuthenticated]


- `accounts/seeker/<int:pk>` RetrieveUpdateDestroyAPIView
    - PUT: update the profile 
    - DELETE: delete the seeker's applications
    - GET: retreive the seeker's profile [IsAuthenticated] (handles if user signed in is a shelter)
- `accounts/shelter/` ListCreateAPIView
    - POST: create a shelter profile [AllowAny]
    - GET: list a view of shelters [AllowAny]
- `accounts/shelter/<int:pk>` RetrieveUpdateDestroyAPIView
    - PUT: update the profile
    - DELETE: delete the shelter's listings + **delete the account as well**
    - GET: show shelter's profile

You do not need to support updating or deleting a comment.
--> no need to create view for a specific comment
