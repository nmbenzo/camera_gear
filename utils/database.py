from typing import List, Dict, Union

from .database_connection import DatabaseConnection

"""
Concerned with storing and retrieving camera gear from a sqlite3 file.
Format of 'db' file:

make, model, sensor_size, megapixels
"""

Camera = Dict[str, Union[str, int]]


def create_camera_table() -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS cameras(model text primary key, '
                       'make text, sensor_size text, megapixels integer, price integer, owned integer)')


def add_cameras(model: str, make: str, sensor_size: str, megapixels: str,
                price: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO cameras VALUES(?, ?, ?, ?, ?, 0)',
                   (model, make, sensor_size, megapixels, price))


def get_all_cameras() -> List[Camera]:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM cameras')
        cameras = [{'model': row[0], 'make': row[1], 'sensor_size': row[2],
             'megapixels': row[3], 'price': row[4], 'owned': row[5]}
                   for row in cursor.fetchall()]

    return cameras


def gear_bought(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE cameras SET owned=1 WHERE model=?', (name,))


def remove_item(model: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM cameras WHERE model=?', (model,))
