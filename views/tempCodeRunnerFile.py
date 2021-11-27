@bp.route('/')
def home():
    return render_template('base.html')