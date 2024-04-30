from test.test_lesson_21.conftest import user_api
from core.api_service.users.assertations.user_aserts import UserAsserts
from core.api_service.users.dtos.payload_create_user import CreateUserPayload
import pytest
from threading import Thread


@pytest.mark.api_tests
def test_get_user_is_the_same_as_in_get_all_users():

    response = user_api.get_all_users()

    trds = [ThreadWithReturnValue(target=user_api.get_user, args=[user.id]) for user in response]  # створюєму список тредів List[user_api.get_user(user.id)] # threads
    [t.start() for t in trds]  # запуск тредів
    thread_results = [t.join() for t in trds]  # завершення тредів. join повертає результат виконання функції
    assert any([k for k in thread_results if k.status == 'active']), 'No one user in status active'


class ThreadWithReturnValue(Thread):

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                        **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return  # join повертає результат виконання функції
