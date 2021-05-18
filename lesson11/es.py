import elasticsearch
from faker import Faker


def main():
    es = elasticsearch.Elasticsearch()
    index_name = "test_sphere_python"

    fake = Faker(locale="Ru_ru")
    for i in range(10):
        doc = {
            "title": fake.address(),
            "descr": fake.sentence(nb_words=5)
        }
        es.index(index=index_name, id=10 + i, body=doc)

    res = es.search(index=index_name, body={"query": {"match_all": {}}})
    print(res)


if __name__ == "__main__":
    main()
