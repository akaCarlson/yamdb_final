import csv
from users.models import User
from reviews.models import Review, Category, Genre, Title, Comment, GenreTitle


def run(*args):

    if 'all' in args:
        Comment.objects.all().delete()
        Review.objects.all().delete()
        GenreTitle.objects.all().delete()
        Genre.objects.all().delete()
        Title.objects.all().delete()
        Category.objects.all().delete()
        User.objects.exclude(is_superuser=True).delete()

    else:
        delete_comments()
        delete_reviews()
        delete_genres()
        delete_titles()
        delete_categories()
        delete_users()


def delete_users():
    users_file = open('/app/static/data/users.csv')
    users_records = csv.reader(users_file)
    count = 1

    for record in users_records:
        if count == 1:
            pass
        else:
            User.objects.get(id=record[0]).delete()
        count += 1


def delete_categories():
    category_file = open('/app/static/data/category.csv')
    category_records = csv.reader(category_file)
    count = 1

    for record in category_records:
        if count == 1:
            pass
        else:
            Category.objects.get(id=record[0]).delete()
        count += 1


def delete_genres():
    genre_title_file = open('/app/static/data/genre_title.csv')
    genre_title_records = csv.reader(genre_title_file)
    count = 1

    for record in genre_title_records:
        if count == 1:
            pass
        else:
            GenreTitle.objects.get(id=record[0]).delete()
        count += 1

    genre_file = open('/app/static/data/genre.csv')
    genre_records = csv.reader(genre_file)
    count = 1

    for record in genre_records:
        if count == 1:
            pass
        else:
            Genre.objects.get(id=record[0]).delete()
        count += 1


def delete_titles():
    titles_file = open('/app/static/data/titles.csv')
    titles_records = csv.reader(titles_file)
    count = 1

    for record in titles_records:
        if count == 1:
            pass
        else:
            Title.objects.get(id=record[0]).delete()
        count += 1


def delete_reviews():
    review_file = open('/app/static/data/review.csv')
    review_records = csv.reader(review_file)
    count = 1

    for record in review_records:
        if count == 1:
            pass
        else:
            Review.objects.get(id=record[0]).delete()
        count += 1


def delete_comments():
    comments_file = open('/app/static/data/comments.csv')
    comments_records = csv.reader(comments_file)
    count = 1

    for record in comments_records:
        if count == 1:
            pass
        else:
            Comment.objects.get(id=record[0]).delete()
        count += 1
