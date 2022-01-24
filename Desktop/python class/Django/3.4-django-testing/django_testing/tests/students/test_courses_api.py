import pytest
from rest_framework.reverse import reverse
from students.models import Course



@pytest.mark.django_db
def test_course(client_api, course_factory):
    # arrange
    course_factory(_quantity=1)
    course = Course.objects.first()
    url = reverse("courses-detail", args=(course.id, ))
    # act
    response = client_api.get(url)
    # assert
    assert response.status_code == 200
    assert response.data["id"] == course.id
    assert response.data["name"] == course.name

@pytest.mark.django_db
def test_get_courses_list(client_api, course_factory):
    # arrange
    url = reverse("courses-list")
    course_factory(_quantity=5)
    # act
    response = client_api.get(url)
    # assert
    assert response.status_code == 200
    assert len(response.data)



@pytest.mark.django_db
def test_get_courses_filters_id(client_api, course_factory):
    # arrange
    course_factory(_quantity=5)
    course = Course.objects.first()
    url = reverse("courses-list")+f'?id={course.id}'
    # act
    response = client_api.get(url)
    # assert
    assert response.status_code == 200
    for item in response.data:
        assert item["id"] == course.id

@pytest.mark.django_db
def test_get_courses_filters_name(client_api, course_factory):
    # arrange
    course_factory(_quantity=5)
    course = Course.objects.first()
    url = reverse("courses-list")+f'?name={course.name}'
    # act
    response = client_api.get(url)
    # assert
    assert response.status_code == 200
    for item in response.data:
        assert item["name"] == course.name


@pytest.mark.django_db
def test_courses_creator(client_api):
    # arrange
    url = reverse("courses-list")
    new_data = {
        "name": "Data science",
        "students": []
    }
    # act
    response = client_api.post(url, new_data)
    # assert
    assert response.status_code == 200
    assert response.data["name"] == new_data["name"]


@pytest.mark.django_db
def test_courses_updates(client_api, course_factory):
    # arrange
    course_factory(_quantity=1)
    course = Course.objects.first()
    url = reverse("courses-detail", args=(course.id, ))
    updated_data = {
        "name": "Python",
    }
    # act
    response = client_api.patch(url, updated_data)
    # assert
    assert response.status_code == 200
    assert response.data["name"] == updated_data["name"]


@pytest.mark.django_db
def test_courses_delete(client_api, course_factory):
    # arrange
    course_factory(_quantity=5)
    course = Course.objects.first()
    url = reverse("courses-detail", args=(course.id, ))
    # act
    response = client_api.delete(url)
    # assert
    assert response.status_code == 204
    assert response.data is None