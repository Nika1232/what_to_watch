from . import db, app
from .views import render_template


@app.errorhandler(404)
def page_not_found(error):
    """Ошибка не найдено."""
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """Ошибка сервера."""
    db.session.rollback()
    return render_template('500.html'), 500
