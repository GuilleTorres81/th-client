from hunterclassic.models.loadout import Loadout

from tools.common import get_client, iter_expeditions


def extract_animals(client, player):

    animals = {}

    for detail in iter_expeditions(client, player):

        reserve = detail["expedition"]["reserve"]

        for kill in detail["kills"]:

            animal = animals.setdefault(
                kill["species"],
                {
                    "name": kill["speciesName"],
                    "reserves": set(),
                    "loadouts": set(),
                },
            )

            animal["reserves"].add(reserve)

            # Solo nos interesan las kills éticas
            if not kill["kill"]["ethical"]:
                continue

            for hit in kill["hits"]:
                animal["loadouts"].add(
                    Loadout(
                        weapon_id=hit["weapon_id"],
                        ammo_id=hit["ammo_id"],
                    )
                )

    return animals


def print_animals(animals):

    print(f"Animales encontrados: {len(animals)}\n")

    for animal_id in sorted(animals):

        animal = animals[animal_id]

        print(f"{animal_id:>3} -> {animal['name']}")

        print(f"    Reservas : {sorted(animal['reserves'])}")

        print("    Loadouts :")

        for loadout in sorted(
            animal["loadouts"],
            key=lambda l: (l.weapon_id, l.ammo_id),
        ):
            print(
                f"        Weapon {loadout.weapon_id} + Ammo {loadout.ammo_id}"
            )

        print()


if __name__ == "__main__":

    client = get_client()

    player = client.users.get_by_hostname("HunterLagger")

    animals = extract_animals(client, player)

    print_animals(animals)