if __name__ == "__main__":
    def sort_peoples(catalog):
        sorted_people = {}
        for k in sorted(catalog, key=catalog.get):
            sorted_people[k] = catalog.get(k)
        return sorted_people

    peoples = {'alex': 28, 'james': 27, 'martin': 35, 'moog': 38, 'peter': 18, 'jack': 51}
    print(sort_peoples(peoples))