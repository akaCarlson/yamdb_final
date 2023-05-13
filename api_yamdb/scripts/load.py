import csv
from users.models import User
from reviews.models import Review, Category, Genre, Title, Comment, GenreTitle


def run():
    create_users()
    create_categories()
    create_genres()
    create_titles()
    create_reviews()
    create_comments()


def create_users():
    users_file = open('/app/static/data/users.csv')
    users_records = csv.reader(users_file)
    count = 1

    User.objects.exclude(is_superuser=True).delete()

    for record in users_records:
        if count == 1:
            pass
        else:
            User.objects.create(id=record[0],
                                username=record[4],
                                email=record[10],
                                role=record[12])
        count += 1


def create_categories():
    category_file = open('/app/static/data/category.csv')
    category_records = csv.reader(category_file)
    count = 1

    Category.objects.all().delete()

    for record in category_records:
        if count == 1:
            pass
        else:
            Category.objects.create(id=record[0],
                                    name=record[1],
                                    slug=record[2])
        count += 1


def create_genres():
    genre_file = open('/app/static/data/genre.csv')
    genre_records = csv.reader(genre_file)
    count = 1

    Genre.objects.all().delete()

    for record in genre_records:
        if count == 1:
            pass
        else:
            Genre.objects.create(id=record[0],
                                 name=record[1],
                                 slug=record[2])
        count += 1


def create_titles():
    titles_file = open('/app/static/data/titles.csv')
    titles_records = csv.reader(titles_file)
    count = 1

    Title.objects.all().delete()

    for record in titles_records:
        if count == 1:
            pass
        else:
            Title.objects.create(id=record[0],
                                 name=record[1],
                                 year=record[2],
                                 category=Category.objects.get(id=record[4]))
        count += 1

    genre_title_file = open('/app/static/data/genre_title.csv')
    genre_title_records = csv.reader(genre_title_file)
    count = 1

    GenreTitle.objects.all().delete()

    for record in genre_title_records:
        if count == 1:
            pass
        else:
            GenreTitle.objects.create(id=record[0],
                                      genre_id=record[1],
                                      title_id=record[2])
        count += 1


def create_reviews():
    review_file = open('/app/static/data/review.csv')
    review_records = csv.reader(review_file)
    count = 1

    Review.objects.all().delete()

    for record in review_records:
        if count == 1:
            pass
        else:
            Review.objects.create(id=record[0],
                                  text=record[1],
                                  score=record[2],
                                  pub_date=record[3],
                                  author=User.objects.get(id=record[4]),
                                  title_id=record[5])
        count += 1


def create_comments():
    comments_file = open('/app/static/data/comments.csv')
    comments_records = csv.reader(comments_file)
    count = 1

    Comment.objects.all().delete()

    for record in comments_records:
        if count == 1:
            pass
        else:
            Comment.objects.create(id=record[0],
                                   text=record[1],
                                   pub_date=record[2],
                                   author=User.objects.get(id=record[3]),
                                   review_id=Review.objects.get(id=record[4]))
        count += 1
