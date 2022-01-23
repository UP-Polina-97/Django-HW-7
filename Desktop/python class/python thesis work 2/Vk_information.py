import requests
import pprint


token_for_vk = input('Token for infomation in vk: ')
#token_for_vk = ''

def get_info_from_vk(user_id):
    """ get infomration from the vk about person."""
    url_vk = 'https://api.vk.com/method/account.getProfileInfo'
    params = {
            'access_token': token_for_vk,
            'user_id': user_id,
            'extended': 1,
            'v': 5.131
        }
    response = requests.get(url_vk, params=params).json()
    items_in_response = response['response']
    return items_in_response['city']['title'], items_in_response['sex'],

#print(GetInfoFromVk(670276685))

def get_photos_vk_data(user_id, count=5):
    """This function would get you the profile picture of the person in best resolution."""
    url_vk = 'https://api.vk.com/method/photos.get'
    params = {
        'access_token': token_for_vk,
        'user_id': user_id,
        'album_id': 'profile',
        'extended': 1,
        'count': count,
        'v': 5.131
        }
    response = requests.get(url_vk, params=params).json()
    items_in_response = response['response']['items']
    for item in items_in_response:
        #return (item['id'])
        return (item['sizes'][-1]['url'])

#print(GetPhotosVkData(670276685))

def get_photos(user_id):
    get_user_photo_url = 'https://api.vk.com/method/photos.get'
    get_user_photo_params = {
        'owner_id': user_id,
        'album_id': 'profile',
        'extended': 1,
        'access_token': token_for_vk,
        'v': 5.131,
    }
    response = requests.get(get_user_photo_url, params=get_user_photo_params)
    return response.json()['response']['items']
#print(get_photos(670276685))

def list_of_cities(user_id):
    """This function would get you the list of cities in the country that you chosen."""
    city, sex = get_info_from_vk(user_id)
    url_vk = 'https://api.vk.com/method/database.getCities'
    params = {
        'access_token': token_for_vk,
        'country_id': 1,
        'region_id': '',
        'q': '',
        'need_all': '',
        'count': 100,
        'v': 5.131
        }
    response = requests.get(url_vk, params=params).json()
    items_in_response = response['response']['items']
    for item in items_in_response:
        if item['title'] == f'{city}':
            return item['id']
        return items_in_response

#print(ListOfCities(670276685))

def sex_number(sex_num):
    if sex_num == 1:
        return 2
    else:
        return 1


age_preferences = {1: [18, 24],
                   2: [25, 34],
                   3: [35, 44],
                   4: [45, 54],
                   5: [55, 64],
                   6: [65, 74],
                   7: [75, 100]
                   }


def get_users_for_date(user_id, number_for_age):
#def get_users_for_date(user_id, age_from, age_to):
    """ get random users photos, names and ids by your criteria for you """
    number = list_of_cities(user_id)
    city_name, sex_num = get_info_from_vk(user_id)
    num_for_part_sex = sex_number(sex_num)
    age_from, age_to = number_for_age
    #age_from, age_to = age_preferences[number_for_age]
    url_vk = 'https://api.vk.com/method/users.search'
    params = {
        'access_token': token_for_vk,
        'q': '',
        'sort': 0,
        'offset': '',
        'count': 3,
        'fields': 'photo',
        'country': 1,
        'city': number,
        'hometown': '',
        'sex': num_for_part_sex,
        'status': 6,
        'age_from': age_from,
        'age_to': age_to,
        'has_photo': 1,
        'v': 5.131
    }
    response = requests.get(url_vk, params=params).json()
    items_in_response = response['response']['items']
    values_of_key = [a_dict['photo'] for a_dict in items_in_response]
    name = [a_dict['first_name'] for a_dict in items_in_response]
    id_of_person = [a_dict['id'] for a_dict in items_in_response]
    photos = get_photos_vk_data(id_of_person)
    return name, id_of_person, photos
    #return name, id_of_person, photos
#print(get_users_for_date(670276685, 1))

def st(nuum):
    if nuum in age_preferences.keys():
        v, g = age_preferences[nuum]
        name, id_of_person, photos = get_users_for_date(670276685, v, g)
        for name, id, photo in zip(name, id_of_person, photos):
            return f"{name}\n https://vk.com/id{id} {photo}"


print(st(1))


import pathlib
pathlib.Path().resolve()

import os
#path = '/Users/mitch/Desktop/python class/python 2/thesis python 2'
#print(os.path.abspath(os.getcwd()))
#print(os.listdir(path))