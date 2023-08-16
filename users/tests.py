from django.test import TestCase
from users.models import User


class UserTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="t3mir1an",
            first_name="Temirlan",
            password="Very$tr0ng",
            telegram_id="123456789"
        )

    def test_user_create(self):
        self.assertEqual(self.user.username, "t3mir1an")
        self.assertEqual(self.user.first_name, "Temirlan")
        self.assertTrue(self.user.check_password("Very$tr0ng"))
        self.assertEqual(self.user.telegram_id, "123456789")
        self.assertTrue(self.user.is_active)

    def test_user_representation(self):
        self.assertEqual(str(self.user), "t3mir1an")
