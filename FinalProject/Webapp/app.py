from flask import Flask, request, render_template, g, url_for
import static.models as models
import static.csv as csv

app = Flask(__name__)


@app.before_request
def load_dataset():
    g.path = csv.dataset_path()


# main page
@app.route('/')
def main_page():
    return render_template("main.html")


# check dataset
@app.route('/check_dataset/page/<int:page_num>', methods=['GET'])
def check_dataset(page_num):
    limits = 20
    pages = csv.cal_dataset_pages(g.path, limits)
    df = csv.show_csv(g.path, page_num, limits)
    return render_template('check_dataset.html', df=df, pages=pages, page_num=page_num)


# get analysis result
@app.route('/result', methods=['GET', 'POST'])
def get_result():
    if request.method == 'POST':
        user_name = request.form['user_name']
        friends_count = request.form['friends_count']
        elite_count = request.form['elite_count']
        fans = request.form['fans']
        average_star = request.form['average_star']
        business_average_star = request.form['buisness_average_star']

        validation_flag = False
        user_name_failed = None
        friends_count_failed = None
        elite_count_failed = None
        fans_failed = None
        average_star_failed = None
        business_average_star_failed = None

        # user name validation
        if len(user_name) == 0:
            validation_flag = True
            user_name_failed = "User Name should not be empty!"

        # review count validation
        try:
            friends_count = int(friends_count)
            if friends_count < 0:
                validation_flag = True
                friends_count_failed = "Friends Count must above 0!"
        except ValueError:
            validation_flag = True
            friends_count_failed = "Friends Count must be an integer!"

        # elite count validation
        try:
            elite_count = int(elite_count)
            if elite_count < 0:
                validation_flag = True
                elite_count_failed = "Elite Count must above 0!"
        except ValueError:
            validation_flag = True
            elite_count_failed = "Elite Count must be an integer!"

        # fans validation
        try:
            fans = int(fans)
            if elite_count < 0:
                validation_flag = True
                fans_failed = "Fans must above 0!"
        except ValueError:
            validation_flag = True
            fans_failed = "Fans must be an integer!"

        # average star validation
        try:
            average_star = float(average_star)
            if average_star < 1.0 or average_star > 5.0:
                validation_flag = True
                average_star_failed = "Average Star must between 1.0 and 5.0"
        except ValueError:
            validation_flag = True
            average_star_failed = "Average Star must be a number!"

        # business_average_star validation
        try:
            business_average_star = float(business_average_star)
            if business_average_star < 1.0 or business_average_star > 5.0:
                validation_flag = True
                business_average_star_failed = "Business Average Star must between 1.0 and 5.0"
        except ValueError:
            validation_flag = True
            business_average_star_failed = "Business Average Star must be a number!"

        if validation_flag:
            return render_template(
                "main.html",
                user_name_failed=user_name_failed,
                friends_count_failed=friends_count_failed,
                elite_count_failed=elite_count_failed,
                fans_failed=fans_failed,
                average_star_failed=average_star_failed,
                business_average_star_failed=business_average_star_failed,
                user_name=user_name,
                friends_count=friends_count,
                elite_count=elite_count,
                average_star=average_star,
                business_average_star=business_average_star
            )
        score = models.random_forest(average_star, elite_count, fans, friends_count, business_average_star)

        return render_template(
            "result.html",
            score=score,
            user_name=user_name,
            friends_count=friends_count,
            fans=fans,
            elite_count=elite_count,
            average_star=average_star,
            business_average_star=business_average_star
        )


if __name__ == '__main__':
    app.run()
