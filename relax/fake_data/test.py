from fake_schema.faker_schema import FakerSchema

# TODO: How to give advise of provider?
fk = FakerSchema(locale="zh-CN")
schema = {
            "title": "name",
            "date": "date",
            "internet": "ssn"}

data = fk.generate_fake(schema)
print(data)

