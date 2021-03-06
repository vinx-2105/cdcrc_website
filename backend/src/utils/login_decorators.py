from django.contrib.auth.decorators import login_required, user_passes_test
user_login_required = user_passes_test(lambda user: hasattr(user, 'team_profile'), login_url='/')
# user_student_profile_completed = user_passes_test(lambda user: user.student_profile_completed)

def team_user_required(view_func):
    decorated_view_func = login_required(user_login_required(view_func))
    return decorated_view_func