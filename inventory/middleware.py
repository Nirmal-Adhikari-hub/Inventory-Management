# # inventory/middleware.py

# from django.shortcuts import redirect, render


# class InventoryMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # Code to be executed before the view is called
#         if request.path.startswith('/inventory/'):
#             # Perform your desired actions here
#             # For example, you can perform authentication, check permissions, or modify the request
#             if not request.user.is_authenticated:
#                 return render (request, 'inventory/login.html')  # Redirect to the login page if user is not authenticated
#                 # pass
#         response = self.get_response(request)

#         # Code to be executed after the view is called
#         # You can modify the response if needed

#         return response
