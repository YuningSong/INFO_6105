from flask import Flask, request, render_template
import static.analysis as analysis

app = Flask(__name__)


# main page
@app.route('/')
def main_page():
    return render_template("main.html")


# check dataset
@app.route('/check_dataset')
def check_dataset():
    return render_template("check_dataset.html")


# get analysis result
@app.route('/result', methods=['GET', 'POST'])
def get_result():
    if request.method == 'POST':
        user_name = request.form['user_name']
        review_count = request.form['review_count']
        elite_count = request.form['elite_count']
        average_star = request.form['average_star']
        business_average_star = request.form['buisness_average_star']

        validation_flag = False
        user_name_failed = None
        review_count_failed = None
        elite_count_failed = None
        average_star_failed = None
        business_average_star_failed = None

        # user name validation
        if len(user_name) == 0:
            validation_flag = True
            user_name_failed = "User Name should not be empty!"

        # review count validation
        try:
            review_count = int(review_count)
            if review_count < 5:
                validation_flag = True
                review_count_failed = "Review Count must above 5!"
        except ValueError:
            validation_flag = True
            review_count_failed = "Review Count must be an integer!"

        # elite count validation
        try:
            elite_count = int(elite_count)
            if elite_count < 0:
                validation_flag = True
                elite_count_failed = "Elite Count must above 0!"
        except ValueError:
            validation_flag = True
            elite_count_failed = "Elite Count must be an integer!"

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
                review_count_failed=review_count_failed,
                elite_count_failed=elite_count_failed,
                average_star_failed=average_star_failed,
                business_average_star_failed=business_average_star_failed,
                user_name=user_name,
                review_count=review_count,
                elite_count=elite_count,
                average_star=average_star,
                business_average_star=business_average_star
            )

        score = analysis.model_analysis(average_star, elite_count, review_count, business_average_star)
        # score = 0
        return render_template(
            "result.html",
            score=score,
            user_name=user_name,
            review_count=review_count,
            elite_count=elite_count,
            average_star=average_star,
            business_average_star=business_average_star
        )


if __name__ == '__main__':
    app.run()
