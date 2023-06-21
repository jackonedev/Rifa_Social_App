import pytest
from app_demo.schemas import premios
from .database import client, session

def test_get_all_posts(client):
    res = client.get("/v1/premios/")

    def validate(premio):
        return premios.Premio(**premio)
    posts_map = map(validate, res.json())
    posts_list = list(posts_map)
    assert res.status_code == 200



def test_get_one_premio_not_exist(client):
    res = client.get(f"/v1/premios/88888")
    assert res.status_code == 404


@pytest.mark.parametrize("nombre, precio", [
    ("Auto", 40000),
    ("Picada x4", 3000),
    ("Chopp", 5000),
])
def test_create_premio(client, session, nombre, precio):
    res = client.post(
        "/v1/premios/", json={"nombre": nombre, "precio": precio})
    created_premio = premios.Premio(**res.json())
    assert res.status_code == 201
    assert created_premio.nombre == nombre
    assert created_premio.precio == precio


def test_get_one_premio(client, session):
    # premio = premios.PremioCreate(nombre="Picada", precio=3000)
    # session.add(premio)
    # session.commit()


    res = client.get(f"/v1/premios/1")
    assert res.status_code == 200
    retrieved_premio = premios.Premio(**res.json())
    assert retrieved_premio.id == 1
    assert retrieved_premio.nombre == 'Auto'
    assert retrieved_premio.precio == 40000






# @pytest.mark.parametrize("title, content, published", [
#     ("awesome new title", "awesome new content", True),
#     ("favorite pizza", "i love pepperoni", False),
#     ("tallest skyscrapers", "wahoo", True),
# ])
# def test_create_post(authorized_client, test_user, test_posts, title, content, published):
#     res = authorized_client.post(
#         "/posts/", json={"title": title, "content": content, "published": published})

#     created_post = schemas.Post(**res.json())
#     assert res.status_code == 201
#     assert created_post.title == title
#     assert created_post.content == content
#     assert created_post.published == published
#     assert created_post.owner_id == test_user['id']


# def test_create_post_default_published_true(authorized_client, test_user, test_posts):
#     res = authorized_client.post(
#         "/posts/", json={"title": "arbitrary title", "content": "aasdfjasdf"})

#     created_post = schemas.Post(**res.json())
#     assert res.status_code == 201
#     assert created_post.title == "arbitrary title"
#     assert created_post.content == "aasdfjasdf"
#     assert created_post.published == True
#     assert created_post.owner_id == test_user['id']


# def test_unauthorized_user_create_post(client, test_user, test_posts):
#     res = client.post(
#         "/posts/", json={"title": "arbitrary title", "content": "aasdfjasdf"})
#     assert res.status_code == 401


# def test_unauthorized_user_delete_Post(client, test_user, test_posts):
#     res = client.delete(
#         f"/posts/{test_posts[0].id}")
#     assert res.status_code == 401


# def test_delete_post_success(authorized_client, test_user, test_posts):
#     res = authorized_client.delete(
#         f"/posts/{test_posts[0].id}")

#     assert res.status_code == 204


# def test_delete_post_non_exist(authorized_client, test_user, test_posts):
#     res = authorized_client.delete(
#         f"/posts/8000000")

#     assert res.status_code == 404


# def test_delete_other_user_post(authorized_client, test_user, test_posts):
#     res = authorized_client.delete(
#         f"/posts/{test_posts[3].id}")
#     assert res.status_code == 403


# def test_update_post(authorized_client, test_user, test_posts):
#     data = {
#         "title": "updated title",
#         "content": "updatd content",
#         "id": test_posts[0].id

#     }
#     res = authorized_client.put(f"/posts/{test_posts[0].id}", json=data)
#     updated_post = schemas.Post(**res.json())
#     assert res.status_code == 200
#     assert updated_post.title == data['title']
#     assert updated_post.content == data['content']


# def test_update_other_user_post(authorized_client, test_user, test_user2, test_posts):
#     data = {
#         "title": "updated title",
#         "content": "updatd content",
#         "id": test_posts[3].id

#     }
#     res = authorized_client.put(f"/posts/{test_posts[3].id}", json=data)
#     assert res.status_code == 403


# def test_unauthorized_user_update_post(client, test_user, test_posts):
#     res = client.put(
#         f"/posts/{test_posts[0].id}")
#     assert res.status_code == 401


# def test_update_post_non_exist(authorized_client, test_user, test_posts):
#     data = {
#         "title": "updated title",
#         "content": "updatd content",
#         "id": test_posts[3].id

#     }
#     res = authorized_client.put(
#         f"/posts/8000000", json=data)

#     assert res.status_code == 404
