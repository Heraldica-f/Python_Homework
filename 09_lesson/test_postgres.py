from SqlMethods import SqlMethods

db = SqlMethods("postgresql://postgres@127.0.0.1:5432/postgres")

def test_create_new_subject():
    # создать новый предмет
    title = "Natural science"
    id = 16
    db.insert(title, id)

    # получить созданный предмет по id
    created_subject = db.get_subject(id)

    # удалить предмет
    db.delete(title)

    assert created_subject[0]["subject_title"] == title
    assert created_subject[0]["subject_id"] == id

def test_update_subject():
    # создать новый предмет
    title = "Works"
    id = 20
    db.insert(title, id)

    # изменить предмет
    new_title = "Technology"
    new_id = 19
    db.update(new_title, new_id, title)

    # Проверить, что предмет обновился
    updated = db.get_subject(new_id)

    # удалить предмет
    db.delete(new_title)

    assert updated[0]["subject_title"] == new_title
    assert updated[0]["subject_id"] == new_id

def test_delete_subject():
    # получить кол-во предметов
    list = db.get_subject_list()
    len_before = len(list)
    
    # создать новый предмет
    title = "ОБЖ"
    id = 17
    db.insert(title, id)

    # получить кол-во предметов
    list = db.get_subject_list()
    len_after = len(list)

    # удалить предмет
    db.delete(title)

    assert len_after - len_before == 1






