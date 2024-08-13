from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserProfileForm

@login_required
def my_account(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            
            # Handle password change
            current_password = form.cleaned_data.get('current_password')
            new_password = form.cleaned_data.get('new_password')
            if current_password and new_password:
                if user.check_password(current_password):
                    user.set_password(new_password)
                    messages.success(request, 'Your password was successfully updated!')
                else:
                    messages.error(request, 'Current password is incorrect.')
                    return render(request, 'my_account.html', {'form': form})

            user.save()
            update_session_auth_hash(request, user)  # Important to keep user logged in
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('my_account')
    else:
        form = UserProfileForm(instance=request.user)
    
    return render(request, 'my_account.html', {'form': form})