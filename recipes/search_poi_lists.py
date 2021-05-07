from locussdk import get_avail_poi_lists


def search(name, **kwargs):
    lists = get_avail_poi_lists('global')

    return lists[lists.name.str.contains(name, **kwargs)]
