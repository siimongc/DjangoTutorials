from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from .views import HomePageView, AboutPageView, ContactPageView, ProductShowView, ProductIndexView, ProductCreateView, ProductListView, ProductViewSet, CommentViewSet, CartView, CartRemoveAllView, RegisterView, ImageViewFactory, ImageViewNoDI
from .utils import ImageLocalStorage

router = DefaultRouter()
router.register(r'products', ProductViewSet)  # /api/products/
router.register(r'comments', CommentViewSet)  # /api/comments/

urlpatterns = [
    # Vistas antiguas
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("products/", ProductIndexView.as_view(), name="index"),  # 👈 Vuelve a agregar esta ruta
    path("products/create", ProductCreateView.as_view(), name="form"),
    path("products/<str:id>/", ProductShowView.as_view(), name="show"),
    path('cart/', CartView.as_view(), name='cart_index'),
    path("cart/add/<str:product_id>", CartView.as_view(), name="cart_add"),
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("password_change/", auth_views.PasswordChangeView.as_view(), name="password_change"),
    path("password_change_done/", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    path('register/', RegisterView.as_view(), name='register'),
    path('image/', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_index'), 
    path('image/save', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_save'),
    path('imagenotdi/', ImageViewNoDI.as_view(), name='imagenodi_index'), 
    path('imagenotdi/save', ImageViewNoDI.as_view(), name='imagenodi_save'),



    path('api/', include(router.urls)),  # Incluye las rutas de la API
]