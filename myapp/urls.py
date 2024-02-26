from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, PasswordChange, Mypasswordrestform, Mysetpasswordform

urlpatterns = [
    path('home/',views.home,name='homepage'),
    path('product-detail/<int:pk>',views.ProductView.as_view(),name='product-detail'),
    path('mobiles/',views.Mobile,name='mobile'),
    path('mobiles/<slug:data>',views.Mobile,name='mobiledata'),
    path('registration/',views.CustomerRegistration.as_view(),name='customerregistration'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='myapp/login.html',authentication_form=LoginForm),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('profile/',views.Profileview.as_view(),name='profile'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='myapp/changepassword.html',form_class=PasswordChange,success_url='/changepassworddone/'),name='changepassword'),
    path('changepassworddone/',auth_views.PasswordChangeDoneView.as_view(template_name='myapp/passwordchangedone.html'),name='changepassworddone'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='myapp/password_reset.html',form_class=Mypasswordrestform),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='myapp/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='myapp/password_reset_confirm.html',form_class=Mysetpasswordform),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='myapp/password_reset_complete.html'),name='password_reset_complete'),
    path('address/',views.Address,name='addresspage'),
    path('addtocart/',views.addtocart,name='cartpage'),
    path('cart/',views.ShowCart,name='carts'),
    path('pluscart/',views.pluscart),
    path('minuscart/',views.minuscart),
    path('removecart/',views.removecart),
    path('checkout/',views.checkout,name='checkout'),
    path('paymentdone/',views.payment,name='paymentdone'),
  
  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


