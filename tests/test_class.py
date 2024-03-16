import requests
import pytest
import json

class TestApi:
	base_url = "https://reqres.in";
	users = "/api/users";
	unknown = "/api/unknown";
	register = "/api/register";
	login = "/api/login";
	valid = 2;
	invalid = 23;
	delayed = 3;

	def test_get_list_users(self):
		response = requests.get(self.base_url + self.users, params = {"page" : 2});
		response_json = json.loads(response.text);
		assert response.status_code == 200;
		assert response_json["total"] == 12;

	def test_get_single_user(self):
		response = requests.get(self.base_url + self.users + "/" + str(self.valid));
		assert response.status_code == 200;

	def test_get_single_user_fail(self):
		response = requests.get(self.base_url + self.users + "/" + str(self.invalid));
		assert response.status_code == 404;

	def test_get_list_resource(self):
		response = requests.get(self.base_url + self.unknown);
		assert response.status_code == 200;

	def test_get_list_resource_fail(self):
		response = requests.get(self.base_url + self.unknown + "/" + str(self.invalid));
		assert response.status_code == 404;

	def test_post_create_user(self):
		payload = { 'name' : 'morpheus', 'job' : 'leader'};
		response = requests.post(self.base_url + self.users, json = payload);
		assert response.status_code == 201;

	def test_put_update_user(self):
		payload = { 'name' : 'morpheus', 'job' : 'zion resident'};
		response = requests.put(self.base_url + self.users + "/" + str(self.valid), data = payload);
		assert response.status_code == 200;

	def test_patch_update_user(self):
		payload = { 'name' : 'morpheus', 'job' : 'zion resident'};
		response = requests.patch(self.base_url + self.users + "/" + str(self.valid), data = payload);
		assert response.status_code == 200;

	def test_delete_user(self):
		response = requests.delete(self.base_url + self.users + "/" + str(self.valid));
		assert response.status_code == 204;

	def test_post_register(self):
		payload = { 'email' : 'eve.holt@reqres.in', 'password' : 'pistol' };
		response = requests.post(self.base_url + self.register, json = payload);
		assert response.status_code == 200;

	def test_post_register_fail(self):
		payload = { 'email' : 'sydney@fife' };
		response = requests.post(self.base_url + self.register, json = payload);
		assert response.status_code == 400;

	def test_post_login(self):
		payload = { 'email' : 'eve.holt@reqres.in', 'password' : 'cityslicka' };
		response = requests.post(self.base_url + self.login, json = payload);
		assert response.status_code == 200;

	def test_post_login_fail(self):
		payload = { 'email' : 'peter@klaven' };
		response = requests.post(self.base_url + self.login);
		assert response.status_code == 400;

	def test_get_list_users_delayed(self):
		response = requests.get(self.base_url + self.users, params = {"page" : 3});
		assert response.status_code == 200;