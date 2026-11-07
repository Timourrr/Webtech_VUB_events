from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "account_type"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "minlength": "3",
            "pattern": r"[\w.@+-]+",
            "title": "Letters, digits and @ . + - _ only",
        })
        self.fields["email"].widget.attrs.update({"placeholder": "name@vub.be"})
        self.fields["password1"].widget.attrs.update({"minlength": "8"})