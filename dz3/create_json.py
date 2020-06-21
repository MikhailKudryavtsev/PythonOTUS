import json
from csv import DictReader

array = []

with open("dz3/users.json", "r") as file_json:
    users_list = json.loads(file_json.read())

    with open('dz3/books.csv', newline='') as file_csv:
        reader_csv = DictReader(file_csv)
        for users, row in zip(users_list, reader_csv):
            user_name = users.get('name')
            user_gender = users.get('gender')
            user_address = users.get('address')
            title = row.get('Title')
            author = row.get('Author')
            height = row.get('Height')

            data = {
                "name": user_name,
                "gender": user_gender,
                "address": user_address,
                "books": [
                    {
                        "title": title,
                        "author": author,
                        "height": height
                    }
                ]
            }

            if not array:
                array = [data]
            else:
                array.append(data)

        users = {"users": array}

        with open("dz3/new_json.json", "a") as file:
            users_json = json.dumps(users, indent=4)
            file.write(users_json)
            print(users_json)
