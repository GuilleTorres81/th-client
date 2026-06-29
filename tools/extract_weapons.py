from tools.common import get_client


def extract_weapons(client):
    """
    Devuelve la respuesta completa del endpoint de la tienda.
    """

    return client.session.get("/v1/Application/shop").json()


def print_weapons(data):

    print(type(data))
    print()

    if isinstance(data, dict):
        print(data.keys())

    elif isinstance(data, list):
        print(f"Elementos: {len(data)}")

        if data:
            print(type(data[0]))
            print()
            print(data[0])


if __name__ == "__main__":

    client = get_client()

    weapons = extract_weapons(client)

    print_weapons(weapons)