"""
Custom CORS Middleware for Mobile App
Add this to your Django settings to allow cross-origin requests from the mobile app.
"""

class CORSMiddleware:
    """
    Simple CORS middleware to allow the mobile app to communicate with the API.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
        # List of allowed origins for the mobile app
        self.allowed_origins = [
            'http://localhost:3000',
            'http://127.0.0.1:3000',
            'http://localhost:8001',       # Mobile app dev server
            'http://127.0.0.1:8001',
            'http://192.168.1.36:8001',
            'http://192.168.1.37:8001',
            'http://192.168.1.36:3000',    # Local Network Access
            'http://192.168.1.36:3001',    # Access from Phone Web Browser
            'http://localhost',            # Capacitor Android
            'capacitor://localhost',       # Capacitor iOS
            'http://192.168.1.36',         # Direct IP
            'http://192.168.1.37',         # Direct IP
        ]
    
    def __call__(self, request):
        # Handle preflight OPTIONS requests
        if request.method == 'OPTIONS':
            response = self._create_preflight_response(request)
            return response
        
        # Process the request normally
        response = self.get_response(request)
        
        # Add CORS headers to the response
        origin = request.META.get('HTTP_ORIGIN', '')
        if origin in self.allowed_origins or self._is_cors_allowed(request):
            response['Access-Control-Allow-Origin'] = origin or '*'
            response['Access-Control-Allow-Credentials'] = 'true'
            response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
            response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Requested-With, Accept'
        
        return response
    
    def _create_preflight_response(self, request):
        """Create a response for preflight OPTIONS requests."""
        from django.http import HttpResponse
        
        response = HttpResponse()
        origin = request.META.get('HTTP_ORIGIN', '')
        
        if origin in self.allowed_origins or self._is_cors_allowed(request):
            response['Access-Control-Allow-Origin'] = origin or '*'
            response['Access-Control-Allow-Credentials'] = 'true'
            response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
            response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Requested-With, Accept'
            response['Access-Control-Max-Age'] = '86400'  # 24 hours
        
        response.status_code = 200
        return response
    
    def _is_cors_allowed(self, request):
        """Check if this is a request to the mobile API or media endpoints."""
        path = request.path
        return path.startswith('/api/mobile/') or path.startswith('/media/')

