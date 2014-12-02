from .base import FunctionalTest
from .home_and_list_pages import HomePage, ListPage

from django.contrib.auth import BACKEND_SESSION_KEY, SESSION_KEY, get_user_model
User = get_user_model()
from django.contrib.sessions.backends.db import SessionStore


class MyListsTests(FunctionalTest):

    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        # Edith is a logged-in user
        self.create_pre_authenticated_session('edith@example.com')

        # She goes to the home page and starts a list
        list_page = HomePage(self).start_new_list('Reticulate splines')
        ListPage(self).add_new_item('Immanetize eschaton')
        first_list_url = self.browser.current_url

        # She notices a "My Lists" link, for the first time
        HomePage(self).go_to_my_lists_page()

        # She sees that her list is in there
        self.browser.find_element_by_link_text('Reticulate splines').click()

        # It is named according to its first list item
        list_page.wait_for_new_item_in_list('Reticulate splines', 1)
        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, first_list_url)
        )

        # She decides to start another list, just to see
        HomePage(self).start_new_list('Click cows')
        second_list_url = self.browser.current_url

        # Under "my lists", her new list appears
        self.browser.find_element_by_link_text('My lists').click()
        self.browser.find_element_by_link_text('Click cows').click()
        self.assertEqual(self.browser.current_url, second_list_url)

        # She logs out. The "My Lists" option disappears
        HomePage(self).logout()
